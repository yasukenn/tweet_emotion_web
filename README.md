# Tweet Emotion Web

`tweet_emotion_web`は、任意の単語に対するツイート感情分析を実施するウェブアプリケーションです。

発表に使用した資料はこちら https://docs.google.com/presentation/d/1xine8HIPAEkH6JlbnZ6gyq_1gJakq6wFaKGjWq9Z1vg/edit?usp=sharing


## ディレクトリ構造
```
tweet_emotion_web
│
├── README.md
│
├── code
│ ├── app.py
│ ├── kanjyo.py
│ ├── tweet_get2.py
│ └── wordcloud_create.py
│
├── static
│ ├── csv
│ │ ├── result1.csv
│ │ └── tweet_text1.csv
│ │
│ └── image
│ ├── figureXXX.jpg
│ ├── graphXXX.jpg
│ ├── plotfigXXX.jpg
│ └── wordcloud_sampleXXX.jpg
│
└── templates
  ├── index.html
  ├── result.html
  └── search.html
```


## 使用方法

（TwitterAPIの開発状況により、使用不可能な可能性があります。）

1. 必要なライブラリやパッケージをインストールしてください。
2. TwitterAPIキーとGooglecloudのCloud Natural Language APIキーを取得し、設定してください。
3. `app.py`を実行して、ウェブアプリを起動します。
4. ブラウザからアクセスし、検索したい**ワード**と**総取得ツイート数**を設定してください。

## 開発者情報

明治大学大学院　先端数理科学研究科 ネットワークデザイン専攻

機械学習システム研究室　

安田健士郎
