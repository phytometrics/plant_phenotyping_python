# 教材の作り方

- 初学者が何をすれば把握できる程度の知識を付与する & 自分でプログラミングできる、させたい人たちにこれ一冊渡せばなんとかなる、を両立するレベルのものにしたい。できるかしらんけど。

- google colaboratory （もしくは相当のクラウドノートブック）で完結するような形式にする
    - colabで作る場合、最初にcolabで作成→コピーをgithubレポジトリに保存する、で当該レポを指定して、notebooks/hogehoge.ipynbと保存する
- 無理がなければjavascriptでUI簡易実装でもよいんじゃない？

- ただし、colab無料枠でngrokとかfastapiとかban対象になるとか聞いたのでちょっと注意する。

- YOLOXやYOLOv5のようにcolabのデモで!python train.py ~~~ みたいなのあるし、そういう形式の事例をのっけてもよいこととする。全部関数記載だと理解の妨げになることもある。

- モデルの訓練がある場合は、極力実行コードをのせることにする。ただし、正常動作確認すれば３分クッキングみたいに、推論部分はできたものを提示、でもよい。
- モデルのサイズが100Mb超えるとgitのレポジトリにのっけることができない。のせないか、最後にzenodo相当のものにアップしてリンクを貼ってwgetみたいな？

- 複雑すぎるアルゴリズムはpypiに登録しちゃうか、ライブラリでまとめてone linerで実行でもよいかも。解説の親切さに依存する。

- 挿絵に関してはgitのレポにアップした画像を引用する形を望む。相対パスだとgithubで見えるけれどcolabでは見えない。vscodeとかIDEのgithubアップ機能を活用するか手動でリンクをはる。小さい画像ならbase64で直接埋め込んでもよい、かも。  挿絵の形式については最後に調整するのでplaceholderでもよいとする。

- notebookやコラム中の引用については、\<sup>数字\</sup>のように記述して、〜のデータセット<sup>1</sup>のようにあらわす。最後のマークダウンセルか文末に
1. 引用文献１
2. リンク１
3. ....

のようにまとめる。引用形式は今のところ自由。最後に統一する（いまのうちに決めたほうがよい？）

#  気をつけること
- GPLv3は使用しても問題ない。商用利用不可に関してはデータセット、レポジトリなどの使用は極力避ける。確認のため、使用レポやデータに関してはライセンス明記する。ex. [U<sup>2</sup>-Net (U-Square Net)を利用した葉領域抽出](notebooks/u2netp.ipynb)
