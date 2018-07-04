# Beautifulsoup4

更加方便的网页解析库，依赖于lxml库，解析速度当然没有lxml快啦！

```python
pip install beautifulsoup4 # 第四个版本
from bs4 import BeautifulSoup # 库（包）源代码（.tar.gz）的文件夹结构（名称）决定的
soup = BeautifulSoup('<html></html>','lxml') #第一个参数是html代码 ，第二个参数是解析方式。
print(soup.select('h2'))
```

## 标签选择器

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

## 标准选择器

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

## CSS选择器

- 通过select()直接传入CSS选择器即可完成选择
- soup.select('#list-2 .element' a)；
- 获取id属性的值：`soup.select('ul')[0]['id']` 或`soup.select('ul')[0].attrs['id']`；
- 获取内容：`soup.select('li')[0].get_text()` , 貌似`soup.select('li')[0].text`也可以;

## 总结

- 推荐使用lxml解析库，必要时使用html.parser解析库；
- 标签选择筛选功能弱但是速度快；
- 建议使用find()、find_all()查询匹配单个结果或者多个结果；
- **如果对CSS熟悉，建议使用select()**；
- 记住常用的获取属性和文本值的方法；