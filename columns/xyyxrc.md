# 座標系と表記順序：xyなのかyxなのか、nhwcなのかnchwなのか。

異なるライブラリを使って画像を操作する際、座標系とその表記の違いに遭遇することがよくあります。例えば、Numpy, OpenCV, scikit-image, Matplotlibなど、各ライブラリは独自の座標系やインデックス順序を採用しています。これらの違いを理解し、適切に扱うことは、画像処理タスクを効率的に遂行するために不可欠です。

特に機械学習のモデルを作成する場合、特段の理由が無い限り多くの方は正方形を入力形式とするでしょう。その場合縦横の順序が違っていてもエラーがなく動いてしまうので、「訓練できたけれど、使い物にならないモデル」に苦しむことになります。

間違えないためには公式のドキュメントを参照し、関数やクラスの使い方を把握することが重要です。代表的なものについて本稿で紹介します。

# Numpy
サイズ: image.shape で取得し、(行, 列, チャネル)の順で表示されます。画像を三次元のnumpy arrayで表現したとき、その次元情報はyxcの順番となります。

```python
import numpy as np
image = np.random.rand(100, 200, 3)  # 縦100px,横200px、3チャンネル（例えばRGB）のランダムノイズ画像を生成する
print(image.shape)  # (100, 200, 3)
pixel_value = image[50, 100]  # 左上を原点として、50行目100列目のピクセル値（色情報）を取得
```

# OpenCV
画像データはnumpyと同様の形式となりますが、resizeを始めとするオペレーションの多くはx,yの順番となります。

```python
import cv2
image = cv2.imread('image.jpg')  # 幅400px、高さ200pxの画像を読み込んだ場合
print(image.shape) # (200, 400, 3)

new_width = 200
new_height = 100
image = cv2.resize(image, (new_width, new_height))
print(image.shape) # (100, 200, 3)

```

# scikit-image 
opencvとは異なりy,xの順番を採用するオペレーションが多い印象です。

```python
from skimage.io import imread
from skimage.transform import resize

image = imread('image.jpg') # 幅400px、高さ200pxの画像を読み込んだ場合
print(image.shape) # (200, 400, 3)

new_height = 100
new_width = 200
image = resize(image, (new_height, new_width))
print(image.shape) # (100, 200, 3)
```

# Matplotlib

グラフ描画用のplotはx,yの順番となり、（通常）原点が左下となります。
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
plt.plot(x, y)
plt.show()  # 右肩上がりのy=xグラフ
```
ただし、plt.imshowで画像を表示させる場合、原点が左下から左上に変更されます（つまり、y軸が逆転します）。上と同じようなグラフをそのまま画像の上に重ね合わせたければy軸の値を正負逆にする必要があります。

```python
import matplotlib.pyplot as plt

plt.imshow(image)  # 画像を表示
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
plt.plot(x, -y)  # y軸が逆転しているのでyの値を正負逆にして対応させる。
plt.show()
```
使用頻度の高い他のコードで考慮すべき順序についても紹介します。
```python
plt.figure(figsize=(10, 5))  # 横10インチ、縦5インチの領域を用意します。

plt.subplot(2, 1, 1)  # 2行1列の1番目の位置（上側）
plt.plot(x, y)

plt.subplot(2, 1, 2)  # 2行1列の2番目の位置（下側）
plt.plot(y, x)
```


# Deep Learningフレームワーク
深層学習のフレームワークにおいて、RGB画像をNHWCやNCHW形式で扱うとの表現があります。

- N: Number of Samples。 バッチ数、つまり何個の画像をいっぺんに扱うかを意味します。単一画像の場合は1となります。
- H: Height。Numpyにおけるyと同義です。
- W: Width。Numpyにおけるxと同義です。
- C: Channel。Numpyにおけるchannelと同義です。RGB画像の場合3となります。

どのようなフォーマットで画像データを扱うかはライブラリによって異なります。以下は近年よく使われるフレームワークの要求フォーマットを表にまとめたものです。

| フレームワーク   | テンソルフォーマット   |
|--------------|-------------------|
| TensorFlow   | NHWC               |
| TFLite       | NHWC               |
| JAX          | NHWC               |
| Keras        | NHWC               |
| PyTorch      | NCHW               |
| ONNX         | NCHW               |
| CoreML       | NCHW               |


要求するフォーマットが違う場合、例えばnumpyのtransposeオペレーションを使って次元を入れ替えることができます。

```python
import numpy as np

# xがテンソルデータ（RGB画像データ）と仮定する。バッチサイズは10とする。
x = np.random.rand(10, 3, 128, 128)  # NCHW フォーマット

# NCHW -> NHWC
x_nhwc = np.transpose(x, (0, 2, 3, 1))
print(x_nhwc.shape)  # Output: (10, 128, 128, 3)

# NHWC -> NCWH
x_nchw = np.transpose(x_nhwc, (0, 3, 1, 2))
print(x_nchw.shape)  # Output: (10, 3, 128, 128)
```

レポジトリの訓練・可視化スクリプトなどをそのまま使う場合、このようなデータの次元を気にする機会は少ないと思います。しかしながら、自身でコードを書いたり改変したりする場合、入出力データがどうなっているかを把握し、理解しているいることは大切です。

---



<img src=https://cdn.jsdelivr.net/gh/phytometrics/plant_phenotyping_python@main/assets/69d1a3f36713caefbe55702e304a27d7afa09254ceec62a7b35e7b2a56bf793d.png width=25%>

打ち上げ花火を横から見るpython。dreamstudio (Stability AI)<sup>1</sup>を用いて生成しました。
1. https://dreamstudio.ai/generate
