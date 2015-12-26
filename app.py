# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib3
import time # Старый низкоуровневый модуль
import datetime # Новый модуль для работы с датой и временем


def makeUrl(year,month,day):
    date = year+'/'+month+'/'+day+'/'
    link = 'http://www.mk.ru/politics/'+date
    return link

def getArticleUrl(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(''.join(r.data))
    some = soup.find("ul", { "class" : "big_listing" })
    a = some.findAll("a", { "class" : "mkh2" })
    urlList=[]
    for item in a:
        urlList.append(item["href"])
    return urlList



def getText(urlList):
    http = urllib3.PoolManager()
    cleanArts=""
    for url in urlList:
        r = http.request('GET', url)
        soup = BeautifulSoup(''.join(r.data))
        article = soup.find("div", { "class" : "content" })

        for p in article.findAll('p'):
            div = p.findAll("div")
            [comment.replaceWith(" ") for comment in div]
            a = p.findAll("a")
            [comment.replaceWith(" ") for comment in a]
            span = p.findAll("span")
            [comment.replaceWith(" ") for comment in span]
            cleanArts = cleanArts + " " + p.text
        cleanArts=cleanArts+"\n\n"

    return cleanArts










dt = datetime.datetime.now()
timedelta1 = datetime.timedelta(days=1)
howMuchDaysInterval = 1

for i in range(howMuchDaysInterval):
    url = makeUrl(str(dt.year), str(dt.month), str(dt.day))
    urlList = getArticleUrl(url)
    if not urlList:
        break
    text = getText(urlList)
    f = open('data/'+str(dt.year)+'_'+str(dt.month)+'_'+str(dt.day)+'.txt', 'w')
    f.write(text.encode('utf8'))
    f.close()
    dt = dt - timedelta1