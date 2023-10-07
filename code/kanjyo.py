# -*- coding: utf-8 -*-


# importゾーン
import pandas as pd
import os
import numpy as np
import json
from matplotlib import pyplot as plt
import seaborn as sns; sns.set()
import random
from google.cloud import language_v1
from google.cloud.language_v1 import gapic
from google.cloud.language_v1.gapic import enums
from google.cloud.language_v1 import types


def kanjyo():

    # Google API　認証キー（事前にディレクトリに秘密鍵をDL）
    #ここは伏せます（安田健士郎）
    credential_path = "##############"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    client = language_v1.LanguageServiceClient()


    # tweets.csvの読み込み
    df_tweet = pd.read_csv('../static/csv/tweet_text1.csv', encoding='utf-8')


    # Google Cloud Natural Language API　に分析を任せる。
    ScoreList = []

    for index,text in df_tweet.iterrows():
        document = types.Document(
        content=str(text["text"]).encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        ScoreList.append(sentiment.score)

    df_tweet["Score"] = ScoreList


    # 感情分析ヒストグラムの作成
    sns.displot(df_tweet["Score"].fillna(-2),kde=False)


    # Cookieの使用により、URLにランダム番号を挿入し、保存
    random_num  =  str(random.randrange(1000))
    URL1 = "../static/image/plotfig.jpg"
    index1 = URL1.find(".jpg")
    final_URL1 = URL1[:index1] + random_num + URL1[index1:]
    plt.savefig(final_URL1)


    # 感情割合円グラフの作成
    percount_min=0
    percount_pra=0
    percount_mid=0

    for i in range(len(df_tweet["Score"])):
        if df_tweet["Score"][i]<0:
            percount_min=percount_min+1
        elif df_tweet["Score"][i]>0:
            percount_pra=percount_pra+1
        elif df_tweet["Score"][i]==0:
            percount_mid=percount_mid+1

    percent_min = percount_min/len(df_tweet["Score"])*100
    percent_pra = percount_pra/len(df_tweet["Score"])*100
    percent_mid = percount_mid/len(df_tweet["Score"])*100

    percent = [percent_min,percent_pra,percent_mid]

    label = ["BAD","GOOD","MIDDLE"]
    plt.figure()
    plt.pie(percent, labels=label, autopct="%1.1f%%")


    # Cookieの使用により、URLにランダム番号を挿入し、保存
    URL2 = "../static/image/graph.jpg"
    index2 = URL2.find(".jpg")
    final_URL2 = URL2[:index2] + random_num + URL2[index2:]
    plt.savefig(final_URL2)


    #　ランダム番号を戻り値
    return random_num
