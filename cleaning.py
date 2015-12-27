# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import nltk
import pymorphy2
import re
import operator
from stop_words import get_stop_words
from collections import defaultdict

Count = defaultdict(int)

def countArtOfDay(y, m, d, Count):
    try:
        f = open("data/" + y + "_" + m + "_"+d+".txt", 'rw')
    except:
        raise

    morph = pymorphy2.MorphAnalyzer()
    articleText = ""
    stop_words = get_stop_words('russian')
    # stop_words.extend([u'это', u'как', u'так', u'и', u'в', u'над', u'к', u'до', u'не', u'на', u'но', u'за', u'то', u'с', u'ли',
    # u'а', u'во', u'от', u'со', u'для', u'о', u'же', u'ну', u'вы', u'бы', u'что', u'кто', u'он', u'она', u'который', u'этот',
    # u'сей', u'тот', u'также', u'быть', u'мочь', u'такой', u'кроме', u'-', u'который',u'быть', u'мочь',
    # u'стать', u'наш', u'свой',u'самый', u'другой',u'очень',u'дать', u'однако', u'весь', u'который', u'такой', u'самый', u'из-за', u'какой-то', u'который'])

    text = f.read().decode('utf8')
    text = re.sub(u'[^а-яА-Я\-\s]','',text)

    articleText = articleText + " " + text.lower()

    tokens = nltk.word_tokenize(articleText)
    tokens = [w for w in tokens if not w in stop_words]

    final = []

    for a in tokens:
        final.append(morph.parse(a)[0].normal_form)

    for word in final:
        Count[word] += 1



DIR = 'data' #path
files = [f for f in listdir(DIR) if isfile(join(DIR, f))]

for l in files:
    l = l[0:-4]
    dt = l.split("_")
    try:
        articlesCount = countArtOfDay(dt[0], dt[1], dt[2], Count)
    except:
        a = 1


newlist = sorted(Count.items(), key=operator.itemgetter(1), reverse=True)
file = open('counts/counted.txt', 'w')

for bn in newlist:
    file.write((bn[0]+" "+str(bn[1])+"\n").encode('utf8'))

file.close()