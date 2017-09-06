#coding:utf-8
import re
import requests
import pymysql
import time
class xiciSpider(object):
    def __init__(self):
        self.req=requests.Session()
        self.headers={
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Referer':'http://www.xicidaili.com/nn/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36',
        }
        self.proxyHeaders={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36',
        }
        self.con=pymysql.Connect(
            host='127.0.0.1',
            user='root',
            password="*****",
            database='xici',
            port=3306,
            charset='utf8',
        )
        self.cur=self.con.cursor()


    def getPage(self,url):
        page=self.req.get(url,headers=self.headers).text
        # print(page)
        return page

    def Page(self,text):
        time.sleep(2)
        pattern=re.compile(u'<tr class=".*?">.*?'
                           +u'<td class="country"><img.*?/></td>.*?'
                           +u'<td>(\d+\.\d+\.\d+\.\d+)</td>.*?'
                           +u'<td>(\d+)</td>.*?'
                           +u'<td>.*?'
                           +u'<a href=".*?">(.*?)</a>.*?'
                           +u'</td>.*?'
                           +u'<td class="country">(.*?)</td>.*?'
                           +u'<td>([A-Z]+)</td>.*?'
                           +'</tr>'
                           ,re.S)
        l=re.findall(pattern,text)
        return l
        # print(result[0])
    def getUrl(self,pageNum):
        url='http://www.xicidaili.com/nn/'+str(pageNum)
        return url

    def insert(self,l):
        print("插入{}条".format(len(l)))
        self.cur.executemany("insert into xc values(%s,%s,%s,%s,%s)",l)
        self.con.commit()
    def select(self):
        a=self.cur.execute("select ip,port,xieyi from xc")
        info=self.cur.fetchall()
        return info
    def getAccessIP(self,size=1):
        info=self.select()
        p=[]
        for i in info:
            if len(p)==size:
                return p
            try:
                self.req.get("http://www.baidu.com",proxies={"{}".format(i[2]):"{}://{}:{}".format(i[2],i[0],i[1])},timeout=5)
                p.append(i)
            except Exception:
                print("{} is valid".format(i))
        print(p)

    def getNewipToMysql(self):
        for i in range(2300):
            page=self.getPage(self.getUrl(i))
            p.insert(self.Page(page))

if __name__=='__main__':
    p=xiciSpider()
    # p.Page(p.getPage('http://www.xicidaili.com/nn/'))

    # for i in range(2300):
    #     page=p.getPage(p.getUrl(i))
    #     p.insert(p.Page(page))
    p.getAccessIP()

