#!/usr/bin/env python
# coding: utf-8
import unicodedata
import string
import re
from num2words import num2words



def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"([.!?])", r" \1", text)
    text = re.sub(r"[^a-zA-Zçğıüöş.!? ]+", r"", text)
    return text


def remove_puncation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def number2string(text):
    match = re.findall(r'(\d+)',text)
    for m in match:
        text = text.replace(m,num2words(int(m),lang="tr"),1)
    return text

def date2string(text,puncation="."):
    tr_months = ["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım","aralık"]
    try:
        match = re.findall(r'(\d+'+ puncation+'\d+' + puncation + '\d+)',text)
        for m in match:
            gün = num2words(int(m.split(puncation)[0]),lang="tr")
            ay = tr_months[int(m.split(puncation)[1])-1]
            yıl = num2words(int(m.split(puncation)[2]),lang="tr")
            text = text.replace(m,gün+" "+ay+ " " + yıl)
    except:
        return text
    return text

def time2string(text):
    match = re.findall(r'(\d+:\d+)',text)
    res = ""
    for m in match:
        try:
            s1 = m.split(":")[0]
            s2 = m.split(":")[1]
            text = text.replace(m,num2words(int(s1),lang="tr")+" "+num2words(int(s2),lang="tr"))
        except:
            return text
    return text

def full_normalization(text):
    text = time2string(text)
    text = date2string(text)
    text = number2string(text)
    text = normalize(text)
    return text