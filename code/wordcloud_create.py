import MeCab
import sys
import re
from collections import Counter
import csv
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager # 文字化け対策
import japanize_matplotlib


def keitaiso_mecab(infile):

    #csvファイル読み込み
    with open(infile) as f:
        timelines = f.read()
    #整形httpsから始まる文字を削除
    #参照：https://www.megasoft.co.jp/mifes/seiki/s310.html
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", timelines)
    # *が多いため、削除
    text.strip("*")

    # MeCabを使用してテキストを形態素解析
    m = MeCab.Tagger ('-Ochasen')

    node = m.parseToNode(text)

    words=[]

    while node:
        hinshi = node.feature.split(",")[0]

        if hinshi in ["名詞","動詞","形容詞"]:
        # if hinshi in ["名詞"]:

            origin = node.feature.split(",")[6]
            words.append(origin)
        node = node.next

    #stopwordの指定
    stop_words = ["する","なる","くる", "ある","いる","てる", "の", "れる", "られる","これ", "それ","さ", "ん", "こちら", "い", "がる", "こと", "せる", "そう"]
    words = [word for word in words if word not in stop_words]

    return words


def csv_write(csv_file_name,counter,words,random_num):

    word_list = []
    count_list = []

    #csvファイルへ書き込み
    with open(csv_file_name, 'w') as f:

        writer = csv.writer(f)
        writer.writerow(['word','count'])
        #csvファイルのヘッダーを設定

        #top10取得用
        i=0
        for word, count in counter.most_common():
            #*が不要のため、除外
            if word !="*":
                writer.writerow([word,count])

                #20位のみ取得
                if word!= i < 20:
                    #図示作成用
                    word_list.append(word)
                    count_list.append(count)
            i=i+1

    pltbarh(word_list,count_list,random_num)


def wordcloud(words,fpath,random_num):
    #wordcloud
    #wordcloudのために、文字列を結合
    wordC_text = ' '.join(words)
    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500).generate(wordC_text)
    URL1 = "../static/image/wordcloud_sample.jpg"
    index1 = URL1.find(".jpg")
    final_URL1 = URL1[:index1] + random_num + URL1[index1:]
    wordcloud.to_file(final_URL1)


####top10のみ図示する

def pltbarh(word_list,count_list,random_num):
    #配列逆順
    word_list.reverse()
    count_list.reverse()

    plt.figure()
    plt.rcParams['font.family'] = 'IPAexGothic'
    plt.barh(word_list, count_list)
    plt.xlabel("word")
    plt.ylabel("count")
    URL2 = "../static/image/figure.jpg"
    index2 = URL2.find(".jpg")
    final_URL2 = URL2[:index2] + random_num + URL2[index2:]
    plt.savefig(final_URL2)


def main():

    # テキストファイルの読み込み
    infile='../static/csv/tweet_text1.csv'
    fpath='/Library/Fonts/Arial Unicode.ttf'
    csv_file_name='../static/csv/result1.csv'

    random_num  =  str(random.randrange(1000))
    words = []
    words=keitaiso_mecab(infile)

    # カウントの降順で出力(カンマ区切り)
    counter = Counter(words)

    csv_write(csv_file_name,counter,words,random_num)
    wordcloud(words,fpath,random_num)
    return random_num
