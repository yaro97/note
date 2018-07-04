# Scrapy

参考：[官网](https://docs.scrapy.org/en/latest/)  [Scrapy教程](http://blog.csdn.net/Inke88/article/details/60573507) [Learn Scrapy](https://learn.scrapinghub.com/scrapy/)

Scrapy，Python开发的一个快速,高层次的web抓取框架；

- Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。
- 其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的，也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。
- Scrapy用途广泛,可以用于数据挖掘、监测和自动化测试
- Scrapy使用了Twisted 异步网络库来处理网络通讯。

## 1、架构和数据流

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

## 2、基本使用过程

参考项目：[腾讯hr招聘信息](https://github.com/yaro97/spider_projects/tree/master/TencentHR_scrapy)

### a、创建项目：

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

### b、创建爬虫：

`scrapy genspider xxx www.xxx.com`

### c、定义item：

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

### d、编写爬虫文件：

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

### e、处理/存储数据：

1、可以使用自带的`Feed exports`到处数据文件；

2、也可以编写Pipeline文件：处理item， 写入/文件数据库等...

### f、执行爬虫：

`scrapy crawl xxx`，当然你也可以通过代码文件`run.py`运行爬虫，参考[官网](https://doc.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script)

## 3、深入介绍

### a、关于爬虫文件

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

### b、关于Pipeline

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



### c、CrawlSpider和rules

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

### d、Middleware

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

### e、缓存

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

### f、多线程

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

## 4、进阶

### a、下载文件/图片

项目参考：DouyuImage_scrapy



## 5、常见问题

### a、项目名称问题

在使用的时候遇到过一个问题，在初始化`scrapy startproject tutorial`的时候，如果使用了一些特殊的名字，如：`test`, `fang`等单词的话，通过`get_project_settings`方法获取配置的时候会出错，改成`tutorial`或一些复杂的名字的时候不会

```python
ImportError: No module named tutorial.settings
```

这是一个bug，在github上有提到：<https://github.com/scrapy/scrapy/issues/428>，但貌似没有完全修复，修改一下名字就好了（当然`scrapy.cfg`和`settings.py`里面也需要修改）

### b、为每个pipeline配置spider

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

### c、获取提取链接的节点信息

通过LinkExtractor提取的`scrapy.Link`默认不带节点信息，有时候我们需要节点的其他attribute属性，`scrapy.Link`有个`text`属性保存从节点提取的`text`值，我们可以通过修改`lxmlhtml._collect_string_content`变量为`etree.tostring`，这样可以在提取节点值就变味渲染节点`scrapy.Link.text`，然后根据`scrapy.Link.text`属性拿到节点的html，最后提取出我们需要的值

```python
from lxml import etree
import scrapy.linkextractors.lxmlhtml
scrapy.linkextractors.lxmlhtml._collect_string_content = etree.tostring
```

### d、从数据库中读取urls

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

### e、如何进行循环爬取

有时候我们需要爬取的一些经常更新的页面，例如：间隔时间为2s，爬去一个列表前10页的数据，从第一页开始爬，爬完成后重新回到第一页

目前的思路是，通过parse方法迭代返回Request进行增量爬取，由于scrapy默认由缓存机制，需要修改

### f、关于去重

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

### g、Pipeline处理不同的Item

scrapy所有的迭代出来的的Item都会经过所有的Pipeline，如果需要处理不同的Item，只能通过`isinstance()`方法进行类型判断，然后分别进行处理，暂时没有更好的方案

### h、url按顺序执行

我们可以通过Request的priority控制url的请求的执行顺序，但由于网络请求的不确定性，不能保证返回也是按照顺序进行的，如果需要进行逐个url请求的话，吧url列表放在meta对象里面，在response的时候迭代返回下一个Request对象到调度器，达到顺序执行的目的，暂时没有更好的方案