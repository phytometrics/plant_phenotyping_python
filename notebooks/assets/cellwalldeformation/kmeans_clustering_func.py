import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable
from IPython.display import HTML
import pandas as pd
from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt
from natsort import natsort
from sklearn.cluster import KMeans
import pandas as pd
from matplotlib.colors import ListedColormap


class processer:
    @staticmethod
    def make_particle_change_lists(change_lists_array, num_list=False):
        particle_num_lists_1d_array = np.asarray([np.hsplit(change_lists_array[num],[1])[0] 
                                for num in range(len(change_lists_array))],dtype=object)

        change_lists_1d_array = np.asarray([np.hsplit(change_lists_array[num],[1])[1] 
                                for num in range(len(change_lists_array))],dtype=object)

        ## remove  nan and inf value
        change_lists_1d_array_mod = np.asarray([np.nan_to_num(change_lists_1d_array[num],nan=0.0, posinf=0.0, neginf=0.0) 
                                            for num in range(len(change_lists_1d_array))],dtype=object)
        result_lists = []

        if num_list == False:
            for i in tqdm(np.unique(particle_num_lists_1d_array[0])):
                change_rate_lists = []
                for j in range(len(change_lists_1d_array)):
                    change_list_1d_array = change_lists_1d_array_mod[j]
                    change_rate = change_list_1d_array[np.where(particle_num_lists_1d_array[j]==i)[0]]
                    if change_rate.size==0:
                        continue
                    else:
                        change_rate_lists.extend(change_rate)
                result_lists.append(change_rate_lists)


        if num_list == True:
            num_list_and_particle_change_rate_lists = []
            for i in tqdm(np.unique(particle_num_lists_1d_array[0])):
                change_rate_lists = []
                for j in range(len(change_lists_1d_array)):
                    change_list_1d_array = change_lists_1d_array_mod[j]
                    change_rate = change_list_1d_array[np.where(particle_num_lists_1d_array[j]==i)[0]]
                    if change_rate.size==0:
                        continue
                    else:   
                        change_rate_lists.extend(change_rate)

                change_rate_lists_2 = np.append(i, change_rate_lists)
                result_lists.append(change_rate_lists_2)

        return result_lists

    @staticmethod
    def modify_change_lists(result_lists, max_num, min_num):
        selected_lists = []
        original_p_n_lists = []
        modified_p_n_lists = []
        for i in tqdm(range(len(result_lists))):
            result_list = result_lists[i]
            if np.max(result_list[1:])> max_num or np.min(result_list[1:]) < min_num:
                original_p_n_lists.append(result_list[0])
                modified_p_n_lists.append(0)
            else:
                selected_lists.append(result_list)
                original_p_n_lists.append(result_list[0])
                modified_p_n_lists.append(result_list[0])

        return selected_lists, original_p_n_lists, modified_p_n_lists

    @staticmethod
    def transform_cell_true(nuclei_list, original_p_n_lists, modified_p_n_lists):
        #set 3D storage
        result_map = np.zeros((nuclei_list[:,:,0].shape[0], nuclei_list[:,:,0].shape[1]))

        #set zero map
        zero_map=np.zeros((nuclei_list[:,:,0].shape[0]*nuclei_list[:,:,0].shape[1]))    

        #set target
        target_nuclei=list(nuclei_list[:,:,-1].flatten())

        #set function
        replace_func = {new: k_label for new, k_label in zip(original_p_n_lists, modified_p_n_lists)} 

        #replace label values to anatomical values
        replace_result=np.asarray(list(map(replace_func.get, target_nuclei)))
        result_index=np.where(replace_result!=None)[0]

        #project the result to zero map
        zero_map[result_index]=replace_result[result_index]

        #save result
        result_map[:,:]=zero_map.reshape((nuclei_list[:,:,0].shape[0], nuclei_list[:,:,0].shape[1]))

        return result_map
    
    @staticmethod
    def kmeans_clustering(selected_lists, num_cluster=8):
        df_mod = pd.DataFrame(selected_lists)
        num_clusters = 8
        kmeans = KMeans(n_clusters=num_clusters, random_state=0)
        model = kmeans.fit(df_mod.iloc[:,1:])
        kmeans_result = model.predict(df_mod.iloc[:,1:])
        
        return kmeans_result
        
    @staticmethod
    def result_visualization_kmeans(nuclei_list, kmeans_results):
        #set 3D storage
        result_map = np.zeros((nuclei_list[:,:].shape[0], nuclei_list[:,:].shape[1]))

        label=np.unique(nuclei_list[:,:])[1:]
        target_nuclei=list(nuclei_list[:,:].flatten())

        #set zero map
        zero_map=np.zeros((nuclei_list[:,:].shape[0]*nuclei_list[:,:].shape[1]))    

        #set function
        replace_func = {new: k_label for new, k_label in zip(label, kmeans_results)} 

        #replace label values to anatomical values
        replace_result=np.asarray(list(map(replace_func.get, target_nuclei)))
        result_index=np.where(replace_result!=None)[0]

        #project the result to zero map
        zero_map[result_index]=replace_result[result_index]

        #save result
        result_map[:,:]=zero_map.reshape((nuclei_list[:,:].shape[0], nuclei_list[:,:].shape[1]))

        return result_map