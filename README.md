# xici---ip
构建自己的代理ip池<br>
<h1>使用方法</h1><br>
设置自己的数据库信息<br>
创建数据库create database xici;<br
创建表create table xc;<br>
根据xc.py中的<br><br>
self.con=pymysql.Connect(<br>
            host='127.0.0.1',<br>
            user='root',<br>
            password="*****",<br>
            database='xici',<br>
            port=3306,<br>
            charset='utf8',<br>
        )<br>
        修改就行<br><br>

导入xiciSpider类<<br>
from xc import xiciSpider<br><br>
生成类对象<br>
p=xiciSpider()<br><br>
#如果是第一次运行的话，先运行这个方法，现爬取ip存入mysql<br>
p.getNewipToMysql()<br><br>
#从数据库中获取可用代理ip,默认获取1个，可指定size大小<br>
ip=p.getAccessIP(size=1)<br>
print(ip)<br><br><br>

<h3>关于代码如何编写可查看此专栏<a href="https://zhuanlan.zhihu.com/c_99646580">python数据分析</a></h3>
