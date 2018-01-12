## 01 爬虫基本概念及原理

### 1.1 爬虫是什么

**请求**网站并**提取**数据的**自动化**程序

### 1.2 爬虫基本过程

1. 发起请求：通过HTTP库向目标站点发起请求，即发送一个Request，请求可以包含额外headers等信息，等待服务器响应。
2. 获取相应内容：如果服务器能正常相应，会返回一个Response给客户端（HTTP库），Response的内容便是所要获取的页面内容，类型可能有HTML、Json字符串（XHR：XML Http Request对象，ajax的核心技术）、二进制数据（eg：图片视频）等类型。
3. 解析内容：得到的内容可能是HTML，可以用正则表达式、网页解析库进行解析；可能是Json，可以直接转为Json对象（dict）解析；可能是二进制数据，可以做存储或者进一步的处理。
4. 保存数据：保存形式多样，可以存为文本；也可以保存至数据库；或者保存特定格式的文件（图片）。

### 1.3 Request & Response

1. HTTP Request：浏览器发送信息给服务器。
2. HTTP Response：服务器收到浏览器发送的信息后，能够根据浏览器发送消息的内容，做出相应的处理，然后把消息回传给浏览器。
3. 浏览器收到服务器的Response信息后，会对信息进行相应的处理，然后展示。

### 1.4 Request中包含了什么？

1. 请求URL：URL统一资源定位符，如：一个网页稳定、一张图片、一个视频等都可以用URL唯一来确定。
2. 请求方式：主要有GET、POST两种类型，另外还有HEAD、PUT、DELETE、OPTIONS等。
3. 请求头：包含请求时的头部信息，如User-Agent、Host、Cookies等信息。
4. 请求体：请求时额外携带的数据，GET请求时不会有内容，只有POST请求是才会有，如表单提交时的表单数据。

### 1.5 Response中包含了什么？

1. 相应状态：200=成功，301跳转，404=找不到页面，500+（502、503...）=服务器错误等。
2. 响应头：如内容类型、内容长度、服务器信息、设置Cookie等。
3. 响应体：最主要的部分，包含了请求资源的内容，如网页HTML、图片二进制数据等。

### 1.6 爬虫能抓取什么数据？

1. 网页文本：HTML文档、Json格式文本（ajax）等。
2. 图片：获取图片的二进制文件，保存为图片格式。
3. 视频：同为二进制文件，保存为视频格式即可。
4. 其他：只要是能请求到的，都能获取。

```python
# 抓取二进制文件实例
import requests
response = requests.get('https://www.baidu.com/img/bd_logo1.png')
print(response.content)  # content是二进制文件，text是html文件
with open('/home/yaro/Download/1.png', 'wb') as f:
 f.write(response.content)
 f.close()  # 可以省略
```

### 1.7 怎样解析处理？

1. 直接处理：返回的是最简单的字符串。
2. Json解析（ajax）：返回的是json格式的字符串。
3. 正则表达式：匹配、提取返回的html中相应的文本。
4. BeautifulSoup解析库：更容易、好用
5. PyQuery解析库：API 同 JQuery
6. XPath解析库：Built-in

### 1.8 为什么用`ctrl+u`与`审查元素-Network中`不一样？

- 拿`m.weibo.com` 举例，在请求时首先返回最初的doc（dom）html框架，然后里面有很多JS；后台会通过ajax请求返回数据，然后用JS“填充至”原html中。
- 我们请求的结果与“浏览源代码（ctrl + u）”是一致的。

### 1.9 怎么解决上面JS渲染导致的问题？

由于我们想要的结果不在请求返回的结果中,我们需要分析Ajax或者使用JS渲染工具;

