# Plant Phenotyping for Biologists with Python

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

## Part 0: Warm Up

### [割米判定アルゴリズムの作成を通じた画像解析基礎](notebooks/rice_proper_broken.ipynb)

- 画像解析基礎
- 最適な閾値のマニュアル定義

### 時系列データ解析基礎

### [グリーンハウスの環境データ分析](notebooks/env_data_analysis.ipynb)

- pandasやplotlyを用いた表データ操作・分析・可視化

## Part 1: Conventional Image Analysis Aproach for Plant Phenotyping

### [種子計数形状解析（１）](notebooks/rice_seed_shape_analysis.ipynb)

- scikit-imageのregionpropsとwatershedを利用したオブジェクトの計数と形状解析

### [ブドウ花粉活性度評価](notebooks/pollencounter.ipynb)

- ImageJマクロのPython再実装
- scikit-imageのregionpropsとwatershedを利用したオブジェクトの計数

### [WEIPS：ドローン画像からの雑草除去およびキクイモ表現型定量](notebooks/WEIPS.ipynb)

- MATLABコードのPython再実装
- RGBとDepth情報を用いた領域抽出
- オルソモザイク画像とデジタルサーフィスモデル画像からの表現型抽出

### [リンゴの葉形状と遺伝的多様性の解析](notebooks/apple_leaf.ipynb) （未完）

- 楕円フーリエ記述子と輪郭形状解析
- SNPを利用したPCA/GWAS/GS 解析

### [Aravib: シロイヌナズナの茎振動の定量](notebooks/aravib.ipynb)

- Color Thresholdによる特徴点抽出とトラッキング
- scipyのfftを活用した振動解析

## Part 2: Training Deep Learning Models for Plant Phenotyping

### [植物病害識別診断モデルの作成](notebooks/plantvilllage.ipynb)

- plantvillageデータセットの活用
- tensorflow.kerasを活用したCNNモデルの構築と訓練

### [大麦種子識別モデルの作成](notebooks/barley_seed_classification.ipynb)

- tensorflow.kerasを活用したCNNモデルの構築と訓練
- 現場データ収集における問題（データ不足、データ不均衡）に対応する
  - class weight
  - 転移学習
  - データ拡張

### ドローン画像からのテンサイ個体認識と病気重症度定量

- https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giac054/6610009

### [作物・雑草セグメンテーションモデルの作成](notebooks/phenobench.ipynb)

- phenobenchデータセットの活用
- segmentation_models_pytorchを用いたセグメンテーションモデルの作成
  - Binary Semantic Segmenatation
  - MultiClass Semantic Segmentation

### [小麦穂検出モデルの作成](notebooks/globalwheat2021.ipynb)

- Global Wheat Head Dataset 2021の活用
- YOLOv8物体検出モデルの学習と推論

### 統合型作物検出・セグメンテーションモデルの開発

- GrowliFlowerデータセットの活用
- detectron2ライブラリの活用

  - object detection
  - semantic segmenatation
  - instance segmenatation

### 深層学習モデルの特徴量解釈

- CNN系の特徴量可視化(Grad-CAMなど)

## Part 3: Utilizing Trained Deep Learning Models for Plant Phenotying

### 種子計数形状解析（２）

- Mask-RCNNを利用した種子Intance Segmentation

### [DeepStomata: マルバツユクサの気孔開度定量](notebooks/dayflower_stomata_quantification.ipynb)

- HOG特徴量を利用した気孔検出
- CNNによる気孔開閉判定
- scikit-imageのregionpropsを利用した気孔開口領域単離と定量

### [イネ収量予測](notebooks/riceyieldcnn.ipynb)

- 学習済CNNモデルを利用したイネ収量推論

### [ChronoRoot:アガープレート生育のシロイヌナズナ根計測](notebooks/chronoroot.ipynb)　（未完）

- semantic segmentationによる根領域の抽出
- 時系列補正
- skeletonizationによるグラフ構造抽出

### [StomaAI:シロイヌナズナの表皮断片顕微鏡画像からの気孔開度定量](notebooks/sai.ipynb)

- detectron2によるinstance segmenatation + keypoint detection

### シロイヌナズナのリーフディスク顕微鏡画像を利用した気孔開度定量

- YOLOXによる気孔検出
- Segmentation Modelsによる気孔開度検出

### [PlantSeg:3D共焦点画像からの細胞壁検出と細胞インスタンス・セグメンテーション](notebooks/plantseg.ipynb)

### [U2-Net (U-Square Net)を利用した葉領域抽出の試み](notebooks/u2netp.ipynb)

## Part X: Foundation Models for Plant Phenotyping

### Grounding DINO

### Segment Anything

- https://github.com/yformer/EfficientSAM

### Vision Task対応LLM

## 他、実装検討中

#### ブロッコリー生育予測

- Drone-Based Harvest Data Prediction Can Reduce On-Farm Food Loss and Improve Farmer Income
  - cc-by
  - [https://spj.science.org/doi/10.34133/plantphenomics.0086](https://spj.science.org/doi/10.34133/plantphenomics.0086)
- [https://github.com/UTokyo-FieldPhenomics-Lab/UAVbroccoli](https://github.com/UTokyo-FieldPhenomics-Lab/UAVbroccoli)
  - MIT。ただしyolov5はGPLv3

#### 葉脈解析

- Network feature-based phenotyping of leaf venation robustly reconstructs the latent space

  - [https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010581](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010581)
  - cc-by
- [https://zenodo.org/records/8020856](https://zenodo.org/records/8020856)
  ----------------------------------
- [https://github.com/MorphometricsGroup/iwamasa-2022](https://github.com/MorphometricsGroup/iwamasa-2022)

  - mit

#### Cell segmentation and tracking from time-series sequential images

- Flexural behavior of wood in the transverse direction investigated using novel computer vision and machine learning approach
  - [https://www.degruyter.com/document/doi/10.1515/hf-2022-0096/html](https://www.degruyter.com/document/doi/10.1515/hf-2022-0096/html)
  - cc-by
- [https://github.com/pywood21/holz_202209](https://github.com/pywood21/holz_202209)

### 他

- colab以外の実装形態
  - .pyファイル
  - ウェブ形式
    - streamlit, gradio ....
- VegAnn
  - [https://www.nature.com/articles/s41597-023-02098-y](https://www.nature.com/articles/s41597-023-02098-y)
  - ccby4.0
  - [https://www.degruyter.com/document/doi/10.1515/hf-2022-0096/html](https://www.degruyter.com/document/doi/10.1515/hf-2022-0096/html)
    -[https://github.com/pywood21/holz_202209](https://github.com/pywood21/holz_202209)
