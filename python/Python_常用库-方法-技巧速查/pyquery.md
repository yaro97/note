# Pyquery相关笔记

项目参考：[WeiXin_ProxyPool](https://github.com/yaro97/spider_projects/blob/master/WeiXin_ProxyPool/main.py)

参考: 

[Pyquery官网](https://github.com/gawel/pyquery)

[Pyquery手册](http://pyquery.readthedocs.io/en/latest/)

[Jquery手册](https://www.w3schools.com/jquery/)

也是一个网页解析库，依赖于lxml库,熟悉jquery建议使用这个，二者语法相似,[Pyquery官网](https://pythonhosted.org/pyquery/), 全部[API](https://pythonhosted.org/pyquery/api.html)。

**安装:** 

```python
pip install pyquery
```

## 加载文档的方式

pyquery uses **lxml** for fast xml and html manipulation. 完全和Jquery同样的API，初始化方式有三种：

```python
pip install pyquery
from pyquery import PyQuery as pq
from lxml import etree/html  # 处理xml/html
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

> 从上面可以看到Pyquery可以直接请求URL, 当然我还是喜欢Requests, 功能太多难免有些不专业!哈哈!!

## 预处理: 规范html源码

为了避免一些html代码不规范, 可以使用lxml.html(或者lxml.etree)格式化一下.

```python
from lxml import html
from lxml import etree
d = pq(html.fromstring("<html>...</html>"))
d = pq(etree.fromstring("<html>...</html>"))
## 出错的话记得转码:
# html = html.encode('uft-8') # 先使用encode('utf-8')转换成字节型字符串;
>>> d = pq(html.fromstring(html))  # 转换成HtmlElement对象,可以使用tosring()再转变成字节型字符串,再次使用decode('utf-8')转换成Unicode字符串
## 意义:当html有缺失/不完整时,会自动补全;
```

> lxml.html 是一个专门用来处理 HTML 文档的，虽然他依旧是基于 HTML parser 的，但是她提供了很多有针对性的 API 。API和lxml.etree相似, 深入了解，请查阅[官方文档](http://lxml.de/)。
>
> lxml的相关入门知识参考: [lxml学习笔记](https://www.jianshu.com/p/e084c2b2b66d)

## 获取html和text方法

```python
d = pq("<html><title>程序员笔记 | 分享IT教程以及相关的笔记</title></html>")
# Now d is like the $ in jquery:
print(d('html').html())
print(d('title').text())
## 输出如下:
# <title>程序员笔记 | 分享IT教程以及相关的笔记</title>
# 程序员笔记 | 分享IT教程以及相关的笔记
```

You can use some of the pseudo classes that are available in jQuery but that are not standard in css such as `:first :last :even :odd :eq :lt :gt :checked :selected :file` :

## 获取属性

```python
d = pq('<div><a href="http://www.school1024.com">程序员笔记</a></div>')
print(d('a').attr('href'))
## 输出:
# http://www.school1024.com
```

## 遍历元素

```python
for li in d('li').items():  # 首先:获取所有li标签(生成器)
	print(li.text(), li('a').attr('href'))
```

## 常用API举例

- 基本的CSS选择器：`doc('#container .list li')`
- `doc('.a.b')` 同时包含a和b; 
- `doc(.a, .b)`包含a或者b;
- `doc('.list').find('li') `选择所有的后代li对象，**等同于`doc('.list li')`** 或 `doc('.list')('li')` ；
- `doc('.list').children('li')` 子对象，**等同于`doc('.list>li')`**
- 父元素: **`doc('.list').parent()`**
- 祖先元素:**`doc('.list').parents()`**
- 兄弟元素：**`doc('.list').siblings()`**
- **遍历：`lis = doc('li').items()`**，通过items()方法生成迭代器，返回的对象还是pyquery对象；
- 获取属性：`a.attr('href')` 或 `a.attr.href`
- 获取文本：`a.text() `获取所有的文本（包含子元素）；
- 获取html：`a.html()` （里面的所有内容，包含html标签和文本）；


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

**DOM操作：可用于复杂的解析**

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

更多CSS选择器可以查看：http://www.w3school.com.cn/css/index.asp