- 分析Ajax请求：返回的是Json的字符串。
- Selenium/WebDriver：模拟浏览器渲染JS，呈现渲染后的结果。

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.taobao.com')
print(driver.page_source)  # 这个数据是不可能用请求库拿到的数据，这里面的数据都是JS渲染后的数据，可以直接解析提取。
```

- Splash库：也是模拟JS渲染的。
- PyV8、Ghost.py等其他库来模拟加载

### 1.10 怎么数据持久化（保存）？

1. 文本：纯文本、Json、Xml等。
2. 关系型数据库：如MySQL、Oracle、SQL Server等具有结构化表结构形式存储。
3. 如MongoDB、Redis等Key-Value形式存储。
4. 二进制文件：图片、视频、音频等直接保存成特定的格式即可。

## 02 爬虫常用工具(库)安装/测试

### 2.1 常用工具分类

爬虫使用到的python库的有：请求库、解析库、存储库、工具库；

请求库：urllib, requests, selenium

解析库： lxml, beautifulsoup, pyquery

存储库：pymysql, pymongo, redis

工具：RE, Json, Chrome, Phantomjs, Mysql, MongoDB, Redis, Sublime_text, Pycharm等

相应的库简介如下：

### 2.2 urlib - Buit-in请求库

```python
import urllib.request
urllib.request.urlopen('http://www.baidu.com')
```

### 2.3 re - Buit-in正则

```python
import re
```

### 2.4 requests - Human请求库

```python
import requests
requests.get('http://www.baidu.com')
```

### 2.5 selenium - 请求+JS解析

主要用来驱动浏览器，用作自动化测试；在做爬虫是会遇到JS渲染的网页，用requests请求无法获取相应的请求内容；

此时，我们可以使用selenium来实现：用selenium库可以直接驱动浏览器，用浏览器执行JS的渲染，得到的结果便是渲染之后的结果，我们便可以拿到渲染之后的内容。

假如使用调用Chrome()对象(浏览器)的话，需要安装对应[chromedrive](https://sites.google.com/a/chromium.org/chromedriver/)。

```python
pip3 install selenium
from selenium import webdriver
drive = webdrive.Chrome() #声明一个webdrive对象，调用一个chrome对象
driver.get('http://www.baidu.com')
driver.page_source  # 获取网页源代码
```

### 2.6 phantomjs - 无界面浏览器

​ 在做爬虫时，一直出现一个浏览器是很不方便的；这是我们就需要一个没有界面的浏览器——phantomjs。

[官网](http://phantomjs.org/), 下载解压后，将/bin子目录配置到环境变量即可。

```python
# 直接在cmd下运行
phantomjs
console.log('Hello World')  # 相当于启动一个控制台
# 在python下运行
from selenium import webdriver
driver.get('http://www.baidu.com')
driver = webdriver.PhantomJS()
driver.page_source  # 同Chrome
```

### 2.7 lxml - xpath解析库

提供了xpath解析方式（方便，高效）

```python
pip install lxml
from lxml import etree
import requests
url = 'http://www.baidu.com'
response = requests.get(url)  # requests.models.Response对象, Response.text属性是html的字符串类型
html = etree.HTML(response.text)  #将字符串类型转换为lxml.etree._Element类型
result = html.xpath('//title/text()')[0] #可以对html使用xpath方法进行解析
```

> 有时我们由于网络问题造成安装库困难的话，我们可以通过如下方法解决：1、google相应的库名，进入pypi.python.org相应的库页面，下载.whl文件（前提需要安装wheel库），然后用 `pip install whl文件路径` 安装即可 ；2、使用国内的相关镜像

### 2.8 beautifulsoup4

更加方便的网页解析库，依赖于lxml库，解析速度当然没有lxml快啦！

```python
pip3 install beautifulsoup4 # 第四个版本
from bs4 import BeautifulSoup # 库（包）源代码（.tar.gz）的文件夹结构（名称）决定的
soup = BeautifulSoup('<html></html>','lxml') #第一个参数是html代码 ，第二个参数是解析方式。
```

### 2.9 pyquery - 和 Jquery API类似

 也是一个网页解析库，同样依赖于lxml库,熟悉jquery建议使用这个，二者语法相似,[Pyquery官网](https://pythonhosted.org/pyquery/), 全部[API](https://pythonhosted.org/pyquery/api.html)。

```python
pip3 install pyquery
from pyquery import PyQuery as pq
doc = pq('<html>Hello</html>')
result = doc('html').text()  # 还有.html()方法
print(result)
# 更多使用方法，参考pyquery官网
```

### 2.10 pymysql - 连接Mysql

用于操作mysql数据库; python2使用`mysql-python`库；在python3中使用`pymysql`代替。

```python
pip install pymysql
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='123456',port='3306', db='mysql')  # 声明一个连接对象
cursor = conn.cursor()  # 调用conn的cursor方法，指定数据库的操作对象
cursor.execute('select * from db')  # 调用一些函数执行sql语句
cursor.fetchone()  # 使用fetchone方法拿到数据库的内容
```

### 2.11 pymongo - 连接MongoDB

用于操作mongodb数据库，是key:value形式（json，类似与python中的字典）的非关系型数据库，在爬虫的数据存储时，使用mongodb来存储是非常方便的；不需要建表，不需要关系表的结构，而且可以动态的增加键名。

```python
pip install pymongo
# 启动mongodb数据库
import pymongo
client = pymongo.MongoClient('localhost')  # 声明一个MongoDB的连接对象
db = client['testdb']  # 调用client声明一个数据库
db['table'].insert({'name':'Bob'})  # 调用db声明一个表名,并插入一条数据
db['table'].find_one({'name':'Bob'})  # 数据的查询
```

### 2.12 redis - 连接Redis

也是非关系型数据库，也是key:value形式存储的。主要应用于后面的分布式爬虫、维护一个爬取队列，运行效率比较高，用它维护一个公共爬取队列，效果比较好。

```python
pip install redis
import redis
r = redis.Redis('localhost', 6379)  #  声明一个redis对象
r.set('name', 'Bob')  # 插入数据
r.get('name')  # 获取数据
```

### 2.13 flask - 简单web框架

是一个web库，后面的代理设置（代理的获取、存储）会用到。

```python
pip install flask  # 依赖的库比较多
```

### 2.14 django - 强大web框架

是一个web服务器框架，提供了完整的后台管理，提供了模板引擎、接口、路由等。可以使用django做一个完整的网站。后面的分布式爬虫维护时会用到。

```python
pip install django  # 依赖的库比较多
```

### 2.15 jupyter - python记事本

运行在网页端的记事本，可以调试命令，支持mk语法。

```python
pip install jupyter  # 依赖的库比较多
jupyter notebook  
```

### 2.16 MongoDB环境配置

windows建议使用--install添加服务，GUI数据查看建议使用robo3t;

```mysql
mongod --bind_ip 0.0.0.0 --logpath D:\Dev\MongoDB\Server\3.6\data\logs\mongo.log --logappend --dbpath D:\Dev\MongoDB\Server\3.6\data\db --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install
# 需要提前创建数据, log文件夹;
db;
show dbs;
db.test.insert({'a':'b'})
```

### 2.17 Redis环境配置

内存中的NoSQL数据库,高效,后面分布式爬虫会用到;

安装: linux直接REPO下载即可; Win版本太多,建议使用[微软的Reids版本](https://github.com/MicrosoftArchive/redis/releases)

GUI可视化管理软件推荐:[RedisDesktopManager](https://github.com/uglide/RedisDesktopManager)

linux下使用`redis-cli`命令启动;

记得配置redis配置文件`vim /etc/redis/redis.conf`

```sh
bind 127.0.0.1（只允许本地）
requirepass foobar 启用密码
redis-cli -a foobar # 使用密码登陆
....
```

修改配置文件：取消限制只有本地连接，添加密码

### 2.18 MySQL环境配置

可以使用MariaDB代替;

```mysql
mysql -uroot -p 
# 可以使用-h参数，参数后面可以有空格，可以没有空格；
# 但是-p后面不能有空格，否则需要重新输入密码。
```

win下GUI管理工具：Navicat/MySQL Front等等。

## 03 常用库的基本使用

### 3.1 Urllib库基本使用

python自带的请求库,下面的Requests是此库的包装;

### 3.2 Requests库基本使用

基于Python编写，基于urllib，采用Apache2 Licensed开源协议的HTTP库。比urllib更方便。

```python
import requests
response = requests.get('http://www.baidu.com') # post/put/delete/head/options
# 记得使用 http://httpbin.org 网站测试
data = {
'name':'bob',
'age':22
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.json()) # 如果返回的是json格式字符串,可以直接转变成dict;等同于josn库里面的json.loads(response.text)
print(response.status_code)
print(response.text)
print(response.content)  # 返回二进制的数据,图片/多媒体等
print(response.cookies)  # 还有url/history/属性

