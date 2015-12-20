from BeautifulSoup import BeautifulSoup
import urllib3



def getHeaders():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.mk.ru/culture/2015/12/18/')
    soup = BeautifulSoup(''.join(r.data))
    # search header
    a = soup.findAll("a", { "class" : "mkh2" })
    # clear header ot span
    for item in a:
        comments = item.findAll("span")
        [comment.extract() for comment in comments]
    return a



def getText():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.mk.ru/culture/2015/12/18/')
    soup = BeautifulSoup(''.join(r.data))
    # search header
    a = soup.findAll("p", { "class" : "text" })
    return a


def concatMass(a,b):
    c = zip(a, b)
    return c


b=getText()
a=getHeaders()
c=concatMass(a,b)
print c




