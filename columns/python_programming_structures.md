| 単位              | 説明                                                                                           | 例示                                      |
|-------------------|------------------------------------------------------------------------------------------------|-------------------------------------------|
| Function (関数)   | 特定のタスクを実行する再利用可能なコードブロック。関数は入力を受け取り、出力を返すことが（も）できます。   | `def greet(name): return f"Hello, {name}!"` |
| Class (クラス)     | オブジェクトを作成するための設計図。クラスはデータとそのデータに対して操作を行うメソッドをカプセル化します。| `class Dog: def __init__(self, name): self.name = name` |
| Module (モジュール)| Pythonの定義と文が含まれているファイル。モジュールは関数、クラス、変数を含むことができます。          | `utils.py` という名前のファイルに複数の関数またはクラスを含んでいるもの。 |
| Package (パッケージ) (コード) | 複数のモジュールまたはサブパッケージを含むディレクトリで、`__init__.py` ファイルを含んだパッケージであることを示します。 | `mypackage` というディレクトリは `__init__.py`, `module1.py`, `module2.py` を含んでいるもの。|
| Library (ライブラリ) | 複数のモジュールおよび/またはパッケージをまとめたもの。               | `numpy`, `pandas`, `requests`  |
| Framework (フレームワーク) | ソフトウェアプロジェクトを開発するための定義済みの構造を提供するライブラリおよびツールのセット。   | `Flask`, `PyTorch`, `Tensorflow`   |