# エラーは怖くない：自分で解決できるようになろう

プログラミングにはエラーメッセージの理解とデバッグがつきものです。プログラミング初心者の人にとっては自分の書いたコードを理解するのに手一杯なのにエラーの理解なんてできない！と考える人も多いと思います。ただ、きちんとエラー出力を読めば、何がいけないのか理解できる形で表示されていることが多いため、それを手がかりにデバッグに努めましょう。

初心者がやりがちな間違いを紹介します。

## やりがちなミスとエラー出力の例

### 変数名のタイポ（打ち間違い）
```python
apple = 10
print(appel)  # appleのつづりミス
```
```shell
NameError: name 'appel' is not defined
```

### 0での除算
```python
result = 10 / 0  # 10を0で割る
```
```shell
ZeroDivisionError: division by zero
```

### インデックスの範囲外アクセス
```python
my_list = [1, 2, 3] 
print(my_list[3])  # my_list[0] ~ my_list[2]までしか指定できない
```
```shell
IndexError: list index out of range
```

### 未定義の関数呼び出し
```python
unknown_function()　# unknown_function()を定義せずに使う
```
```shell
NameError: name 'unknown_function' is not defined
```

### インデントのエラー
```python
def greet():
print("Hello!")  # タブ1つもしくはスペース4つ分でインデントしなければならない
```

```shell
IndentationError: expected an indented block
```
### 括弧のミス
```python
print("Hello, World!"  # 括弧の閉じ忘れ
```
```shell
SyntaxError: unexpected EOF while parsing
```

### 型の不一致
```python
age = "20"  # この変数は数値ではなく、文字列
print(age + 5)  # 文字列　+ 数値　は型の不一致
```
```shell
TypeError: can only concatenate str (not "int") to str
```

### 未初期化の変数の使用
```python
print(x)  # x = 1などと宣言せずにxを使おうとする
```
```shell
NameError: name 'x' is not defined
```
### 辞書のキーが存在しない
```python
my_dict = {'apple': 10}
print(my_dict['banana'])  # my_dictにはappleキーしか存在しない
```
```
KeyError: 'banana'
```
### ライブラリやモジュールのインポートエラー
```python
import numpy as np  # numpyをインストールしていないのにインポートしようとしている
```
```shell
ModuleNotFoundError: No module named 'numpy'
```

### インポートした関数を変数などで再定義してしまう

``` python
from skimage.measure import label

# labelという名前の変数を定義して上書きしてしまう
label = "some text"

# この後でskimageのlabel関数を使用しようとするとエラーが発生する
result = label(image)
```

```shell
TypeError: 'str' object is not callable
# skimageのlabel機能ではなく、文字列として上書きしてしまっているために生じたエラー。
```

## エラーってどうやって読むの？

下のようなコードをcolaboratoryで実行したとします。
```python
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    result = a - b
    return result

def multiply_numbers(a, b):
    c = a * b
    return res

def divide_numbers(a, b):
    return a / b

print(add_numbers(5, 3))
print(subtract_numbers(5, 3))
print(multiply_numbers(5, 3))
print(divide_numbers(5, 3))
```
下のようなエラーを含む出力結果が得られました。
```shell
8
2
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-b96fa697b89b> in <cell line: 17>()
     15 print(add_numbers(5, 3))
     16 print(subtract_numbers(5, 3))
---> 17 print(multiply_numbers(5, 3))
     18 print(divide_numbers(5, 3))

<ipython-input-1-b96fa697b89b> in multiply_numbers(a, b)
      8 def multiply_numbers(a, b):
      9     c = a * b
---> 10     return res
     11 
     12 def divide_numbers(a, b):

NameError: name 'res' is not defined
```
1. add_numbersとsubtract_numbersが正常に実行され、まず8と2が出力されます。
2. 17行目のmultiply_numbersを実行しようとしてエラーが出ました。
    ```shell
    ---> 17 print(multiply_numbers(5, 3))
    ``` 
3. multiply_numbers関数を定義する部分を見てみるとc = a * bと書いているのでreturn cと書くべきところがresを使っているのでエラーが出ていることがわかります。
    ```shell
    ---> 10     return res
    ...
    NameError: name 'res' is not defined
    ```

multiple_numbersの戻値をreturn resからreturn cとすれば解決するでしょう。

## エラーの調べ方
エラーメッセージだけで問題を解決するのは難しい場合もあります。そのような場合は、インターネットで調べるのも有効です。例えば、Stack OverflowやQiita, Zennなどのコミュニティや情報共有サイトは、多くのプログラマーが日常的に利用している質問応答サイトや技術情報を共有する場所です。エラーメッセージや問題のキーワードをこれらのサイトの検索ボックスに入力してみると（或いはgoogleの検索エンジンの結果からサイトの記事に直接飛ぶと）、同じ問題に直面して解決方法を見つけた他のプログラマーの経験や知識が共有されていることが多いです。

もちろん、全ての記事が正しいことを言っているとは限りません。たとえ正しかったとしても昔の環境に対する解決方法で今のあなたの環境での解法となるとは限りません。記事や回答のイイネ（up vote）や執筆・回答日時を確認して、信頼ある情報を選別できるように練習しましょう。

そしてChatGPTなどの生成AIもエラーの解決の手助けとなることがあります。コードとエラーメッセージをそのまま貼り付けて質問するだけで、可能な解決策やヒントを得ることができることがあります。様々なツールを駆使し、自身でエラーを解決できるようになりましょう。

### おまけ
- ChatGPT4に下記のコードをエラー付きで質問してみましょう
    ```shell
    age = "20"
    print(age + 5)

    TypeError: can only concatenate str (not "int") to str
    ```
- ChatGPT4の返答
    - The error you're seeing is due to the fact that the variable age is a string (because it's enclosed in quotes), and you're trying to add an integer (5) to it. In Python, you can't directly add a string to an integer.
    - To fix this, you need to convert the string to an integer first using the int() function. Then you can perform the addition:

        ```python
        Copy code
        age = "20"
        print(int(age) + 5)
        ```
- 追加で質問しましょう。「日本語で答えてください。python初心者なのでわかりやすく丁寧にお願いします。」
- ChatGPT4の返答
    - あなたが書いたコードのエラーは、age という変数が文字列（ダブルクオーテーションで囲まれているため）で、その文字列に整数（5）を足そうとしているからです。Pythonでは、文字列と整数を直接足すことはできません。
    - この問題を解決するためには、文字列を整数に変換する必要があります。そのための関数が int() です。以下のように書き換えれば、計算ができます。
    ```python
    age = "20"
    print(int(age) + 5)
    ```
    - このコードを実行すると、出力結果は 25 になります。
    - この int() 関数は、文字列を整数に変換するためのものです。この変換を行った後に、整数の足し算をすることができます。

便利な時代になりましたね。