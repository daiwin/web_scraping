# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
import urllib3
import datetime # Новый модуль для работы с датой и временем


def makeUrl(year, month, day, theme):
    date = year+'/'+month+'/'+day+'/'
    link = 'http://www.mk.ru/'+theme+'/'+ date
    return link


def getArticleUrl(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data,'html.parser')
    some = soup.find("ul", { "class" : "big_listing" })
    try:
        a = some.findAll("a", { "class" : "mkh2" })
    except:
        return
    urlList=[]
    for item in a:
        urlList.append(item["href"])
    return urlList



def getText(urlList):
	http = urllib3.PoolManager()
	cleanArts = ""
	for url in urlList:
		r = http.request('GET', url)
		soup = BeautifulSoup(r.data,'html.parser')
		article = soup.find("div", { "class" : "content" })
		if article is None:
			continue
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




dt = datetime.date(2014, 6, 23)
timedelta = datetime.timedelta(days=1)


theme='politics'

for x in range(3600):
    url = makeUrl(str(dt.year), str(dt.month).zfill(2), str(dt.day).zfill(2), theme)
    urlList = getArticleUrl(url)
    if urlList is None:
        dt = dt + timedelta
        continue
    else:
        text = getText(urlList)
        f = open('data/'+theme+'/'+str(dt.year)+'_'+str(dt.month).zfill(2)+'_'+str(dt.day).zfill(2)+'.txt', 'wb')
        f.write(text.encode(sys.stdout.encoding, errors='replace'))
        f.close()
        dt = dt + timedelta