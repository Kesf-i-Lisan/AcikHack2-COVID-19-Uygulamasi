#!/usr/bin/env python
# coding: utf-8

# In[1]:


import codecs
import requests
import httplib2
import datetime
from bs4 import BeautifulSoup,SoupStrainer


index = 0
def get_text(url):
    global index
    print(url)
    date = datetime.datetime.now()
    key_words = ["korona", "Kovid-19", "Corona", "Korona","corona","covid-19"]
    filter_element = "b-article__text"
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    x = soup.findAll("div", {"class": "story-body__inner"})
    text = x[0].findAll(text=True)
    text = str(text)[1:-1]
    for k in key_words:
        if k in text:
            print(text)
            text_file = codecs.open("./bbc/"+str(index)+ "d9"+ ".txt","w",encoding="utf-8")
            text_file.write(text.strip())
            text_file.close()
            index = index +1
            source.write("name: " + str(index)+ " link: " + url + " date: " +str(date.year) + "-" + str(date.month) + "-" + str(date.day)+ "\n")



# In[2]:


list_of_link = open("./list_of_link.txt","r",encoding="utf-8").readlines()

for url in list_of_link:
    http = httplib2.Http()
    status, req = http.request(url)
    for l in BeautifulSoup(req,"html.parser", parse_only=SoupStrainer('a')):
        if l.has_attr('href'):
            link = l['href']
            try:
                get_text("https://www.bbc.com"+link)
            except Exception as e:
                print(e)


# In[ ]:




