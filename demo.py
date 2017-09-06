from xc import xiciSpider

p=xiciSpider()
#第一次先运行这个方法，现将ip存入mysql
p.getNewipToMysql()
#获取可用代理ip,默认获取1个，可指定size大小
ip=p.getAccessIP()
print(ip)