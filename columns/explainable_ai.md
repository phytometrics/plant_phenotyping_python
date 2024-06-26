# あなたの「説明可能なAI」研究は、本当に説明可能ですか？

近年、機械学習（深層学習）の分野で「説明可能なAI」（Explainable AI, XAI）が注目されています。これは、AIモデルの予測や判断の背後にある理由を人間が理解しやすい形で解釈できるようにする取り組みです。しかし、すべてのXAIを名乗るプロジェクトが、本当にその名の通り「説明可能」なのでしょうか？

例えば、深層学習モデルを訓練した後、複数の可視化手法を用いてモデルの判断根拠を視覚的に示すことのみをもって「説明可能なAI」と主張する場合があります。しかし、これだけでは十分な説明とは言えません。特定の病気であると判断された画像の場合、可視化手法間で結果が異なっていたら、どれを採用するでしょうか？直感と合致する手法だけを採用し、「人間の直感と一致した」と主張するのはチェリーピッキングに他なりません。さらに、可視化結果自体が訓練済モデル固有であり、条件を変えてモデルを再訓練すれば結果が大きく変わることもあります。このような場合、可視化結果はモデルの判断根拠を説明するものとして信頼性に欠けるでしょう。

AIの予測がどれだけ正確であっても、その結果が実際の専門知識や現場の経験と整合していなければ、その説明は信頼性に欠けます。真のXAIは、ドメインエキスパートの知識とともに運用され、相互補完するものであるべきです。

「説明可能なAI」は、単にモデルの内部を可視化するだけでなく、その予測がどのようにして導かれたのかを理解し、コミュニティにおけるコンセンサスを形成することで初めて成立するものです。可視化手法から得られた知見をもとに、遺伝学的・生理学的実験の設計や研究対象の生物学的意味を見出すことができれば、それは真のXAIと言えるでしょう。

<img width=50% src="assets/DALLE2023-11-03.png">

DALLE3で出力したExplainable AIを用いる研究者の図。生成プロンプトにExplainable AIを入れているにも関わらず、高確率で綴りを間違えます（2023年11月3日時点）。絵は正確に生成できるのに、なぜ文字は苦手なのか。その理由を人間が理解できる形で解釈できるようにする取り組みは、「説明可能なAI」の一例と言えるでしょう。
