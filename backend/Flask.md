参考: [flask课件](https://nunchakushuang.gitbooks.io/flask/content/di-si-zhang-ff1a-flask-ru-men-ff08-mo-ban-ff09.html)

# 01 工具/环境准备

- python3.6+
- pycharm
- 虚拟环境:
    - pip install pipenv
    - mkdir flask_project && cd flask_project
    - pipenv install # 当前目录新建虚拟环境
    - 修改 Pipfile 文件中的 pip repo 地址为: https://pypi.tuna.tsinghua.edu.cn/simple
    - pipenv install flask # 在当前虚拟环境安装flask

# 02 认识WEB

## URL介绍

URL是Uniform Resource Locator的简写，统一资源定位符。

一个URL由以下几部分组成：
```
scheme://host:port/path/?query-string=xxx#anchor
```

- scheme：代表的是访问的协议，一般为`http`或者`https`以及`ftp`等。
- host：主机名，域名，比如`www.baidu.com`。
- port：端口号。当你访问一个网站的时候，浏览器默认使用80端口。
- path：查找路径。比如：`www.jianshu.com/trending/now`，后面的`trending/now`就是path。
- query-string：查询字符串，比如：`www.baidu.com/s?wd=python`，后面的`wd=python`就是查询字符串。
- anchor：锚点，后台一般不用管，前端用来做页面定位的。比如：https://baike.baidu.com/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923?fr=aladdin`#7`

## web服务器/应用服务器/web应用框架：

- web服务器：
负责处理http请求，响应`静态文件`，常见的有Apache，Nginx以及微软的IIS.

- 应用服务器：
负责处理逻辑的服务器(`动态文件`)。比如php、python的代码，是不能直接通过nginx这种web服务器来处理的，只能通过应用服务器来处理，常见的应用服务器有uwsgi、tomcat等。

- web应用框架：
一般使用某种语言，封装了常用的web功能的框架就是web应用框架，flask、Django以及Java中的SSH(Structs2+Spring3+Hibernate3)框架都是web应用框架。
![逻辑图0](https://i.loli.net/2019/02/14/5c6548b7bca36.png)
![逻辑图1](https://i.loli.net/2019/02/14/5c6543391505b.png)
![逻辑图3](https://i.loli.net/2019/02/14/5c65433928987.png)
![逻辑图2](https://i.loli.net/2019/02/14/5c65433925c4a.jpg)

## Content-type和Mime-type的作用和区别：

两者都是指定服务器和客户端之间传输数据的类型，区别如下：
- Content-type：既可以指定传输数据的类型，也可以指定数据的编码类型，例如：text/html;charset=utf-8
- Mime-type：不能指定传输的数据编码类型。例如：text/html

常用的数据类型如下：
- text/html（默认的，html文件）
- text/plain（纯文本）
- text/css（css文件）
- text/javascript（js文件）
- application/x-www-form-urlencoded（普通的表单提交）
- multipart/form-data（文件提交）
- application/json（json传输）
- application/xml（xml文件）

# 03flask入门（URL）

## Flask简介

Flask是一个使用 Python 编写的轻量级 Web 应用框架。特点如下:
- 为框架/简洁/只做它需要做的,给开发者提供了很大的扩展性;
- Flask和相关的依赖(Jinja2,Werkzeug)设计得非常优秀,用起来很爽;
- 开发效率非常高,比如使用SQLAlchemy的ORM操作数据库可以节省开发者大量书写sql语句的时间;
- 社区活跃度非常高;

Flask是多个库的集合,[常用依赖如下](https://github.com/pallets):
- Flask==1.0.2
    - click [required: >=5.1, installed: 7.0]
    - itsdangerous [required: >=0.24, installed: 1.1.0]
    - Jinja2 [required: >=2.10, installed: 2.10]
        - MarkupSafe [required: >=0.23, installed: 1.1.0]
    - Werkzeug [required: >=0.14, installed: 0.14.1]

## 第一个Flask程序详解

```python
# 从flask包中导入Flask类
# Flask类是项目的核心
# 以后的操作,如(注册url/注册蓝图...)都是基于这个类
from flask import Flask

# 创建一个Flask对象(传递__name__)参数
app = Flask(__name__)


# 通过装饰器将 url的 根目录(/) 映射到 hello_world 函数
# 返回根目录, 会将 hello_world 函数的返回值, 返回给浏览器
@app.route('/')
def hello_world():
    return 'Hello World!'


# 如果本文件作为主文件运行, 通过run方法在在本地启动这个网站服务
# app.run() 是Flask中的一个测试用的 应用服务器
# 既然是测试用的, 性能自然不是特别好, 生成环境记得替换为 uWSGI 等
# 内部原理相当于:
# while True:
#       listen()
#       ...
if __name__ == '__main__':
    app.run()  # 可以传参, 修改host,port...等
```

## debug模式详解

默认情况下,代码出现异常只会在pycharm中提示,不会在浏览器中提示.
如果开启debug模式:
- 浏览器中会提示异常信息;而且修改代码后,
- `ctrl + s` Flask会`自动重启服务器`

开启debug模式的方式:
- 方法1:pycharm的话, 在 `edit configrations` 中勾选 `FALSK_DEBUG` 选项即可.

> 以下方法需要在 `flask虚拟环境中` 运行 `python app.py` 命令

- 方法2:

    ```python
    if __name__ == '__main__':
        app.run(debug=True)
    ```

- 方式3: `app.debug = True`
- 方式4: 通过配置开启`app.config.update(DEBUG=True)`, `app.config`是一个dict, 可以调用`update()`方法
- 方式5: 
```python
# 新建 config.py 配置文件, 写入如下内容:
DEBUG=True

# 在 app.py 文件中引入 并 通过from_object()方法读取
import config
app.config.from_object(config)
```

> 另外我们可以通过 `Debugger PIN: 203-347-448` 直接在网页中对应的frame处开启交互式 python shell 调试 . PIN码默认有8h有效期(放在cookie中).

## 配置文件两种方式详解

- 方式1: 使用 `app.config.from_object`的方式加载配置文件
    1. 新建 `config.py` 文件;
    2. 导入 `import config`
    3. 引入配置文件 `app.config.from_object(config)`

- 方式2: 使用 `app.config.from_pyfile`的方式加载配置文件
    1. 这种方式不需要 `import`, 直接使用使用 `app.config.from_pyfile('config.py')`即可;
    - 配置文件不一定是 `.py`文件, `.txt`文件亦可; 但是后缀名不可省
    - 这种方式可以传递第二个参数 `(silent=True)` - 当文件不存在时不报错, 默认是报错的(False)

## URL中两种方式传参

我已已经知道:Flask中URL与视图函数的映射是通过`@app.route()`装饰器实现,装饰器可以接受用户传递的参数.接受用户传递的参数有两种方式:
1. 通过path的形式;
2. 通过查询字符串的形式(get中`?`的方式);

### 通过path的形式;

- 传递参数:
    传递参数的语法为: `/<参数名>/`,然后在试图函数中,也需要定义同名的参数.

    ```python
    @app.route('/p/<article_id>')
    def article_detail(article_id):
        return '您访问的文章的id为:{}'.format(article_id)
    ```

- 参数的数据类型
    语法为: `<converter:variable_name>`, 如:

    ```python
    @app.route('/post/<int:post_id>')
    def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    ```

    常用的转换器类型如下:

    ```
    string	(缺省值)接受任何不包含斜杠的文本
    int 接受正整数
    float	接受正浮点数
    path	类似 string ，但可以包含斜杠
    uuid	接受 UUID 字符串
    any 可以指定多个路径映射到同一个视图函数
    ```

    **Note:** 
    - string(默认)类型的参数不能接受 `aa/bb/cc`(报错), 只能接受不含`/`的值(如:`aa`); path却可以,会把所有的值`aa/bb/cc`都传递给参数.

        ```python
        @app.route('/p/<path:article_id>')
        def article_detail(article_id):
            return '您访问的文章的id为:{}'.format(article_id)
        # path类型 - 可以访问`http://127.0.0.1:5000/p/aa/bb/cc`
        ```
    - UUID 是 通用唯一识别码（Universally Unique Identifier）的缩写.重复概率: 如果地球上每个人都各有6亿笔GUID，发生一次重复的机率是50%

        ```python
        # python生成随机的uuid
        import uuid
        print(uuid.uuid4())
        ```

    - any 多个路径映射到同一个视图函数

        ```python
        # /blog/<id>/
        # /user/<id>/
        @app.route('/<any(blog, user):url_path>/<id>/')
        def item(url_path, id):
            if url_path == 'blog':
                return '博客详情:{}'.format(id)
            else:
                return '用户详情:{}'.format(id)
        ```

        如此,便可以访问`http://127.0.0.1:5000/blog/xxx`和`http://127.0.0.1:5000/user/xxx`都映射到item函数

### 通过查询字符串的形式

```python
from flask import request

@app.route('/q/')
def wd():
    wd = request.args.get('wd')
    return '您通过查询字符串(问号)方式传递的参数是:{}'.format(wd)
```

> 如此, 便可以获取url中`?`后的参数, 如: `http://127.0.0.1:5000/q/?wd=eddcc`中的`wd=eddcc`

### 两种方式的区别/选择

- 前台页面涉及到SEO优化,建议使用path方式传参,**这个页面对SEO更友好**;
- 后台CMS系统不需要考虑SEO优化, 可以选择查询字符串方式传参, **写起来更简单**;

## url_for使用详解

之前使用`app.route()`把url映射到视图函数, `url_for`的功能相反 - 通过视图函数找到对应的`url`.

### `url_for`的基本使用：
- `url_for`第一个参数，是视图函数的名字的`字符串`。后面的参数就是传递给`url`。
- 如果传递的参数之前在`url`中已经定义了，那么这个参数就会被当成`path`的形式给
- `url`。如果这个参数之前没有在`url`中定义，那么将变成`查询字符串`的形式放到`url`中。
```pythonthon
from flask import url_for

@app.route('/post/list/<page>/')
def my_list(page):
    return 'my list'

print(url_for('my_list',page=1,count=2))
# def url_for(endpoint, **values): pass
# 第一个参数为视图函数,第二个参数为关键字参数
# 构建出来的url：/my_list/1/?count=2
# 视图函数有 page 参数 -> path传参
# 视图函数没有 count 参数 -> 查询字符串传参
```

### 为什么需要`url_for`：
1. 将来如果重新规划网站`URL`，但没有修改该URL对应的函数名，就不用到处去替换URL了。
2. `url_for`会自动的处理那些特殊的字符，不需要手动去处理。
    ```pythonthon
    url = url_for('login',next='/')
    # 会自动的将/编码，不需要手动去处理。
    # url=/login/?next=%2F
    ```

> 强烈建议以后在使用url的时候，使用`url_for`来反转url。

## 自定义URL转换器

之前介绍url 通过path方式传参时, 可以使用系统自带的转换器(string,int,path...),我们也可以自定义转换器. 

### 自定义URL转换器的方式：

1. 定义一个类，继承自`BaseConverter`。
2. 在自定义的类中，重写`regex`，也就是这个变量的正则表达式。
3. 将自定义的类，映射到`app.url_map.converters`上。比如：

```python
from flask import Flask
from werkzeug.routing import BaseConverter  # 查看BaseConverter类的定义便可以发现端倪

app = Flask(__name__)


class TelConverter(BaseConverter):  # 自定义转换器: 一个url中含有一个变量 - 该变量必须是手机号码格式.
    regex = r'1[34578]\d{9}'


app.url_map.converters['tel'] = TelConverter  # 把tel映射到TelConverter类


@app.route('/tel/<tel:my_tel>')
def tel_view(my_tel):
    return '手机号码是: {}'.format(my_tel)
    # http://127.0.0.1:5000/tel/13310213212


if __name__ == '__main__':
    app.run()
```

### `to_python`的作用：
这个方法的返回值，将会传递到view函数中作为参数。

```python
from flask import Flask
from werkzeug.routing import BaseConverter  # 查看BaseConverter类的定义便可以发现端倪

app = Flask(__name__)


class ListConverter(BaseConverter):
    def to_python(self, value):
        # to_python 方法转换传递的参数, 并把返回值交给 视图函数
        return value.split('+')


app.url_map.converters['list'] = ListConverter


@app.route('/posts/<list:boards>')
def posts(boards):
    """
    传入类 a+b 的参数, 自动分割成 a,b  -> 访问a,b板块下的posts
    如: http://127.0.0.1:5000/posts/a+b
    得到: 你提交的板块是: ['a', 'b']
    """
    return '你提交的板块是: {}'.format(boards)


if __name__ == '__main__':
    app.run()
```

### `to_url`的作用：
这个方法的返回值，将会在调用url_for函数的时候生成符合要求的URL形式。

```python
from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        # 返回值当做 url_for 的结果
        return '+'.join(value)


app.url_map.converters['list'] = ListConverter


@app.route('/')
def hello_world():
    # 访问主页, 返回 list元素拼接后的字符串
    return url_for('posts', boards=['a', 'b'])


@app.route('/posts/<list:boards>')
def posts(boards):
    return '你提交的板块是: {}'.format(boards)


if __name__ == '__main__':
    app.run()

```

## 必会的小细节知识点

### 让其它局域网电脑能访问我们的网站

如果想在同一个局域网下的其他电脑访问自己电脑上的Flask网站，
那么可以设置`host='0.0.0.0'`才能访问得到。

### 指定端口号

Flask项目，默认使用`5000`端口。如果想更换端口，那么可以设置`port=9000`。

### url唯一

在定义url的时候，一定要记得在最后加一个斜杠。
1. 如果不加`/`，用户访问这个url是自己添加了`/`，那么就访问不到。这样用户体验不太好。如果url后面带`/`,无论用户自己是否添加了`/`,都可以正常访问(其实不加`/`的url会重定向到有`/`的url).
2. 搜索引擎会将不加斜杠的和加斜杠的视为两个不同的url。而其实加和不加斜杠的都是同一个url，那么就会给搜索引擎造成一个误解。加了斜杠，就不会出现没有斜杠的情况。

### `GET`和`POST`请求

在网络请求中有许多请求方式，比如：GET、POST、DELETE、PUT请求等。那么最常用的就是`GET`和`POST`请求了。
1. `GET`请求：目的是从服务器上获取资源,不会更改服务器的状态。。
2. `POST`请求：目的是向服务器提交一些数据或者文件,一般POST请求是会对服务器的状态产生影响。
3. 关于参数传递：
    - `GET`请求：把参数放到`url`中，通过`?xx=xxx`的形式传递的。因为会把参数放到url中，所以如果视力好，一眼就能看到你传递给服务器的参数。这样不太安全。
    - `POST`请求：把参数放到`Form Data`中。会把参数放到`Form Data`中，避免了被偷瞄的风险，但是如果别人想要偷看你的密码，那么其实可以通过抓包的形式。因为POST请求可以提交一些数据给服务器，比如可以发送文件，那么这就增加了很大的风险。所以POST请求，对于那些有经验的黑客来讲，其实是更不安全的。
4. 浏览器默认发送的是`GET`请求,`POST`请求需要使用`form表单`或者`curl`等调试工具, 如: `curl -d "name=yaro" http://localhost:5000/`;
5. 在`Flask`中，`route`方法，默认将只能使用`GET`的方式请求这个url，如果想要设置自己的请求方式，那么应该传递一个`methods`参数。

    ```python
    @app.route('/', methods=['GET', 'POST'])
    def hello_world():
        return 'Hello World!'

    @app.route('/login')
    def login():
        if request.method == 'GET':
            return render_template('login.html')
            # 提前创建 templates>login.html 文件
            # login.html 里面使用form变淡提交post请求
        else:
            return 'success!'
    ```

## 重定向：

### 重定向概述

重定向分为永久性重定向和暂时性重定向，在页面上体现的操作就是浏览器会从一个页面自动跳转到另外一个页面。比如用户访问了一个需要权限的页面，但是该用户当前并没有登录，因此我们应该给他重定向到登录页面。

- 永久性重定向：`http`的状态码是`301`，多用于旧网址被废弃了要转到一个新的网址确保用户的访问，最经典的就是京东网站，你输入`www.jingdong.com`的时候，会被重定向到`www.jd.com`，因为`jingdong.com`这个网址已经被废弃了，被改成`jd.com`，所以这种情况下应该用永久重定向。

- 暂时性重定向：`http`的状态码是`302`，表示页面的暂时性跳转。比如访问一个需要权限的网址，如果当前用户没有登录，应该重定向到登录页面，这种情况下，应该用暂时性重定向。

### flask中的重定向：
`flask`中有一个函数叫做`redirect`，可以重定向到指定的页面。

语法: `def redirect(location, code=302, Response=None):`,默认为`302`(临时重定向). 

示例代码如下：

```pythonthon
# 访问 /profile/ ,如果后面的 查询字符串 不含有 name字段, 则重定向到 /login/ 
from flask import Flask,request,redirect,url_for

app = Flask(__name__)

@app.route('/login/')
def login():
    return '这是登录页面'

@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '个人中心页面'
    else:
        # redirect 重定向
        return redirect(url_for('login'))
```

## 视图函数Response返回值详解

### 视图函数中可以返回哪些值：

1. 如果返回的是一个合法的相应(`werkzeug.wrappers.Response`)对象, 则直接返回;
2. 如果返回字符串：Flask会重新创建一个`werkzeug.wrappers.Response`对象,其中,将该字符串作为`主体`, 状态码为`200`, MIME类型为`text/html`, 然后返回该Response对象.相当于: 

    ```python
    from flask import Resonse
    # 本质是 werkzeug.wrappers.Response
    @app.route('/')
    def index():
        # return Response(response='index page', status=200, content_type='text/html;charset=utf-8')
        return 'index page' # 本质是上一行代码
    ```

3. 可以返回元组：元组的形式是: `(response, status_code, headers)`，status_code 会覆盖默认的200状态码, headers可以是一个列表或词典,作为额外的响应头; 也不一定三个都要写，写两个也是可以的。返回的元组，其实在底层也是包装成了一个`Response`对象。

    ```python
    from flask import Resonse

    @app.route('/')
    def index():
        return 'index', 200, {X-NAME: 'yaro'}
        # 返回一个元素, 最后一项为响应头信息
    ```

> The return type must be a string, tuple, Response instance, or WSGI callable.

4. 如果以上三个条件都不满足, Flask会架设返回值是一个合法的 `WSGI` 应用, 并通过`Response.force_type(rv, request.environ)`强制转换为一个请求对象; **如果转换失败(如: 返回一个`dict`/`list`),会报错. 此时, 我们可以通过自定义的`Response`对象手动转换/包装.**


### 实现一个自定义的`Response`对象：

> 参考: [Flask设置返回json格式数据](https://www.polarxiong.com/archives/Flask%E8%AE%BE%E7%BD%AE%E8%BF%94%E5%9B%9Ejson%E6%A0%BC%E5%BC%8F.html)

1. 必须继承自`Response`类。
2. 实现方法`force_type(cls,rv,environ=None)`。
3. 必须指定`app.response_class`为你自定义的`X_Response`对象。
4. 如果视图函数返回的数据，不是字符串，也不是元组，也不是Response对象，那么就会将返回值传给`force_type`，然后再将`force_type`的返回值返回给前端。

> 即, 自定义的`Response`对象继承`Response`对象, 重写了`Response.force_type()`方法, **该方法只有在返回值不是`Response`对象/不是字符串/不是Tuple时才会调用**.

```python
# 将视图函数中返回的字典,转换为JSON对象(restful-api都是通过JSON传递数据),然后返回

from flask import Flask, Response, jsonify

app = Flask(__name__)


class JSONResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        # if type(response == dict):
        if isinstance(response, dict):  # 貌似不能使用 type 判断
            response = jsonify(response)
            # jsonify 在python自带的json.dumps()的基础上, 还把JSON字符串包装成了 Response对象
        return super(JSONResponse, cls).force_type(response, environ)  # 这里的返回值只能是Response对象


app.response_class = JSONResponse


@app.route('/list1/')
def list1():
    res = Response('list1')  # 有时Response对象比字符串更方便
    res.set_cookie('country', 'china')
    return res


@app.route('/list2/')
def list2():
    return {'username': 'yaro', 'age': 18}


if __name__ == '__main__':
    app.run()
```

# 04 flask入门（模板）

## 初识jinjia模板

在之前的章节中，视图函数直接返回文本，而在实际生产环境中其实很少这样用，因为实际的页面大多是带有样式和复杂逻辑的HTML代码.

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    # 会到 templates 文件夹下找 index.html


@app.route('/list/')
def my_list():
    return render_template('posts/list.html')


if __name__ == '__main__':
    app.run()
```

> 可以在实例化Flask对象是,指定默认的 templates文件夹: `app = Flask(__name__, template_folder=r'templ')`

## jinjia模板语法概述

Jinja模板是简单的一个纯文本文件（html\/xml\/csv...），不仅仅是用来产生html文件，后缀名也依照你自己的心情而定。当然，尽量命名为模板正确的文件格式，增加可读性。

- `{{ ... }}`：用来装载一个变量，模板渲染的时候，会把这个变量代表的值替换掉。并且可以间接访问一个变量的属性或者一个字典的key。关于点.号访问和[]中括号访问，没有任何区别，都可以访问属性和字典的值。
- `{% ... %}`：用来装载一个控制语句，以上装载的是for循环，以后只要是要用到控制语句的，就用{% ... %}。
- `{# ... #}`：用来装载一个注释，模板渲染的时候会忽视这中间的值。

## jinjia传参/变量 `{{ 变量 }}`

- 在使用`render_template`渲染模版的时候，可以传递关键字参数。以后直接在模版中使用就可以了。

- 如果你的参数过多，那么可以将所有的参数放到一个字典中，然后在传这个字典参数的时候，使用两个星号，将字典打散成关键参数。

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return render_template('index.html', name='yaro', age=18)  # 方法1: 变量太多不方便
    context = {
        'name': 'yaro',
        'age': 18
    }
    # return render_template('index.html', context=context)  # 方法2: html文件使用变量需要context.name
    return render_template('index.html', **context)  # 方法3(推荐): html文件使用变量,直接用 name


if __name__ == '__main__':
    app.run()
```

## 模板中使用`url_for`: {{ url_for() }}

模版中的`url_for`跟我们后台视图函数中的`url_for`使用起来基本是一模一样的。也是传递视图函数的名字，也可以传递参数。

使用的时候，需要在`url_for`左右两边加上一个`{{ url_for('login') }}`

> Flask中 `{{ 变量 }}`用来向html模板文件传递变量, `{% 函数/逻辑 %}` 用来向html模板文件传递函数/逻辑; `url_for` 使用  `{{ url_for() }}`

```python
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
```

```html
{#index.html#}
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>知了课堂</title>
</head>
<body>
<h1>这是从模板渲染的内容</h1>
{#<h2><a href="/login/">login页面</a></h2>#}
<h2><a href="{{ url_for('login') }">login页面</a></h2>
</body>
</html>
```

## 过滤器的基本使用

### 什么是过滤器，语法是什么：

1. 有时候我们想要在模版中对一些变量进行处理，那么就必须需要类似于Python中的函数一样，可以将这个值传到函数中，然后做一些操作。在模版中，过滤器相当于是一个函数，把当前的变量传入到过滤器中，然后过滤器根据自己的功能，再返回相应的值，之后再将结果渲染到页面中。
2. 基本语法：`{{ variable|过滤器名字 }}`。使用管道符号`|`进行组合。

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'position': -100,
        'signature': '我就是我,不一样的烟火...'
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run()
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<h1>位置的绝对值为: {{ position | abs }}</h1>
<p>个性签名为: {{ signature | default('此人很赖,没有签名') }}</p>
</body>
</html>
```

### 常用内置过滤器：

- `default`过滤器：

    > 如: 个性签名 - 如果你自己没有编写,会显示`此人很懒, 没有个性签名`

    - 使用方式: `{{ value|default('默认值') }}`。
    - 如果value这个`key`**不存在**，那么就会使用`default`过滤器提供的默认值。
    - 如果value存在,但是使用了类似于：None、空字符串、空列表、空字典等，那么就必须要传递另外一个参数`{{ value|default('默认值',boolean=True) }}`。
    - 可以使用`or`来替代`default('默认值',boolean=True)`。例如：`{{ signature or '此人很懒，没有留下任何说明' }}`。

- 自动转义过滤器：
    1. `escape(value)`或e：转义字符，会将<、>等符号转义成HTML中的符号(**而不是解析成代码**)。示例：content|escape或content|e。可以用禁止变量中含有`<script>alert('hello')</script>`脚本的执行.
    2. `safe(value)`：如果开启了全局转义，那么safe过滤器会将变量关掉转义(前面的字符串是安全的,不需要转义)。示例：content_html|safe。
    3. `autoescape`标签，可以对他里面的代码块关闭或开启自动转义。
        ```jinja
        {% autoescape off/on %}
            ...代码块
        {% endautoescape %}
        ```

- 其他[常用内置过滤器](http://jinja.pocoo.org/docs/dev/templates/#builtin-filters)

    - first(value)：返回一个序列(如:`list`)的第一个元素。names|first。
    - last(value)：返回一个序列的最后一个元素。示例：names|last。
    - format(value,*arags,**kwargs)：格式化字符串。例如以下代码：

        ```
        {{ "%s" - "%s"|format('Hello?',"Foo!") }}
        # 将输出：`Helloo? - Foo!`
        ```

    - length(value)：返回一个序列或者字典的长度。示例：names|length。
    - join(value,d=u'')：将一个序列用d这个参数的值拼接成字符串。
    - int(value)：将值转换为int类型。
    - float(value)：将值转换为float类型。
    - lower(value)：将字符串转换为小写。
    - upper(value)：将字符串转换为小写。
    - replace(value,old,new)： 替换将old替换为new的字符串。
    - truncate(value,length=255,killwords=False)：截取length长度的字符串(**后面三个字符为`...`**)。
    - striptags(value)：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格。
    - trim：截取字符串前面和后面的空白字符。
    - string(value)：将变量转换成字符串。
    - wordcount(s)：计算一个长字符串中单词的个数。
    - reverse: 翻转遍历可遍历对象

### 自定义过滤器

> 当内置过滤器的功能不能满足需求时, 需要自定义过滤器.

- 过滤器本质上就是一个函数。如果在模版中调用这个过滤器，那么就会将这个变量的值作为第一个参数传给过滤器这个函数，然后函数的返回值会作为这个过滤器的返回值。需要使用到一个装饰器将该过滤器注册到jinjia模板：`@app.template_filter('cut')`(里面的`cut`为过滤器的名称)

    ```python
    @app.template_filter('cut')
    def cut(value):
        value = value.replace("hello",'')
        return value
    ```

    ```html
    <p>{{ article|cut }}</p>
    ```

- 案例: 时间处理过滤器(给一个文章的 `发表日期`, 处理成 `xx 小时/天前`)

    ```python
    from flask import Flask, render_template
    from datetime import datetime

    app = Flask(__name__)

    @app.route('/')
    def index():
        context = {
            'create_time': datetime(2019, 2, 15, 19, 0, 0)
        }
        return render_template('index.html', **context)

    @app.template_filter('handle_time')
    def handle_time(time):
        """
        1. 如果1min之内 - 刚刚
        2. 如果1h之内 - xx分钟前
        3. 如果24h之内 - xx小时前
        4. 如果30d以内 - xx天之前
        5. 如果大于30d - 具体时间: 2019/02/21 16:32
        """
        if isinstance(time, datetime):
            now = datetime.now()
            delt_time = (now - time).total_seconds()
            if delt_time < 60:
                return '刚刚'
            elif delt_time < 60 * 60:
                return '{}分钟之前'.format(int(delt_time / 60))
            elif delt_time < 60 * 60 * 24:
                return '{}小时之前'.format(int(delt_time / 60 / 60))
            elif delt_time < 60 * 60 * 24 * 30:
                return '{}天之前'.format(int(delt_time / 60 / 60 / 24))
            else:
                return time.strftime('%Y/%m/%d %H:%M')
        else:
            return time

    if __name__ == '__main__':
        app.run()
    ```

    ```html
    {#index.html#}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>发表时间: {{ create_time | handle_time }}</h1>
    </body>
    </html>
    ```
## 转义

转义的概念: 在模板渲染字符串的时候，字符串有可能包括一些非常危险的字符比如`<`、`>`等，这些字符会破坏掉原来HTML标签的结构，更严重的可能会发生XSS跨域脚本攻击，因此应该转义成HTML能正确表示这些字符的写法，比如`>`在HTML中应该用`&lt;`来表示等。

- Flask默认没有开启全局自动转义; 原因：
    - 渲染到模板中的字符串并不是所有都是危险的，大部分还是没有问题的，如果开启自动转义，那么将会带来大量的不必要的开销。
    - Jinja2很难知道原字符串是否已经被转义过了，因此如果开启自动转义，将对一些已经被转义过的字符串发生二次转义，在渲染后会破坏原来的字符串。

- Flask针对那些以`.html、.htm、.xml和.xhtml`结尾的文件，如果采用`render_template`函数进行渲染的，则会开启自动转义。并且当用`render_template_string`函数的时候，会将所有的字符串进行转义后再渲染。

- 在没有开启自动转义的模式下（比如以.conf结尾的文件），对于一些不信任的字符串，可以通过`{{ content_html|e }}`或者是`{{ content_html|escape }}`的方式进行转义。
- 在开启了自动转义的模式下，如果想关闭自动转义，可以通过`{{ content_html|safe }}`的方式关闭自动转义。而`{%autoescape true/false%}...{%endautoescape%}`可以将一段代码块放在中间，来关闭或开启自动转义，例如以下代码关闭了自动转义：

    ```html
    {% autoescape false %}
        <p>autoescaping is disabled here
        <p>{{ will_not_be_escaped }}
    {% endautoescape %}
    ```

## 数据类型：

Jinja支持许多数据类型，包括：`字符串、整型、浮点型、列表、元组、字典、true/false`。注意其中的布尔类型是true/false，都是小写，不是Python中的True/False。

## 运算符：

- `+`号运算符：可以完成数字相加，字符串相加，列表相加。但是并不推荐使用`+`运算符来操作字符串，字符串相加应该使用`~`运算符。
- `-`号运算符：只能针对两个数字相减。
- `/`号运算符：对两个数进行相除。
- `%`号运算符：取余运算。
- `*`号运算符：乘号运算符，并且可以对字符进行相乘。
- `**`号运算符：次幂运算符，比如`2**3=8`。
- `in`操作符：跟python中的`in`一样使用，比如`{{1 in [1,2,3]}}`返回true。
- `~`号运算符：拼接多个字符串，比如`{{"Hello" ~ "World"}}`将返回HelloWorld。

## if语句详解

```html
{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny!  You bastard!!!
{% else %}
    Kenny looks okay --- so far
{% endif %}
```

## for循环详解

与python类似, jinjia中的`for...in`循环可以遍历任何一个序列包括数组、字典、元组。但是没有`continue`和`break`语句(可以用loop.xx等变量控制循环的状态),并且可以进行反向遍历.

- 普通的遍历：

    ```html
    <ul>
    {% for user in users %}
        <li>{{ user.username|e }}</li>
    {% endfor %}
    </ul>
    ```

- 遍历字典

    ```html
    <dl>
    {% for key, value in my_dict.items() %}
        <dt>{{ key|e }}</dt>
        <dd>{{ value|e }}</dd>
    {% endfor %}
    </dl>
    ```

    > 同python3 只能变量字典的 `items()`, `keys()`, `values()` 这三个可遍历对象.

- 如果序列中没有值的时候,进入`else`语句

    ```html
    <ul>
        {% for user in users %}
            <li>{{ user }}</li>
        {% else %}
            <p>users列表没有任何元素...</p>
        {% endfor %}
    </ul>
    ```

- 通过反向遍历可以通过`reverse`过滤器实现

    ```html
    # users = {'person1', 'person2'}
    <ul>
        {% for user in users | reverse %}
            <li>{{ user }}</li>
        {% else %}
            <p>列表没有任何元素...</p>
        {% endfor %}
    </ul>
    ```

    > 注意reverse过滤器的位置,如果给user加,会变成把user翻转(1nosrep)

- jinjia的for循环不能使用`continue`和`break`控制,所以有如下变量获取循环的状态:

```
变量	描述
loop.index	当前迭代的索引（从1开始）
loop.index0	当前迭代的索引（从0开始）
loop.first	是否是第一次迭代，返回True\/False
loop.last	是否是最后一次迭代，返回True\/False
loop.length	序列的长度
```

- 也可以在for循环中使用if语句控制循环

```html
<table border="1" cellspacing="0" style="border-collapse: collapse">
    <tbody>
        {% for x in range(1, 10) %}
            <tr>
                {# {% for y in range(1, x + 1) %} #}
                {% for y in range(1, 56) if y < x %}
                    <td>{{ y }} * {{ x }} = {{ x * y }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </tbody>
</table>
```

## 测试器

测试器主要用来判断一个值是否满足某种类型，并且这种类型一般通过普通的`if`判断是有很大的挑战的。语法是：`if...is...`，先来简单的看个例子：

```html
{% if variable is escaped %}
    value of variable: {{ escaped }}
{% else %}
    variable is not escaped
{% endif %}
```

以上判断variable这个变量是否已经被转义了，Jinja中内置了许多的测试器，看以下列表：

- callable(object)：是否可调用。
- defined(object)：是否已经被定义了。
- escaped(object)：是否已经被转义了。
- upper(object)：是否全是大写。
- lower(object)：是否全是小写。
- string(object)：是否是一个字符串。
- sequence(object)：是否是一个序列。
- number(object)：是否是一个数字。
- odd(object)：是否是奇数。
- even(object)：是否是偶数。

## 宏(macro)->重复代码段

模板中的宏跟python中的函数类似，可以传递参数，但是不能有返回值，可以将一些经常用到的代码片段放到宏中，然后把一些不固定的值抽取出来当成一个变量。

> Macro: A single instruction that expands automatically into a set of instructions to perform a particular task.

### 宏的基本使用

使用宏的时候，参数可以为默认值。相关示例代码如下：

```html
{#创建macro#}
{% macro input(name="", value="", type="text") %}
    <label>
        <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
    </label>
{% endmacro %}

{#调用macro#}
<h1>登录xxx</h1>
用户名:
{{ input("username") }}
<br>
密码:
{{ input("password", type="password") }}
<br>
{{ input(value="提交", type="submit") }}
```

以上例子可以抽取出了一个input标签，指定了一些默认参数。那么我们以后创建input标签的时候，可以通过他快速的创建：

### 宏的导入()import语句)

上节macro的基本使用中,macro的`创建`与`调用`在同一个文件;

实际开发中,我们往往把所有的`macro创建`放在同一个文件`macros.html`(与模板文件分离)中,在其他文件中通过`import`语句`导入`并`调用`.

- 简单使用: 从"macros.html"文件中引入`input`宏, `as`可以改名

    ```html
    {% from "macros.html" import input %}
    {% from "macros.html" import input as xxx %}
    ```

- 也可以把整个"macros.html"文件引入,但是必须使用`as`,使用方式:`xxx.input`

    ```html
    {% import "macros.html" as xxx %}
    ```

- `macros.html`文件中不需要html框架(直接写macros即可)
- `import` 语句中引入`macros.html`的路径是根据`templates文件夹`确定的,而不是`index.html`

- `app.py`文件只是与`index.html`文件关联(`render_template("index.html")`), 如果想在`macros.html`中使用`app.py`文件中的变量,需要`with context`

    ```html
    {% import "macros.html" as macros with context %}
    ```

## include -> 组件化开发

- 使用场景: 网页分为header/content/footer, 分别独立为header.html/content.html/footer.html, 只需要在index.html中需要其他组件的地方 `{% include "header.html" %}` 即可;
- 子组件html文件中可以带有html框架,也可以不带;
- 路径跟`import`一样，直接以`templates` 为根目录下去找.
- 父组件只要`include`子组件后, 子组件可以直接使用`app.py`的变量, 不需要使用`with context`。

```html
<body>
    {% include "header.html" %}
    <div>内容</div>
    {% include "footer.html" %}
</body>
```

## set、with -> jinjia模板的变量

上文中的我们可以在`app.py`文件中定义变量(`context`),进而通过`render_template("index.html")`在主组件(`index.html`)中使用, 可以通过`{% include "header.html" %}`语句在子组件中使用.

除此之外,我们可以在`index.html`中通过`set语句`创建变量,在index.html及子组件中使用.

- set语句：

    ```html
    {% set username='知了课堂' %}
    <p>用户名：{{ username }}</p>
    ```

    - `set`语句应该在最上面声明, 这样**后面的内容**才可以使用该变量;
    - 父组件声明的变量,子组件可以使用; 反之,则不行

- `with`语句块：
    `set`语句后面所有的内容可以访问该变量,如果想要缩写使用范围,需要`with`语句(类似python中的创建上下文)

    `with`语句定义的变量，只能在`with`语句块中使用，超过了这个代码块，就不能再使用了。
    
    - 使用方法1:

        ```html
        {% with classroom = 'zhiliao1班' %}
        <p>班级：{{ classroom }}</p>
        {% endwith %}
        ```

        > `include "header.html"`只要在`with`语句块中,子组件便可访问该变量;否则,不可以.

    - 使用方法2:
        `with`语句也不一定要跟一个变量，可以定义一个空的`with`语句，以后在`with`块中通过`set`定义的变量，就只能在这个`with`块中使用了：

        ```html
        {% with %}
            {% set classroom = 'zhiliao1班' %}
            <p>班级：{{ classroom }}</p>
        {% endwith %}
        ```

## 加载静态文件的路径写法

静态文件: css, js, 字体, 图片 ...

falsk中所有的静态文件放在static文件夹中,jinjia模板中加载静态文件使用的是`url_for`函数。

第一个参数需要为`static`，第二个参数需要为一个关键字参数`filename='路径'`。示例：

```html
{{ url_for("static",filename='xxx/yyy.zzz') }}
```

## 模板的继承

前面使用`include语句`实现了代码的重用,但是如果有两个页面/父组件(`index.html`, `detail.html`)都使用了`header.html`和`footer.html`子组件, 就需要在两个页面中同时`include`. 这就会造成两个父组件的内容还是有很多重复的.

为了进一步实现代码的复用,jinjia提供了模板的继承: 从`index.html` `detail.html`两个父组件中提取公共的部分为`base.html`(使用`block`语句提供接口), 然后在子模板中的继承即可(`{% extends 'base.html' %}`) 

### 语法：

- 父模板(base.html 公共部分)

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>COCO</title>
    </head>
    <body>
        {% block block_name %}
        {% endblock %}
    </body>
    </html>
    ```

- 子模板(`index.html` `detail.html`)

    ```html
    {% extends "base.html" %}

    {% block block_name %}
        <h1>我是index页面</h1>
    {% endblock %}

    ```

### 子模板继承父模版代码block中的代码

默认情况下，子模板block中的代码就会覆盖掉父模板中的代码(可以有自己的代码)。可以使用`{{ super() }}`保留父模板block中的代码：

- 父模板：

    ```html
    {% block block_name %}
        <p>父模板</p>
    {% endblock %}
    ```
- 子模板：

    ```html
    {% extends "base.html" %}

    {% block block_name %}
        {{ super() }}
        <h1>子模板</h1>
    {% endblock %}
    ```

### 调用同一个模板中其他block的代码：

如果想要在另外一个模版中使用其他模版中的代码。使用`{{ self.其他block名字() }}`：

```html
{% extends "base.html" %}

{% block title %}
    主页
{% endblock %}

{% block body_block %}
    {{ self.title() }}
    <h1>子模板</h1>
{% endblock %}
```

### 其他注意事项：
``
- **切记!!** 子模板中，所有的代码必须放在`block`中。如果放到其他地方，不会被jinjia渲染。
- `extends`语句必须在子模板的第一行。

# flask入门（视图高级）

## `app.route`装饰器与`add_url_rule方法`：

- `app.route(rule,**options)`装饰器底层，其实也是使用`add_url_rule(rule,endpoint=None,view_func=None)`来实现url与视图函数映射的。

- `add_url_rule`这个方法用来添加url与视图函数的映射。如果没有填写`endpoint`，那么默认会使用`view_func`的名字作为`endpoint`。

- 以后在使用`url_for`的时候，就要看在映射的时候有没有传递`endpoint`参数，如果传递了，那么就应该使用`endpoint`指定的字符串，如果没有传递，那么就应该使用`view_func`的名字。

## 类视图

之前我们接触的视图都是函数，所以一般简称视图函数。其实视图也可以基于类来实现，类视图的好处是支持继承，但是类视图不能跟函数视图一样，写完类视图还需要通过app.add_url_rule(url_rule,view_func)来进行注册。以下将对两种类视图进行讲解：

### 标准类视图：

```python
from flask import Flask, views

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


class ListView(views.View):
    def dispatch_request(self):
        # dispatch  分发, 派遣
        return 'List View'


app.add_url_rule('/list/', endpoint='my_list', view_func=ListView.as_view('list'))
# 第一个参数:url路径; 第二个参数: 起个名字; 第三个参数: 利用ListView类的as_view方法把ListView中的dispatch_request方法变成视图函数,并把名称修改为'list'

if __name__ == '__main__':
    app.run()
```

1. 标准类视图，必须继承自`flask.views.View`.
2. 必须实现`dipatch_request`方法，以后请求过来后，都会执行这个方法。这个方法的返回值就相当于是之前的函数视图一样。也必须返回`Response`或者子类的对象，或者是字符串，或者是元组。
3. 由于是类,没有装饰器; 必须通过`app.add_url_rule(rule,endpoint,view_func)
`来做url与视图的映射。`view_func`这个参数，需要使用类视图下的`as_view`类方法类转换：`ListView.as_view('list')`。
4. 如果指定了`endpoint`，那么在使用`url_for`反转的时候就必须使用`endpoint`指定的那个值。如果没有指定`endpoint`，那么就可以使用`as_view(视图名字)`中指定的视图名字来作为反转。
5. 类视图有以下好处：可以继承，把一些共性的东西抽取出来放到父视图中，子视图直接拿来用就可以了。但是也不是说所有的视图都要使用类视图，这个要根据情况而定。

    ```python
    # 多个url都需要返回json数据
    class JSONView(views.View):
        def get_data(self):
            raise NotImplemented  # 私有方法,不允许外部调用
    
        def dispatch_request(self):
            return jsonify(self.get_data())
        # 以后的类视图继承JSONView,且实现get_data()方法即可实现自动jsonify化
    
    
    class ListView(JSONView):
        def get_data(self):
            return {'username': 'yaro', 'password': 'xxx'}
    ```



### 基于请求方法的类视图：
1. 基于方法的类视图，是根据请求的`method`来执行不同的方法的。如果用户是发送的`get`请求，那么将会执行这个类的`get`方法。如果用户发送的是`post`请求，那么将会执行这个类的`post`方法。其他的method类似，比如`delete`、`put`。
2. 这种方式，可以让代码更加简洁。所有和`get`请求相关的代码都放在`get`方法中，所有和`post`请求相关的代码都放在`post`方法中。就不需要跟之前的函数一样，通过`request.method == 'GET'`。

### 类视图中的装饰器：
1. 如果使用的是函数视图，那么自己定义的装饰器必须放在`app.route`下面。否则这个装饰器就起不到任何作用。
2. 类视图的装饰器，需要重写类视图的一个类属性`decorators`，这个类属性是一个列表或者元组都可以，里面装的就是所有的装饰器。

## 蓝图：

1. 蓝图的作用就是让我们的Flask项目更加模块化，结构更加清晰。可以将相同模块的视图函数放在同一个蓝图下，同一个文件中，方便管理。
2. 基本语法：
    * 在蓝图文件中导入Blueprint：
        ```python
        from flask import Blueprint
        user_bp = Blueprint('user',__name__)
        ```。
    * 在主app文件中注册蓝图：
        ```python
        from blueprints.user import user_bp
        app.regist_blueprint(user_bp)
        ```
3. 如果想要某个蓝图下的所有url都有一个url前缀，那么可以在定义蓝图的时候，指定url_prefix参数：
    ```python
    user_bp = Blueprint('user',__name__,url_prefix='/user/')
    ```
    在定义url_prefix的时候，要注意后面的斜杠，如果给了，那么以后在定义url与视图函数的时候，就不要再在url前面加斜杠了。

4. 蓝图模版文件的查找：
    * 如果项目中的templates文件夹中有相应的模版文件，就直接使用了。
    * 如果项目中的templates文件夹中没有相应的模版文件，那么就到在定义蓝图的时候指定的路径中寻找。并且蓝图中指定的路径可以为相对路径，相对的是当前这个蓝图文件所在的目录。比如：
        ```python
        news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='zhiliao')
        ```
        因为这个蓝图文件是在blueprints/news.py，那么就会到blueprints这个文件夹下的zhiliao文件夹中寻找模版文件。

5. 蓝图中静态文件的查找规则：
    * 在模版文件中，加载静态文件，如果使用url_for('static')，那么就只会在app指定的静态文件夹目录下查找静态文件。
    * 如果在加载静态文件的时候，指定的蓝图的名字，比如`news.static`，那么就会到这个蓝图指定的static_folder下查找静态文件。

6. url_for反转蓝图中的视图函数为url：
    * 如果使用蓝图，那么以后想要反转蓝图中的视图函数为url，那么就应该在使用url_for的时候指定这个蓝图。比如`news.news_list`。否则就找不到这个endpoint。在模版中的url_for同样也是要满足这个条件，就是指定蓝图的名字。
    * 即使在同一个蓝图中反转视图函数，也要指定蓝图的名字。

### 蓝图实现子域名：
1. 使用蓝图技术。
2. 在创建蓝图对象的时候，需要传递一个`subdomain`参数，来指定这个子域名的前缀。例如：`cms_bp = Blueprint('cms',__name__,subdomain='cms')`。
3. 需要在主app文件中，需要配置app.config的SERVER_NAME参数。例如：
    ```python
    app.config['SERVER_NAME'] = 'jd.com:5000'
    ```
    * ip地址不能有子域名。
    * localhost也不能有子域名。
4. 在`C:\Windows\System32\drivers\etc`下，找到hosts文件，然后添加域名与本机的映射。例如：
    ```python
    127.0.0.1   jd.com
    127.0.0.1   cms.jd.com
    ```
    域名和子域名都需要做映射。