# 写入多媒体文件
with open('test.jpg', 'wb') as f:
f.write(response.content)

# 添加headers
headers = {........}
response = requests.get('https://www.zhihu.com/explore', headers = headers)

# post请求
data = {'name':'bob', 'age': '22'}
headers = {........}
response = requests.post('http://httpbin.org', data = data, headers = headers)

# 文件上传
files = {'file':open('test.jpg', 'rb')}
response = requests.post('http://httpbin.org',file=files)

# 获取cookies
response = requests.get('http://www.baidu.com')
for key, value in response.cookies.items():
print(key + '=' + value)

# 会话维持
# 证书验证
# 代理设置
proxies = {'http':'http://127.0.0.1:9743', 'https':'https://127.0.0.1:9744'}
response = requests.get('http://www.taobao.com', proxies = proxies)
# 超时设置
# 认证设置
# 异常处理
```

### 3.3 正则表达式基础

方便地提取html中的相关信息。

**当我们需要提取的信息在html源码中，但是不在标签中，只存在与JS的相关变量中时**（今日头条-街拍），就不能使用Beautifulsoup，Pyquery等解析库提取了。正则表达式就很方便了。

```python
import re
content = 'price is $5.20, hahaha'  # 记得转义 $ .
result = re.match('pattern', content, re.S) #pattern content flag
print(result)
print(result.group(1)) # 0 或者 空 ，都代表所有字符
# re.match是从第一个字符匹配的，第一个字符不符合就匹配不成功，使用起来不方便。
# re.serach就方便的多-搜索整个字符串，多个成功匹配,只返回第一个；
pattern = re.compile('xxx.*xx', re.S)
result = pattern.search(content)  # 可以重复使用,节约compile时间;
# result = re.search(pattern, conntent)
```

总结：

- 能用`字符串.Method`,尽量不用RE,比如字符串的`split()`方法,无法实现用不同的`分割符`分割,RE可以; 
- 尽量使用泛匹配（ `.*` 代替比较长的字符）；
- pattern中使用括号获取匹配目标(组),0或者空代表所有组；
- 尽量使用非贪婪模式(.*?)；
- 有换行符就是用 `re.S` Flag(让 . 可以匹配换行符)；
- 尽量使用search代替match, re.serach搜索整个字符串，多个成功匹配,只**返回第一个匹配**；
- re.findall查找所有符合的字符串，返回`一个列表`，里面是`各个匹配结果组成的元组`；
- re.sub('\d+', 'Replacement', content) 将content中匹配到的字符串用Replacement替换,返回替换后的结果；
- re.sub('(\d+)', r'\1 Replacement', content) 可以实现在源字符串后面追加, `\1` 别是前面的分组`(\d+)`;
- 习惯使用`res = re.compile(pattern, re.S), res.search('content')`,在重复compile时,比`re.search(pattern, content)`更高效;

### 3.4 BeautifulSoup库详解

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.select('h2'))
```

