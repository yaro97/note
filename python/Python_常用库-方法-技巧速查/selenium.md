# selenium-爬虫-总结

## 快速开始

项目参考：[TaoBaoGoods_selenium](https://github.com/yaro97/spider_projects/tree/master/TaoBaoGoods_selenium)

主要用来驱动浏览器，用作自动化测试；在做爬虫是会遇到JS渲染的网页，用requests请求无法获取相应的请求内容；

此时，我们可以使用selenium来实现：用selenium库可以直接驱动浏览器，用浏览器执行JS的渲染，得到的结果便是渲染之后的结果，我们便可以拿到渲染之后的内容。

假如使用调用Chrome()对象(浏览器)的话，需要安装对应[chromedrive](https://sites.google.com/a/chromium.org/chromedriver/)。

```python
pip install selenium
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

## selenium概述

Selenium 是自动化测试工具。它支持各种浏览器，包括 Chrome，Safari，Firefox ，PhantomJS等浏览器。

再白话点，就是：Selenium是一个驱动，可以操作Chrome等浏览器；我们可以通过python等编程语言来通过Selenium控制浏览器。

Selenium 有两个版本：最新版的Selenium2 ，又名 WebDriver，它的主要新功能是集成了 Selenium 1.0 以及 WebDriver（WebDriver 曾经是 Selenium 的竞争对手）。也就是说 Selenium 2 是 Selenium 和 WebDriver 两个项目的合并，即 Selenium 2 兼容 Selenium，它既支持 Selenium API 也支持 WebDriver API。

## selenium 工作原理

webdriver 是按照 server – client 的经典设计模式设计的。 server 端就是 remote server，可以是任意的浏览器。当我们的脚本启动浏览器后，该浏览器就是remote server，它的职责就是等待 client 发送请求并做出响应； client 端简单说来就是我们的测试代码，我们测试代码中的一些行为，比如打开浏览器，转跳到特定的 url 等操作是以 http 请求的方式发送给被 测试浏览器，也就是 remote server；remote server 接受请求，并执行相应操作，并在 response 中返回执行状态、返回值等信息； webdriver 的工作流程：

WebDriver 启动目标浏览器， 并绑定到指定端口。 该启动的浏览器实例， 做为 web driver 的 remote server。
Client 端通过 CommandExcuter 发送 HTTPRequest 给 remote server 的侦听端口（通信协议： the webriver wire protocol）
Remote server 需要依赖原生的浏览器组件（如：IEDriverServer .exe、chromedriver .exe） ，来转化转化浏览器的 native 调用。
Python版Selenium提供了一套用于编写功能测试及验收测试的API。利用这套简单的API，不仅可以很直观的接触到Selenium WebDriver的所有功能，而且还可以很方便的访问各类WebDrivers，如Firefox、Ie、Chrome、Remote等。目前Selenium支持的Python版本：2.7、3.2、3.3和3.4。

## selenium-爬虫使用场景

提取网站的中目标信息可能遇到的情况有: 1. 目标信息在response中, 2. 通过Ajax返回,3. 通过js渲染得到.

前两种方法都很容易直接提取,遇到js渲染,甚至js加密的就不那么容易提取.

但是,网站的内容总是要给用户看到吧,所以无论你使用那些技术,目标信息都会呈现在浏览器中,即,浏览器(Chrome等)会使用自己的引擎来解释这些js,所以我们直接提取Chrome展示的结果即可.

Python想要操作浏览器,就需要selenium了,当然在实际操作时,用无界面浏览器PhantomJS比Chrome的效率更高.

## 第一个脚本

```python
#coding = utf-8     
from selenium import webdriver
from selenium.webdriver.common.keys import keys  
  
driver = webdriver.Firefox()  # 创建Firefoxwebdriver实例
driver.get('http://www.python.org')  # get请求
assert 'python' in driver.title  # 断言判断标题中是否有"python"
elem = driver.find_element_by_name('q')  # find_element_by_* 定位元素
elem.send_keys('pycon')  # send_keys 模拟键盘操作
elem.send_keys(keys.RETURN)  # 模拟键盘操作:回车
assert 'No results found.' not in driver.page_source  
driver.close() # quit推出浏览器,close关闭标签;一个标签时,二者等效
```

> Selenium.webdriver模块提供了webdriver的实现方法，目前支持这些方法的有Firefox、Chrome、IE和Remote。其中，Keys类提供了操作键盘的快捷键，如RETURE、F1、ALT等。

## 编写测试脚本

Selenium可用来编写测试用例，虽然Selenium并没有提供测试框架，但可以调用python的unittest模块，或py.test和nose。
本节给出了一个实现搜索python.org功能的测试用例，其中使用的是unittest框架。

```python
import unittest  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
   
class PythonOrgSearch(unittest.TestCase):  
   
  def setUp(self):  
    self.driver = webdriver.Firefox()  
   
  def test_search_in_python_org(self):  
    driver = self.driver  
    driver.get("http://www.python.org")  
    self.assertIn("Python", driver.title)  
    elem = driver.find_element_by_name("q")  
    elem.send_keys("pycon")  
    elem.send_keys(Keys.RETURN)  
    assert "No results found." not in driver.page_source  
   
  def tearDown(self):  
    self.driver.close()  
   
if __name__ == "__main__":  
  unittest.main()
```

更多测试脚本相关内容参考: [selenium测试总结](http://blog.csdn.net/intel80586/article/details/8783279)   [Python必会的单元测试框架 —— unittest](https://huilansame.github.io/huilansame.github.io/archivers/python-unittest)

## 操作浏览器

我们平时使用浏览器，常用的操作（如：点击连接，滚动滑轮，定位输入框，输入法内容，提交-回车，等等）Selenium同样也可以完成。

```python
## 定位元素
element = driver.find_element_by_id("passwd-id")
# 定位元素的方法除了id，还有有很多：name xpath link_text partial_link_text tag_name class_name css_selector 等等
# 另外，还可以通过By类来定位元素，如：
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')

# 模拟键盘
element.send_keys('some text')  # send content
element.send_keys('keys.RETURN')  # return key
element.clear()  # clear content
# 其他的表单元素（多选，下拉框等），selenium也相应的API

# 前进/后退
element.forard()  
element.back()  

# 另外，selenium还可以窗口切换（多标签）、元素拖拽、弹窗处理、cookie处理等
```

更多内容请参考：[Selenium with Python](http://selenium-python.readthedocs.io/)    [爬虫利器-selenium](https://cuiqingcai.com/2599.html)

## 获取元素

通过`driver = webdriver.Firefox()  `获取浏览器对象（`selenium.webdriver.chrome.webdriver.WebDriver`对象），我们可以把`driver`看成浏览器，可以对其进行：点击链接、刷新、返回、前进、新建标签、表单输入/提交等等；

在相应一系列的操作过后，可以使用`driver.title`和`driver.page_source`分别获取**当前页面**的title和html源码；

在定位（`element = driver.find_element_by_*`）特定元素后(获取`selenium.webdriver.remote.webelement.WebElement`对象),我们可以使用`element.text`获取**定位元素（及其子元素）的内容**,可以进一步对`element`对象进行定位元素的操作,这点和JQuery类似。

## 页面等待

[Wait-官网](http://selenium-python.readthedocs.io/waits.html)

These days most of the web apps are using AJAX techniques. When a page is loaded by the browser, the elements within that page may load at different time intervals. This makes locating elements difficult: if an element is not yet present in the DOM, a locate function will raise an ElementNotVisibleException exception. Using waits, we can solve this issue. Waiting provides some slack between actions performed - mostly locating an element or any other operation with the element.

Selenium Webdriver provides two types of waits - implicit & explicit. An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution. An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.

### 显示等待（  implicit waits）

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
```

This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds. WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully. A successful return is for ExpectedCondition type is Boolean return true or not null return value for all other ExpectedCondition types.

上述例子中，等待10s，直到满足expected_conditions，否则抛出TimeoutException 异常；10s内没0.5s检测一次expected_conditions是否满足。

内置**Expected Conditions**有如下，当然你也可以自己定义：

- title_is
- title_contains
- presence_of_element_located
- visibility_of_element_located
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_c

### 隐式等待（Implicit Waits）

An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0. Once set, the implicit wait is set for the life of the WebDriver object.

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```

## 一个例子

项目含有两个文件`main.py`和`config.py`

**config.py内容如下**：

```python
MONGO_URL = "localhost"
MONGO_DB = "taobao"
MONGO_TABLE = "products"

SERVICE_ARGS = ["--load-images=false", "--disk-cache=true"]

TAOBAO_URL = "https://www.taobao.com"  # 请勿修改
KEYWORD = "女装"
```

**main.py文件内容如下**:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yaro

# 内置库
import re

# 第三方库
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pymongo

# 项目文件
from config import *

# 设置MongoDB
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

# 设置浏览器
driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
driver.set_window_size(1400, 900)

wait_until = WebDriverWait(driver, 10).until


def search(taobao_url, keyword):
    """
    根据关键词请求页面
    :param taobao_url:
    :param keyword: 搜索啥?
    :return: 搜索结果的总页数
    """
    print("正在搜索...")
    try:
        driver.get(taobao_url)
        search_input = wait_until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))  # 等待"搜索框"加载完成,并赋值
        search_submit = wait_until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")))  # 等待"搜索按钮"加载完成,并赋值
        search_input.send_keys(keyword)  # 输入"keyword"到"搜索框"
        search_submit.click()  # 搜索
        total_page_num_text = wait_until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))  # 等待"共xxx页"加载完成,并赋值
        total_page_num = int(re.compile('(\d+)').search(total_page_num_text.text).group(1))  # 获取"共xxx页"中的"xxx"(数字)
        return total_page_num
    except TimeoutException:
        return search(taobao_url, keyword)


def next_page(page_num):
    """
    通过输入的指定页数,翻页
    :param page_num: 搜索页面底部:"到第xx页"
    :return:None
    """
    print("正在翻页...")
    try:
        page_num_input = wait_until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        page_num_submit = wait_until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        page_num_input.clear()
        page_num_input.send_keys(page_num)
        page_num_submit.click()
        wait_until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active > span"),
            str(page_num)))  # 判断是否是page_num页
    except TimeoutException:
        next_page(page_num)


def get_products():
    """
    解析当前页面,得到各个产品的信息(生成器)
    :return: 当前页面各产品的信息
    """
    wait_until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist .items .item")))  # 等待当前页产品信息加载结束
    d = pq(driver.page_source)  # 把当前页html源码转化为PyQuery对象
    products = d.find("#mainsrp-itemlist .items .item").items()  # 解析当前页所有产品(列表)
    for product in products:
        yield {
            "image": product.find(".pic .img").attr("src"),
            "price": product.find(".price").text(),
            "deal": product.find(".deal-cnt").text()[:-3],
            "title": product.find(".title").text(),
            "shop": product.find(".shop").text(),
            "location": product.find(".location").text()
        }


def save_to_mongo(product):
    """
    保存到MongoDB
    :param product:某个产品的信息
    :return: None
    """
    try:
        if db[MONGO_TABLE].insert(product):
            print("保存到MongoDB成功", product)
    except Exception:
        print("保存到MongoDB失败", product)


def main():
    try:
        # 执行search函数,并返回搜索结果总页数(int)
        total_page_num = search(TAOBAO_URL, KEYWORD)

        # 保存首页每一个product信息到数据库
        for product in get_products():
            save_to_mongo(product)

        # 循环第2页之后的页面
        for page_num in range(2, total_page_num + 1):
            next_page(page_num)
            for product in get_products():
                save_to_mongo(product)

    # except Exception:
    #     print("貌似哪儿出错了!!")
    finally:
        driver.close()


if __name__ == '__main__':
    main()
```

