### import everthing we need
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import os
import mahotas as mh
from skimage.measure import label, regionprops, regionprops_table
import natsort  # package for naturally sort name of image sequence
from tqdm import tqdm
import pandas as pd
import cv2
import trackpy as tp # important package for particle tracking
import gc
from mpl_toolkits.axes_grid1 import make_axes_locatable


class analyzer:
    
    def __init__(self, im_list, search_range=3, memory=0):
        self.im_list = im_list
        self.search_range = search_range
        self.memory = memory

    @staticmethod
    #watershed segmentation
    def watershed_segmentation(im):
        locmax = mh.regmax(im)
        seeds, nr_nuclei = mh.label(locmax)
        T = mh.thresholding.otsu(np.uint8(im))
        dist = mh.distance(np.uint8(im) > T)
        dist = dist.max() - dist
        dist -= dist.min()
        dist = dist/float(dist.ptp()) * 255
        dist = dist.astype(np.uint8)
        nuclei, lines = mh.cwatershed(dist, seeds, return_lines=True)

        #parameters extraction-1
        nuclei_without_border = mh.labeled.remove_bordering(nuclei)
        nuclei_new = label(nuclei_without_border)
        return nuclei_new, lines
    
    @staticmethod
    #extract coordinates of centroids    
    def extract_centroids(nuclei):
        #use scikit image func
        props=regionprops(nuclei)
        centroids_y=[props[i].centroid[0].astype('float32') for i in range(len(props))]
        centroids_x=[props[i].centroid[1].astype('float32') for i in range(len(props))]
        labels=[np.int32(props[i].label) for i in range(len(props))]
        return centroids_y, centroids_x, labels
    
    def extract_feature(self):
        im_list = self.im_list
        nuclei_list=[] #segemented images
        centroids_x_list=[] # x axis of centroids
        centroids_y_list=[] # y axis of centroids
        frame_num_list=[] # number of frame
        labels_list=[] # number of labels
        
        for i in tqdm(range(len(im_list))):
            nuclei, _ = analyzer.watershed_segmentation(im_list[i])
    
            #centroids extraction
            centroids_y, centroids_x, labels = analyzer.extract_centroids(nuclei)
    
            #frame number
            frame_num = np.ones(len(centroids_y), dtype="int32")*i
    
            #save results
            nuclei_list.append(nuclei)
            centroids_y_list.extend(centroids_y)
            centroids_x_list.extend(centroids_x)
            frame_num_list.extend(frame_num)
            labels_list.extend(labels)
        
        return nuclei_list, centroids_x_list, centroids_y_list, frame_num_list, labels_list
    
    @staticmethod
    #extract the cells correctly tracked by the algorithm
    def extract_cell_tracking_result(nuclei_list, track_result_filtered, check_number):
        #set 3D storage
        nuclei_track_result = np.zeros((nuclei_list[0].shape[0], nuclei_list[0].shape[1], check_number))

        #extract particle num satisfying check number
        frame_num_list=np.unique(track_result_filtered['frame'])

        for frame_num in tqdm(frame_num_list):
            #extract information of the certain frame
            track_result_certain_frame=track_result_filtered[track_result_filtered["frame"]==frame_num]

            #set target
            target_label=np.asarray(track_result_certain_frame["label"])
            target_particle=np.asarray(track_result_certain_frame["particle"])
            target_nuclei=list(nuclei_list[frame_num].flatten())

            #create temporary zero matrix
            zero_map=np.zeros((nuclei_list[0].shape[0]*nuclei_list[0].shape[1]))

            #set function
            #replace_func = {label: new for label, new in zip(target_label_sort, new_label)} 
            replace_func = {label: new for label, new in zip(target_label, target_particle)} 

            #replace label values to anatomical values
            replace_result=np.asarray(list(map(replace_func.get, target_nuclei)))
            result_index=np.where(replace_result!=None)[0]

            #project the result to zero map
            zero_map[result_index]=replace_result[result_index]

            #merge result of each frame to 3D storage
            nuclei_track_result[:,:,frame_num]=zero_map.reshape((nuclei_list[0].shape[0], nuclei_list[0].shape[1]))
            
        return nuclei_track_result
    
    
    def tracker(self, nuclei_list, centroids_x_list, centroids_y_list, frame_num_list, labels_list):
        features_data = np.vstack((centroids_y_list, centroids_x_list, frame_num_list, labels_list)).T
        features_frame = pd.DataFrame(features_data, columns=["y", "x", "frame", "label"])
        track_result = tp.link_df(features_frame, search_range=self.search_range, memory=self.memory)
        
        #set check number
        check_number=len(np.unique(track_result["frame"]))

        #count the frequency of each particle in all frames
        particle_num_list, counts=np.unique(track_result["particle"], return_counts=True)
    
        #filtering dataframe based on above-extracted particle num
        track_result_filtered=track_result[track_result.particle.isin(np.where(counts==check_number)[0])]

        #extract particle num satisfying check number
        nuclei_true = analyzer.extract_cell_tracking_result(nuclei_list, track_result_filtered, check_number)
        
        return track_result_filtered, nuclei_true, check_number
    
    def parameter_changes_cal(self, nuclei_true, check_number, num=5):
        area_lists = [] # measure cell area
        ecc_lists = [] # measure cell eccentricity
        aspect_axis_lists = [] # measure fitted ellipse aspect ratio
        aspect_bbox_lists = [] # measure bounding box aspect ratio
        
        for i in tqdm(range(check_number)):
            label = np.asarray([label for label in np.unique(nuclei_true[:,:,i])])
            props = regionprops(np.int32(nuclei_true[:,:,i]))

            #calculate each param
            area = np.asarray([props[j].area for j in range(len(props))])
            ecc = np.asarray([props[j].eccentricity for j in range(len(props))])
            major_axis = np.asarray([props[j].major_axis_length for j in range(len(props))])
            minor_axis = np.asarray([props[j].minor_axis_length for j in range(len(props))])
            aspect_ratio_axis = major_axis/minor_axis # calculate fitted ellipse aspect ratio
            vert = np.asarray([props[j].bbox[2] for j in range(len(props))])-np.asarray([props[j].bbox[0] for j in range(len(props))])
            hori = np.asarray([props[j].bbox[3] for j in range(len(props))])-np.asarray([props[j].bbox[1] for j in range(len(props))])
            aspect_ratio_bbox = vert/hori # calcuate bounding box aspect ratio

            # transform to lists
            area_list = np.stack((label[1:], area), axis=-1)
            ecc_list = np.stack((label[1:], ecc), axis=-1)
            aspect_axis_list = np.stack((label[1:], aspect_ratio_axis), axis=-1)
            aspect_bbox_list = np.stack((label[1:], aspect_ratio_bbox), axis=-1)

            area_lists.append(area_list)
            ecc_lists.append(ecc_list)
            aspect_axis_lists.append(aspect_axis_list)
            aspect_bbox_lists.append(aspect_bbox_list)
        
        area_lists_array = np.asarray(area_lists)
        ecc_lists_array = np.asarray(ecc_lists)
        aspect_axis_lists_array = np.asarray(aspect_axis_lists)
        aspect_bbox_lists_array = np.asarray(aspect_bbox_lists)
        
        
        num = num

        #reset the first_list
        first_list_area = []
        first_list_ecc = []
        first_list_aspect_axis = []
        first_list_aspect_bbox = []

        for j in range(len(area_lists_array[0])):
            average_value_area = np.average([area_lists_array[k][j][1:2].astype('float') for k in range(num)])
            average_num_area = np.average([area_lists_array[k][j][0:1].astype('float') for k in range(num)])
            average_area = np.asarray([average_num_area, average_value_area])
            first_list_area.append(average_area)

            average_value_ecc = np.average([ecc_lists_array[k][j][1:2].astype('float') for k in range(num)])
            average_num_ecc = np.average([ecc_lists_array[k][j][0:1].astype('float') for k in range(num)])
            average_ecc = np.asarray([average_num_ecc, average_value_ecc])
            first_list_ecc.append(average_ecc)

            average_value_aspect_axis = np.average([aspect_axis_lists_array[k][j][1:2].astype('float') for k in range(num)])
            average_num_aspect_axis = np.average([aspect_axis_lists_array[k][j][0:1].astype('float') for k in range(num)])
            average_aspect_axis = np.asarray([average_num_aspect_axis, average_value_aspect_axis])
            first_list_aspect_axis.append(average_aspect_axis)

            average_value_aspect_bbox = np.average([aspect_bbox_lists_array[k][j][1:2].astype('float') for k in range(num)])
            average_num_aspect_bbox = np.average([aspect_bbox_lists_array[k][j][0:1].astype('float') for k in range(num)])
            average_aspect_bbox = np.asarray([average_num_aspect_bbox, average_value_aspect_bbox])
            first_list_aspect_bbox.append(average_aspect_bbox)

        area_lists_array_mod = np.vstack((np.expand_dims(first_list_area, axis=0),area_lists_array[num:]))
        ecc_lists_array_mod = np.vstack((np.expand_dims(first_list_ecc, axis=0),ecc_lists_array[num:]))
        aspect_axis_lists_array_mod = np.vstack((np.expand_dims(first_list_aspect_axis, axis=0),aspect_axis_lists_array[num:]))
        aspect_bbox_lists_array_mod = np.vstack((np.expand_dims(first_list_aspect_bbox, axis=0),aspect_bbox_lists_array[num:]))

        #reset the change_list
        area_change_lists_mod = []
        ecc_change_lists_mod = []
        aspect_axis_change_lists_mod = []
        aspect_bbox_change_lists_mod = []

        for i in tqdm(range(len(area_lists_array_mod))):
            first_list_area = area_lists_array_mod[0]
            target_list_area = area_lists_array_mod[i]
            selected_list_area = first_list_area[np.where(first_list_area[:,:1]==np.intersect1d(first_list_area[:,:1], target_list_area[:,:1]))[0]]
            area_change = ((target_list_area[:,1:2] - selected_list_area[:,1:2])/selected_list_area[:,1:2])*100
            area_change_list = np.stack((target_list_area[:,:1][:,0], area_change[:,0]), axis=-1)
            area_change_lists_mod.append(area_change_list)

            first_list_ecc = ecc_lists_array_mod[0]
            target_list_ecc = ecc_lists_array_mod[i]
            selected_list_ecc = first_list_ecc[np.where(first_list_ecc[:,:1]==np.intersect1d(first_list_ecc[:,:1], target_list_ecc[:,:1]))[0]]
            ecc_change = ((target_list_ecc[:,1:2] - selected_list_ecc[:,1:2])/selected_list_ecc[:,1:2])*100
            ecc_change_list = np.stack((target_list_ecc[:,:1][:,0], ecc_change[:,0]), axis=-1)
            ecc_change_lists_mod.append(ecc_change_list)

            first_list_aspect_axis = aspect_axis_lists_array_mod[0]
            target_list_aspect_axis = aspect_axis_lists_array_mod[i]
            selected_list_aspect_axis = first_list_aspect_axis[np.where(first_list_aspect_axis[:,:1]==np.intersect1d(first_list_aspect_axis[:,:1], target_list_aspect_axis[:,:1]))[0]]
            aspect_axis_change = ((target_list_aspect_axis[:,1:2] - selected_list_aspect_axis[:,1:2])/selected_list_aspect_axis[:,1:2])*100
            aspect_axis_change_list = np.stack((target_list_aspect_axis[:,:1][:,0], aspect_axis_change[:,0]), axis=-1)
            aspect_axis_change_lists_mod.append(aspect_axis_change_list)

            first_list_aspect_bbox = aspect_bbox_lists_array_mod[0]
            target_list_aspect_bbox = aspect_bbox_lists_array_mod[i]
            selected_list_aspect_bbox = first_list_aspect_bbox[np.where(first_list_aspect_bbox[:,:1]==np.intersect1d(first_list_aspect_bbox[:,:1], target_list_aspect_bbox[:,:1]))[0]]
            aspect_bbox_change = ((target_list_aspect_bbox[:,1:2] - selected_list_aspect_bbox[:,1:2])/selected_list_aspect_bbox[:,1:2])*100
            aspect_bbox_change_list = np.stack((target_list_aspect_bbox[:,:1][:,0], aspect_bbox_change[:,0]), axis=-1)
            aspect_bbox_change_lists_mod.append(aspect_bbox_change_list)
            
        area_change_lists_array = np.asarray(area_change_lists_mod)
        ecc_change_lists_array = np.asarray(ecc_change_lists_mod)
        aspect_axis_change_lists_array = np.asarray(aspect_axis_change_lists_mod)
        aspect_bbox_change_lists_array = np.asarray(aspect_bbox_change_lists_mod)
        
        return area_change_lists_array, ecc_change_lists_array, aspect_axis_change_lists_array, aspect_bbox_change_lists_array

    
    def result_visualize(self, nuclei_list, track_result_filtered, change_rate_result, num=5):
        
        start_point = num-1
        #set 3D storage
        result_map = np.zeros((nuclei_list[:,:,0].shape[0], nuclei_list[:,:,0].shape[1], len(change_rate_result)))

        #extract particle num satisfying check number
        frame_num_list=np.unique(track_result_filtered['frame'])[start_point:]

        for i in tqdm(range(len(frame_num_list))):
            frame_num = frame_num_list[i]
            #extract information of the certain frame
            track_result_certain_frame=track_result_filtered[track_result_filtered["frame"]==frame_num]        
            #set target
            #target_label=np.asarray(track_result_certain_frame["label"])
            #target_particle=np.asarray(track_result_certain_frame["particle"])
            new_label=np.unique(nuclei_list[:,:, frame_num])[1:]
            target_nuclei=list(nuclei_list[:,:, frame_num].flatten())
            target_change_rate_result=change_rate_result[i]

            #set zero map
            zero_map=np.zeros((nuclei_list[:,:,0].shape[0]*nuclei_list[:,:,0].shape[1]))    

            #set function
            replace_func = {new: change_rate for new, change_rate in target_change_rate_result} 

            #replace label values to anatomical values
            replace_result=np.asarray(list(map(replace_func.get, target_nuclei)))
            result_index=np.where(replace_result!=None)[0]

            #project the result to zero map
            zero_map[result_index]=replace_result[result_index]

            #save result
            result_map[:,:,i]=zero_map.reshape((nuclei_list[:,:,0].shape[0], nuclei_list[:,:,0].shape[1]))

        return result_map