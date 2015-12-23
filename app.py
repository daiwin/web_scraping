# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib3

def makeUrl(year,month,day):
    date = year+'/'+month+'/'+day+'/'
    link = 'http://www.mk.ru/politics/'+date
    return link

def getHeaders(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(''.join(r.data))
    bitch = soup.find("ul", { "class" : "big_listing" })
    a = bitch.findAll("a", { "class" : "mkh2" })

    list=[]

    for item in a:
        comments = item.findAll("span")
        [comment.extract() for comment in comments]
        list.append(item.text)
    return list



def getText(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(''.join(r.data))
    # search header
    a = soup.findAll("p", { "class" : "text" })

    list=[]
    for item in a:
        list.append(item.text)
    return list


def concatMass(a,b):
    string = ""
    for item1, item2 in zip(a, b):
        string =string + " " + item1+" "+item2
    return string


year = ['2011', '2012', '2013', '2014', '2015']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
       '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

for y in year:
    for m in month:
        for d in day:
            url = makeUrl(y, m, d)
            b = getText(url)
            if not b:
                break
            f = open('data/'+y+'_'+m+'_'+d+'.txt', 'w')
            a = getHeaders(url)
            c = concatMass(a, b)
            f.write(c.encode('utf8'))
            f.close()