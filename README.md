# Image-Analysis for Plant Biologists with Python

## [はじめに](columns/introduction.md)
## コラム
### [なんでもかんでもAIっていうんじゃない](columns/using_the_term_AI.md)
### [エラーは怖くない：自分で解決できるようになろう](columns/error.md)
### [ファイルとフォルダの命名方法](columns/file_name.md)
### [Pythonの命名規則](columns/styleguide.md)
### [座標系と表記順序：xyなのかyxなのか、nhwcなのかnchwなのか。](columns/xyyxrc.md)
### [機械学習におけるデータセットのフォーマット](columns/dataset_format.md)
### [データリーク](columns/dataleak.md)
### [巨人の肩での研究: ソフトウェアライセンスについて](columns/license_rules.md)
### [あなたの「説明可能なAI」研究は、本当に説明可能ですか？](columns/explainable_ai.md)
### [「レナ」を超えて](columns/lenna.md)

## Colaboratoryハンズオン
### [Python基礎](notebooks/basics.ipynb)
### 画像解析基礎
### [グリーンハウスの環境データ分析](notebooks/env_data_analysis.ipynb)
- pandasやplotlyを用いた表データ操作・分析・可視化
### [種子計数形状解析（１）](notebooks/rice_seed_shape_analysis.ipynb) 
- scikit-imageのregionpropsとwatershedを利用したオブジェクトの計数と形状解析
### [ブドウ花粉活性度評価](notebooks/pollencounter.ipynb)
- ImageJマクロのPython再実装
- scikit-imageのregionpropsとwatershedを利用したオブジェクトの計数
### [WEIPS：ドローン画像からの雑草除去およびヤクイモ表現型定量](notebooks/WEIPS.ipynb)
- MATLABコードのPython再実装
- RGBとDepth情報を用いた領域抽出
- オルソモザイク画像とデジタルサーフィスモデル画像からの表現型抽出
### [リンゴの葉形状と遺伝的多様性の解析](notebooks/apple_leaf.ipynb)  *GWAS解析の検証とGSの追加が必要*
- 楕円フーリエ記述子と輪郭形状解析
- SNPを利用したPCA/GWAS/GS 解析
### 種子計数形状解析（２）
- Mask-RCNNを利用した種子Intance Segmentation
### [DeepStomata: マルバツユクサの気孔開度定量](notebooks/dayflower_stomata_quantification.ipynb)
- HOG特徴量を利用した気孔検出
- CNNによる気孔開閉判定
- scikit-imageのregionpropsを利用した気孔開口領域単離と定量
### [植物病害識別診断モデルの訓練と通じたImage Classification型CNNの理解](notebooks/plantvilllage.ipynb)
- tensorflow.kerasを活用したCNNモデルの構築と訓練
### ChronoRoot:バーティカルプレート上で生育させたシロイヌナズナ根の計測
- semantic segmentationによる根領域の抽出
- 時系列補正
- skeletonizationによるグラフ構造抽出
### [イネ収量予測](notebooks/riceyieldcnn.ipynb)  
- 学習済CNNモデルを利用したイネ収量推論
### [ドローン画像からの小麦穂検出モデル作成](notebooks/globalwheat2021.ipynb)
- YOLOv8物体検出モデルの学習と推論
### 雑草検出モデルの作成と利用
- detectron2で全部やる
  - object detection
  - semantic segmenatation
  - instance segmenatation
### [StomaAI:シロイヌナズナの表皮断片顕微鏡画像からの気孔開度定量](notebooks/sai.ipynb)
- detectron2によるinstance segmenatation + keypoint detection
### シロイヌナズナのリーフディスク顕微鏡画像からの気孔開度定量
- YOLOXによる気孔検出
- Segmentation Modelsによる気孔開度検出
### データ解析と機械学習モデルの解釈
- PCAの合成ベクトルの意味
- RandomForestの特徴量寄与率
- CNN系の特徴量可視化
  - Grad-CAMなど

### [PlantSeg:3D共焦点画像からの細胞壁検出と細胞インスタンス・セグメンテーション](notebooks/plantseg.ipynb)
### [U<sup>2</sup>-Net (U-Square Net)を利用した葉領域抽出の試み](notebooks/u2netp.ipynb)


### 実装したい

#### foundation model
- sam
- grounding dino
etc.

#### 野外でのダイズ種子計数
- P2PNet-Soyを利用した点検出ネットワーク

#### ブロッコリー生育予測
- Drone-Based Harvest Data Prediction Can Reduce On-Farm Food Loss and Improve Farmer Income
  - cc-by
  - https://spj.science.org/doi/10.34133/plantphenomics.0086
- https://github.com/UTokyo-FieldPhenomics-Lab/UAVbroccoli
  - MIT。ただしyolov5はGPLv3
#### 葉脈解析
- Network feature-based phenotyping of leaf venation robustly reconstructs the latent space
  - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010581
  - cc-by
- https://zenodo.org/records/8020856
  - 
- https://github.com/MorphometricsGroup/iwamasa-2022
  - mit
#### Aravib: 
- High-Throughput Analysis of Arabidopsis Stem Vibrations to Identify Mutants With Altered Mechanical Properties
  - https://www.frontiersin.org/articles/10.3389/fpls.2018.00780/full
#### Cell segmentation and tracking from time-series sequential images
- Flexural behavior of wood in the transverse direction investigated using novel computer vision and machine learning approach
  - https://www.degruyter.com/document/doi/10.1515/hf-2022-0096/html
  - cc-by
- https://github.com/pywood21/holz_202209

## 謝辞


  
おまけ？
  - Segment Anything
  - Grounding DINO


- VegAnn
  - https://www.nature.com/articles/s41597-023-02098-y
  - ccby4.0

- colab以外の実装形態
  - .pyファイル
  - ウェブ形式
    - streamlit, gradio ....


  - https://www.degruyter.com/document/doi/10.1515/hf-2022-0096/html
  -https://github.com/pywood21/holz_202209