**标签选择器**

- 标签选择器只选择第一个标签的内容；
- 内容的选择用.string属性，貌似用text也可以？？；
- soup.title.name, soup.title['name'] 可以获得对应的标签名，和标签的属性；
- soup.head.title.string，可以嵌套，返回的结果都是Tag对象
- soup.p.contents可以返回p标签的所有子节点（列表）；
- soup.p.children可以返回p标签的所有子节点（迭代器）；
- soup.p.descendants可以返回p标签的所有子孙节点（迭代器）；
- soup.a.parent可以返回a标签的父节点；
- soup.a.parents可以返回a标签的所有祖先节点；
- soup.a.netx_siblings/previous_siblings兄弟节点；

**标准选择器**

- 可根据标签名、属性、内容查找文档：find_all(name,attrs,recursive,text,**kwargs)
- soup.find_all(attrs={'name':'element'}) 等同于 soup.find_all(name='element')
- 当属性中含有class（html中特殊属性，表示`类`）时，需要写成`soup.find_all(class_='element')`
- 还可以使用text查找（标签的内容）；
- find是返回第一个值；
- find_parent(), find_parents()返回父节点， 所有祖先节点；
- find_next_sibling(), find_next_siblings()
- find_previous_sibling(), find_previous_siblings()
- find_all_next(), find_next()
- find_all_previous(), find_all_previous()

