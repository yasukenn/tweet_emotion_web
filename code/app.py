#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 02:35:04 2021

@author: yasudakenshirou
"""


from flask import Flask, render_template, request, redirect
from tweet_get2 import tweet_get_to_csv
from kanjyo import kanjyo
from wordcloud_create import  main

app = Flask(__name__)
    

@app.route('/')
def index():       
    #表紙画面              
    return render_template("index.html")

    
@app.route('/search')
def search():
    #単語、ワード数入力画面
    return render_template("search.html")
 
    
@app.route('/result', methods=["GET","POST"])
def result():
    #出力結果画面
    if request.method ==  "GET":
        return render_template("result.html")
    else:
        word  =  request.form.get("word")
        wordcount  =  request.form.get("wordcount")
        tweet_get_to_csv(word, wordcount)
        
        random_num = kanjyo()
        random_num2 = main()
        
        URL1 = "/static/image/plotfig.jpg"
        index1 = URL1.find(".jpg")
        final_URL1 = URL1[:index1] + random_num + URL1[index1:]
        
        URL2 = "/static/image/graph.jpg"
        index2 = URL2.find(".jpg")
        final_URL2 = URL2[:index2] + random_num + URL2[index2:]
        
        URL3 = "/static/image/wordcloud_sample.jpg"
        index3 = URL3.find(".jpg")
        final_URL3 = URL3[:index3] + random_num2 + URL3[index3:]
        
        URL4 = "/static/image/figure.jpg"
        index4 = URL4.find(".jpg")
        final_URL4 = URL4[:index4] + random_num2 + URL4[index4:]
        
        return render_template("result.html"
                               ,word=word
                               ,wordcount=wordcount
                               ,final_URL1=final_URL1
                               ,final_URL2=final_URL2
                               ,final_URL3=final_URL3
                               ,final_URL4=final_URL4)


if __name__ == "__main__":
    app.run(debug=True)
    
    

    