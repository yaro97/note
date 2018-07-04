# Python爬虫知识点及代码实例

## 1、Linux相关

必备技能，参考：

[linux基础知识与系统管理](https://github.com/yaro97/note/blob/master/linux/linux%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E4%B8%8E%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86.md)

[linux网络服务管理](https://github.com/yaro97/note/blob/master/linux/linux%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E7%AE%A1%E7%90%86.md)

[其他Linux相关](https://github.com/yaro97/note/tree/master/linux)

## 2、Python相关

### 2.1、基础知识

略。

### 2.2、面向对象（class）

[Python面向对象总结梳理](https://github.com/yaro97/note/blob/master/python/python_class_object-oriented_%E6%80%BB%E7%BB%93%E5%8F%8A%E6%A2%B3%E7%90%86.md)

### 2.3、IO编程

- 文件读写：略，参考：[菜鸟教程](http://www.runoob.com/python/python-files-io.html)


- 操作文件和目录：os/shutil模块


- 序列化

```python
try:
  import cPickle as pickle
except ImportError:
  import pickle
d = dict(...) 
pickle.dumps(d)  # 序列化
pickle.dump(d, f)  # 到文件
# loads/loads 反序列化
# Json 可以在不同编程语言之间传递数据
```

其他参考：[廖雪峰Python IO教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917590955542f9ac5f5c1479faf787ff2b028ab47000)

### 2.4、网络编程

略。参考： [网络编程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320037274136d31bd9979d648cd822375394e29a871000)

### 2.5、线程/进程(并发)

参考：[Python并发相关技术](https://github.com/yaro97/note/blob/master/python/python_multiprocessing_threading_%E5%A4%9A%E7%BA%BF%E7%A8%8B_%E5%A4%9A%E8%BF%9B%E7%A8%8B.md)

### 2.6、网络编程

略

### 2.7、数据库编程

略

## 3、Web前端

略。

## 4、工具相关

[Git知识点](https://github.com/yaro97/note/blob/master/tools/git_tutorial.md)

[Docker相关](https://github.com/yaro97/note/tree/master/docker)

## 5、爬虫基础

### 5.1、基本概念Q&A

#### 爬虫是什么？

**请求**网站并**提取**数据的**自动化**程序

#### 爬虫基本过程

1. 发起请求：通过HTTP库向目标站点发起请求，即发送一个Request，请求可以包含额外headers等信息，等待服务器响应。
2. 获取相应内容：如果服务器能正常相应，会返回一个Response给客户端（HTTP库），Response的内容便是所要获取的页面内容，类型可能有HTML、Json字符串（XHR：XML Http Request对象，ajax的核心技术）、二进制数据（eg：图片视频）等类型。
3. 解析内容：得到的内容可能是HTML，可以用正则表达式、网页解析库进行解析；可能是Json，可以直接转为Json对象（dict）解析；可能是二进制数据，可以做存储或者进一步的处理。
4. 保存数据：保存形式多样，可以存为文本；也可以保存至数据库；或者保存特定格式的文件（图片）。

#### Request & Response

1. HTTP Request：浏览器发送信息给服务器。
2. HTTP Response：服务器收到浏览器发送的信息后，能够根据浏览器发送消息的内容，做出相应的处理，然后把消息回传给浏览器。
3. 浏览器收到服务器的Response信息后，会对信息进行相应的处理，然后展示。

#### Request中包含了什么？

1. 请求URL：URL统一资源定位符，如：一个网页稳定、一张图片、一个视频等都可以用URL唯一来确定。
2. 请求方式：主要有GET、POST两种类型，另外还有HEAD、PUT、DELETE、OPTIONS等。
3. 请求头：包含请求时的头部信息，如User-Agent、Host、Cookies等信息。
4. 请求体：请求时额外携带的数据，GET请求时不会有内容，只有POST请求是才会有，如表单提交时的表单数据。

#### Response中包含了什么？

1. 相应状态：200=成功，301跳转，404=找不到页面，500+（502、503...）=服务器错误等。
2. 响应头：如内容类型、内容长度、服务器信息、设置Cookie等。
3. 响应体：最主要的部分，包含了请求资源的内容，如网页HTML、图片二进制数据等。

#### 爬虫能抓取什么数据？

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

#### 怎样解析处理？

1. 直接处理：返回的是最简单的字符串。
2. Json解析（ajax）：返回的是json格式的字符串。
3. 正则表达式：匹配、提取返回的html中相应的文本。
4. BeautifulSoup解析库：更容易、好用
5. PyQuery解析库：API 同 JQuery
6. XPath解析库：Built-in

#### `ctrl+u`与`inspect-Elements中`区别？

- 拿`m.weibo.com` 举例，在请求时首先返回最初的doc（dom）html框架，然后里面有很多JS；后台会通过ajax请求返回数据，然后用JS“填充至”原html中。
- 我们请求的结果与“浏览源代码（ctrl + u）”是一致的。

#### 怎么解决上面JS渲染导致的问题？

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

#### 怎么数据持久化（存储）？

1. 文本：纯文本、Json、Xml等。
2. 关系型数据库：如MySQL、Oracle、SQL Server等具有结构化表结构形式存储。
3. 如MongoDB、Redis等Key-Value形式存储。
4. 二进制文件：图片、视频、音频等直接保存成特定的格式即可。

### 5.2、爬虫常用库/工具

#### 工具总览

爬虫使用到的python库的有：请求库、解析库、存储库、工具库；

请求库：urllib, requests, selenium

解析库： lxml, beautifulsoup, pyquery

存储库：pymysql, pymongo, redis

常用工具：ipython, jupyter, RE, Json, Chrome, Phantomjs, Mysql, MongoDB, Redis, Sublime_text, Pycharm等

#### Urllib库基本使用

python自带的请求库,下面的Requests是此库的包装;

#### Requests库基本使用

见《requests.md》

#### Re 正则表达式

项目参考：[MaoYan100_re](https://github.com/yaro97/spider_projects/blob/master/MaoYan100_re/main.py)

方便地提取html中的相关信息。

**当我们需要提取的信息在html源码中，但是不在标签中，只存在与JS的相关变量中时**（今日头条-图片），就不能使用Beautifulsoup，Pyquery等解析库提取了。正则表达式就很方便了。

**re 模块的常用函数**

| 用途 | 函数声明                                          | 返回值           |
| ---- | ------------------------------------------------- | ---------------- |
| 编译 | `re.compile(pattern, flags=0)`                    | `re.RegexObject` |
| 查找 | `re.search(pattern, string, flags=0)`             | `re.MatchObject` |
| 查找 | `re.findall(pattern, string, flags=0)`            | `list`           |
| 查找 | `re.finditer(pattern, string, flags=0)`           | `iterator`       |
| 替换 | `re.sub(pattern, repl, string, count=0, flags=0)` | `string`         |
| 分割 | `re.split(pattern, string, maxsplit=0, flags=0)`  | `list`           |

其中，比较常用的是 `re.sub`、`re.split` 和 `re.findall`。

`re.compile` 返回的对象 `re.RegexObject` 也支持 re 模块下的大部分函数；也就是说，你可以这样调用

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

使用 `re.compile` 会提前编译给定的 RE，避免每次都重新编译；不过 Python 也没有那么蠢，它会缓存编译过的 RE。

> `re.match()`的用途比较窄，一般只用来做**完全匹配**，关于它与 `re.search`，参考 [search() vs. match()](https://docs.python.org/3/library/re.html#search-vs-match)
>
> 因为几乎用不到它，所以最好别记住它，不然你每次都会纠结它跟 `re.search` 有什么区别。

**使用示例**

中文语料清洗

数据格式：

```python
["text1", "text2", "text3", ...]
```

代码

```python
data = ["近日南京市下发《关于加强出租汽车市场规范管理的意见》（代拟稿），按照《意见》规定\n",
        "Outlook 2010中新增了一个“人物窗格”（People Pane）功能，\n",
        "Steam上已经发布了超过6800款游戏，而2016年这个数字为5028，2015年为2991款。\n"]

RE_zh_en = re.compile(r"[^\u4e00-\u9fa5a-zA-Z]")
"""匹配所有非中英文字符"""
RE_white_space = re.compile(r"(\s)+")
"""匹配连续的空白符"""

for line in data:
    # 把除中文、英文外的字符转为空格
    line = RE_zh_en.sub(' ', line)
    # 去掉首尾的空格
    line = line.strip()
    # 把多个空白符转空格
    line = RE_white_space.sub(' ', line)
    print(line)
```

具体的要做哪些处理视数据而定，
一个复杂的例子：gensim 处理 wiki 语料

处理结果

```sh
近日南京市下发 关于加强出租汽车市场规范管理的意见 代拟稿 按照 意见 规定
Outlook 中新增了一个 人物窗格 People Pane 功能
Steam上已经发布了超过 款游戏 而 年这个数字为 年为 款
```

数据清理后，下一步就是**分词**了，未完待续。

**总结：**

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

#### Lxml - xpath解析库

详细见《xml.md》

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

#### PyQuery详解

略，详细见《pyquery.md》

#### Beautifulsoup4

略，详细见《beautifulsoup4.md》

#### Selenium详解

略，详细见《selenium.md》

#### Pymysql - 连接Mysql

用于操作mysql数据库; python2使用`mysql-python`库；在python3中使用`pymysql`代替。

```python
pip install pymysql
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='123456',port='3306', db='mysql')  # 声明一个连接对象
cursor = conn.cursor()  # 调用conn的cursor方法，指定数据库的操作对象
cursor.execute('select * from db')  # 调用一些函数执行sql语句
cursor.fetchone()  # 使用fetchone方法拿到数据库的内容
```

#### Pymongo - 连接MongoDB

项目参考：[TaoBaoGoods_selenium](https://github.com/yaro97/spider_projects/blob/master/TaoBaoGoods_selenium/main.py)

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

#### Redis - 连接Redis

也是非关系型数据库，也是key:value形式存储的。主要应用于后面的分布式爬虫、维护一个爬取队列，运行效率比较高，用它维护一个公共爬取队列，效果比较好。

```python
pip install redis
import redis
r = redis.Redis('localhost', 6379)  #  声明一个redis对象
r.set('name', 'Bob')  # 插入数据
r.get('name')  # 获取数据
```

#### Phantomjs - 无界面浏览器

项目参考：[TaoBaoGoods_selenium](https://github.com/yaro97/spider_projects/blob/master/TaoBaoGoods_selenium/main.py)

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

#### Flask - 简单web框架

是一个web库，后面的代理设置（代理的获取、存储）会用到。

```python
pip install flask  # 依赖的库比较多
```

#### Django - 强大web框架

是一个web服务器框架，提供了完整的后台管理，提供了模板引擎、接口、路由等。可以使用django做一个完整的网站。后面的分布式爬虫维护时会用到。

```python
pip install django  # 依赖的库比较多
```

#### Jupyter - python记事本

运行在网页端的记事本，可以调试命令，支持mk语法。

```python
pip install jupyter  # 依赖的库比较多
jupyter notebook  
```

#### MongoDB环境配置

windows建议使用--install添加服务，GUI数据查看建议使用robo3t;

```mysql
mongod --bind_ip 0.0.0.0 --logpath D:\Dev\MongoDB\Server\3.6\data\logs\mongo.log --logappend --dbpath D:\Dev\MongoDB\Server\3.6\data\db --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install
# 需要提前创建数据, log文件夹;
db;
show dbs;
db.test.insert({'a':'b'})
```

#### Redis环境配置

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

#### MySQL环境配置

可以使用MariaDB代替;

```mysql
mysql -uroot -p 
# 可以使用-h参数，参数后面可以有空格，可以没有空格；
# 但是-p后面不能有空格，否则需要重新输入密码。
```

win下GUI管理工具：Navicat/MySQL Front等等。

#### 各工具的效率/选择的思考

解析库中，Pyquery和Beautifulsoup4都是基于Lxml库的，网上很多人证明Lxml库的效率更高!

当然，Pyquery和Beautifulsoup4既然包装了Lxml,易用性肯定更高！

那么我们如何选择呢,选择易用性 or 效率 ？

首先，引入python实现并行任务的相关概念：

由于CPython的GIL的原因，python无法实现多线程,导致CPU密集型任务使用多线程反而降低效率,但是在I/O密集型的任务上，多线程(Threading)依然可以有效的提升效率！

为什么说这个呢？对于任何计算机实现的任务,我们都可以这么理解：

为了实现一个网络任务，计算机需要 **联网** - **访问数据** - **下载数据** - **解析数据** - **保存数据(I/O)** ， 而在所有的过程中，都需要**CPU计算**, 整个网络任务的执行时间(效率)取决于效率最低(时间最多)的那个环节！

So，请求库/解析库的效率真的是你特别需要解决的么？ 相信你已经有了答案!😄

## 5、Scrapy框架

参考：[官网](https://docs.scrapy.org/en/latest/)  [Scrapy教程](http://blog.csdn.net/Inke88/article/details/60573507) [Learn Scrapy](https://learn.scrapinghub.com/scrapy/)

Scrapy，Python开发的一个快速,高层次的web抓取框架；

- Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。
- 其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的，也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。
- Scrapy用途广泛,可以用于数据挖掘、监测和自动化测试
- Scrapy使用了Twisted 异步网络库来处理网络通讯。

### 5.1、架构和数据流

![](https://doc.scrapy.org/en/latest/_images/scrapy_architecture_02.png)

1. The [Engine](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine) gets the initial Requests to crawl from the [Spider](https://doc.scrapy.org/en/latest/topics/architecture.html#component-spiders).
2. The [Engine](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine) schedules the Requests in the [Scheduler](https://doc.scrapy.org/en/latest/topics/architecture.html#component-scheduler) and asks for the next Requests to crawl.
3. The [Scheduler](https://doc.scrapy.org/en/latest/topics/architecture.html#component-scheduler) returns the next Requests to the [Engine](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine).
4. The [Engine](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine) sends the Requests to the [Downloader](https://doc.scrapy.org/en/latest/topics/architecture.html#component-downloader), passing through the [Downloader Middlewares](https://doc.scrapy.org/en/latest/topics/architecture.html#component-downloader-middleware) (see [`process_request()`](https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.DownloaderMiddleware.process_request)).
5. Once the page finishes downloading the [Downloader](https://doc.scrapy.org/en/latest/topics/architecture.html#component-downloader) generates a Response (with that page) and sends it to the Engine, passing through the [Downloader Middlewares](https://doc.scrapy.org/en/latest/topics/architecture.html#component-downloader-middleware) (see [`process_response()`](https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.DownloaderMiddleware.process_response)).
6. The [Engine](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine) receives the Response from the [Downloader](https://doc.scrapy.org/en/latest/topics/architecture.html#component-downloader) and sends it to the [Spider](https://doc.scrapy.org/en/latest/topics/architecture.html#component-spiders) for processing, passing through the [Spider Middleware](https://doc.scrapy.org/en/latest/topics/architecture.html#component-spider-middleware) (see [`process_spider_input()`](https://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_input)).
7. The [Spider](https://doc.scrapy.org/en/latest/topics/architecture.html#component-spiders) processes the Response and returns scraped items and new Requests (to follow) to the [Engine](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine), passing through the [Spider Middleware](https://doc.scrapy.org/en/latest/topics/architecture.html#component-spider-middleware) (see [`process_spider_output()`](https://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_output)).
8. The [Engine](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine) sends processed items to [Item Pipelines](https://doc.scrapy.org/en/latest/topics/architecture.html#component-pipelines), then send processed Requests to the [Scheduler](https://doc.scrapy.org/en/latest/topics/architecture.html#component-scheduler) and asks for possible next Requests to crawl.
9. The process repeats (from step 1) until there are no more requests from the [Scheduler](https://doc.scrapy.org/en/latest/topics/architecture.html#component-scheduler).

其他参考：[Architecture Overview](https://doc.scrapy.org/en/latest/topics/architecture.html#component-engine)

### 5.2、基本使用过程

参考项目：[腾讯hr招聘信息](https://github.com/yaro97/spider_projects/tree/master/TencentHR_scrapy)

#### a、创建项目：

`scrapy startproject turoial`

生成项目目录如下：

```
scrapy.cfg:         项目的配置文件
tutorial/:          该项目的python模块, 在这里添加代码
    items.py:       项目中的item文件
    pipelines.py:   项目中的pipelines文件.
    settings.py:    项目全局设置文件.
    spiders/        爬虫模块目录
```

#### b、创建爬虫：

`scrapy genspider xxx www.xxx.com`

#### c、定义item：

即，你想获得的数据。Item 定义结构化数据字段，用来保存爬取到的数据；其使用方法和python字典类似

可以通过创建一个 `scrapy.Item` 类， 并且定义类型为 `scrapy.Field`的类属性来定义一个Item。

```python
import scrapy
class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名
    positionName = scrapy.Field()
    # 职位详情链接
    positionLink = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
	...
```

#### d、编写爬虫文件：

parse方法`yield item` 和 `yield scrapy.Request`

```python
import scrapy
from TencentHR_scrapy.items import TencentHrScrapyItem
class TecentHrSpider(scrapy.Spider):
    name = "tencent_hr"
    allowed_domains = ["tencent.com"]
    base_url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [base_url + str(offset)]  # 构建第一页

    def parse(self, response):
        positions = response.css('#position .even,.odd')  # 提取单页所有职位信息
        for position in positions:
            item = TencentHrScrapyItem()  # 构建item对象，用来保存数据
            # 提取每个职位的具体信息
            item['positionName'] = position.css('td:nth-child(1) a::text').extract()[0]
            item['peopleNumber'] = position.css('td:nth-child(3)::text').extract()[0]
            ...

        if not response.css('.tablelist .pagenav .noactive#next'):  # 如果不是最后一页
            self.offset += 10
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)  # 调用回调函数parse解析下一页
```

> 爬虫文件使用可以使用Scrapy自带的Selectors解析数据(xpath/css/re/extract)，也可以使用第三方库解析（lxml/pyquery/beautifulsoup4）；过程中可以使用`scrapy shell http://xxx`来调试。

#### e、处理/存储数据：

1、可以使用自带的`Feed exports`到处数据文件；

2、也可以编写Pipeline文件：处理item， 写入/文件数据库等...

#### f、执行爬虫：

`scrapy crawl xxx`，当然你也可以通过代码文件`run.py`运行爬虫，参考[官网](https://doc.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script)

### 5.3、深入介绍

#### a、关于爬虫文件

1、scrapy.Spider类

如上面的`TecentHrSpider`类，继承于`scrapy.Spider`类，用于构造Request对象给Scheduler。

常用属性和方法：

- `name`：爬虫的名字，必须唯一（如果在控制台使用的话，必须配置）
- `start_urls`：爬虫初始爬取的链接列表
- `custom_settings`：自定义配置，覆盖`settings.py`中的默认配置


- `start_requests`：启动爬虫的时候调用，默认是调用`make_requests_from_url`方法爬取`start_urls`的链接，可以在这个方法里面定制，如果重写了该方法，start_urls默认将不会被使用，可以在这个方法里面定制一些自定义的url，如登录，从数据库读取url等，本方法返回Request对象
- `make_requests_from_url`：默认由`start_requests`调用，可以配置Request对象，返回Request对象
- `parse`：response到达spider的时候默认调用，如果在Request对象配置了callback函数，则不会调用，parse方法可以迭代返回`Item`或`Request`对象，如果返回Request对象，则会进行增量爬取

2、Request与Response对象

- 每个请求都是一个Request对象，Request对象定义了请求的相关信息（`url`, `method`, `headers`, `body`, `cookie`, `priority`）和回调的相关信息（`meta`, `callback`, `dont_filter`, `errback`），通常由spider迭代返回；其中`meta`相当于附加变量，可以在请求完成后通过`response.meta`访问
- 请求完成后，会通过`Response`对象发送给spider处理，常用属性有（`url`, `status`, `headers`, `body`, `request`, `meta`, ）

详细介绍参考官网：[request-objects](https://doc.scrapy.org/en/latest/topics/request-response.html#request-objects)  [response-object](https://doc.scrapy.org/en/latest/topics/request-response.html#response-objects)

看看下面的例子：

```python
from scrapy import Spider
from scrapy import Request
 
class TestSpider(Spider):
    name = 'test'
    start_urls = ["http://www.qq.com/",]
 
    def login_parse(self, response):
        # 如果登录成功,手动构造请求Request迭代返回
        print response
        for i in range(0, 10):
            yield Request('http://www.example.com/list/1?page={0}'.format(i))
 
    def start_requests(self):
        # 覆盖默认的方法(忽略start_urls),返回登录请求页,制定处理函数为login_parse
        return Request('http://www.example.com/login', method="POST" body='username=bomo&pwd=123456', callback=self.login_parse)
 
    def parse(self, response):
        #默认请求处理函数
        print response
```

3、Selector选择器

css和xpath自己选择即可，当然还有re，extract方法可以提取`data`属性值；

其他参考[官网](https://doc.scrapy.org/en/latest/topics/selectors.html)

#### b、关于Pipeline

item声明结构化数据，spider负责爬取数据，然后交给Pipeline处理（处理，过滤，保存），可以创建多个Pipeline，创建的Pipeline记得在settings中激活/排序（优先级）。常见的处理如下：

- cleansing HTML data
- validating scraped data (checking that the items contain certain fields)
- checking for duplicates (and dropping them)
- storing the scraped item in a database

每个Pipeline都是一个类，必须实现如下方法：

`process_item`(*self*, *item*, *spider*)

其他方法可选：

- `open_spider`(*self*, *spider*)


- `close_spider`(*self*, *spider*)


- `from_crawler`(*cls*, *crawler*)

  If present, this classmethod is called to create a pipeline instance from a [`Crawler`](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.Crawler). It must return a new instance of the pipeline. Crawler object provides access to all Scrapy core components like settings and signals; it is a way for pipeline to access them and hook its functionality into Scrapy.

更多请参考[官网](https://doc.scrapy.org/en/latest/topics/item-pipeline.html)

实例参考如下：

```python
# 写入MongoDB
import pymongo

class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
```



#### c、CrawlSpider和rules

爬虫的通常需要在一个网页里面爬取其他的链接，然后一层一层往下爬，scrapy提供了LinkExtractor类用于对网页链接的提取，使用LinkExtractor需要使用`CrawlSpider`爬虫类中，`CrawlSpider`与`Spider`相比主要是多了`rules`，可以添加一些规则，先看下面这个例子，爬取链家网的链接。

> 适合整站爬取，具体参考[官网](https://doc.scrapy.org/en/latest/topics/spiders.html)

```python
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
 
class LianjiaSpider(CrawlSpider):
    name = "lianjia"
 
    allowed_domains = ["lianjia.com"]
 
    start_urls = [
        "http://bj.lianjia.com/ershoufang/"
    ]
 
    rules = [
        # 匹配正则表达式,处理下一页
        Rule(LinkExtractor(allow=(r'http://bj.lianjia.com/ershoufang/pg\s+$',)), callback='parse_item'),
 
        # 匹配正则表达式,结果加到url列表中,设置请求预处理函数
        # Rule(FangLinkExtractor(allow=('http://www.lianjia.com/client/', )), follow=True, process_request='add_cookie')
    ]
 
    def parse_item(self, response):
        # 这里与之前的parse方法一样，处理
        pass
```

#### d、Middleware

`SpiderMiddleware`：通常用于配置爬虫相关的属性，引用链接设置，Url长度限制，成功状态码设置，爬取深度设置，爬去优先级设置等

`DownloadMiddlware`：通常用于处理下载之前的预处理，如请求Header（Cookie,User-Agent），登录验证处理，重定向处理，代理服务器处理，超时处理，重试处理等

**1、SpiderMiddleware**

爬虫中间件有下面几个方法

- `process_spider_input`：当response通过spider的时候被调用，返回None（继续给其他中间件处理）或抛出异常（不会给其他中间件处理，当成异常处理）
- `process_spider_output`：当spider有item或Request输出的时候调用
- `process_spider_exception`：处理出现异常时调用
- `process_start_requests`：spider当开始请求Request的时候调用

下面是scrapy自带的一些中间件（在`scrapy.spidermiddlewares`命名空间下）

- UrlLengthMiddleware
- RefererMiddleware
- OffsiteMiddleware
- HttpErrorMiddleware
- DepthMiddleware

> 其他参考[官网](http://doc.scrapy.org/en/latest/topics/spider-middleware.html)

**2、DownloaderMiddleware**

下载中间件有下面几个方法

- `process_request`：请求通过下载器的时候调用
- `process_response`：请求完成后调用
- `process_exception`：请求发生异常时调用
- `from_crawler`：从crawler构造的时候调用
- `from_settings`：从settings构造的时候调用

> 更多详细的参数解释见[这里](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/downloader-middleware.html#id2)

在爬取网页的时候，使用不同的`User-Agent`可以提高请求的随机性，定义一个随机设置User-Agent的中间件`RandomUserAgentMiddleware

```python
import random

class RandomUserAgentMiddleware(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    # 从crawler构造，USER_AGENTS定义在crawler的配置的设置中
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    # 从settings构造，USER_AGENTS定义在settings.py中
    @classmethod
    def from_settings(cls, settings):
        return cls(settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # 设置随机的User-Agent
        request.headers.setdefault('User-Agent', random.choice(self.agents))
```

在`settings.py`设置USER_AGENTS参数

```python
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    ...
]
```

配置爬虫中间件的方式与pipeline类似，第二个参数表示优先级

```python
# 配置爬虫中间件
SPIDER_MIDDLEWARES = {
    'myproject.middlewares.CustomSpiderMiddleware': 543,
    # 如果想禁用默认的中间件的话，可以设置其优先级为None
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': None,
}

# 配置下载中间件
DOWNLOADER_MIDDLEWARES = {
    'myproject.middlewares.RandomUserAgentMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}
```

#### e、缓存

scrapy默认已经自带了缓存的功能，通常我们只需要配置即可，打开`settings.py`

```python
# 打开缓存
HTTPCACHE_ENABLED = True
 
# 设置缓存过期时间（单位：秒）
#HTTPCACHE_EXPIRATION_SECS = 0
 
# 缓存路径(默认为：.scrapy/httpcache)
HTTPCACHE_DIR = 'httpcache'
 
# 忽略的状态码
HTTPCACHE_IGNORE_HTTP_CODES = []
 
# 缓存模式(文件缓存)
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```

> 更多参数参见[这里](http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings)

#### f、多线程

scrapy网络请求是基于Twisted，而Twisted默认支持多线程，而且scrapy默认也是通过多线程请求的，并且支持多核CPU的并发，通常只需要配置一些参数即可

```python
# 默认Item并发数：100
CONCURRENT_ITEMS = 100
 
# 默认Request并发数：16
CONCURRENT_REQUESTS = 16
 
# 默认每个域名的并发数：8
CONCURRENT_REQUESTS_PER_DOMAIN = 8
 
# 每个IP的最大并发数：0表示忽略
CONCURRENT_REQUESTS_PER_IP = 0
```

> 更多参数参见[这里](https://doc.scrapy.org/en/latest/topics/settings.html#concurrent-items)

### 5.4、进阶

#### a、下载文件/图片

项目参考：DouyuImage_scrapy



### 5.4、常见问题

#### a、项目名称问题

在使用的时候遇到过一个问题，在初始化`scrapy startproject tutorial`的时候，如果使用了一些特殊的名字，如：`test`, `fang`等单词的话，通过`get_project_settings`方法获取配置的时候会出错，改成`tutorial`或一些复杂的名字的时候不会

```python
ImportError: No module named tutorial.settings
```

这是一个bug，在github上有提到：<https://github.com/scrapy/scrapy/issues/428>，但貌似没有完全修复，修改一下名字就好了（当然`scrapy.cfg`和`settings.py`里面也需要修改）

#### b、为每个pipeline配置spider

上面我们是在settings.py里面配置pipeline，这里的配置的pipeline会作用于所有的spider，我们可以为每一个spider配置不同的pipeline，设置`Spider`的`custom_settings`对象

```python
class LianjiaSpider(CrawlSpider):
    ...
    # 自定义配置
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.TestPipeline.TestPipeline': 1,
        }
    }
```

#### c、获取提取链接的节点信息

通过LinkExtractor提取的`scrapy.Link`默认不带节点信息，有时候我们需要节点的其他attribute属性，`scrapy.Link`有个`text`属性保存从节点提取的`text`值，我们可以通过修改`lxmlhtml._collect_string_content`变量为`etree.tostring`，这样可以在提取节点值就变味渲染节点`scrapy.Link.text`，然后根据`scrapy.Link.text`属性拿到节点的html，最后提取出我们需要的值

```python
from lxml import etree
import scrapy.linkextractors.lxmlhtml
scrapy.linkextractors.lxmlhtml._collect_string_content = etree.tostring
```

#### d、从数据库中读取urls

有时候我们已经把urls下载到数据库了，而不是在start_urls里配置，这时候可以重载spider的`start_requests`方法

```python
def start_requests(self):
    for u in self.db.session.query(User.link):
        yield Request(u.link)
```

我们还可以在Request添加元数据，然后在response中访问

```python
def start_requests(self):
    for u in self.db.session.query(User):
        yield Request(u.link, meta={'name': u.name})
 
def parse(self, response):
    print response.url, response.meta['name']
```

#### e、如何进行循环爬取

有时候我们需要爬取的一些经常更新的页面，例如：间隔时间为2s，爬去一个列表前10页的数据，从第一页开始爬，爬完成后重新回到第一页

目前的思路是，通过parse方法迭代返回Request进行增量爬取，由于scrapy默认由缓存机制，需要修改

#### f、关于去重

scrapy默认有自己的去重机制，默认使用`scrapy.dupefilters.RFPDupeFilter`类进行去重，主要逻辑如下

```python
if include_headers:
    include_headers = tuple(to_bytes(h.lower())
                             for h in sorted(include_headers))
cache = _fingerprint_cache.setdefault(request, {})
if include_headers not in cache:
    fp = hashlib.sha1()
    fp.update(to_bytes(request.method))
    fp.update(to_bytes(canonicalize_url(request.url)))
    fp.update(request.body or b'')
    if include_headers:
        for hdr in include_headers:
            if hdr in request.headers:
                fp.update(hdr)
                for v in request.headers.getlist(hdr):
                    fp.update(v)
    cache[include_headers] = fp.hexdigest()
return cache[include_headers]
```

默认的去重指纹是sha1(method + url + body + header)，这种方式并不能过滤很多，例如有一些请求会加上时间戳的，基本每次都会不同，这时候我们需要自定义过滤规则

```python
from scrapy.dupefilter import RFPDupeFilter
 
class CustomURLFilter(RFPDupeFilter):
    """ 只根据url去重"""
 
    def __init__(self, path=None):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)
 
    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)
```

配置setting

```python
DUPEFILTER_CLASS = 'tutorial.custom_filters.CustomURLFilter'
```

#### g、Pipeline处理不同的Item

scrapy所有的迭代出来的的Item都会经过所有的Pipeline，如果需要处理不同的Item，只能通过`isinstance()`方法进行类型判断，然后分别进行处理，暂时没有更好的方案

#### h、url按顺序执行

我们可以通过Request的priority控制url的请求的执行顺序，但由于网络请求的不确定性，不能保证返回也是按照顺序进行的，如果需要进行逐个url请求的话，吧url列表放在meta对象里面，在response的时候迭代返回下一个Request对象到调度器，达到顺序执行的目的，暂时没有更好的方案

## 