# Image-Analysis for Plant Biologists with Python

## 序章
### 本書の目的と対象読者
- 本書は、植物科学者や農学者が植物の画像を解析し、いわゆる植物フェノタイピングを行うために必要な知識を提供する実践形式の資料集です。
- Pythonの基本的な使い方について詳しく解説しません。既に書店やインターネット上には良質なPythonのチュートリアルや技術記事が豊富に存在します。それらのリソースを活用することを強くお勧めします。
- 各章ではGoogle Colaboratory（Jupyter Notebook）を用いた実行可能なコードとその解説を提供します。ChromeブラウザとGoogle関連サービスへのアクセスが可能なインターネット環境があれば、誰でも手順を再現できます。
- 本書では画像解析、機械学習、深層学習のために使用するライブラリやフレームワークを統一せず、それぞれのテーマに最適なものを紹介します。これは、読者が多様なコードの書き方に触れることが重要と考えるからです。
- 課題解決に際し、より好ましい道筋はあっても、唯一無二の正しいアプローチはありません。
- 本書を通じて、読者自身が植物画像解析を行う能力を身につけることを目指します。また、自分自身で解析が行えなくとも、他者に適切な相談ができるようになることを期待しています。つまり、「どのようなコード（手法）を使えば何ができるのか」を理解することが本書の目的です。
- 本書はバイオインフォマティクス以外の分野の研究者が新たなスキルを身につける助けとなることを願っています。"AI"の流行に乗じて不適切な方法で売り込もうとする人たちに騙されないよう、自身で価値を判断できる力を身につけることが重要です。
- 本来はColaboratoryのような対話型実行環境だけでなく、Pythonのスクリプトを記述し、直接実行できるようになることが望ましいです。しかし、本書では読者が簡単にコードを実行できるようにするために、本形式を採用しました。本書を読了後、読者がスクリプトを実行するための環境を構築することを期待しています。
- レポジトリやデータセットにはライセンスが各々付与されています。本書では、非商用の制限があるものは取り扱いません。本書のコードはApache 2.0で公開します。ただし、GPLv3のライセンスが付与されているレポジトリについてはGPLv3を優先して継承します。各章のライセンスのご注意ください。

### 免責事項
- Colaboratoryや、依存するpypiパッケージの仕様が変更されることにより、本書のコードが実行できなくなる可能性があります。例えばColaboratoryにプレインストールされているpytorchやtensorflowのバージョンの変更などがあげられます。その場合は、本書のコードを適宜修正する必要がありますが、その責任は筆者にはありません。それでもなお、本書のレポジトリにおいて最新の動作コードの提供を目指します。ご了承ください。

### 見本
セルのコードの書き方、コメント行、マークダウンセル、実行結果、画像可視化、データフレーム出力について説明する。

### Plant Phenotyping Themes
- U-Net
- きゅうりの形状解析
  - cc by
    - https://github.com/workpiles/CUCUMBER-9
    - ![img_3.png](assets/img_3.png)
- イネ種子の割れ米分類
  - classical, svm, cnn
- 葉や果実の形状解析
  - 楕円フーリエ記述子を使ったクラスタリング、潜在空間へのマッピング
  - 
  - 
- 植物病害クラス分類 (PlantVillage)
  - CNN学習
    - keras sequential API?を使ってcnnを自分で書いてみる
    - 特徴量の可視化
- Arabidopsis leaf segmentation
  - https://zenodo.org/record/168158
  - cc by attribution
  - ![img_2.png](assets/img_2.png)
- 植物病斑物体検出（PlantDoc）
  - yolo-x
  - yolov8
- 領域分割（Arabidopsis Leaf Dataset）
  - unet
- 顕微鏡画像解析がなにか１つほしい
  - ためしげさん　気孔
    - detectron2?
- ドローンの物体検出植物
  - https://www.mdpi.com/2072-4292/12/8/1246
  - ccby4.0
  - ![img.png](assets/img.png)
- 小麦穂検出（global wheat dataset challenge）
  - ![img_1.png](assets/img_1.png)
  - LICENSEを確認
    - yolov8? 
    - kaggleの使い方
- VegAnn
  - https://www.nature.com/articles/s41597-023-02098-y
  - ccby4.0
### 応用
- 葉脈パターンのグラフ変換と種分類
  - https://www.jstage.jst.go.jp/article/jsbbs/72/1/72_21078/_article/-char/ja/

### Common Dataset Format
- COCO Format
- PASCAL VOC Format
- TFDataset

### おまけ
- u2netによる背景除去
- Foundation modelを活用したゼロショット推論
- colab以外の実装形態
  - .pyファイル
  - ウェブ形式
    - streamlit, gradio ....