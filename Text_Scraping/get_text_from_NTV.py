#!/usr/bin/env python
# coding: utf-8

# In[1]:


import codecs
import requests
import httplib2
import datetime
import unicodedata 
from bs4 import BeautifulSoup,SoupStrainer
import html.parser as htmlparser
parser = htmlparser.HTMLParser()

#source = open("feature_cnn_d9.txt","w")


def normalize_text(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.replace(u'\\n', u' ')
    text = text.replace(u'\\', u' ')
    text = parser.unescape(text)
    return text
    
index = 0
def get_text(url):
    global index
    date = datetime.datetime.now()
    key_words = ["korona", "Kovid-19", "Corona", "Korona","corona","covid-19"]
    filter_element = "application/ld+json"
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    x = soup.find_all('script',type=filter_element)
    try:
        headline = str(x[1]).split("headline")[1].split("image")[0][3:-3]
        text1 = str(x[1]).split("description")[1].split("articleSection")[0][3:-3]
        text2 = str(x[1]).split("articleBody")[1].split("wordCount")[0][3:-3]
        date = str(x[0]).split("datePublished")[1].split("dateModified")[0][3:-3]
        label = str(x[1]).split("articleSection")[1].split("articleBody")[0][3:-3]
    except:
        headline = str(x[0]).split("headline")[1].split("image")[0][3:-3]
        text1 = str(x[0]).split("description")[1].split("articleSection")[0][3:-3]
        text2 = str(x[0]).split("articleBody")[1].split("wordCount")[0][3:-3]
        date = str(x[1]).split("datePublished")[1].split("dateModified")[0][3:-3]
        label = str(x[0]).split("articleSection")[1].split("articleBody")[0][3:-3]
    
    headline = normalize_text(headline)
    text1 = normalize_text(text1)
    text2 = normalize_text(text2)
    try:
        text2 = text2.replace(text1[:-1],"")
    except:
        text2 = text2
    text = text1 + text2
    for k in key_words:
        if k in text:
            text_file = codecs.open("./NTV_Clean/"+str(index) +".txt","w",encoding="utf-8")
            text_file.write(label + "\n" + headline + "\n" +  date+ "\n"+text1+"\n"+text2+"\n"+url)
            text_file.close()
            index = index +1
            break
            #source.write("name: " + str(index)+ " link: " + url + " date: " +str(date.year) + "-" + str(date.month) + "-" + str(date.day)+ "\n")

list_of_link = open("./list_of_link.txt","r",encoding="utf-8").readlines()


for url in list_of_link:
    try:
        get_text(url.strip())
    except Exception as e:
        print(e)

