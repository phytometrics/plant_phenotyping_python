# Image-Analysis for Plant Biologists with Python

#### [はじめに](columns/introduction.md)
## Table of Contents
### コラム
#### [なんでもかんでもAIっていうんじゃない](columns/using_the_term_AI.md)
#### [エラーは怖くない：自分で解決できるようになろう](columns/error.md)
#### [ファイルとフォルダの命名方法](columns/file_name.md)
#### [Pythonの命名規則](columns/styleguide.md)
#### [座標系と表記順序：xyなのかyxなのか、そして原点はどこなのか](columns/xyyxrc.md)
#### [機械学習におけるデータセットのフォーマット](columns/dataset_format.md)
#### [データリーク](columns/dataleak.md)
#### [巨人の肩での研究: ソフトウェアライセンスについて](columns/license.md)
#### [「レナ」を超えて](lenna.md)

### ハンズオン
#### プログラミング基礎
- Python（とColaboratory）の基礎
- 植物画像解析でよく使われるColaboratoryにおけるPythonコードの紹介
#### [イネ種子計数形状解析（１）](notebooks/rice_seed_shape_analysis.ipynb) 
#### [ブドウ花粉活性度評価](notebooks/pollencounter.ipynb)
- scikit-imageのregionpropsとWatershedを利用したオブジェクトの計数
- scikit-imageのregionpropsとWatershedを利用したオブジェクトの計数と形状解析
#### [リンゴの葉形状と遺伝的多様性の解析](notebooks/apple_leaf.ipynb)  *GWAS解析の検証とGSの追加が必要*
- 楕円フーリエ記述子と輪郭形状解析
- SNPを利用したPCA/GWAS/GS 解析
#### [植物病害識別診断モデルの訓練と通じたImage Classification型CNNの理解](notebooks/plantvilllage.ipynb)
- tensorflow.kerasを活用したCNNの学習と活用
- ファインチューニング
#### マルバツユクサの気孔開度定量
- HOG特徴量を利用した気孔検出
- CNNによる気孔開閉判定
- scikit-imageのregionpropsを利用した気孔開度定量
#### [イネ収量予測](notebooks/riceyieldcnn.ipynb)  
- 学習済CNNモデルを利用したイネ収量推論
#### [ドローン画像からの小麦穂検出モデル作成](notebooks/globalwheat2021.ipynb)
- YOLOv8物体検出モデルの学習と推論
#### イネの種子計数形状解析（２）
- Mask-RCNNを利用した種子Intance Segmentation
#### 雑草検出モデルの作成
- detectron2で全部やる
  - object detection
  - semantic segmenatation
  - instance segmenatation
#### [StomaAI:シロイヌナズナのepidermal peel気孔開度定量](notebooks/sai.ipynb)
- detectron2によるinstance segmenatation + keypoint detection
#### シロイヌナズナのleaf disc気孔開度定量
- YOLOXによる気孔検出
- Segmentation Modelsによる気孔開度検出
#### 機械学習モデルの解釈
#### [PlantSeg:3D共焦点画像からの細胞壁検出と細胞インスタンス・セグメンテーション](notebooks/plantseg.ipynb)

#### [U<sup>2</sup>-Net (U-Square Net)を利用した葉領域抽出の試み](notebooks/u2netp.ipynb)
#### 葉脈解析

  
- おまけ？
  - Segment Anything
  - Grounding DINO


- VegAnn
  - https://www.nature.com/articles/s41597-023-02098-y
  - ccby4.0

- colab以外の実装形態
  - .pyファイル
  - ウェブ形式
    - streamlit, gradio ....