**CSS选择器**

- 通过select()直接传入CSS选择器即可完成选择
- soup.select('#list-2 .element' a)；
- 获取id属性的值：`soup.select('ul')[0]['id']` 或`soup.select('ul')[0].attrs['id']`；
- 获取内容：`soup.select('li')[0].get_text()` , 貌似`soup.select('li')[0].text`也可以;

**总结**：

- 推荐使用lxml解析库，必要时使用html.parser解析库；
- 标签选择筛选功能弱但是速度快；
- 建议使用find()、find_all()查询匹配单个结果或者多个结果；
- **如果对CSS熟悉，建议使用select()**；
- 记住常用的获取属性和文本值的方法；

### 3.5 PyQuery详解

pyquery uses **lxml** for fast xml and html manipulation. 完全和Jquery同样的API，初始化方式有三种：

```python
>>> from pyquery import PyQuery as pq
>>> from lxml import etree/html  # 处理xml/html
# lxml参考:https://www.cnblogs.com/ospider/p/5911339.html

# html = html.encode('uft-8') # 可选,先使用encode('utf-8')转换成字节型字符串;
>>> d = pq(html.fromstring(html))  # 转换成HtmlElement对象,可以使用tosring()再转变成字节型字符串,再次使用decode('utf-8')转换成Unicode字符串
## 意义:当html有缺失/不完整时,会自动补全;

# 字符串初始化
>>> html = "<html></html>"
>>> d = pq(html)

# URL初始化
>>> d = pq(url=your_url)
>>> d = pq(url=your_url,
...        opener=lambda url, **kw: urlopen(url).read())

# 文件初始化
>>> d = pq(filename=path_to_html_file)
```

Now d is like the `$` in jquery:

```python
>>> d("#hello")
[<p#hello.hello>]
>>> p = d("#hello")
>>> print(p.html())
Hello world !
>>> p.html("you know <a href='http://python.org/'>Python</a> rocks")
[<p#hello.hello>]
>>> print(p.html())
you know <a href="http://python.org/">Python</a> rocks
>>> print(p.text())
you know Python rocks
```

You can use some of the pseudo classes that are available in jQuery but that are not standard in css such as `:first :last :even :odd :eq :lt :gt :checked :selected :file` :

```python
>>> d('p:first')
[<p#hello.hello>]
```

- 基本的CSS选择器：doc('#container .list li')
- doc('.a.b') 同时包含a和b; doc(.a, .b)包含a或者b;
- doc('.list').find('li') 选择所有的后代li对象，**等同于doc('.list li')** 或 doc('.list')('li') ；
- doc('.list').children('li') 子对象，**等同于doc('.list>li')**
- 父元素: **doc('.list').parent()**
- 祖先元素: **doc('.list').parents()**
- 兄弟元素：**doc('.list').siblings()**
- **遍历：lis = doc('li').items()**，通过items()方法生成迭代器，返回的对象还是pyquery对象；
- 获取属性：a.attr('href') 或 a.attr.href
- 获取文本：a.text() 获取所有的文本（包含子元素）；
- 获取html：a.html() （里面的所有内容，包含html标签和文本）；
- DOM操作：可用于复杂的解析
- addClass()、removeClass()
- attr('name','link')、 css('font-size','14px')  , 添加name属性和style属性
- remove() ，删除多余的内容，比较有用

```python
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())
```

> 其他DOM方法：<http://pyquery.readthedocs.io/en/latest/api.html>

- 伪类选择器

```python
html = '''
<div class="wrap">
  <div id="container">
      <ul class="list">
           <li class="item-0">first item</li>
           <li class="item-1"><a href="link2.html">second item</a></li>
           <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
           <li class="item-1 active"><a href="link4.html">fourth item</a></li>
           <li class="item-0"><a href="link5.html">fifth item</a></li>
       </ul>
   </div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)') # great than 2 ，索引从0开始？
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')  #包含 second 文本
print(li)
```

更多CSS选择器可以查看：http://www.w3school.com.cn/css/index.asp

官方文档：<http://pyquery.readthedocs.io/>

### 3.6 Selenium详解

