# -*- coding: utf-8 -*-
import nltk
import string
import pymorphy2
import xlwt
from collections import Counter


from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')



morph = pymorphy2.MorphAnalyzer()

year = ['2011', '2012', '2013', '2014', '2015']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
       '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

text = ""

for y in year:
    for m in month:
        for d in day:
            try:
                f = open("data/" + y + "_" + m + "_"+d+".txt", 'rw')
                text = text + f.read().decode('utf8').lower()

            except:
                a=1

tokens = nltk.word_tokenize(text)
tokens = [i for i in tokens if ( i not in string.punctuation )]
stop_words = stopwords.words('russian')
stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на','»','«','«За','а'])
tokens = [i for i in tokens if ( i not in stop_words )]


final=[]

for azaza in tokens:
    final.append(morph.parse(azaza)[0].normal_form)

c = Counter(final)

file = open('cleaned/final.txt', 'w')

for item in c:
    file.write(  (item +" : "+ str(c[item])+"\n").encode('utf8'))

file.close()