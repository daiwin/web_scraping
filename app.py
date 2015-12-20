from BeautifulSoup import BeautifulSoup
import urllib3

def getHeaders(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(''.join(r.data))
    # search header
    a = soup.findAll("a", { "class" : "mkh2" })
    # clear header ot span
    for item in a:
        comments = item.findAll("span")
        [comment.extract() for comment in comments]
    return a

def getText(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    soup = BeautifulSoup(''.join(r.data))
    # search header
    a = soup.findAll("p", { "class" : "text" })
    return a

def concatMass(a,b):
    c = zip(a, b)
    return c


def makeUrl(year,month,day):
    date = year+'/'+month+'/'+day
    link = 'http://www.mk.ru/culture/'+date+'/'
    return link



year = ['2011']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']




for y in year:
    for m in month:
        for d in day:
            url=makeUrl(y, m, d)
            b=getText(url)
            if not b:
                break

            f = open('data/'+y+'_'+m+'_'+d+'.txt', 'w')
            a=getHeaders(url)
            c=concatMass(a,b)
            f.write(str(c))
            f.close()