自动化测试工具，支持多种浏览器。爬虫中主要用来解决JS渲染的问题（网页源代码中没有我们想要的内容，渲染后才能找到）。

```python
from selenium import webdriver
browser = webdriver.Chrome()  # PhantomJS/Firefox/Edge/Safari
tyr:
browser.get('http://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('Python')
input.send_keys(Kyes.ENTER)
wait = WebDriverWait(browser, 10)
# wait.until(EC.presence_of_element_located((By.ID, 'content_left'))
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
finally:
browser.close()

## 查找元素（貌似都是取得page_source后，用解析库获取）
browser.find_element_by_id('q')
browser.find_element_by_name('q')
browser.find_element_by_xpath('q')
browser.find_element_by_css_selector('q')
browser.find_element_by_link_text('q')
browser.find_element_by_tag_name('q')
browser.find_element_by_class_name('q')
# 上面只是查找单个元素，想要查找多个元素，需要使用 elements 

## 元素交互操作
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPad')
time.sleep(1)
input.clear()
input.send_keys('iPhone')
button = browser.find_element_by_class_name('btn-serach')
button.click()
# 更多api参考： http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement

## 交互动作
from selenium import webdriver
from selenium.webdriver import ActionCharins
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jquery-api-deroppable'
browser.get(url)
browser.switch_to_frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
# 更多api参考： http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

## 执行JS
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom)')

## 获取元素信息
logo = browser.find_element_by_id('zh-top-lnk-logo')
logo.get_attribute('class')  # 获取属性
input = browser.find_element_by_class_name('zu-top-add-question')
input.text  # 获取文本值，还可以获取 id/location/tag_name/size

## Frame 相当于一个单独的网页，需要先
browser.sitch_to_frame('iframeResult')  # 需要先切换到特定id的frame

## 等待
browser.implicitly_wait(10)  # 隐式等待没有必要
# 显式等待
from selenium.webdrive.common.by import By
from selenium.webdrive.support.ui import WebDriverWait
from selenium.webdrive.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.Id, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'btn-search')))
# 更多api参考： http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

## 前进后退
browser.get('https://www.taobao.com/')
browser.get('https://www.baidu.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

## Cookies
browser.get_cookies()
browser.add_cookie({'name':'bob',...})
browser.delete_all_cookies()

## 选项卡管理
browser.get('http://www.taobao.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('http://www.baidu.com')

## 异常处理（比较多，需要的时候查看官方文档）
browser.find_element_by_id('hello')  # 查找一个不存在的元素
# 以上会报错 NoSuchElementException
try:
browser.find_element_by_id('hello')
except NoSuchElementException:
print('No Element')
finally:
browser.close()
```

### 3.7 总结

上面介绍了那么多库, 具体怎么选择呢? 个人习惯思路如下:

- 首先使用Requests库请求目标站点,获取目标内容,(比Urllib易用);
- 倘若是JS站点,Requests不易获取目标内容,先查看Ajax,不行再使用Selenium;
- 将得到的内容交给lxml.html进行处理,修复得到的html代码;
- 使用pyquery进行解析(选择自己熟练的解析库);
- 最后入库,保存数据,分析数据,展现数据,应用数据;

## 04 关于各工具的效率/选择的思考

解析库中,Pyquery和Beautifulsoup4都是基于Lxml库的, 网上很多人证明Lxml库的效率更高!

当然,Pyquery和Beautifulsoup4既然包装了Lxml,易用性肯定更高!

那么我们如何选择呢,选择易用性 or 效率 ?

首先,引入python实现并行任务的相关概念:

由于CPython的GIL的原因,python无法实现多线程,导致CPU密集型任务使用多线程反而降低效率,但是在I/O密集型的任务上,多线程(Threading)依然可以有效的提升效率! 

为什么说这个呢? 对于任何计算机实现的任务,我们都可以这么理解:

为了实现一个网络任务, 计算机需要 **联网** - **访问数据** - **下载数据** - **解析数据** - **保存数据(I/O)** , 而在所有的过程中,都需要**CPU计算**, 整个网络任务的执行时间(效率)取决于效率最低(时间最多)的那个环节!

So, 请求库/解析库的效率真的是你特别需要解决的么? 相信你已经有了答案!😄





