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

## 5、基本概念Q&A

### 爬虫是什么？

### **请求**网站并**提取**数据的**自动化**程序

### 爬虫基本过程

1. 发起请求：通过HTTP库向目标站点发起请求，即发送一个Request，请求可以包含额外headers等信息，等待服务器响应。
2. 获取相应内容：如果服务器能正常相应，会返回一个Response给客户端（HTTP库），Response的内容便是所要获取的页面内容，类型可能有HTML、Json字符串（XHR：XML Http Request对象，ajax的核心技术）、二进制数据（eg：图片视频）等类型。
3. 解析内容：得到的内容可能是HTML，可以用正则表达式、网页解析库进行解析；可能是Json，可以直接转为Json对象（dict）解析；可能是二进制数据，可以做存储或者进一步的处理。
4. 保存数据：保存形式多样，可以存为文本；也可以保存至数据库；或者保存特定格式的文件（图片）。

### Request & Response

1. HTTP Request：浏览器发送信息给服务器。
2. HTTP Response：服务器收到浏览器发送的信息后，能够根据浏览器发送消息的内容，做出相应的处理，然后把消息回传给浏览器。
3. 浏览器收到服务器的Response信息后，会对信息进行相应的处理，然后展示。

### Request中包含了什么？

1. 请求URL：URL统一资源定位符，如：一个网页稳定、一张图片、一个视频等都可以用URL唯一来确定。
2. 请求方式：主要有GET、POST两种类型，另外还有HEAD、PUT、DELETE、OPTIONS等。
3. 请求头：包含请求时的头部信息，如User-Agent、Host、Cookies等信息。
4. 请求体：请求时额外携带的数据，GET请求时不会有内容，只有POST请求是才会有，如表单提交时的表单数据。

### Response中包含了什么？

1. 相应状态：200=成功，301跳转，404=找不到页面，500+（502、503...）=服务器错误等。
2. 响应头：如内容类型、内容长度、服务器信息、设置Cookie等。
3. 响应体：最主要的部分，包含了请求资源的内容，如网页HTML、图片二进制数据等。

### 爬虫能抓取什么数据？

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

### 怎样解析处理？

1. 直接处理：返回的是最简单的字符串。
2. Json解析（ajax）：返回的是json格式的字符串。
3. 正则表达式：匹配、提取返回的html中相应的文本。
4. BeautifulSoup解析库：更容易、好用
5. PyQuery解析库：API 同 JQuery
6. XPath解析库：Built-in

### `ctrl+u`与`inspect-Elements中`区别？

- 拿`m.weibo.com` 举例，在请求时首先返回最初的doc（dom）html框架，然后里面有很多JS；后台会通过ajax请求返回数据，然后用JS“填充至”原html中。
- 我们请求的结果与“浏览源代码（ctrl + u）”是一致的。

### 怎么解决上面JS渲染导致的问题？

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

### 怎么数据持久化（存储）？

1. 文本：纯文本、Json、Xml等。
2. 关系型数据库：如MySQL、Oracle、SQL Server等具有结构化表结构形式存储。
3. 如MongoDB、Redis等Key-Value形式存储。
4. 二进制文件：图片、视频、音频等直接保存成特定的格式即可。

## 6、爬虫常用库/工具

### 工具总览

爬虫使用到的python库的有：请求库、解析库、存储库、工具库；

请求库：urllib, requests, selenium

解析库： lxml, beautifulsoup, pyquery

存储库：pymysql, pymongo, redis

常用工具：ipython, jupyter, RE, Json, Chrome, Phantomjs, Mysql, MongoDB, Redis, Sublime_text, Pycharm等

### Urllib库基本使用

python自带的请求库,下面的Requests是此库的包装;

### Requests库基本使用

见《requests.md》

### Re 正则表达式

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

### Lxml - xpath解析库

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

### PyQuery详解

略，详细见《pyquery.md》

### Beautifulsoup4

略，详细见《beautifulsoup4.md》

### Selenium详解

略，详细见《selenium.md》

### Pymysql - 连接Mysql

用于操作mysql数据库; python2使用`mysql-python`库；在python3中使用`pymysql`代替。

```python
pip install pymysql
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='123456',port='3306', db='mysql')  # 声明一个连接对象
cursor = conn.cursor()  # 调用conn的cursor方法，指定数据库的操作对象
cursor.execute('select * from db')  # 调用一些函数执行sql语句
cursor.fetchone()  # 使用fetchone方法拿到数据库的内容
```

### Pymongo - 连接MongoDB

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

### Redis - 连接Redis

也是非关系型数据库，也是key:value形式存储的。主要应用于后面的分布式爬虫、维护一个爬取队列，运行效率比较高，用它维护一个公共爬取队列，效果比较好。

```python
pip install redis
import redis
r = redis.Redis('localhost', 6379)  #  声明一个redis对象
r.set('name', 'Bob')  # 插入数据
r.get('name')  # 获取数据
```

### Phantomjs - 无界面浏览器

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

### Flask - 简单web框架

是一个web库，后面的代理设置（代理的获取、存储）会用到。

```python
pip install flask  # 依赖的库比较多
```

### Django - 强大web框架

是一个web服务器框架，提供了完整的后台管理，提供了模板引擎、接口、路由等。可以使用django做一个完整的网站。后面的分布式爬虫维护时会用到。

```python
pip install django  # 依赖的库比较多
```

### Jupyter - python记事本

运行在网页端的记事本，可以调试命令，支持mk语法。

```python
pip install jupyter  # 依赖的库比较多
jupyter notebook  
```

### MongoDB环境配置

windows建议使用--install添加服务，GUI数据查看建议使用robo3t;

```mysql
mongod --bind_ip 0.0.0.0 --logpath D:\Dev\MongoDB\Server\3.6\data\logs\mongo.log --logappend --dbpath D:\Dev\MongoDB\Server\3.6\data\db --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install
# 需要提前创建数据, log文件夹;
db;
show dbs;
db.test.insert({'a':'b'})
```

### Redis环境配置

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

### MySQL环境配置

可以使用MariaDB代替;

```mysql
mysql -uroot -p 
# 可以使用-h参数，参数后面可以有空格，可以没有空格；
# 但是-p后面不能有空格，否则需要重新输入密码。
```

win下GUI管理工具：Navicat/MySQL Front等等。

### 各工具的效率/选择的思考

解析库中，Pyquery和Beautifulsoup4都是基于Lxml库的，网上很多人证明Lxml库的效率更高!

当然，Pyquery和Beautifulsoup4既然包装了Lxml,易用性肯定更高！

那么我们如何选择呢,选择易用性 or 效率 ？

首先，引入python实现并行任务的相关概念：

由于CPython的GIL的原因，python无法实现多线程,导致CPU密集型任务使用多线程反而降低效率,但是在I/O密集型的任务上，多线程(Threading)依然可以有效的提升效率！

为什么说这个呢？对于任何计算机实现的任务,我们都可以这么理解：

为了实现一个网络任务，计算机需要 **联网** - **访问数据** - **下载数据** - **解析数据** - **保存数据(I/O)** ， 而在所有的过程中，都需要**CPU计算**, 整个网络任务的执行时间(效率)取决于效率最低(时间最多)的那个环节！

So，请求库/解析库的效率真的是你特别需要解决的么？ 相信你已经有了答案!😄

## 7、Scrapy框架

略，详情见《scrapy.md》


## 