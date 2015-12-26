# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import nltk
import pymorphy2
import re
from collections import Counter
from nltk.corpus import stopwords
nltk.download('stopwords')

def countArtOfDay(y, m, d):
    try:
        f = open("data/" + y + "_" + m + "_"+d+".txt", 'rw')
    except:
        raise

    morph = pymorphy2.MorphAnalyzer()
    articleText = ""
    stop_words = stopwords.words('russian')
    stop_words.extend([u'это', u'как', u'так', u'и', u'в', u'над', u'к', u'до', u'не', u'на', u'но', u'за', u'то', u'с', u'ли',
    u'а', u'во', u'от', u'со', u'для', u'о', u'же', u'ну', u'вы', u'бы', u'что', u'кто', u'он', u'она', u'который', u'этот',
    u'сей', u'тот', u'также', u'быть', u'мочь', u'такой', u'кроме', u'-'])

    text = f.read().decode('utf8')
    text = re.sub(u'[^а-яА-Я\-\s]','',text) #delete all not bukva
    articleText = articleText + " " + text.lower()

    tokens = nltk.word_tokenize(articleText)
    tokens = [i for i in tokens if (i not in stop_words)]

    final = []

    for a in tokens:
        final.append(morph.parse(a)[0].normal_form)

    return Counter(final)





DIR = 'data'
files = [f for f in listdir(DIR) if isfile(join(DIR, f))]

for l in files:
            l = l[0:-4]
            dt = l.split("_")
            try:
                countArtOfDay(dt[0], dt[1], dt[2])
            except:
                a = 1

# tokens = [i for i in tokens if (i not in string.punctuation)]
# tokens = [i for i in tokens if (i not in stop_words)]
# final=[]

# for azaza in tokens:
    # final.append(morph.parse(azaza)[0].normal_form)

# c = Counter(final)

# file = open('cleaned/final.txt', 'w')

# for item in c:
    # file.write(  (item +" : "+ str(c[item])+"\n").encode('utf8'))

# file.close()