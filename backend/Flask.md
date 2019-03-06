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

# 03 flask入门（URL）

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

```python
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
    ```python
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

```python
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

总结:
- 静态文件归于static/文件夹。
- 将第三方库跟你自己的静态文件隔离开来。
- 在你的模板里指定你的favicon的路径。
- 使用Flask-Assets来在模板插入你的静态文件。
- Flask-Assets可以编译，合并以及压缩你的静态文件。
- [更多](https://wizardforcel.gitbooks.io/explore-flask/content/9-static_files.html)

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

# 05 flask入门（视图高级）

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

使用场景举例: 

- 多个类视图都需要实现相同的功能(如:返回JSON数据的功能)
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

- 多个类视图都需要的变量(如: 多个页面都需要广告)
    ```python
    class ADSView(views.View):
        def __init__(self):
            super(ADSView, self).__init__()
            self.context = {
                'ads': '今年过节不收礼'
            }

    class LoginView(ADSView):
        def dispatch_request(self):
            self.context.update({
                'username': 'zhiliao'
            })
            return render_template('login.html',**self.context)

    class RegistView(ADSView):
        def dispatch_request(self):
            return render_template('regist.html',**self.context)

    app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
    app.add_url_rule('/regist/',view_func=RegistView.as_view('regist'))
    ```

### 基于请求方法的类视图：

如果使用之前的`视图函数`实现根据不同`GET/POST`请求方式映射不同的处理逻辑,需要如下:

```python
@app.route('/')
def index():
    if request.method == 'GET':
        return '请求方法是get'
    else:
        # 写一些post请求的代码
```

其实,Flask还为我们提供了另外一种类视图`flask.views.MethodView`，对每个HTTP方法执行不同的函数（映射到对应方法的**小写的同名方法**上），这对`RESTful API`尤其有用，以下将用一个例子来进行讲解：

1. 基于方法的类视图，是根据请求的`method`来执行不同的方法的。如果用户是发送的`get`请求，那么将会执行这个类的`get`方法。如果用户发送的是`post`请求，那么将会执行这个类的`post`方法。其他的method类似，比如`delete`、`put`。
2. 通过类视图的这种方式，可以让代码更加简洁。所有和`get`请求相关的代码都放在`get`方法中，所有和`post`请求相关的代码都放在`post`方法中。就不需要像之前的函数视图一样，通过`request.method == 'GET'`判断。

```python
## app.py
from flask import Flask, views, render_template, request

app = Flask(__name__)


class LoginView(views.MethodView):
    def __render(self, error=None):  # 定义私有方法
        return render_template('login.html', error=error)

    def get(self):  # 定义get请求返回的内容
        return self.__render()

    def post(self):  # 定义post请求返回的内容
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'yaro' and password == '123':
            return '登录 success'
        else:
            return self.__render(error='用户名或密码错误')


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    app.run()

# 如此, 可以实现:
# get方式访问 login 页面 -> 登录页面
# post方式访问 login 页面 -> 获得用户的登录帐号/密码, 并检验.
    
# curl命令也可也可实现调试:
# curl http://127.0.0.1:5000/login/
# curl -d "username=yaro&password=123" http://127.0.0.1:5000/login/
```

```html
<!-- login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="" method="post">
        <table>
            <tbody>
                <tr>
                    <td>用户名:</td>
                    <td><input type="text" name="username"></td>
                </tr>
                <tr>
                    <td>密码:</td>
                    <td><input type="password" name="password"></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="立即登录"></td>
                </tr>
            </tbody>
        </table>
        {% if error %}
            <p style="color: red;">{{ error }}</p>
        {% endif %}
    </form>
</body>
</html>
```

### 类视图中的装饰器：

1. 如果使用的是函数视图，那么自己`定义的装饰器`必须放在`app.route`下面。否则这个装饰器就起不到任何作用。
2. 类视图的装饰器，需要重写类视图的一个类属性`decorators`，这个类属性是一个列表或者元组都可以，里面装的就是所有的装饰器。

```python
from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)


def login_required(func):
    # 定义装饰器: 只要登录后才能settings
    @wraps(func)
    def wrapper(*args, **kwargs):
        # /settings/?username=xxx
        username = request.args.get('username')
        if username and username == 'yaro':
            return func(*args, **kwargs)
        else:
            return '请先登录'
    return wrapper  # 必须为"函数名"


@app.route('/settings/')
@login_required  # 函数视图装饰器
# 必须在 @app.route 之下, 否则无效; 即,必须先处理完逻辑,在分分配由.
def settings():
    return '这是设置界面'


class ProfileView(views.View):
    decorators = [login_required]  # 类视图装饰器

    def dispatch_request(self):
        return '这是个人中心页面'


app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))

if __name__ == '__main__':
    app.run()

```

## 蓝图：

1. 总结:
    - 一个蓝图包括了可以作为独立应用的视图，模板，静态文件和其他插件。
    - 蓝图是组织你的应用的好办法。
    - 在分区式架构下，每个蓝图对应你的应用的一个部分。
    - 在功能式架构下，每个蓝图就只是视图的集合。所有的模板和静态文件都放在一块。
    - 要使用蓝图，你需要定义它，并在应用中用Flask.register_blueprint()注册它。
    - 你可以给一个蓝图中的所有路由定义一个动态URL前缀。
    - 你也可以给蓝图中的所有路由定义一个动态子域名。
    - 仅需五步走，你可以用蓝图重构一个应用。
    - [更多](https://wizardforcel.gitbooks.io/explore-flask/content/7-blueprints.html)

    蓝图的作用就是让我们的Flask项目更加模块化，结构更加清晰。可以将相同模块(`user模块, news模块...`)的视图函数放在同一个蓝图下，同一个文件中，方便管理。

    ![项目模块化](https://i.loli.net/2019/02/23/5c70f3c4c0a55.png)

2. 基本使用：

    - 在蓝图文件(子模块)中导入Blueprint类,定义Blueprint实例(该实例`news_bp`的用法基本同Flask的实例`app`):

        ```python
        # news.py
        from flask import Blueprint  # 导入蓝图class
        news_bp = Blueprint('news', __name__)  # 新建蓝图实例(news 为蓝图的name)

        @news_bp.route('/list/')
        def news_list():
            return 'news list 页面'

        @news_bp.route('/detail/')
        def news_detail():
            return 'news detail 页面'
        ```

        ```python
        # user.py
        from flask import Blueprint

        user_bp = Blueprint('user', __name__)

        @user_bp.route('/profile/')
        def profile():
            return '个人中心页面'

        @user_bp.route('/settings/')
        def settings():
            return '个人设置页面'
        ```

    - 在主app文件中注册蓝图到Flask实例：
        ```python
        from flask import Flask
        from blue_print.news import news_bp  # 导入蓝图实例
        from blue_print.user import user_bp

        app = Flask(__name__)
        app.register_blueprint(news_bp)  # 注册蓝图实例到Flask实例(app)上
        app.register_blueprint(user_bp)

        if __name__ == '__main__':
            app.run()
        ```

    - 如此便可以访问如下url了
        ```
        http://127.0.0.1:5000/list/
        http://127.0.0.1:5000/detail/
        http://127.0.0.1:5000/profile/
        http://127.0.0.1:5000/settings/
        ```
3. 如果想要某个蓝图下的所有url都有一个url前缀，那么可以在定义蓝图的时候，指定url_prefix参数：
    
    ```python
    news_bp = Blueprint('user',__name__,url_prefix='/news')
    user_bp = Blueprint('user',__name__,url_prefix='/user')
    # http://127.0.0.1:5000/news/list/
    # http://127.0.0.1:5000/news/detail/
    # http://127.0.0.1:5000/user/profile/
    # http://127.0.0.1:5000/user/settings/
    ```
    
    > 注意`url_prefix='/news'`和视图url参数(`@user_bp.route('/detail/')`)的写法，最终url是二者的拼接。如果前者为`/news/`,后者为`/detail/`就可能出现两个`//`的情况(`http://127.0.0.1:5000/news//list/`)

4. 蓝图模版文件(`render_template`)的查找顺序：

    > 实际项目中,我们经常把模版文件全部放在`/template/`文件夹中,所以,以下内容多余!

    - 蓝图文件`/blue_print/news.py`也可以使用`render_template`指定模板文件;
    - 优先查找`/templates/`文件夹有无对应的模板文件, 再查找`实例化蓝图`时自定义`template`路径;自定义`template`路径的方式如下;

        ```python
        news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='zhiliao')
        # 此路径为相对路径: 相对于/blue_print/news.py -> /blue_print/template 文件夹
        ```

5. 蓝图相关静态文件的查找顺序：

    > 实际项目中,我们经常把模版文件全部放在`/static/`文件夹中,所以,以下内容多余!

    - 在模版文件`/template/index.html`中，加载静态文件，如果使用`{{ url_for('static') }}`，那么就只会在app指定的静态文件夹目录下(默认是`/static/`)查找静态文件。
    - 如果在加载静态文件的时候，指定的蓝图的名字，比如`{{ url_for('news.static') }}`，那么就会到这个蓝图指定的static_folder下查找静态文件。

6. url_for反转蓝图中的视图函数为url：
    - 如果使用蓝图，那么以后想要反转蓝图中的视图函数为url，那么就应该在使用url_for的时候指定这个蓝图。比如`news.news_list`。否则就找不到这个endpoint。有如下三种情况需要`url_for`:
        - 在主`/app.py`主文件中;
        - 在蓝图`/blue_print/news.py`中(即使是同一个蓝图文件中的视图函数);
        - 在模版文件`/template/index.html`中的`{{ url_for }}`同样也是要指定蓝图的名字。

## 使用蓝图实现子域名：

- 子域名介绍: 如:主域名为`jd.com`,子域名为`cms.jd.com`/`xxx.jd.com`/`www.jd.com`。
- 实现子域名的步骤:
    - 在创建蓝图实例的时候，需要传递一个`subdomain`参数，来指定这个子域名的前缀。例如：`cms_bp = Blueprint('cms', __name__, subdomain='cms')`。
    - 需要在主app.py文件中，需要配置`app.config[`SERVER_NAME`]参数:
        ```python
        # app.py 主文件
        from flask import Flask
        from blue_print.cms import cms_bp

        app = Flask(__name__)
        app.register_blueprint(cms_bp)

        app.config['SERVER_NAME'] = 'jd.com:5000'

        if __name__ == '__main__':
            app.run()
        ```

        ```python
        # cms.py 蓝图(文件)
        from flask import Blueprint

        cms_bp = Blueprint('cms', __name__, subdomain='cms')

        @cms_bp.route('/')
        def cmd_index():
            return 'cms index 页面'
        ```

    - 修改hosts文件:
        ```
        # 127.0.0.1   jd.com
        127.0.0.1   cms.jd.com
        ```
        > 主域名/子域名都需要单独做映射(只映射主域名对子域名无效)。

    - 访问 `cms.jd.com:5000`
        > hosts映射后,无法再通过ip访问(`127.0.0.1:5000`)

# 06 flask入门（SQLALchemy数据库）

总结:
- 使用SQLAchemy来搭配关系型数据库。
- 使用Flask-SQLAlchemy来包装SQLAlchemy。
- Alembic会在数据库模式改变时帮助你管理数据迁移。
- 你可以用NoSQL搭配Flask，但具体做法取决于具体引擎。
- 记得备份你的数据！

## 概述

数据库是一个网站的基础，在Flask中可以自由的使用MySQL、PostgreSQL、SQLite、Redis、MongoDB来写原生的语句实现功能，也可以使用更高级别的数据库抽象方式，如SQLAlchemy或MongoEngine这样的OR(D)M。本教程以MySQL+SQLAlchemy的组合来进行讲解。

- 环境安装: mariadb/mysql, 及相关库(`pip install pymysql sqlalchemy`)

> `lask-sqlalchemy库` 在 `sqlalchemy库` 的基础上，提供了一些常用的工具，并预设了一些默认值，帮助你更轻松地完成常见任务。用起来比直接用 sqlalchemy 方便、省事，不过有些高级一点的功能如果不了解 sqlalchemy 的话会用不好。建议最好先直接用 `sqlalchemy` 工作一小段时间，感受一下 `sqlalchemy` 到底是怎样运行起来的。等有了一定了解后，如果觉得有必要，再改用 `flask-sqlalchemy`，提高编程效率。

## 使用SQLAlchemy去连接数据库：

使用SQLALchemy去连接数据库，需要使用一些配置信息，然后将他们组合成满足条件的字符串(`DB_URI`)：

前提: 先创建`first_sqlalchemy`表(`CREATE DATABASE first_sqlalchemy charset utf8;`);

```python
from sqlalchemy import create_engine

# 配置数据库相关常量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'  # 需要先创建
USERNAME = 'root'
PASSWORD = ''
# 语法格式: dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)  # 创建数据库引擎
conn = engine.connect()  # 连接数据库(conn: 指挥操舵 -> 操作句柄/游标)
result = conn.execute('SELECT 1')  # 操作数据库
# result = conn.execute('show tables')
print(result.fetchone())
```
然后使用`create_engine`创建一个引擎`engine`，然后再调用这个引擎的`connect`方法，就可以得到这个对象，然后就可以通过这个对象对数据库进行操作了：
```python
engine = create_engine(DB_URI)

# 判断是否连接成功
conn = engine.connect()
result = conn.execute('select 1')
print(result.fetchone())
```

## 用SQLAlchemy执行原生SQL

```python
from sqlalchemy import create_engine
from constants import DB_URI  # DB_URI同上

#连接数据库
engine = create_engine(DB_URI,echo=True)

# 使用with语句连接数据库，如果发生异常会被捕获
with engine.connect() as con:
    # 先删除users表
    con.execute('drop table if exists users')
    # 创建一个users表，有自增长的id和name
    con.execute('create table users(id int primary key auto_increment,'
                'name varchar(25))')
    # 插入两条数据到表中
    con.execute('insert into users(name) values("xiaoming")')
    con.execute('insert into users(name) values("xiaotuo")')
    # 执行查询操作
    rs = con.execute('select * from users')
    # 从查找的结果中遍历
    for row in rs:
        print row
```

## 用SQLAlchemy通过ORM操作数据库

### ORM介绍：

- 背景问题: 项越大，原生SQL问题就出现了：重复利用率不高;会出现很多相近的SQL语句;很多SQL语句是在业务逻辑中拼出来的->不易修改;SQL注入等安全问题。
- ORM：Object Relationship Mapping 对象关系映射，对象模型(python)与数据库表的映射; 通过ORM我们可以通过类的方式去操作数据库，而不用再写原生的SQL语句
    - 类 -> 表(二维)
    - 类的属性 -> 表的字段(列) 
    - 类的实例 -> 表的记录(行)
- ORM的优点: 
    - 易用性：使用ORM做数据库的开发可以有效的减少重复SQL语句的概率，写出来的模型也更加直观、清晰。
    - 性能损耗小：ORM转换成底层数据库操作指令确实会有一些开销。但从实际的情况来看，这种性能损耗很少（不足5%），只要不是对性能有严苛的要求，综合考虑开发效率、代码的阅读性，带来的好处要远远大于性能损耗，而且项目越大作用越明显。
    - 设计灵活：可以轻松的写出复杂的查询。
    - 可移植性：SQLAlchemy封装了底层的数据库实现，支持多个关系数据库引擎，包括流行的MySQL、PostgreSQL和SQLite。可以非常轻松的切换数据库。

### 将ORM模型映射到数据库中：

```python
from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'  # 需要先创建数据库
USERNAME = 'root'
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URI)
# 1. 用declarative_base 根据 engine 创建基类 Base
Base = declarative_base(engine)

# create table person(id int primary key autoincrement, name varchar(50), age int)
# 2. 根据基类Base创建ORM类
class Person(Base):
    __tablename__ = 'person'  # 会自动创建一张 person 表.
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(INTEGER)

# 3.映射ORM模型到数据库(操作数据库 -> 创建表person -> DESC person;)
# Base.metadata.drop_all()  # 移除Base下绑定的所有表
Base.metadata.create_all()
```

具体步骤说明:

1. 用`declarative_base`根据`engine`创建一个ORM基类。

    ```python
    from sqlalchemy.ext.declarative import declarative_base
    engine = create_engine(DB_URI)
    Base = declarative_base(engine)
    ```

2. 用这个`Base`类作为基类来写自己的ORM类。要定义`__tablename__`类属性，来指定这个模型映射到数据库中的表名。

    ```python
    class Person(Base):
        __tablename__ = 'person'
    ```

3. 创建属性来映射到表中的字段，所有需要映射到表中的属性都应该为Column类型：

    ```python
    class Person(Base):
        __tablename__ = 'person'
        # 2. 在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射。这些属性必须是sqlalchemy给我们提供好的数据类型。
        id = Column(Integer,primary_key=True,autoincrement=True)
        name = Column(String(50))
        age = Column(Integer)
    ```

4. 使用`Base.metadata.create_all()`来将模型映射到数据库中。
5. 注意: 一旦使用`Base.metadata.create_all()`将模型映射到数据库中后，即使改变了模型的字段，重新执行程序, 也不会重新映射了;(如:追加了字段`sex = Column(String(50))`, 重新执行程序,`person`表的字段没有改变)

### 用session做数据的增删改查操作：

1. 构建session对象：所有和数据库的ORM操作都必须通过一个叫做`session`的会话对象来实现，通过以下代码来获取会话对象：

    ```python
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(DB_URI)
    session = sessionmaker(engine)()
    ```

2. 添加对象：
    - 创建对象，也即创建一条数据：
        ```python
        p = Person(name='zhiliao',age=18,country='china')
        ```
    - 将这个对象添加到`session`会话对象中：
        ```python
        session.add(p)
        ```
    - 将session中的对象做commit操作（提交）：
        ```python
        session.commit()
        ```
    - 一次性添加多条数据：
        ```python
        p1 = Person(name='zhiliao1',age=19,country='china')
        p2 = Person(name='zhiliao2',age=20,country='china')
        session.add_all([p1,p2])
        session.commit()
        ```
3. 查找对象：
    ```python
    # 查找某个模型对应的那个表中所有的数据：
    all_person = session.query(Person).all()
    # 使用filter_by来做条件查询
    all_person = session.query(Person).filter_by(name='zhiliao').all()
    # 使用filter来做条件查询
    all_person = session.query(Person).filter(Person.name=='zhiliao').all()
    # 使用get方法查找数据，get方法是根据id来查找的，只会返回一条数据或者None
    person = session.query(Person).get(primary_key)
    # 使用first方法获取结果集中的第一条数据
    person = session.query(Person).first()
    ```
4. 修改对象：首先从数据库中查找对象，然后将这条数据修改为你想要的数据，最后做commit操作就可以修改数据了。
    ```python
    person = session.query(Person).first()
    person.name = 'ketang'
    session.commit()
    ```
5. 删除对象：将需要删除的数据从数据库中查找出来，然后使用`session.delete`方法将这条数据从session中删除，最后做commit操作就可以了。
    ```python
    person = session.query(Person).first()
    session.delete(person)
    session.commit()
    ```

### SQLAlchemy常用数据类型：

1. Integer：整形，映射到数据库中是int类型。
2. Float：浮点类型，映射到数据库中是float类型。他占据的32位。
3. Double：双精度浮点类型，映射到数据库中是double类型，占据64位。
4. String(50)：长度为50的(可变)字符类型，映射到数据库中是varchar类型.
5. Boolean：布尔类型，映射到数据库中的是tinyint类型。
6. DECIMAL(10, 4)：定点类型。是专门为了解决`浮点类型精度丢失`的问题的。在存储`钱`相关的字段的时候建议大家都使用这个数据类型。并且这个类型使用的时候需要传递两个参数，**第一个参数是用来标记这个字段总能能存储多少个数字，第二个参数表示小数点后有多少位**。
7. Enum("python", "flask")：枚举类型。指定某个字段**只能是枚举中指定的几个值(如: `性别`)**，存储其他值会报错。在ORM模型中，使用Enum来作为枚举，示例代码如下：
    ```python
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        tag = Column(Enum("python",'flask','django'))
    ```
    在Python3中，已经内置了enum这个枚举的模块，我们也可以使用这个模块去定义相关的字段。示例代码如下：
    ```python
    import enum
    class TagEnum(enum.Enum):  # 自定义枚举类
        python = "python"
        flask = "flask"
        django = "django"

    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        tag = Column(Enum(TagEnum))  # 使用自定义的枚举类

    article = Article(tag=TagEnum.flask)  # "flask"字符串也可
    ```
8. Date：存储时间，只能存储年月日。映射到数据库中是date类型。在Python代码中，可以使用`datetime.date`来指定。示例代码如下：
    ```python
    from sqlalchemy import Date
    from datetime import date
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        create_time = Column(Date)

    article = Article(create_time=date(2017,10,10))
    ```
9. DateTime：存储时间，可以存储年月日时分秒毫秒等。映射到数据库中也是datetime类型。在Python代码中，可以使用`datetime.datetime`来指定。示例代码如下：
    ```python
    from sqlalchemy import DateTime
    from datetime import datatime
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        create_time = Column(DateTime)

    article = Article(create_time=datetime(2011,11,11,11,11,11))
    ```
10. Time：存储时间，可以存储时分秒。映射到数据库中也是time类型。在Python代码中，可以使用`datetime.time`来至此那个。示例代码如下：
    ```python
    from sqlalchemy import Time
    from datetime import time
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        create_time = Column(Time)

    article = Article(create_time=time(hour=11,minute=11,second=11))
    ```
11. Text：存储长字符串。一般可以存储6W多个字符。如果超出了这个范围，可以使用LONGTEXT类型。映射到数据库中就是text类型。
12. LONGTEXT：长文本类型，映射到数据库中是longtext类型。`from sqlalchemy.dialects.mysql import LONGTEXT`


### Column常用参数：

1. primary_key=True：设置某个字段为主键。
2. autoincrement=True：设置这个字段为自动增长的。
3. default=datetime.now：设置某个字段的默认值(可以是值或者是函数)。在发表时间这些字段上面经常用。
4. nullable=True：指定某个字段是否为空。默认值是True，就是可以为空。
5. unique=True：指定某个字段的值是否唯一。默认是False。
6. onupdate：在`数据表任何字段更新的时候`, `该字段`会调用这个参数指定的值或者函数。在第一次插入这条数据的时候，不会用onupdate的值，只会使用default的值。常用的就是`update_time=datetime.now`（每次更新数据的时候都要更新的值）。
7. name：ORM模型中,属性的名字默认会当做数据库的字段名。可以通过`name`选项来指定某属性映射到表中的字段名。这个参数也可以当作位置参数，在第1个参数来指定。
    ```python
    title = Column(String(50),nullable=False)  # 默认字段名为 title
    title = Column(String(50),name='field_name',nullable=False)
    title = Column('field_name',String(50),nullable=False)
    ```

### query可用参数：

1. 模型对象。指定查找这个模型中所有的对象。`session.query(Article).all()`
2. 模型中的属性。可以指定只查找某个模型的其中几个属性。`session.query(Article.title, Article.price).all()`
3. 聚合函数`session.query(fun.count(Article.id)).first()`。计算的结果只有一个,所以是first()
    - func.count：统计行的数量。
    - func.avg：求平均值。
    - func.max：求最大值。
    - func.min：求最小值。
    - func.sum：求和。
    
`func`上，其实没有任何聚合函数。但是因为他底层做了一些魔术，只要`mysql中有的聚合函数`，都可以通过func调用(`select sum(price) from article`)。

```python
from sqlalchemy import create_engine,Column,Integer,String,DateTime,String,Float,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

HOSTNAME = '127.0.0.1'
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
from datetime import datetime

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    price = Column(Float,nullable=False)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# Base.metadata.drop_all()
# Base.metadata.create_all()

# for x in range(6):
#     article = Article(title='title%s'%x,price=random.randint(50,100))
#     print(article)
#     session.add(article)
# session.commit()

# 模型对象
# articles = session.query(Article).all()
# # for article in articles:
# #     print(article)
# print(articles)

# 模型中的属性
# articles = session.query(Article.title,Article.price).all()
# print(articles)

# 聚合函数
count = session.query(func.count(Article.id)).first()
print(count)

avg = session.query(func.avg(Article.price)).first()
print(avg)

max = session.query(func.max(Article.price)).first()
print(max)

min = session.query(func.min(Article.price)).first()
print(min)

sum = session.query(func.sum(Article.price)).first()
print(sum)

print(func.sum(Article.title))
```

### filter过滤条件：

可以使用`filter_by(title=="xxx")`或`filter(Article.title=="xxx")`来来过滤查询的结果, 但是`filter`使用相对来说更强大.

过滤是数据提取的一个很重要的功能，以下对一些常用的过滤条件进行解释，并且这些过滤条件都是只能通过`filter`方法实现的：

1. equals：
    ```python
    article = session.query(Article).filter(Article.title == "title0").first()
    print(article)
    ```
2. not equals:
    ```python
    query.filter(User.name != 'ed')
    ```
2. like & ilike(不区分大小写)
    ```python
    articles = session.query(Article).filter(Article.title.like('%title%')).all()
    # 不分区大小写
    articles = session.query(Article).filter(Article.title.ilike('%title%')).all()
    print(articles)
    # %类似于通配符中的 * 
    ```

3. in：
    ```python
    query.filter(User.name.in_(['ed','wendy','jack']))
    # 同时，in也可以作用于一个Query
    query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))
    ```

4. not in：
    ```python
    # 以下两种方式皆可
    query.filter(~User.name.in_(['ed','wendy','jack']))
    query.filter(User.name.notin_(['ed','wendy','jack']))
    ```
5.  is null：
    ```python
    query.filter(User.name==None)
    # 或者是
    query.filter(User.name.is_(None))
    ```

6. is not null:
    ```python
    query.filter(User.name != None)
    # 或者是
    query.filter(User.name.isnot(None))
    ```

7. and：
    ```python
    from sqlalchemy import and_
    query.filter(and_(User.name=='ed',User.fullname=='Ed Jones'))
    # 或者是传递多个参数
    query.filter(User.name=='ed',User.fullname=='Ed Jones')
    # 或者是通过多次filter操作
    query.filter(User.name=='ed').filter(User.fullname=='Ed Jones')
    ```

8. or：
    ```python
    from sqlalchemy import or_  
    query.filter(or_(User.name=='ed',User.name=='wendy'))
    ```

如果想要查看orm底层转换的sql语句，可以在filter方法后面不要再执行任何方法直接打印就可以看到了。比如：
    ```python
        articles = session.query(Article).filter(or_(Article.title=='abc',Article.content=='abc'))
        print(articles)
    ```

```python
from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime, String, Float, func,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

HOSTNAME = '127.0.0.1'
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
from datetime import datetime

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    price = Column(Float,nullable=False)
    content = Column(Text)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# session.query(Article).filter(Article.id)
# 筛选关键字
# session.query(Article).filter_by(id=1)

# 1.equal
# article = session.query(Article).filter(Article.id == 1).first()
# print(article)

# # 2.not equal
# article = session.query(Article).filter(Article.title != 'title0').all()
# print(article)

# # 3. like
# articles = session.query(Article).filter(Article.title.like('%title%')).all()
# # 不分区大小写
# articles = session.query(Article).filter(Article.title.ilike('%title%')).all()
# print(articles)

# #  4. in
# articles = session.query(Article).filter(Article.title.in_(['title1','title2'])).all()
# print(articles)

# # 5. not in & ~
# articles = session.query(Article).filter(~Article.title.in_(['title1'])).all()
# # articles = session.query(Article).filter(Article.title.notin_(['title1'])).all()
# print(articles)

# # 6. is null
# articles = session.query(Article).filter(Article.content == None).all()
# print(articles)

# # 7. is not null
# articles = session.query(Article).filter(Article.content != None).all()
# print(articles)

# # 8. and
# # articles = session.query(Article).filter(Article.title=='title0' and Article.content == '123').all()
# articles = session.query(Article).filter(and_(Article.title=='title0',Article.content == '123')).all()
# print(articles)

# 9. or
articles = session.query(Article).filter(or_(Article.title=='title0',Article.content=='123')).all()
print(articles)
```

### 查找方法：

介绍完过滤条件后，有一些经常用到的查找数据的方法也需要解释一下：
- all()：返回一个Python列表（list）：
    ```python
    query = session.query(User).filter(User.name.like('%ed%').order_by(User.id)
    # 输出query的类型
    print type(query)
    > <type 'list'>
    # 调用all方法
    query = query.all()
    # 输出query的类型
    print type(query)
    > <class 'sqlalchemy.orm.query.Query'>
    ```
- first()：返回Query中的第一个值：
    ```python
    user = session.query(User).first()
    print user
    > <User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
    ```
- one()：查找所有行作为一个结果集，如果结果集中只有一条数据，则会把这条数据提取出来，如果这个结果集少于或者多于一条数据，则会抛出异常。总结一句话：有且只有一条数据的时候才会正常的返回，否则抛出异常：
    ```python
    # 多于一条数据
    user = query.one()
    > Traceback (most recent call last):
    > ...
    > MultipleResultsFound: Multiple rows were found for one()
    # 少于一条数据
    user = query.filter(User.id == 99).one()
    > Traceback (most recent call last):
    > ...
    > NoResultFound: No row was found for one()
    # 只有一条数据
    > query(User).filter_by(name='ed').one()
    ```
- one_or_none()：跟one()方法类似，但是在结果集中没有数据的时候也不会抛出异常。
- scalar()：底层调用one()方法，并且如果one()方法没有抛出异常，会返回查询到的第一列的数据：
    ```python
    session.query(User.name,User.fullname).filter_by(name='ed').scalar()
    ```

### 文本SQL：

SQLAlchemy还提供了使用文本SQL的方式来进行查询，这种方式更加的灵活。而文本SQL要装在一个text()方法中，看以下例子：

```python
from sqlalchemy import text
for user in session.query(User).filter(text("id<244")).order_by(text("id")).all():
    print user.name
```

如果过滤条件比如上例中的244存储在变量中，这时候就可以通过传递参数的形式进行构造：

```python
session.query(User).filter(text("id<:value and name=:name")).params(value=224,name='ed').order_by(User.id)
```

在文本SQL中的变量前面使用了:来区分，然后使用params方法，指定需要传入进去的参数。另外，使用from_statement方法可以把过滤的函数和条件函数都给去掉，使用纯文本的SQL:

```python
sesseion.query(User).from_statement(text("select * from users where name=:name")).params(name='ed').all()
```

使用from_statement方法一定要注意，from_statement返回的是一个text里面的查询语句，一定要记得调用all()方法来获取所有的值。

### 计数（Count）：

Query对象有一个非常方便的方法来计算里面装了多少数据：

```python
session.query(User).filter(User.name.like('%ed%')).count()
```

当然，有时候你想明确的计数，比如要统计users表中有多少个不同的姓名，那么简单粗暴的采用以上count是不行的，因为姓名有可能会重复，但是处于两条不同的数据上，如果在原生数据库中，可以使用distinct关键字，那么在SQLAlchemy中，可以通过func.count()方法来实现：

```python
from sqlalchemy import func
session.query(func.count(User.name),User.name).group_by(User.name).all()
# 输出的结果
> [(1, u'ed'), (1, u'fred'), (1, u'mary'), (1, u'wendy')]
```

另外，如果想实现select count(*) from users，可以通过以下方式来实现：

```python
session.query(func.count(*)).select_from(User).scalar()
```

当然，如果指定了要查找的表的字段，可以省略select_from()方法：

```python
session.query(func.count(User.id)).scalar()
```

### 表关系：

表之间的关系存在三种：一对一、一对多、多对多。mysql中表关系是通过外键(约束)实现的; 而SQLAlchemy中的ORM也可以模拟这三种关系。因为一对一其实在SQLAlchemy中底层是通过一对多的方式模拟的，所以下面了解外键约束之后,首先看下一对多的关系：

#### 外键：

在MySQL中，外键可以让表之间的关系更加紧密，而SQLAlchemy同样支持外键。通过`ForeignKey`类来实现，并且可以指定表的外键约束。相关示例代码如下:

注意: `子表`与`父表`对应的`外键字段类型`必须保持一致。

示例代码如下：
```python
from sqlalchemy import create_engine, Column, Integer, Text, String, 
DateTime, String, Float, func,and_,or_,ForeignKey

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)

    # 外键
    uid = Column(Integer,ForeignKey("user.id"))  # 关联的是 表名 ,而不是 类名

Base.metadata.drop_all()
Base.metadata.create_all()
```

> 可以使用` SHOW CREATE TABLE user\G` 显示该表的`创建语句`(可以得知是否具有外键约束); 显示结果中的必须是`ENGINE=InnoDB`才支持外键约束,其他引擎不支持.

外键约束有以下几项： 
1. RESTRICT(默认就是这一项)：如果有引用,会阻止在MySQL层面删除(但是在ORM层面用python语句可以删除 -> 陷阱, 可以通过设置`nullable=False`避免)。
2. NO ACTION：在MySQL中，同RESTRICT。 
3. CASCADE：级联删除。 
4. SET NULL：父表数据被删除，子表数据会设置为NULL。

```python
from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime, String, Float, func,and_,or_,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

HOSTNAME = '127.0.0.1'
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
from datetime import datetime

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

# 父表/从表
# user/article

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50))

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)

    # 外键，没有指定，就默认为RESTRICT
    # RESTRICT:阻止删除数据
    # uid = Column(Integer,ForeignKey("user.id",ondelete="RESTRICT"))
    # 级联删除
    # uid = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    # 只有父表被删除，子表修改为NULL
    uid = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))

Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username = 'angle')
session.add(user)
session.commit()

article = Article(content='abc',title='123',uid=1)
session.add(article)
session.commit()
```

#### ORM关系以及一对多(`一个作者 <-> 多篇文章`)：

mysql级别的外键，不够优雅(必须拿到A表的外键，然后通过这个外键去B表中查找)。

```python
# 表之间的关系
article = session.query(Article).first()
uid = article.uid
print(article)
# get方法只匹配主键字段
user = session.query(User).get(uid)
print(user)
print(uid)
```

SQLAlchemy提供了一个`relationship`，这个类可以定义属性，以后在访问相关联的表的时候就直接可以通过属性访问的方式就可以访问得到了。示例代码：

```python
class User(Base):
    ....
    articles = relationship('Article')

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class Article(Base):
    ....
    # 映射到User模型
    # backref:反向引用,为user添加一个属性
    author = relationship("User")

    def __repr__(self):
        return "<Article(title:%s),content:%s>" % (self.title,self.content)



article = session.query(Article).first()
print(article.author.username)

user = session.query(User).first()
print(user.articles)
```

上面代码中两个类中都定义了外键相关的`relationship`，其实可以通过`backref`来指定反向访问的属性名称(只需要在Article中定义即可)。articles是有多个。他们之间的关系是一个一对多的关系。

```python
class Article(Base):
    ......
    # 映射到User模型
    # backref:反向引用,为user添加一个属性
    author = relationship("User",backref="articles")
```

汇总代码如下:

```python
from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime, String, Float, func,and_,or_,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
import random

HOSTNAME = '127.0.0.1'
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
from datetime import datetime

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

# 父表/从表
# user/article

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50))

    # articles = relationship('Article')

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))

    # 映射到User模型
    # backref:反向引用,为user添加一个属性
    author = relationship("User",backref="articles")

    def __repr__(self):
        return "<Article(title:%s),content:%s>" % (self.title,self.content)

Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username = 'angle')
session.add(user)
session.commit()

article = Article(content='abc1',title='123',uid=1)
session.add(article)
session.commit()

# 一对多时, article有多个
article1 = Article(content='abc1',title='111')
article2 = Article(content='abc2',title='222')
user.articles.append(article1)
user.articles.append(article2)
session.add(user)  # 会自动把 article1 article2 添加
session.commit()

# 一对多时, article只有一个
user = User(username = 'angle')
article = Article(content='abc1',title='123')
article.author = user
session.add(article)
session.commit()

# 表之间的关系
article = session.query(Article).first()
uid = article.uid
print(article)
# get方法只匹配主键字段
user = session.query(User).get(uid)
print(user)
print(uid)

article = session.query(Article).first()
print(article.author.username)

user = session.query(User).first()
print(user.articles)
```

#### 一对一的关系(`一个用户 <-> 一个用户扩展`)：

> 一对一关系实际背景: 用户的信息很多,但是有些是常用的,有些是不常用的(如: 毕业学习,籍贯等..),为了提升数据库的查询效率,我们可以把不常用的信息单独放一张表.

在sqlalchemy中，如果想要将两个模型映射成一对一的关系，那么应该在父模型中，指定引用的时候，要传递一个`uselist=False`这个参数进去。就是告诉父模型，以后引用这个从模型的时候，不再是一个列表了，而是一个对象了。示例代码如下：

```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    extend = relationship("UserExtend",uselist=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer,ForeignKey("user.id"))

    user = relationship("User",backref="extend")
```

当然，也可以借助`sqlalchemy.orm.backref`来简化代码：

```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    # extend = relationship("UserExtend",uselist=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer,ForeignKey("user.id"))

    user = relationship("User",backref=backref("extend",uselist=False))
```

#### 多对多的关系(`多个文章 <-> 多个标签`)：

1. 多对多的关系需要通过一张中间表`Table`来记录他们之间的关系。
2. 先把两个需要做多对多的模型定义出来
3. 使用Table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键”。
4. 在两个需要做多对多的模型中`随便选择`一个模型，定义一个`relationship`属性，来绑定三者之间的关系，在使用`relationship`的时候，需要传入一个`secondary=中间表`。

```python
from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime, String, Float, func, and_, or_, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
import random

DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
from datetime import datetime

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

# article表
# id/title
# 1/'title'

# article_tag中间表
# article_id/tag_id
# 1/1,
# 1/1

# tag表
# id/name
# 1/'tag1'

"""
Create Table: CREATE TABLE `article_tag` (
  `article_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`article_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `article_tag_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  CONSTRAINT `article_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""
article_tag = Table(  # 用Table定义中间表
    "article_tag",
    Base.metadata,
    Column("article_id",Integer,ForeignKey("article.id"),primary_key=True), 
    Column("tag_id",Integer,ForeignKey("tag.id"),primary_key=True) # 和上一行都是主键 -> 复合主键 -> 减少数据冗余
)

"""
Create Table: CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
"""
class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)

    def __repr__(self):
        return "<Article(title:{})>".format(self.title)

    # tags = relationship('Tag',backref='articles',secondary=article_tag)
    # 不需要指定外键, 只需要secondary参数即可

"""
Create Table: CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""
class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)

    articles = relationship("Article",backref="tags",secondary=article_tag)

    def __repr__(self):
        return "<Tag(name:{})>".format(self.name)

# 1. 先把两个需要多对多的模型定义出来
# 2. 使用Table定义定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让它们两个来作为一个"复合主键"
# 3.在两个需要做多对多的模型中随便选择一个模型，定义一个relationship属性，来绑定三者之间的关系，在使用relationship的时候，需要传入一个secondary=中间表

# 插入数据(以下n行)
Base.metadata.drop_all()
Base.metadata.create_all()

article1 = Article(title="angle1")
article2 = Article(title="angle2")

tag1 = Tag(name="tag1")
tag2 = Tag(name="tag2")

article1.tags.append(tag1)
article1.tags.append(tag2)

article2.tags.append(tag1)
article2.tags.append(tag2)

session.add(article1)
session.add(article2)
session.commit()

# 查询数据段
article = session.query(Article).first()
print(article.tags)  # 某篇文章的所有tags

tag = session.query(Tag).first()
print(tag.articles)  # 某个tag下所有的articles
```

### ORM层面可以mysql层面删除约束的数据 -> 解决：

在mysql层面, 外键约束的数据默认是不允许删除的. 但是ORM层面删除数据，会无视mysql级别的外键约束。直接会将对应的数据删除，内部其实是先将从表中的那个外键设置为NULL。如果想要避免这种行为，应该将从表中的外键的`nullable=False`。

```python
class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    # 会起到限制
    uid = Column(Integer,ForeignKey('user.id'),nullable=False)
    # uid = Column(Integer,ForeignKey('user.id'))

    author = relationship("User",backref="articles")

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username = 'angle1')
# article = Article(title = 'angle2')
#
# article.author = user
#
# session.add(article)
# session.commit()

user = session.query(User).first()
# 删除user表，article表的外键修改为null
session.delete(user)
session.commit()
```

### ORM层面的cascade(级联)操作控制：

**在SQLAlchemy，只要将一个数据添加到session中，和他相关联的数据都可以一起存入到数据库中了**。这些是怎么设置的呢？其实是通过relationship的时候，有一个关键字参数cascade如下值：

1. save-update：默认选项. 在添加一条数据的时候，会把其他和他相关联的数据都添加到数据库中。这种行为就是save-update属性影响的。 
2. delete：表示当删除某一个模型中的数据的时候，是否也删掉使用relationship和他关联的数据。
3. delete-orphan：表示当对一个ORM对象解除了父表中的关联对象的时候，自己便会被删除掉。当然如果父表中的数据被删除，自己也会被删除。这个选项只能用在一对多上，不能用在多对多以及多对一上。并且还需要在子模型中的relationship中，增加一个single_parent=True的参数。 
4. merge：默认选项。当在使用session.merge，合并一个对象的时候，会将使用了relationship相关联的对象也进行merge操作。 
5. expunge：移除操作的时候，会将相关联的对象也进行移除。这个操作只是从session中移除，并不会真正的从数据库中删除。 
6. all：是对save-update, merge, refresh-expire, expunge, delete几种的缩写。

```python
"relationship("模型类",backref="另外一个模型类的属性",cascade="save-update,delete")"

from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime, String, Float, func, and_, or_, \
    ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref

HOSTNAME = '127.0.0.1'
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    # articles = relationship("Article",cascade="save-update,delete")
    # comments = relationship('Comment',cascade="save-update,delete")

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    uid = Column(Integer,ForeignKey("user.id"))

    # 不会执行添加操作 -- not add Article
    # author = relationship("User",backref="articles",cascade="")
    # 保存并更新数据
    # delete:级删除
    # author = relationship("User", backref="articles", cascade="save-update,delete")
    # author = relationship("User", backref="articles", cascade="delete")

    # author = relationship("User", cascade="save-update,delete")
    author = relationship("User", backref=backref("articles",cascade="save-update,delete"),cascade="save-update,delete")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer,primary_key=True,autoincrement=True)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('user.id'))

    author = relationship("User")

def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    user = User(username="angle")
    article = Article(title="miku")
    article.author = user

    comment = Comment(content="xxxx")
    comment.author = user
    session.add(comment)
    session.add(article)
    session.commit()

def operation():
    # article = session.query(Article).first()
    # session.delete(article)

    user = session.query(User).first()
    session.delete(user)

    session.commit()

if __name__ == "__main__":
    # my_init_db()
    operation()
```

```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    # articles = relationship("Article",cascade="save-update,delete")
    # comments = relationship('Comment',cascade="save-update,delete")

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    uid = Column(Integer,ForeignKey("user.id"))

    # 不会执行添加操作 -- not add Article
    # author = relationship("User",backref="articles",cascade="")
    # 保存并更新数据
    # delete:级删除
    # author = relationship("User", backref="articles", cascade="save-update,delete")
    # author = relationship("User", backref="articles", cascade="delete")

    # author = relationship("User", cascade="save-update,delete")
    # single_parent=True,唯一的父表
    # cascade="all"，除了delete-orphan都包含了
    author = relationship("User", backref=backref("articles",cascade="save-update,delete,delete-orphan,merge,expunge"),cascade="save-update",single_parent=True)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer,primary_key=True,autoincrement=True)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('user.id'))

    author = relationship("User",backref="comments")

def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    user = User(username="angle")
    article = Article(title="miku")
    article.author = user

    comment = Comment(content="xxxx")
    comment.author = user
    session.add(comment)
    session.add(article)
    session.commit()

def operation():
    # article = session.query(Article).first()
    # session.delete(article)

    # user = session.query(User).first()
    # # session.delete(user)
    # user.articles = []

    # user = User(id=1,username="angle2")
    # article = Article(id=2,title="angle3")
    # user.articles.append(article)
    # # 合并，主键重复，替换值，不重复，添加进去
    # session.merge(user)
    # session.merge(article)
    # 移除操作,与session.add()操作相反

    user = User(username="angle2")
    article = Article(title="angle3")
    article.author = user
    session.add(user)
    session.add(article)
    # 只会从会话中删除数据，不会从数据库把数据删除
    session.expunge(user)
    session.commit()

"""
用户--文章
删除用户可以删除所有文章
删除一遍文章，不会删除用户
"""

if __name__ == "__main__":
    # my_init_db()
    operation()
```

### 排序(-> 帖子发表时间排序)：

1. order_by：可以指定根据这个表中的某个字段进行排序。

```python
# 默认正序排序
articles = session.query(Article).order_by(Article.create_time).all()
# 降序排序1:desc()
articles = session.query(Article).order_by(Article.create_time.desc()).all()
# 降序排序2:在字段前面加个负号代表降序
articles = session.query(Article).order_by("-create_time").all()
```

2. 在模型定义的时候指定默认排序：有些时候，不想每次在查询的时候都指定排序的方式，可以在定义模型的时候就指定排序的方式。有以下两种方式：
    - relationship的order_by参数：在指定relationship的时候，传递order_by参数来指定排序的字段。
    - 在模型定义中，添加以下代码：
        ```python
        __mapper_args__ = {
            "order_by": title
        }
        # 即可让文章使用标题来进行排序。
        ```

    ```python
    class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    # 注意default里面的datetime.now，没有()
    create_time = Column(DateTime,nullable=False,default=datetime.now)
    uid = Column(Integer,ForeignKey('user.id'))
    
    # 排序1
    # author = relationship("User",backref=backref("articles",order_by=create_time.desc()))
    author = relationship("User", backref=backref("articles"))

    # 排序2
    __mapper_args__ = {
        "order_by":create_time.desc(),
    }
    ```

3. 正序排序与倒序排序：默认是使用正序排序。如果需要使用倒序排序，那么可以:
    - 使用这个字段的`desc()`方法，
    - 或者是在排序的时候使用这个`字段的字符串名字`，然后在前面加一个`负号`。

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, String, Integer, Float, ForeignKey, DateTime, Date, Column, desc,asc
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker,relationship,backref
from datetime import datetime

HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    # 注意default里面的datetime.now，没有()
    create_time = Column(DateTime,nullable=False,default=datetime.now)
    uid = Column(Integer,ForeignKey('user.id'))

    # author = relationship("User",backref=backref("articles",order_by=create_time.desc()))
    author = relationship("User", backref=backref("articles"))

    # 排序
    __mapper_args__ = {
        "order_by":create_time.desc(),
    }

    # 重写函数
    def __repr__(self):
        return "<Article(title:{},create_time:{})>".format(self.title,self.create_time)


# Base.metadata.drop_all()
# Base.metadata.create_all()
# 添加数据
# article1 = Article(title="title1")
# article2 = Article(title="title2")
# user = User(username='miku')
# user.articles = [article1,article2]
# session.add(user)
# session.commit()
# -----------------------------------
# article1 = Article(title="angle1")
# user = User(username="miku")
# user.articles = [article1]
# session.add(user)
# session.commit()
#
# import time
# time.sleep(2)
#
# article2 = Article(title="angle2")
# user.articles.append(article2)
# session.commit()


# 默认正序排序
# 降序排序
# articles = session.query(Article).order_by(Article.create_time.desc()).all()
# 降序，在字段前面加个符号代表降序
# articles = session.query(Article).order_by("-create_time").all()

articles = session.query(Article).all()
for article in articles:
    print(article)

user = session.query(User).first()
print(user.articles)
```

### limit、offset和切片操作：

1. limit：可以限制每次查询的时候只查询几条数据。
    ```python
    articles = session.query(Article).limit(10).all()  # 获取前10条数据
    ```
2. offset：可以限制查找数据的时候过滤掉前面多少条。
    ```python
    select * from article limit 4 offset 9
    select * from article limit 9,4
    articles = session.query(Article).order_by(Article.id.desc()).offset(10).limit(10).all()
    slice(limit,offset),desc()降序
    articles = session.query(Article).order_by(Article.id.desc()).slice(0,10).all()
    ```
3. 切片：可以对Query对象使用切片操作，来获取想要的数据。可以使用`slice(start,stop)`方法来做切片操作。也可以使用`[start:stop]`的方式来进行切片操作。一般在实际开发中，中括号的形式是用得比较多的。希望大家一定要掌握。示例代码如下：
    ```python
    articles = session.query(Article).order_by(Article.id.desc())[0:10]
    ```

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, String, Integer, Float, ForeignKey, DateTime, Date, Column, desc,asc
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker,relationship,backref
from datetime import datetime

HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    create_time = Column(DateTime,default=datetime.now)

    def __repr__(self):
        return "<Article(title:%s,create_time:%s)>" % (self.title,self.create_time)

# 添加数据
# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# for i in range(100):
#     title = "title %s" % i
#     article = Article(title=title)
#     session.add(article)
#     session.commit()

# 实战
# articles = session.query(Article).all()
# 获取前10条数据
# articles = session.query(Article).limit(10).all()
# offset(10)代表从第几条的数据开始
# select * from article limit 4 offset 9
# select * from article limit 9,4
# articles = session.query(Article).order_by(Article.id.desc()).offset(10).limit(10).all()
# slice(limit,offset),desc()降序
# articles = session.query(Article).order_by(Article.id.desc()).slice(0,10).all()
# 切片
articles = session.query(Article).order_by(Article.id.desc())[0:10]
print(articles)
```

### 数据查询的懒加载技术：

如果把所有的数据查询后拿出来,然后再通过后续代码逻辑过滤, 这样效能不高! 如果能在查找数据的时候就能过滤,只拿过滤后的数据,数据查询性能会提高.这就是数据查询懒加载技术.

在一对多，或者多对多的时候，如果想要获取多的这一部分的数据的时候，往往能通过一个属性就可以全部获取了。比如有一个作者，想要或者这个作者的所有文章，那么可以通过user.articles就可以获取所有的。但有时候我们不想获取所有的数据，比如只想获取这个作者今天发表的文章，那么这时候我们可以给relationship传递一个lazy='dynamic'，以后通过user.articles获取到的就不是一个`列表`，而是一个`AppenderQuery对象`了。这样就可以对这个对象再进行一层过滤和排序等操作。

通过`lazy='dynamic'`，获取出来的多的那一部分的数据，就是一个`AppenderQuery`对象了。这种对象既可以添加新数据，也可以跟`Query`一样，可以再进行一层过滤。
总而言之一句话：如果你在获取数据的时候，想要对多的那一边的数据再进行一层过滤，那么这时候就可以考虑使用`lazy='dynamic'`。
lazy可用的选项：

1. `select`：这个是默认选项。还是拿`user.articles`的例子来讲。如果你没有访问`user`的`articles`这个属性，那么sqlalchemy就不会从数据库中查找文章。一旦你访问了这个属性，那么sqlalchemy就会立马从数据库中查找所有的文章，并把查找出来的数据组装成一个列表返回。这也是懒加载。
2. `dynamic`：这个就是我们刚刚讲的。就是在访问`user.articles`的时候返回回来的不是一个列表，而是`AppenderQuery`对象。

```python
from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text,func,and_,or_,ForeignKey,Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
# 在Python3中才有这个enum模块，在python2中没有
import enum
from datetime import datetime
import random

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50),nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime,nullable=False,default=datetime.now)
    uid = Column(Integer,ForeignKey("user.id"))

    author = relationship("User",backref=backref("articles",lazy="dynamic"))

    def __repr__(self):
        return "<Article(title: %s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='zhilio')
# for x in range(100):
#     article = Article(title="title %s" % x)
#     article.author = user
#     session.add(article)
# session.commit()

from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.dynamic import AppenderQuery
from sqlalchemy.orm.query import Query
user = session.query(User).first()
# 是一个Query对象。
# print(user.articles.filter(Article.id > 50).all())
# 可以继续追加数据进去
article =Article(title='title 100')
user.articles.append(article)
session.commit()
```

### group_by子句：
根据某个字段进行分组。比如想要根据性别进行分组，来统计每个分组分别有多少人，那么可以使用以下代码来完成：
```python
session.query(User.gender,func.count(User.id)).group_by(User.gender).all()
```

### having子句：
having是对查找结果进一步过滤。比如只想要看未成年人的数量，那么可以首先对年龄进行分组统计人数，然后再对分组进行having过滤。示例代码如下：
```python
result = session.query(User.age,func.count(User.id)).group_by(User.age).having(User.age >= 18).all()
```

### 高级查询：

#### join实现复杂查询：

1. join分为left join（左外连接）和right join（右外连接）以及内连接（等值连接）。
2. 参考的网页：http://www.jb51.net/article/15386.htm
3. 在sqlalchemy中，使用join来完成内连接。在写join的时候，如果不写join的条件，那么默认将使用外键来作为条件连接。
4. query查找出来什么值，不会取决于join后面的东西，而是取决于query方法中传了什么参数。就跟原生sql中的select 后面那一个一样。
比如现在要实现一个功能，要查找所有用户，按照发表文章的数量来进行排序。示例代码如下：

    ```python
    result = session.query(User,func.count(Article.id)).join(Article).group_by(User.id).order_by(func.count(Article.id).desc()).all()
    ```

```python
from sqlalchemy import create_engine,Column,String,ForeignKey,Float,DateTime,Date,Integer,Enum,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from datetime import datetime

HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    def __repr__(self):
        return "<User(id:%s,username:%s)>" % (self.id,self.username)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    create_time = Column(DateTime,nullable=False,default=datetime.now)
    uid = Column(Integer,ForeignKey("user.id"))

    author = relationship("User",backref=backref("articles"))

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# 添加数据
# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username="angle")
# user2 = User(username="miku")
#
# for i in range(1):
#     article = Article(title="title1 %s" % i)
#     article.author = user1
#     session.add(article)
# session.commit()
#
# for i in range(1,3):
#     article = Article(title="title1 %s" % i)
#     article.author = user2
#     session.add(article)
# session.commit()

# 找到所有的用户，按照发表的文章数量进行排序
# 默认会使用外键作为连接条件
# select user.username,count(article.id) fro m user join article on user.id = article.uid group by user.id order by count(article.id) desc;
# result = session.query(User.username,func.count(Article.id)).outerjoin(Article,User.id==Article.id).group_by(User.id).order_by(func.count(Article.id).desc()).all()

# # 左外连接
# result = session.query(User).join(Article).group_by(User.id).order_by(func.count(Article.id).desc()).all()
# # # 右外连接,注意类和left的类位置，调换
# result = session.query(Article).join(User).group_by(User.id).order_by(func.count(Article.id).desc()).all()
# # # outerjoin
# result = session.query(Article).outerjoin(User).group_by(User.id).order_by(func.count(Article.id).desc()).all()
# print(result)
```

#### 别名

当多表查询的时候，有时候同一个表要用到多次，这时候用别名就可以方便的解决命名冲突的问题了：

```python
from sqlalchemy.orm import aliased
adalias1 = aliased(Address)
adalias2 = aliased(Address)
for username,email1,email2 in session.query(User.name,adalias1.email_address,adalias2.email_address).join(adalias1).join(adalias2).all():
    print username,email1,email2
```

#### subquery实现复杂查询：

子查询(`subquery`)可以让多个查询变成一个查询，只要查找一次数据库，性能相对来讲更加高效一点。不用写多个sql语句就可以实现一些复杂的查询。那么在sqlalchemy中，要实现一个子查询，应该使用以下几个步骤：
1. 将子查询按照传统的方式写好查询代码，然后在`query`对象后面执行`subquery`方法，将这个查询变成一个子查询。
    ```python
    user = session.query(func.max(User.age).label("age")).subquery()
    ```
2. 在子查询中，将以后需要用到的字段通过`label`方法，取个别名。
    ```python
    session.query(func.max(User.age).label("age"))
    ```
3. 在父查询中，如果想要使用子查询的字段，那么可以通过子查询的返回值上的`c`属性拿到。
    ```python
    result = session.query(User).filter(User.age == user.c.age).all()
    ```

整体的示例代码如下：

```python
from sqlalchemy import create_engine,Column,String,ForeignKey,Float,DateTime,Date,Integer,Enum,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from datetime import datetime

HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "xt_flask"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)
    city = Column(String(50),nullable=False)
    age = Column(Integer,default=0)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username="A",city="M城",age=15)
# user2 = User(username="B",city="G城",age=21)
# user3 = User(username="C",city="H城",age=12)
# user4 = User(username="D",city="J城",age=20)
#
# session.add_all([user1,user2,user3,user4])
# session.commit()

# # mysql> select * from user where age = 21;
user = session.query(func.max(User.age).label("age")).subquery()
result = session.query(User).filter(User.age == user.c.age).all()
print(result)

# # 实现子查询
# subuser = session.query(User.city.label("city"),User.age.label("age")).filter(User.username == 'A').subquery()
# # subquery.column.city == subquery.c.city
# result = session.query(User).filter(User.city == subuser.c.city).all()
# print(result)
```

## 用Flask-SQLAlchemy操作数据库

SQLAlchemy是基础(必会),但是使用起来有点繁琐! 所有有另一个框架，叫做Flask-SQLAlchemy对SQLAlchemy进行了一个简单的封装，使得我们在flask中使用sqlalchemy更加的简单。

SQLAlchemy`纯python文件`就可以运行, 而Flask-SQLAlchemy需要`Flask项目`运行.

- 安装: `pip install flask-sqlalchemy`。

    ```sh
    # 依赖关系如下
    > pipenv graph
    Flask-SQLAlchemy==2.3.2
        - Flask [required: >=0.10, installed: 1.0.2]
            - click [required: >=5.1, installed: 7.0]
            - itsdangerous [required: >=0.24, installed: 1.1.0]
            - Jinja2 [required: >=2.10, installed: 2.10]
            - MarkupSafe [required: >=0.23, installed: 1.1.1]
            - Werkzeug [required: >=0.14, installed: 0.14.1]
        - SQLAlchemy [required: >=0.8.0, installed: 1.2.18]
    ```

- 数据库初始化：数据库初始化不再是通过create_engine，请看以下示例：
    1. 跟sqlalchemy一样，定义好数据库连接字符串DB_URI。
    2. 将这个定义好的数据库连接字符串DB_URI，通过`SQLALCHEMY_DATABASE_URI`这个键放到`app.config`中。示例代码：`app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI`.
    3. 使用`flask_sqlalchemy.SQLAlchemy`这个类定义一个对象，并将`app`传入进去。示例代码：`db = SQLAlchemy(app)`。

    ```python
    from flask import Flask
    from flask_sqlalchemyu import SQLAlchemy
    from constants import DB_URI
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    db = SQLAlchemy(app)
    ```

- 创建ORM模型：之前都是通过Base = declarative_base()来初始化一个基类，然后再继承，在Flask-SQLAlchemy中更加简单了（代码依赖以上示例）：
    1. 还是跟使用sqlalchemy一样，定义模型。现在不再是需要使用`delarative_base`来创建一个基类。而是使用`db.Model`来作为基类。
    2. 在模型类中，`Column`、`String`、`Integer`以及`relationship`等，都不需要导入了，直接使用`db`下面相应的属性名就可以了。
    3. 在定义模型的时候，可以不写`__tablename__`，那么`flask_sqlalchemy`会默认使用当前的模型的名字转换成小写来作为表的名字，并且如果这个模型的名字使用了多个单词并且使用了驼峰命名法，那么会在多个单词之间使用下划线来进行连接。**虽然flask_sqlalchemy给我们提供了这个特性，但是不推荐使用。因为明言胜于暗喻**

    ```python
    class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120),unique=True)
    def __init__(self,username,email):
        self.username = username
        self.email = email
    def __repr__(self):
        return '<User %s>' % self.username
    ```

- 将ORM模型映射到数据库：使用Flask-SQLAlchemy所有的类都是继承自db.Model，并且所有的Column和数据类型也都成为db的一个属性。但是有个好处是不用写表名了，Flask-SQLAlchemy会自动将类名小写化，然后映射成表名。写完类模型后，要将模型映射到数据库的表中，使用以下代码创建所有的表：
    1. db.drop_all()
    2. db.create_all()

- 使用session：
    以后session也不需要使用`sessionmaker`来创建了。直接使用`db.session`就可以了。操作这个session的时候就跟之前的`sqlalchemy`的`session`是iyimoyiyang的。

- 添加数据：这时候就可以在数据库中看到已经生成了一个user表了。接下来添加数据到表中：
    ```python
    admin = User('admin','admin@example.com')
    guest = User('guest','guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    # 添加数据和之前的没有区别，只是session成为了一个db的属性。
    ```
- 查询数据：查询数据不再是之前的session.query了，而是将query属性放在了db.Model上，所以查询就是通过Model.query的方式进行查询了. 如果查找数据只是查找一个模型上的数据，那么可以通过`模型.query`的方式进行查找。`query`就跟之前的sqlalchemy中的query方法是一样用的。示例代码如下：

    ```python
    users = User.query.all()
    # 再如：
    admin = User.query.filter_by(username='admin').first()
    # 或者：
    admin = User.query.filter(User.username='admin').first()
    ```

    > 更复杂的查询可能还需要借助`db.session.query`实现.

- 删除数据：删除数据跟添加数据类似，只不过session是db的一个属性而已：
    ```python
    db.session.delete(admin)
    db.session.commit()
    ```

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "first_flask"
USERNAME = "root"
PASSWORD = "123456"
# dialect+dricer://username:password@host:port/database
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# 配置
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 数据库
# db == > app
# 通过db访问app
db = SQLAlchemy(app)

# 定义orm模型
# 继承自db.Model
# UserModel == > user_model
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return "<Article(username:%s)>" % self.username

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey("user.id"))

    author = db.relationship("User",backref=db.backref("articles"))

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

@app.route('/')
def hello_world():
    return 'Hello World!'

def init_data():
    db.drop_all()
    db.create_all()
    user = User(username="angle")
    article = Article(title="title one")
    article.author = user
    # user.articles.append(article)
    db.session.add(article)
    db.session.commit()

def query():
    # db.session.query(User)与下面效果一样
    # order_by
    # filter
    # filter_by
    # group_by
    # join
    # subquery
    # user = User.query.filter(User.id == 1).all()
    # users = User.query.order_by(User.id.desc()).all()
    # print(users)
    # 过滤、删除
    user = User.query.filter(User.username == "angle3").first()
    db.session.delete(user)
    db.session.commit()

if __name__ == '__main__':
    # init_data()
    query()
    # app.run()
```

## alembic数据库迁移(flask_migrate的底层)

### 概述

- 前面我们处理表时, 经常使用`db.drop_all()`和`db.create_all()`删除表/创建表,但是实际工作中,我们最需要的不是删除表,而是改变表.这时就需要alembic.
- alembic是sqlalchemy的作者开发的。用来做ORM模型与数据的迁移与映射。**alembic配合sqlalchem使用,是对其的补充, 不依赖flask项目;**ayalembic使用方式跟git有点类似，表现在两个方面:
    - 第一，alembic的所有命令都是以alembic开头，
    - 第二，alembic的迁移文件也是通过版本进行控制的。

- 安装: pip install alembic进行安装。以下将解释alembic的用法:

### alembic基本使用

使用alembic的步骤：
1. 初始化alembic仓库:在终端中，cd到项目目录中，然后执行`alembic init alembic`，创建一个名叫alembic的仓库。
2. 创建模型类:创建一个models.py模块，然后在里面定义模型类，示例代码:
    ```python
    from sqlalchemy import create_engine,Column,String,Float,Integer
    from sqlalchemy.ext.declarative import declarative_base
    # from sqlalchemy.orm import sessionmaker

    HOSTNAME = "127.0.0.1"
    PORT = "3306"
    DATABASE = "alembic_demo"
    USERNAME = "root"
    PASSWORD = "123456"
    # dialect+dricer://username:password@host:port/database
    DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

    engine = create_engine(engine)
    Base = declarative_base(engine)
    # session = sessionmaker(engine)()

    class User(Base):
        __tablename__ = "user"
        id = Column(Integer,primary_key=True,autoincrement=True)
        username = Column(String(50),nullable=False)
    ```
3. 修改配置文件：
    - 在`alembic.ini`中，给`sqlalchemy.url`设置数据库的连接方式。这个连接方式跟sqlalchemy的方式一样的。
        ```python
        sqlalchemy.url = mysql+pymysql://root:123456@localhost/alembic_demo?charset=utf8
        ```
    - 为了使用模型类更新数据库,需要在`alembic/env.py`中的`target_metadata`设置模型的`Base.metadata`。但是要导入`models`，当前文件夹不是模块, 所有需要使用sys模块把当前项目的路径导入到path中:
        ```python
        import sys,os
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        # ....
        taget_metadata = models.Base.metadata
        ```
4. 将ORM模型生成迁移脚本：在cmd中输入`alembic revision --autogenerate -m '第一次提交'`(会在/alembic/version/下生成`xx第一次提交.py`文件)。
5. 将生成的脚本映射/写入到数据库中：`alembic upgrade head`。
6. 以后如果修改了模型中的类(数据库中表的字段)等，重复4、5步骤。更新数据库中表的字段等.
7. 注意事项：在终端中，如果想要使用alembic，则需要首先进入到安装了alembic的虚拟环境中，不然就找不到这个命令。

### 常用命令：

1. init：创建一个alembic仓库。
2. revision/rɪˈvɪʒn/(修订)：创建一个新的版本文件。
3. --autogenerate：自动将当前模型的修改，生成迁移脚本。
4. -m：本次迁移做了哪些修改，用户可以指定这个参数，方便回顾。
5. upgrade：将指定版本的迁移文件映射到数据库中，会执行版本文件中的upgrade函数。如果有多个迁移脚本没有被映射到数据库中，那么会执行多个迁移脚本。
6. [head]：代表最新的迁移脚本的版本号。
7. downgrade：会执行指定版本的迁移文件中的downgrade函数。
8. heads：展示head指向的脚本文件版本号。
9. history：列出所有的迁移版本及其信息。
10. current：展示当前数据库中的版本号。

> 另外，在第一次执行的upgrade的时候，就会在数据库中创建一个alembic_version表，这个表只会有一条数据，记录当前数据库映射的是哪个版本的迁移文件

### 经典错误：

1. FAILED: Target database is not up to date.
    - 原因：主要是heads和current不相同。current落后于heads的版本。
    - 解决办法：将current移动到head上。alembic upgrade head
2. FAILED: Can't locate revision identified by '77525ee61b5b'
    - 原因：数据库中存的版本号不在迁移脚本文件中
    - 解决办法：删除数据库的alembic_version表中的数据，重新执行alembic upgrade head
3. 执行`upgrade head`时报某个表已经存在的错误：
    - 原因：执行这个命令的时候，会执行所有的迁移脚本，因为数据库中已经存在了这个表。然后迁移脚本中又包含了创建表的代码。
    - 解决办法：（1）删除versions中所有的迁移文件。（2）修改迁移脚本中创建表的代码。

```sh
# head
代表最新版本的迁移脚本的版本号

alembic upgrade Revision ID

把数据映射到数据库中
alembic upgrade head

# 查看Revision ID
alembic heads

# 查看当前版本号
alembic current

# 更新字段/添加字段
alembic revision --autogenerate -m "add country column"
# 执行
alembic upgrade head

# 删除字段
alembic revision --autogenerate -m "delete contry column"
alembic upgrade head

# 查看所有历史消息
alembic history

# 降级
将数据库降级到最初版本
alembic downgrade base
将数据库降级到执行版本，使用alembic downgrade+版本号
alembic downgrade <version>
```

## Flask-SQLAlchemy下alembic的配置

alembic是sqlalchemy的补充,可以独立于flask运行; 那么如何在Flask-SQLAlchemy库中使用alembic呢?

其实: 只需要修改`env.py`中的`target_metadata = myapp.db.Model.metadata`即可,其余同上一节.

- myapp.py

    ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    import config

    app = Flask(__name__)
    app.config.from_object(config)
    db = SQLAlchemy(app)

    # alembic revision --autogenerate -m "第一次提交"
    # alembic upgrade head

    # alembic revision --autogenerate -m "add age column"
    # alembic upgrade head
    class User(db.Model):
        __tablename__ = "user"
        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        username = db.Column(db.String(50),nullable=False)
        age = db.Column(db.Integer)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)
    ```

- config.py

    ```python
    HOSTNAME = "127.0.0.1"
    PORT = "3306"
    DATABASE = "alembic_demo"
    USERNAME = "root"
    PASSWORD = "123456"
    # dialect+dricer://username:password@host:port/database
    DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    ```

- env.py

    ```python
    ...
    import sys,os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import myapp
    ....
    target_metadata = myapp.db.Model.metadata
    ...
    ```

## Flask-Script插件(模块)

Flask-Script是Flask的插件; 类似于alembic可以在cmd命令行中运行, Flask-Script的作用: 可以通过命令行的形式来操作Flask。如: 通过命令跑一个开发版本的服务器/设置数据库/定时任务等

- 应用场景: 通过bash/cmd为网站后台添加管理员账号`python manage.py add_user -u yaro -p xxx`;

- 安装: `pip install flask-script`

### 命令的添加方式：

1. 使用`manage.commad`装饰符：这个方法是用来添加那些不需要传递参数的命令。示例代码如下：
    ```python
    from flask_script import Manager
    from myapp import app,BackendUser,db
    from db_script import db_manager

    # 使用Manager创建一个对象
    manager = Manager(app)

    @manager.command
    def greet():
        print("你好")

    if __name__ == '__main__':
        manager.run()
    # cmd执行命令:python manage.py greet
    ```
2. 使用`manage.option`装饰符：这个方法是用来添加那些需要传递参数的命令。有几个参数就需要写几个`option`。示例代码如下：
    ```python
    from flask_script import Manager
    from myapp import app,BackendUser,db
    from db_script import db_manager

    # 使用Manager创建一个对象
    manager = Manager(app)

    @manager.option("-u","--username",dest="username")
    @manager.option("-a","--age",dest="age")
    def add_user1(username,age):
        print("用户名:{},年龄:{}".format(username,age))

    @manager.option("-u","--username",dest="username")
    @manager.option("-e","--email",dest="email")
    def add_user2(username,email):
        user = BackendUser(username=username,email=email)
        db.session.add(user)
        db.session.commit()

    if __name__ == '__main__':
        manager.run()
    # cmd执行命令: python manage.py add_user1 -u angle -a 18
    ```

    > tips:可以有多个`@option`选项参数，命令即可使用-u，又可使用--username，dest指定用户输入命令时将值作为参数传给了函数中的username。

3. 创建command子类: 如果有一些命令是针对某个功能的。比如有一堆命令是针对ORM与表映射的，那么可以将这些命令单独放在一个文件中方便管理。也是使用`Manager`的对象来添加。然后到主manage文件中，通过`manager.add_command`来添加。示例代码如下：

    ```python
    from flask_script import Manager  ，Server
    from flask_script import Command  
    from debug import app  

    manager = Manager(app)  

    class Hello(Command):
        def run(self):
            print('测试')

    #自定义命令一/将类Hello()映射为hello
    manager.add_command('hello', Hello())

    #自定义命令二/启动命令
    manager.add_command("runserver", Server()) #命令是runserver
    if __name__ == '__main__':
        manager.run()
    ```

    ```python
    # db_script.py
    from flask_script import  Manager

    db_manager = Manager()

    @db_manager.command
    def init():
        print('迁移仓库创建完毕')

    @db_manager.command
    def revision():
        print("迁移脚本生成成功")

    @db_manager.command
    def upgrade():
        print("脚本映射到数据库成功")
    ```

    ```python
    # manage.py
    from flask_script import Manager
    from myapp import app,BackendUser,db
    from db_script import db_manager

    # 使用Manager创建一个对象
    manager = Manager(app)

    # 添加子命令
    # python manage.py db init
    manager.add_command("db",db_manager)

    if __name__ == '__main__':
        manager.run()
    ```

    cmd执行命令:`python manage.py db init`

    > tips:执行db_script.py下init函数; add_command()添加子类，将db_manager映射为db

## 项目结构重构

上面的项目不够专业: models太多的时候应该单独放在一个文件`models.py`, 但是`models.py`和`app.py`之间存在循环引用(前者需要后者的`db`, 后者需要前者的`User`), 为了解决循环引用需要引入第三方模块`exts.py`:

- exts.py

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

- models.py

```python
from exts import db
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
```
- config.py

```python
DB_USERNAME = 'root'
DB_PASSWORD = '123456'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'flask_migrate_demo'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
```
- app.py

```python
from flask import Flask
import config
from exts import db

app = Flask(__name__)
app.config.from_object(config)
# 获取app
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/profile/")
def profile():
    pass


if __name__ == '__main__':
    app.run()
```

## flask_migrate插件(模块)：

> 类似于 `flask-sqlalchemy`之于`sqlalchemy`; `flask_migrate`是`alembic`的封装,使用起来更方便. 而且`flask_migrate`的内部实现/使用参考了`flask_script`.

在实际的开发环境中，经常会发生数据库修改的行为。一般我们修改数据库不会直接手动的去修改，而是去修改ORM对应的模型，然后再把模型映射到数据库中。这时候如果有一个工具能专门做这种事情，就显得非常有用了，而flask-migrate就是做这个事情的。flask-migrate是基于Alembic进行的一个封装，并集成到Flask中，而所有的迁移操作其实都是Alembic做的，他能跟踪模型的变化，并将变化映射到数据库中。

- 安装：`pip install flask-migrate`

- 配置flask-migrate

    ```python
    # 在manage.py中的代码：
    from flask_script import Manager
    from zhiliao import app
    from exts import db
    from flask_migrate import Migrate,MigrateCommand

    manager = Manager(app)

    # 用来绑定app和db到flask_migrate的
    Migrate(app,db)
    # 添加Migrate的所有子命令到db下
    manager.add_command("db",MigrateCommand)

    if __name__ == '__main__':
        manager.run()
    ```

    ```python
    # models.py
    from exts import db

    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        username = db.Column(db.String(50),nullable=False)
        age = db.Column(db.Integer)
    ```

- flask_migrate常用命令：
    1. 使用init命令创建迁移仓库：`python manage.py db init`
    2. 使用migrate命令将模型映射到迁移脚本中：`python manage.py db migrate [-m "initial migratetion"]`
    3. 使用upgrade命令将迁移脚本映射到数据库：`python manage.py db downgrade version(上一个版本的版本号)`
    4. 更多命令：python manage.py db --help

    ```sh
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    # 添加新字段后重复2~3步骤
    # 回滚操作
    python manage.py db downgrade version
    # python manage.py db downgrade 289402d590c2
    ```

# 07 Flask知识点补充

## WTForms表单验证

Flask-WTF是简化了WTForms操作的一个第三方库，这个库一般有两个作用。第一个就是做表单验证，把用户提交上来的数据进行验证是否合法。第二个就是做模版渲染。当然还包括一些其他的功能:CSRF保护，文件上传等，安装Flask-WTF默认也会安装WTForms。

### 做表单验证：

- 基本使用
    1. 自定义一个表单类，继承自`wtforms.Form`类。
    2. 定义好需要验证的字段，字段的名字必须和模版中那些需要验证的input标签的name属性值保持一致。
    3. 在需要验证的字段上，需要指定好具体的数据类型。
    4. 在相关的字段上，指定验证器。
    5. 以后在视图中，就只需要使用这个表单类的对象，并且把需要验证的数据，也就是request.form传给这个表单类，以后调用form.validate()方法，如果返回True，那么代表用户输入的数据都是合法的，否则代表用户输入的数据是有问题的。如果验证失败了，那么可以通过form.errors来获取具体的错误信息。
    示例代码如下：

    源码：
    ```python
    # app.py
    from flask import Flask,request,render_template
    from wtforms import Form,StringField
    from wtforms.validators import Length,EqualTo

    # 继承Form
    class RegistForm(Form):
        # message指定错误信息
        username = StringField(validators=[Length(min=3,max=10,message="用户名长度必须在3到10位之间")])
        password = StringField(validators=[Length(min=6,max=10)])
        # EqualTo指定与之保持相同值的字段
        password_repeat = StringField(validators=[Length(min=6,max=10),EqualTo("password")])

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route("/regist/",methods=["GET","POST"])
    def regist():
        if request.method == "GET":
            return render_template("regist.html")
        else:
            form = RegistForm(request.form)
            if form.validate():
                return "success"
            else:
                # 打印失败原因
                print(form.errors)
                return "fail"

    if __name__ == '__main__':
        app.run(debug=True)
    ```

    ```html
    <!-- regist.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>注册表</title>
    </head>
    <body>
        <form method="POST">
            <table>
                <tbody>
                    <tr>
                        <td>用户名:</td>
                        <td><input type="text" name="username"/></td>
                    </tr>
                    <tr>
                        <td>密  码:</td>
                        <td><input type="text" name="password"/></td>
                    </tr>
                    <tr>
                        <td>确认密码:</td>
                        <td><input type="text" name="password_repeat"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="submit" value="立即注册"/></td>
                    </tr>
                </tbody>
            </table>

        </form>
    </body>
    </html>
    ```

- 常用的验证器：
    数据发送过来，经过表单验证，因此需要验证器来进行验证，以下对一些常用的内置验证器进行讲解：
    1. Email：验证上传的数据是否为邮箱。
    2. EqualTo：验证上传的数据是否和另外一个字段相等，常用的就是密码和确认密码两个字段是否相等。
    3. InputRequir：原始数据的需要验证。如果不是特殊情况，应该使用InputRequired。
    3. Length：长度限制，有min和max两个值进行限制。
    4. NumberRange：数字的区间，有min和max两个值限制，如果处在这两个数字之间则满足。
    5. Regexp：自定义正则表达式。
    6. URL：必须要是URL的形式。
    7. UUID：验证UUID。

    ```python
    # 验证邮箱
    email = StringField(validators=[Email()])
    # EqualTo指定与之保持相同值的字段
    password_repeat = StringField(validators=[Length(min=6,max=10),EqualTo("password")])
    # 验证用户是否输入
    username = StringField(validators=[input_required()])
    # Length:长度限制，有min和max两个值进行限制
    username = StringField(validators=[Length(min=3,max=10,message="用户名长度必须在3到10位之间")])
    # 验证范围
    age = IntegerField(validators=[NumberRange(12,18)])
    # 正则表达式
    phone = StringField(validators=[Regexp(r'1[34578]\d{9}')])
    # url验证
    home_page = StringField(validators=[URL()])
    # uuid值验证
    uuid = StringField(validators=[UUID()])
    ```

- 自定义验证器：
    如果想要对表单中的某个字段进行更细化的验证，那么可以针对这个字段进行单独的验证。步骤如下：
    1. 定义一个方法，方法的名字规则是：`validate_字段名(self,filed)`。
    2. 在方法中，使用`field.data`可以获取到这个字段的具体的值。
    3. 如果数据满足条件，那么可以什么都不做。如果验证失败，那么应该抛出一个`wtforms.validators.ValidationError`的异常，并且把验证失败的信息传到这个异常类中。
    示例代码：
    ```python
    class LoginForm(Form):
        .....
        # 1234
        captcha = StringField(validators=[Length(4,4)])

        # 自定义验证器
        # valiedate_name
        def validate_captcha(self,field):
            # print(type(field))
            # 字段数据值
            # print(field.data)
            if field.data != "1234":
                raise ValidationError("验证码错误")
    ```

### 使用WTForms渲染模版(有点鸡肋)

form还可以渲染模板,但有点鸡肋,平时开发不怎么使用.

创建一个SettingsForm类

```python
class SettingsForm(Form):
    username = StringField("用户名",validators=[InputRequired()])
    age = IntegerField("年龄",validators=[NumberRange(0,100)])
    remember = BooleanField("记住")
    tags = SelectField("标签",choices=[("1","python"),("2","java"),("3","c++")])
```

可以通过form对象调用一些方法，将表单写好

```python
# myapp.py
form = SettingsForm()
return render_template("settings.html",form=form)
```

```html
<!-- settings.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .username-input{
            background-color: red;
        }
    </style>
</head>
<body>
    <form action="" method="post">
        <table>
            <tbody>
                <tr>
                    <td>{{ form.username.label }}</td>
{#                    <td><input type="text" name="username"/></td>#}
                    <td>{{ form.username(class="username-input") }}</td>
                </tr>
                <tr>
                    <td>{{ form.age.label }}</td>
                    <td>{{ form.age() }}</td>
                </tr>
                <tr>
                    <td>{{ form.remember.label }}</td>
                    <td>{{ form.remember() }}</td>
                </tr>
                <tr>
                    <td>{{ form.tags.label }}</td>
                    <td>{{ form.tags() }}</td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="提交"/></td>
                </tr>
            </tbody>
        </table>
    </form>
</body>
</html>
```

## 文件上传

### 文件的上传及上传后的获取

1. 在模版中，form表单中，需要指定`encotype='multipart/form-data'`才能上传文件。
    ```html
    <form action="" method="post" enctype="multipart/form-data">
        <table>
            <tbody>
                <tr>
                    <td>头像:</td>
                    <td><input type="file" name="avatar"/></td>
                </tr>
                <tr>
                    <td>描述信息:</td>
                    <td><textarea name="desc"></textarea></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="提交"/></td>
                </tr>
            </tbody>
        </table>
    </form>
    ```
2. 在后台如果想要获取上传的文件，那么应该使用`request.files.get('avatar')`来获取。
    ```python
    # 获取文件
    avatar = request.files.get("avatar")
    ```
3. 保存文件之前，先要使用`werkzeug.utils.secure_filename`来对上传上来的文件名进行一个过滤。这样才能保证不会有安全问题。 
    ```python
    # 将文件名，包装一下，避免发生安全隐患
    filename = secure_filename(avatar.filename)
    ```
4. 获取到上传上来的文件后，使用`avatar.save(路径)`方法来保存文件。、
    ```python
    UPLOAD_PATH = os.path.join(os.path.dirname(__file__),"upload")
    avatar.save(os.path.join(UPLOAD_PATH,filename))
    ```
5. 从服务器上读取文件，应该定义一个url与视图函数，来获取指定的文件。在这个视图函数中，使用`send_from_directory(文件的目录,文件名)`来获取。
    ```python
    @app.route("/images/<filename>/")
    def get_images(filename):
        # send_from_directory(path,文件名)
        return send_from_directory(UPLOAD_PATH,filename)
    ```

示例代码如下：
```python
@app.route('/upload/',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # 获取描述信息
        desc = request.form.get("desc")
        avatar = request.files.get("avatar")
        filename = secure_filename(avatar.filename)
        avatar.save(os.path.join(UPLOAD_PATH,filename))
        print(desc)
        return '文件上传成功'

@app.route('/images/<filename>/')
def get_image(filename):
    return send_from_directory(UPLOAD_PATH,filename)
```

### 使用flask_wtf对上传文件使用表单验证

1. 定义表单的时候，对文件的字段，需要采用`FileField`这个类型。
2. 验证器应该从`flask_wtf.file`中导入。`flask_wtf.file.FileRequired`是用来验证文件上传是否为空。`flask_wtf.file.FileAllowed`用来验证上传的文件的后缀名。
3. 在视图文件中，使用`from werkzeug.datastructures import CombinedMultiDict`来把`request.form`与`request.files`来进行合并。再传给表单来验证。
    ```python
    form = UploadForm(CombinedMultiDict([request.form,request.files]))
    ```

示例代码如下：

```python
# upload.py
@app.route("/upload/",methods=["GET","POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        form = UploadFrom(CombinedMultiDict([request.form,request.files]))
        if form.validate():
        # 通过form.字段名.data来获取数据
            desc = form.desc.data
            avatar = form.avatar.data
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH,filename))
            print(os.path.join("\\".join(UPLOAD_PATH.split('/')),filename))
            return "文件上传成功"
        else:
            print(form.errors)
            return "fail"
```

```python
# forms.py
from wtforms import Form,FileField,StringField
from wtforms.validators import  InputRequired
# flask_wtf
from flask_wtf.file import FileAllowed,FileRequired

class UploadFrom(Form):
    # 使用Flask - WTF提供的FileRequired、FileAllowed验证函数
    avatar = FileField(validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    desc = StringField(validators=[InputRequired()])
```

## Cookie和Session

### 概述

- cookie：在网站中，http请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求是哪个用户。cookie的出现就是为了解决这个问题，第一次登录后服务器返回一些数据（cookie）给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个了。cookie存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过4KB。因此使用cookie只能存储一些小量的数据。
    1. cookie有有效期：服务器可以设置cookie的有效期，以后浏览器会自动的清除过期的cookie。
    2. cookie有域名的概念：只有访问同一个域名，才会把之前相同域名返回的cookie携带给服务器。也就是说，访问谷歌的时候，不会把百度的cookie发送给谷歌。

- session: session和cookie的作用有点类似，都是为了存储用户相关的信息。不同的是，cookie是存储在本地浏览器，而session存储在服务器。存储在服务器的数据会更加的安全，不容易被窃取。但存储在服务器也有一定的弊端，就是会占用服务器的资源，但现在服务器已经发展至今，一些session信息还是绰绰有余的。session是一个思路、一个概念、一个服务器存储授权信息的解决方案，不同的服务器，不同的框架，不同的语言有不同的实现。虽然实现不一样，但是他们的目的都是服务器为了方便存储数据的。session的出现，是为了解决cookie存储数据不安全的问题的。

- cookie和session结合使用：web开发发展至今，cookie和session的使用已经出现了一些非常成熟的方案。在如今的市场或者企业里，一般有两种存储方式：
    - session存储在服务端：服务器端可以采用mysql、redis、memcached等来存储session信息。原理是，客户端发送验证信息过来（比如用户名和密码），服务器验证成功后，把用户的相关信息存储到session中，然后随机生成一个唯一的session_id，再把这个session_id存储cookie中返回给浏览器。浏览器以后再请求我们服务器的时候，就会把这个session_id自动的发送给服务器，服务器再从cookie中提取session_id，然后从服务器的session容器中找到这个用户的相关信息。这样就可以达到安全识别用户的需求了。这种专业术语叫做server side session。
    - session存储到客户端: 原理是，客户端发送验证信息过来（比如用户名和密码）。服务器把相关的验证信息进行一个非常严格和安全的加密方式进行加密，然后再把这个加密后的信息存储到cookie，返回给浏览器。以后浏览器再请求服务器的时候，就会自动的把cookie发送给服务器，服务器拿到cookie后，就从cookie找到加密的那个session信息，然后也可以实现安全识别用户的需求了。这种专业术语叫做client side session。flask采用的就是这种方式，但是也可以替换成其他形式。



### flask操作cookie：

cookies：在Flask中操作cookie，是通过response对象来操作，可以在response返回之前，通过response.set_cookie来设置，这个方法有以下几个参数需要注意：

- key：设置的cookie的key。
- value：key对应的value。
- max_age：改cookie的过期时间，如果不设置，则浏览器关闭后就会自动过期。
- expires：过期时间，应该是一个datetime类型。
- domain：该cookie在哪个域名中有效。一般设置子域名，比如cms.example.com。
- path：该cookie在哪个路径下有效。
- secure设置为True只能在HTTPS协议下使用
- httponly设置为Truecookie只能被浏览器读取，不能被js读取
    ```sh
    set_cookie(self, key, value='',max_age=None, expires=None,path='/', domain=None,
    secure=False, httponly=False,samesite=None)
    ```

1. 设置cookie：设置cookie是应该在Response的对象上设置。`flask.Response`对象有一个`set_cookie`方法，可以通过这个方法来设置`cookie`信息。
    ```python
    # response对象
    resp = Response("name")
    # 设置cookie值
    resp.set_cookie("name","value")
    ```

    在Chrome浏览器中查看cookie的方式：
    - 右键->检查->Network->重新加载页面->找到请求，然后查看Response Headers中的cookie
    - 点击url输入框左边的信息icon，然后找到相应的域名，再展开查看cookie。
    - 在Chrome的设置界面->高级设置->内容设置->所有cookie->找到当前域名下的cookie。 

2. 删除cookie：通过`Response.delete_cookie("key_name")`，指定cookie的key，就可以删除cookie了。
3. 设置cookie的有效期：
    - max_age：以秒为单位，距离现在多少秒后cookie会过期。
    - expires：为datetime类型。这个时间需要设置为格林尼治时间，也就是要距离北京少8个小时的时间。
    - 如果max_age和expires都设置了，那么这时候以max_age为标准。
    - max_age在IE8以下的浏览器是不支持的。expires虽然在新版的HTTP协议中是被废弃了，但是到目前为止，所有的浏览器都还是能够支持，所以如果想要兼容IE8以下的浏览器，那么应该使用expires，否则可以使用max_age。
    - 默认的过期时间：如果没有显示的指定过期时间，那么这个cookie将会在浏览器关闭后过期。

    ```python
    @app.route('/')
    def hello_world():
        # response对象
        resp = Response("name")
        # # 设置cookie值
        # max_age:距离多少秒后cookie值过期
        # resp.set_cookie("name","value",max_age=10)
        # expires = datetime(year=2018,month=7,day=14,hour=16,minute=29,second=0)
        # 使用expires参数，就必须使用格林尼治时间
        # 要相对北京时间少8个小时
        # expires = datetime(year=2018, month=7, day=14, hour=8, minute=29, second=0)
        # 设置距离多久
        # 在新版本的http协议中，expires参数视为废弃
        # 注意同时指定了expires参数和max_age参数，则使用max_age参数
        expires = datetime.now() + timedelta(seconds=1) - timedelta(hours=8)
        resp.set_cookie("name", "value", expires=expires)
        # 删除指定cookie
        # resp.delete_cookie("name")
        return resp
    # secure设置为True只能在HTTPS协议下使用
    # httponly设置为Truecookie只能被浏览器读取，不能被js读取
    # expires无效日期
    # max_age:以秒为单位，距离现在多久过期
    # set_cookie(self, key, value='',
    #            max_age=None, expires=None,
    #            path='/', domain=None,
    #            secure=False, httponly=False,
    #            samesite=None)
    ```

4. 设置cookie的有效域名：cookie默认是只能在主域名下使用。如果想要在子域名下使用，那么应该给`set_cookie`传递一个`domain='.hy.com'`，这样其他子域名才能访问到这个cookie信息。

    - 定义蓝图
        ```python
        cmsviews.py
        from flask import Blueprint
        cms = Blueprint("cms",name,subdomain="cms")
        @cms.route("/")
        def index():
            return "cms 首页"
        cookie.demo.py
        ....
        from cmsviews import cms
        ```
    - 注册蓝图
        ```python
        app.register_blueprint(cms)
        app.config["SERVER_NAME"] = "ty.com:5000"
        ....
        ```
    - 地址映射:在hosts文件中添加以下映射
        ```
        127.0.0.1 ty.com
        127.0.0.1 cms.ty.com
        ```
    - 设置set_cookie中的domain参数
        ```python
        resp = Response("name")
        resp.set_cookie("name", "value",domain=".ty.com")
        ```

### flask操作session：

1. 设置session：通过`flask.session`就可以操作session了。操作`session`就跟操作字典是一样的。`session['username']='zhiliao'`。
2. 获取session：也是类似字典，`session.get(key)`。
3. 删除session中的值：也是类似字典。可以有三种方式删除session中的值。
    - `session.pop(key)`。
    - `del session[key]`。
    - `session.clear()`：删除session中所有的值。
4. 设置session的有效期：如果没有设置session的有效期。那么默认就是浏览器关闭后过期。如果设置session.permanent=True，那么就会默认在31天后过期。如果不想在31天后过期，那么可以设置`app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hour=2)`在两个小时后过期。

- 注意，使用session需要配置SECRET_KEY
    ```python
    import os
    ...
    # os.unrandom(n):产生24位的随机数
    app.config["SECRET_KEY"] = os.urandom(24)
    ```

## CSRF攻击与防御

### CSRF攻击原理

- 概述: CSRF(Cross Site Request Forgery，跨站请求伪造)是一种网络的攻击方式，它在2007年曾被列为互联网20大安全隐患之一。其他安全隐患，比如SQL脚本注入，跨站域脚本攻击等在近年来已经逐渐为众人熟知，很多网站也都针对他们进行了防御。然而，对于大多数人来说，CSRF却依然是一个陌生的概念。即便是大名鼎鼎的Gmail，在2007年底也存在CSRF漏洞，从而被黑客攻击而使Gmail的用户造成巨大的损失

- 原理: 网站是通过cookie来实现登录功能的。而cookie只要存在浏览器中，那么浏览器在访问这个cookie的服务器的时候，就会自动的携带cookie信息到服务器上去。那么这时候就存在一个漏洞了，如果你访问了一个别有用心或病毒网站，这个网站可以在网页源代码中插入js代码，**这个js脚本会控制你的浏览器模拟你自动给某个服务器发送请求(比如ICBC的转账请求)**。那么因为在发送请求的时候，浏览器会自动的把cookie发送给对应的服务器，这时候响应的服务器(比如ICBC网站)，就不知道这个请求时是伪造的，就被欺骗过去了，从而达到在用户不知情的情况下，给某个服务器发送了一个请求(比如转账)。

### 实战项目-中国工商银行注册功能完成

```python
# ICBC.py
from flask import Flask,render_template,views,request
from forms import RegistForm
from exts import db
import config
from models import User

app = Flask(__name__)
# 初始化app
db.init_app(app)
# 导入配置
app.config.from_object(config)

# 首页
@app.route('/')
def index():
    return render_template("index.html")

# 注册模块
class RegistView(views.MethodView):

    # get请求
    def get(self):
        return render_template("regist.html")
    # post请求
    def post(self):
        # request.form:获取所有表单数据
        # 将表单数据传入RegistForm中进行验证数据是否输入正确
        form = RegistForm(request.form)
        # 如果验证成功则会通过validate()方法返回一个True，反之False
        if form.validate():
            # 通过form.字段名.data获取表单数据
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data
            # 创建user对象
            user = User(email=email,username=username,password=password,deposit=deposit)
            # 插入数据库中
            #-------------
            # 添加对象
            db.session.add(user)
            # 提交到数据库中
            db.session.commit()
            return "注册成功"
        else:
            # form.errors:验证失败错误的原因
            print(form.errors)
            return "注册失败"
# 通过类，进行添加url
app.add_url_rule("/regist/",view_func=RegistView.as_view("regist"))


if __name__ == '__main__':
    app.run(debug=True)
```

```python
# config.py
DB_URI = "mysql+pymysql://root:123456@localhost:3306/icbc?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
```

```python
# models.py
from exts import db

class User(db.Model):
    # 数据库表名
    __tablename__ = "user"
    # db.Column:字段
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    deposit = db.Column(db.Float(50),default=0)
```

```python
# manage.py

# 管理
from flask_script import Manager
from ICBC import app
from exts import db
# 迁移
# Migrate用来绑定app和db的
# MigrateCommand:迁移命令
from flask_migrate import MigrateCommand,Migrate
# 导入模型,便于执行迁移时，检测到模型
from models import User

# 创建一个实例化管理对象，具有app的功能
manager = Manager(app)

# 绑定
Migrate(app,db)
# 映射迁移命令:db
manager.add_command('db',MigrateCommand)
# 初始化仓库
# python manage.py db init
# 执行迁移
# python manage.py db migrate
# 把数据模型映射到数据库中
# python manage.py db upgrade

if __name__ == "__main__":
    manager.run()
```

```python
# exts.py

# 存储db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

```python
# forms.py

# 字段类型
from wtforms import Form,StringField,FloatField
# 验证
from wtforms.validators import Email,Length,EqualTo,InputRequired

class RegistForm(Form):
    # 验证是否是邮箱格式
    email = StringField(validators=[Email()])
    # 验证输入的长度是否达到3~20
    username = StringField(validators=[Length(3,20)])
    # 同上
    password = StringField(validators=[Length(6, 20)])
    # 验证是否和password字段的值一样
    password_repeat = StringField(validators=[EqualTo("password")])
    # 判断是否输入值
    deposit = FloatField(validators=[InputRequired()])
```

```html
<!-- regist.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>中国工商注册页面</title>
</head>
<body>
    <form action="" method="post">
        <table>
            <tbody>
                <tr>
                    <td>邮箱:</td>
                    <td><input type="emial" name="email"/></td>
                </tr>
                <tr>
                    <td>用户名:</td>
                    <td><input type="text" name="username"/></td>
                </tr>
                <tr>
                    <td>密码:</td>
                    <td><input type="password" name="password"/></td>
                </tr>
                <tr>
                    <td>重复密码:</td>
                    <td><input type="password" name="password_repeat"/></td>
                </tr>
                <tr>
                    <td>余额:</td>
                    <td><input type="text" name="deposit"/></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="立即注册"/></td>
                </tr>
            </tbody>
        </table>
    </form>
</body>
</html>
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>中国工商银行首页</title>
</head>
<body>
    <h1>欢迎来到中国工商银行</h1>
    <div>
        <ul>
            <li><a href="{{ url_for("regist") }}" >立即注册</a></li>
        </ul>
    </div>
</body>
</html>
```

### 实战项目-中国工商银行登录和转账实现

```python
# ICDB.py

from flask import Flask, render_template, views, request, session, redirect,url_for
from forms import RegistForm,LoginForm,TransferForm
from exts import db
import config
from models import User
from auth import login_required

app = Flask(__name__)
# 初始化app
db.init_app(app)
# 导入配置
app.config.from_object(config)

# 首页
@app.route('/')
def index():
    return render_template("index.html")

# 注册模块
class RegistView(views.MethodView):

    # get请求
    def get(self):
        return render_template("regist.html")
    # post请求
    def post(self):
        # request.form:获取所有表单数据
        # 将表单数据传入RegistForm中进行验证数据是否输入正确
        form = RegistForm(request.form)
        # 如果验证成功则会通过validate()方法返回一个True，反之False
        if form.validate():
            # 通过form.字段名.data获取表单数据
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data
            # 创建user对象
            user = User(email=email,username=username,password=password,deposit=deposit)
            # 插入数据库中
            #-------------
            # 添加对象
            db.session.add(user)
            # 提交到数据库中
            db.session.commit()
            return "注册成功"
        else:
            # form.errors:验证失败错误的原因
            print(form.errors)
            return "注册失败"
# 通过类，进行添加url
app.add_url_rule("/regist/",view_func=RegistView.as_view("regist"))

# 登录
class LoginView(views.MethodView):

    def get(self):
        return render_template("login.html")

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = User.query.filter(User.email==email,User.password==password).first()
            if user:
                session["user_id"] = user.id
                # return "登录成功"
                return redirect(url_for("index"))
            else:
                return "邮箱或密码错误!"
        else:
            return render_template("login.html")
app.add_url_rule(rule="/login/",view_func=LoginView.as_view("login"))

# 转账
class TransferView(views.MethodView):

    decorators = [login_required]

    def get(self):
        return render_template("transfer.html")

    def post(self):
        form = TransferForm(request.form)
        if form.validate():
            email = form.email.data
            money = float(form.money.data)
            user = User.query.filter(User.email==email).first()
            print(user.deposit)
            if user:
                # 从会话中读取用户id
                user_id = session.get("user_id")
            #     # 如果没登录就跳转登录页面
            #     if user_id is None:
            #         return redirect(url_for("login"))
            #     print(user_id)
                # User.query.get()以id进行查询
                myself = User.query.get(user_id)
                print(type(myself.deposit))
                if myself.deposit >= money:
                    user.deposit += money
                    myself.deposit -= money
                    db.session.commit()
                    return "转账成功"
                else:
                    return "余额不足"
            else:
                return "该用户不存在"
        else:
            return "数据填写不正确"
app.add_url_rule(rule="/transfer/",view_func=TransferView.as_view("transfer"))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- transfer.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>中国工商银行转账页面</title>
</head>
<body>
    <form action="" method="post">
        <table>
            <tbody>
                <tr>
                    <td>转到邮箱:</td>
                    <td><input type="text" name="email"/></td>
                </tr>
                <tr>
                    <td>转到金额:</td>
                    <td><input type="text" name="money"/></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="立即转账"/></td>
                </tr>
            </tbody>
        </table>
    </form>
</body>
</html>
```

```python
# forms.py

# 字段类型
from wtforms import Form,StringField,FloatField,IntegerField
# 验证
from wtforms.validators import Email,Length,EqualTo,InputRequired,NumberRange
# from models import User

class RegistForm(Form):
    # 验证是否是邮箱格式
    email = StringField(validators=[Email()])
    # 验证输入的长度是否达到3~20
    username = StringField(validators=[Length(3,20)])
    # 同上
    password = StringField(validators=[Length(6, 20)])
    # 验证是否和password字段的值一样
    password_repeat = StringField(validators=[EqualTo("password")])
    # 判断是否输入值
    deposit = FloatField(validators=[InputRequired()])

class LoginForm(Form):
    # 注意一定要Email填上括号
    email = StringField(validators=[Email()])
    password = StringField(validators=[Length(6,20)])

    # # 自定义验证器
    # def validate_password(self):
    #     pass

    # 验证等同于post请求里面的验证
    # def validate(self):
    #     # 调用父类
    #     result = super(LoginForm,self).validate()
    #     if not result:
    #         return False
    #     # 获取数据
    #     email = self.email.data
    #     password = self.password.data
    #     # 利用模型从数据库中过滤信息
    #     user = User.query.filter(User.email == email,User.password == password).first()
    #     if not user:
    #         self.email.errors.append("邮箱或密码错误")
    #         return False
    #     return True

class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[NumberRange(1,10000000)])
```

```html
<!-- login.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>中国工商银行登录界面</title>
</head>
<body>
    <form action="" method="post">
        <table>
            <tbody>
                <tr>
                    <td>邮箱:</td>
                    <td><input type="text" name="email"/></td>
                </tr>
                <tr>
                    <td>密码:</td>
                    <td><input type="password" name="password"/></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" valule="登录"/></td>
                </tr>
            </tbody>
        </table>
    </form>
</body>
</html>
```

```python
# auth.py

from functools import wraps
from flask import session
from flask import redirect,url_for

# 验证，防止跨越权限访问
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        user_id = session.get("user_id")
        if user_id:
            return func(*args,**kwargs)
        else:
            return redirect(url_for("login"))
    return wrapper
```

### 实战项目-病毒网站使用CSRF漏洞转账

```python
# stealer.py

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transfer/')
def transfer():
    return render_template('transfer.html')


if __name__ == '__main__':
    app.run(debug=True,port=5001)
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>病毒网站</title>
</head>
<body>
    <img src="http://cms-bucket.nosdn.127.net/312e057a25f148519dc02b40812c78fe20170510155251.gif" alt="" width="100%" height="100%">
<iframe width="0" height="0" src="{{ url_for("transfer") }}" frameborder="0">
</iframe>
</body>
</html>
```

```html
<!-- transfer.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
     <script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
</head>
<body>
    <form action="http://icbc.com:5000/transfer/" method="post" id="myform">
<table>
            <tbody>
                <tr>
{#                    <td>转到邮箱:</td>#}
                    <td><input type="hidden" name="email" value="stealer@qq.com"/></td>
                </tr>
                <tr>
{#                    <td>转到金额:</td>#}
                    <td><input type="hidden" name="money" value="1000"/></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="开始游戏"/></td>
                </tr>
            </tbody>
        </table>
    </form>
<script>
    $(function(){
        $("#myform").submit();
    });
</script>
</body>
</html>
```

### CSRF防御原理

ICBC网站在处理请求时做了两件事情:
- 返回form表单中添加了一个随机`csrf_token`字段;
- 同时在浏览器本地cookie中也添加的相同的`csrf_token`字段(可能和session一起加密, 所以本地cookie不一定能看到此字段)

服务器处理请求时,如果这两个`csrf_token`值不相同,则拒绝服务; 
> 实际上: 如果查看form表单的`csrf_token`值和服务端`session.get("csrf_token")`获取的cookie的`csrf_token`值并不一样; 二者之间还有一层加密/解密工序.

由于浏览器的限制,不允许JS跨站访问cookie, **即病毒网站无法通过JS访问ICBC网站的cookie信息**. 故病毒网站的伪造JS代码向ICBC服务器发送请求(表单)时无法携带正确的`csrf_token`字段.

CSRF攻击可以在受害者毫不知情的情况下以受害者名义伪造请求发送给受攻击站点，从而在并未授权的情况下执行在权限保护之下的操作。 ... 因此，可以通过验证Referer值来防御CSRF攻击。

### Flask中CSRF防御的方法与原理

```python
# ICBC.py

from flask_wtf import CSRFProtect
# 在cookie中添加crsf_token字段
CSRFProtect(app)

# 该字段可能和session一起加密, 所以本地cookie不一定能看到此字段
# 但服务端可以通过获取csrf_token字段
csrf_token = session.get("csrf_token")
```

```html
<!-- login.html -->

<!-- 在表单中添加 crsf_token 字段-->
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
```

### AJAX中处理CSRF攻击

- 方法一: 把`csrf_token`字段写在form表单中

    ```html
    <!-- login.html -->

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>中国工商银行登录界面</title>
        <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
        <script src="{{ url_for('static',filename='login.js') }}"></script>
    </head>
    <body>
        <form action="" method="post">
    {#        {{ form.csrf_token }}#}
            <input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
            <table>
                <tbody>
                    <tr>
                        <td>邮箱:</td>
                        <td><input type="text" name="email"/></td>
                    </tr>
                    <tr>
                        <td>密码:</td>
                        <td><input type="password" name="password"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="submit" valule="登录" id="submit"/></td>
                    </tr>
                </tbody>
            </table>
        </form>
    </body>
    </html>
    ```

    ```python
    # login.js

    $(function () {
        $('#submit').click(function (event) {
            // 阻止默认的提交表单的行为
            event.preventDefault();
            var email = $('input[name=email]').val();
            var password = $('input[name=password]').val();
            var csrf_token = $('input[name=csrf_token]').val()
            $.post({
                'url': '/login/',
                'data': {
                    'email': email,
                    'password': password,
                    'csrf_token':csrf_token
                },
                'success': function (data) {
                    console.log("成功");
                },
                'fail': function (error) {
                    console.log(error);
                }
            });
        });
    });
    ```

- 方法二: 把`csrf_token`字段写在meta中

    ```html
    <!-- login.html -->

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>中国工商银行登录界面</title>
        <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
        <script src="{{ url_for('static',filename='login.js') }}"></script>
        <meta name="csrf_token" content="{{ csrf_token() }}">
    </head>
    <body>
        <form action="" method="post">
            <table>
                <tbody>
                    <tr>
                        <td>邮箱:</td>
                        <td><input type="text" name="email"/></td>
                    </tr>
                    <tr>
                        <td>密码:</td>
                        <td><input type="password" name="password"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="submit" valule="登录" id="submit"/></td>
                    </tr>
                </tbody>
            </table>
        </form>
    </body>
    </html>
    ```

    ```python
    # login.js

    var csrf_token = $('meta[name=csrf_token]').attr('content');

        $.ajaxSetup({
            "beforeSend":function(xhr,settings){
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain){
                    xhr.setRequestHeader("X-CRSFToken",csrf_token)
                }
            }
        });
    ```

## Flask上下文

### 预热知识: Thread Local对象

- `from flask import request`之后,我们便可以通过全局变量(公用)`request`获取用户请求的相关数据, 但是如果是生产环境,多个用户同时访问,如何保证多个`request`不冲突呢?
![Snipaste_2019-03-02](https://i.loli.net/2019/03/02/5c79ef4643eea.png)

- 在'Flask'中，类似于'request'的对象，其实是绑定到了一个'werkzeug.local.Local'对象上。这样即使是同一个对象，那么在多个线程中都是隔离的，类似的对象还有'session'以及'g'对象; Thread Local:只要绑定在Local对象上的属性，在每个线程中都是独立隔离的

![Local对象](https://i.loli.net/2019/03/02/5c79efc73ab93.png)

```python
from threading import Thread
from werkzeug.local import Local
# 此Local 是 threading.local (线程Local对象)的进一步包装

local = Local()
local.request = '123'  
# 把request挂载到local上
# 只要绑定到Local对象上的属性, 每个线程都是隔离的

class MyThread(Thread):
    def run(self):
        local.request = 'abc'
        print('子线程',local.request)

mythread = MyThread()
mythread.start()
mythread.join()

print("主线程",local.request)

“”“
子线程 abc
主线程 123
“”“
# 此时的两个线程是隔离/独立的
```

### 应用(app)上下文和请求(request)上下文：

Flask项目中有两个上下文，一个是应用上下文（app），另外一个是请求上下文（request）。

- `应用上下文`和`请求上下文`都是分别存放到`LocalStack`的栈中:
    - 和应用app相关的操作就必须要用到`应用上下文`，比如通过`current_app.name`获取当前的这个`app`的名称。
    - 和请求相关的操作就必须用到请求上下文，比如使用`url_for`反转视图函数。

- **在视图函数中**，不用担心上下文的问题。因为视图函数是通过访问url的方式执行的，那么这种情况下，Flask底层就已经**自动**的帮我们把`请求上下文`和`应用上下文`都推入到了相应的栈中。

- 但是,**如果想要在视图函数外面执行相关的操作**，比如获取当前的app(`current_app`)，或者是反转rul(`url_for`)，那么就必须要**手动**推入相关的上下文：
    - 手动推入`app上下文`：
        ```python
        # 第一种方式：
        app_context = app.app_context()
        app_context.push()
        # 第二种方式：
        with app.app_context():
            print(current_app)
        ```
    - 手动推入`请求上下文`：推入请求上下文到栈中，会**首先判断有没有应用上下文，如果没有那么就会先推入应用上下文到栈中，然后再推入请求上下文到栈中**：
        ```python
        with app.test_request_context():
            print(url_for('my_list'))
        ```

- 为什么上下文需要放在栈中：

    - 应用上下文：Flask底层是基于werkzeug，werkzeug是可以包含多个app的，所以这时候用一个栈来保存。如果你在使用app1，那么app1应该是要在栈的顶部，如果用完了app1，那么app1应该从栈中删除。方便其他代码使用下面的app。
    - 如果在写测试代码，或者离线脚本的时候，我们有时候可能需要创建多个请求上下文，这时候就需要存放到一个栈中了。使用哪个请求上下文的时候，就把对应的请求上下文放到栈的顶部，用完了就要把这个请求上下文从栈中移除掉。

### 保存全局对象的`g对象`：

`g对象(global)`是在整个Flask应用运行期间都是可以使用的, 类似于JS中`window`对象。并且他也是跟request一样，是线程隔离的。这个对象是专门用来存储开发者自己定义的一些数据，方便在整个Flask程序中都可以使用。一般使用就是，将一些经常会用到的数据绑定到上面，以后就直接从g上面取就可以了，而不需要通过传参的形式，这样更加方便。

```python
from flask import Flask g
# global --> g

@app.route('/')
def index():
    username = request.args.get("username")
    g.username = username
    # 如此在整个Flask项目下都可以访问g.username
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

### 总结

Flask项目中有两个上下文，一个是应用上下文（app），另外一个是请求上下文（request）。

请求上下文request和应用上下文current_app都是一个全局变量。所有请求都共享的。Flask有特殊的机制可以保证每次请求的数据都是隔离的，即A请求所产生的数据不会影响到B请求。所以可以直接导入request对象，也不会被一些脏数据影响了，并且不需要在每个函数中使用request的时候传入request对象。

这两个上下文具体的实现方式和原理可以没必要详细了解。只要了解这两个上下文的四个属性就可以了：

- request：请求上下文上的对象。这个对象一般用来保存一些请求的变量。比如method、args、form等。
- session：请求上下文上的对象。这个对象一般用来保存一些会话信息。
- current_app：返回当前的app。
- g：应用上下文上的对象。处理请求时用作临时存储的对象。


## 常用钩子函数

钩子函数是指在执行函数和目标函数之间挂载的函数, 框架开发者给调用方提供一个point -挂载点, 至于挂载什么函数有我们调用方决定, 这样大大提高了灵活性

在Flask中钩子函数是`使用特定的装饰器装饰`的函数。为什么叫做钩子函数呢，是因为钩子函数可以在正常执行的代码中，插入一段自己想要执行的代码。那么这种函数就叫做钩子函数。（hook）

- `before_first_request`：处理第一次请求之前执行。例如以下代码：
    ```python
    @app.before_first_request
    def first_request():
        print 'first time request'
    ```
- `before_request`：在每次请求之前执行。通常可以用这个装饰器来给视图函数增加一些变量。例如以下代码：
    ```python
    @app.before_request
    def before_request():
        if not hasattr(g,'user'):
            setattr(g,'user','xxxx')
    ```
- `context_processor`：上下文处理器。这个钩子函数，必须返回一个字典。这个字典中的值在所有模版中都可以使用(每个视图函数的变量只能在对应的模板中使用`render_template`)。例如：
    ```python
    @app.context_processor
    return {'current_user':'xxx'}
    ```
- `errorhandler`：在发生一些异常的时候，比如404错误，比如500错误。那么如果想要优雅的处理这些错误，就可以使用`errorhandler`来出来。需要注意几点：
    - 在errorhandler装饰的钩子函数下，记得要返回相应的状态码。
    - 在errorhandler装饰的钩子函数中，必须要写一个参数，来接收错误的信息，如果没有参数，就会直接报错。
    - 使用`flask.abort`可以手动的抛出相应的错误，比如开发者在发现参数不正确的时候可以自己手动的抛出一个400错误。例如：
    ```python
    @app.errorhandler(404)
    def page_not_found(error):
        return 'This page does not exist',404
    ```
- `teardown_appcontext`：不管是否有异常，注册的函数都会在每次请求之后执行。
    ```python
    @app.teardown_appcontext
    def teardown(exc=None):
        if exc is None:
            db.session.commit()
        else:
            db.session.rollback()
        db.session.remove()
    ```
- `template_filter`：在使用Jinja2模板的时候自定义过滤器。比如可以增加一个`upper_filter`的过滤器（当然Jinja2已经存在这个过滤器，本示例只是为了演示作用）：
    ```python
    @app.template_filter
    def upper_filter(s):
        return s.upper()
    ```

## 信号

> 背景: 打仗,烽火台,狼烟 -> (定义)商量好狼烟个数与人数的关系... -> 后线监听哨兵负责查看远处烽火台是否有狼烟 -> 前线哨兵负责发送狼烟信号.

### 自定义信号

使用信号分为3步，第一是定义一个信号，第二是监听一个信号，第三是发送一个信号。以下将对这三步进行讲解：

1. 定义信号：定义信号需要使用到blinker这个包(`pip install blinker`)的Namespace类来创建一个命名空间。比如定义一个在访问了某个视图函数的时候的信号。示例代码如下：
    ```python
    # Namespace的作用：为了防止多人开发的时候，信号名字冲突的问题
    from blinker import Namespace

    mysignal = Namespace()
    visit_signal = mysignal.signal('fire')
    ```
2. 监听信号：监听信号使用singal对象的connect方法，在这个方法中需要传递一个函数，用来接收以后监听到这个信号该做的事情。示例代码如下：
    ```python
    def call_back(sender):
        print(sender)  # 发送者, 默认为None
        print('敌人来了')
    mysignal.connect(call_back)  # 监听, 监听到信号后,触发回调函数
    ```
3. 发送信号：发送信号使用singal对象的send方法，这个方法可以传递一些其他参数过去。示例代码如下：
    ```python
    mysignal.send('sender_name')  # 指定发送者发送信号
    ```

```python
from flask import Flask
from blinker import Namespace

# Namespace 命名空间
# 1.定义信号
namespace = Namespace()
fire_signal = namespace.signal('fire')

# 2.监听信号
def fire_test(sender):
    print(sender)
    print("start fire")
fire_signal.connect(fire_test)

# 3. 发送一个信号
fire_signal.send()
```

### 案例: 通过自定义信号记录日志

定义/监听一个用户登陆的信号 -> 用户登陆后, 就发送这个信号 -> 监听到这个信号后,触发回调函数,把用户的相关信息保存成日志.

> 通过访问的URL判断是否登陆: URL的查询字符串中如果含有`username`字段(http://www.xxx.com?username=yyy),则表示登陆成功.

```python
# signal_demo.py

from flask import Flask,request,render_template,g
from blinker import Namespace
from signals import login_signal

# 定义一个登陆的信号，以后用户登录进来以后就发送一个登陆信号，然后能够监听这个信号,然后能够监听这个信号，在监听到这个信号以后，就记录当前这个用户登录的信息，用信号的方式，记录用户的登录信息

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    username = request.args.get('username')  # http://www.xxx.com?username=yyy
    if username:
        g.username = username  # 全局化变量
        # 3. 发送信号
        login_signal.send()
        return '登录成功'
    else:
        return '请输入用户名'

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# signals.py

from blinker import Namespace
from datetime import datetime
from flask import request, g

# 1. 定义信号
namespace = Namespace()
login_signal = namespace.signal('login')

def login_log(sender,username): # 定义监听信号的回调函数
    # print('用户登录')
    # 记录 用户名，登录时间，ip地址
    now = datetime.now()  # 获取当前时间
    ip = request.remote_addr  # 获取ip
    log = "登录日志:用户名:{},登录时间:{},ip地址:{}\n".format(g.username, now, ip)
    print(log)  # 调试信息
    # 写入日志文件
    with open('login_log.txt','a+',encoding='utf-8') as f:
        f.write(log)
# 2. 监听信号 -> 回调函数
login_signal.connect(login_log)
```

### Flask内置的信号

上一节我们自定义/监听信号, 然后手动触发信号. 其实Flask内部预定义了若干信号, 并在特定的条件下发送信号, 我们只需要监听这些信号即可.

1. template_rendered：模版渲染完成后的信号。

    ```python
    from flask import Flask,request,g,template_rendered,render_template
    from blinker import Namespace

    app = Flask(__name__)

    def template_rendered_func(sender,template,context):  # 定义回调函数(接受系统定义的三个参数)
        print('sender:',sender)
        print('template:',template)
        print('context:',context)
    template_rendered.connect(template_rendered_func)  # 监听信号 -> 模版渲染完毕执行回调函数

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)

    ```
2. before_render_template：模版渲染之前的信号。
3. request_started：模版开始渲染。
4. request_finished：模版渲染完成。
5. request_tearing_down：request对象被销毁的信号。
6. got_request_exception：视图函数发生异常的信号。一般可以监听这个信号，来记录网站异常信息。
7. appcontext_tearing_down：app上下文被销毁的信号。
8. appcontext_pushed：app上下文被推入到栈上的信号。
9. appcontext_popped：app上下文被推出栈中的信号
10. message_flashed：调用了Flask的`flashed`方法的信号。

## Flask-Restful

### Restful API规范介绍

网络应用程序，分为前端和后端两个部分。当前的发展趋势，就是前端设备层出不穷（手机、平板、桌面电脑、其他专用设备......）。因此，必须有一种统一的机制，方便不同的前端设备与后端进行通信。这导致API构架的流行，甚至出现"API First"的设计思想。RESTful API是目前比较成熟的一套互联网应用程序的API设计理论,使用这个规范可以让前后端开发变得更加轻松。

- 协议:采用http或https协议
- 域名:
    - 应该尽量将API部署在专用域名之下:`https://api.example.com`
    - 如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下:`https://example.org/api/`
- 版本: 
    - 应该将API的版本号放入URL:`https://api.example.com/v1/`
    - 另一种做法是，将版本号放在HTTP头信息中，但不如放入URL方便和直观。Github采用这种做法。
- 数据传输格式:数据之间传输的格式应该都使用json，而不使用xml
- 路径:
    - 又称"终点"（endpoint）,即url链接中;在RESTful架构中，每个网址代表一种资源（resource）;
    - 所以网址中不能有动词，只能有名词，而且所用的名词往往与数据库的表格名对应;
    - 如果出现复数，那么应该在后面加s, 且往往都是复数;
    - 结尾不应该含有`/`, 如果有,应该使用301重定向;
    - 应该使用`-`提高url可读性, 而不是`_`;
    - 多数情况下应该使用小写, 而不是大写;

- HTTP请求的方法
    - GET:从服务器上获取资源
    - POST:在服务器上新创建一个资源
    - PUT:在服务器上更新资源。(客户端提供所有改变后的数据--user的所有信息:姓名/性别/年龄...)
    - PATCH:在服务器上更新资源。(客户端只提供需要改变的属性--user的需要改变的信息:如:年龄)
    - DELETE:从服务器上删除资源
    - 示例如下:
        - GET/users/:获取所有用户
        - POST/users/:新建一个用户
        - GET/users/id/:根据id获取一个用户
        - PUT/users/id/:更新某个id的用户的信息(需要提供用户的所有信息)
        - PATCH/users/id/:更新某个id的用户信息(只需要提供更改的信息)
        - DELETE/users/id/:删除一个用户
    > 虽然常用的有这5个方法,但是很多公司实际中只采用GET/POST,更新/删除数据都用POST实现,这样虽然没有符合Restful规范, 但是更简单.
- 过滤信息
    - 如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。
        ```
        ?limit=10：指定返回记录的数量
        ?offset=10：指定返回记录的开始位置。
        ?page=2&per_page=100：指定第几页，以及每页的记录数。
        ?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
        ?animal_type_id=1：指定筛选条件
        ```
    - 参数的设计应允许存在冗余，即允许API路径和URL参数偶尔有重复。比如，`GET /zoo/ID/animals` 与 `GET /animals?zoo_id=ID` 的含义是相同的。
- 状态码:
    - 200	ok	服务器成功响应客户端的请求
    - 400	INVALID REQUEST	用户发出的请求有误，服务器没有进行新建或修改数据的操作
    - 401	Unauthorized	用户没有权限访问这个请求
    - 403	Forbidden	因为某些原因禁止访问这个请求
    - 404	NOT FOUND	用户发送的请求的url不存在
    - 406	NOT Acceptable	用户请求不被服务器接收(比如服务器期望客户端发送某个字段，但是没有发送)
    - 500	Internal server error	服务器内部错误，比如出现了bug
- 错误处理: 如果状态码是4xx，就应该向用户返回出错信息。一般来说，返回的信息中将error作为键名，出错信息作为键值即可。
    ```json
    {
        error: "Invalid API key"
    }
    ```
- 返回结果: 针对不同操作，服务器向用户返回的结果应该符合以下规范:
    ```
    GET /collection：返回资源对象的列表（数组）
    GET /collection/resource：返回单个资源对象
    POST /collection：返回新生成的资源对象
    PUT /collection/resource：返回完整的资源对象
    PATCH /collection/resource：返回完整的资源对象
    DELETE /collection/resource：返回一个空文档
    ```
- Format:只用以下常见的3种body format：
    - Content-Type: application/json
        ```
        POST /v1/animal HTTP/1.1
        Host: api.example.org
        Accept: application/json
        Content-Type: application/json
        Content-Length: 24

        {   
            "name": "Gir",
            "animalType": "12"
        }
        ```
    - Content-Type: application/x-www-form-urlencoded (浏览器POST表单用的格式)
        ```
        POST /login HTTP/1.1
        Host: example.com
        Content-Length: 31
        Accept: text/html
        Content-Type: application/x-www-form-urlencoded

        username=root&password=Zion0101
        ```
    - Content-Type: multipart/form-data; boundary=—-RANDOM_jDMUxq4Ot5 (表单有文件上传时的格式)

### Flask-Restful基本使用

Flask实现Restful可以使用自带的`jsonify`, 当然使用`Flask-Restful`插件更便捷;

安装: `pip install flask-restful`(需要Flask 0.8+)

基本使用步骤:
1. 从`flask_restful`中导入`Api`，来创建一个`api`对象。
2. 写一个视图函数，让他继承自`Resource`，然后在这个里面，使用你想要的请求方式来定义相应的方法，比如你想要将这个视图只能采用`post`请求，那么就定义一个`post`方法。
3. 使用`api.add_resource`来添加视图与`url`。


```python
from flask import Flask,render_template,url_for
from flask_restful import Api,Resource

app = Flask(__name__)
# 用Api来绑定app
api = Api(app)

# 可以直接返回Json数据
class IndexView(Resource):
    def get(self,username=None):
        return {"username":"angle"}

# 可以指定多个url
api.add_resource(IndexView,'/index/<username>/','/regist/',endpoint='index')

with app.test_request_context():
    print(url_for('index',username='angle'))

if __name__ == '__main__':
    app.run(debug=True)
```

> **注意事项:**
> 如果你想返回json数据，那么就使用flask_restful，如果你是想渲染模版，那么还是采用之前的方式，就是`app.route`的方式。
> endpoint是用来给url_for反转url的时候指定的。如果不写endpoint，那么将会使用视图的名字的小写作为endpoint。
> add_resource的第二个参数是访问这个视图函数的url，这个url可以跟之前的route一样，可以传递参数，并且还有一点不同的是，这个方法可以传递多个url来指定这个视图函数

### Flask-Restful参数验证：

Flask-Restful插件提供了类似WTForms来验证提交的数据(`POST请求...`)是否合法的包，叫做reqparse。以下是基本用法：

```python
parser = reqparse.RequestParser()
parser.add_argument('username',type=str,help='请输入用户名')
args = parser.parse_args()
```

add_argument可以指定这个字段的名字，这个字段的数据类型等。以下将对这个方法的一些参数做详细讲解： 
1. `default`：默认值，如果这个参数没有值，那么将使用这个参数指定的值。 
2. `required`：是否必须。默认为False，如果设置为True，那么这个参数就必须提交上来。
3. `type`：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。
4. `choices`：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。
5. `help`：错误信息。如果验证失败后，将会使用这个参数指定的值作为错误信息。 
6. `trim`：是否要去掉前后的空格。

其中的type，可以使用python自带的一些数据类型，也可以使用`flask_restful.inputs`下的一些特定的数据类型来强制转换。比如一些常用的： 
1. `url`：会判断这个参数的值是否是一个url，如果不是，那么就会抛出help参数里面的异常信息。 
2. `regex`：正则表达式。 
3. `date`：将这个字符串转换为datetime.date数据类型。如果转换不成功，则会抛出一个异常。

```python
from flask import Flask,render_template,url_for
from flask_restful import Api,Resource,reqparse,inputs

app = Flask(__name__)
# 用Api来绑定app
api = Api(app)

# Json数据
class LoginView(Resource):
    def post(self):
        # username
        # password
        parser = reqparse.RequestParser()
        parser.add_argument('birthday', type=inputs, help='生日字段验证')
        # # 验证日期
        # parser.add_argument('birthday',type=inputs.date,help='生日字段验证')
        # # 利用正则表达式验证手机号码
        # parser.add_argument('telphone',type=inputs.regex(r'1[3578]\d{9}'))
        # # 验证输入的url地址
        # parser.add_argument('home_page',type=inputs.url,help='个人中心链接验证错误')
        # parser.add_argument('username',type=str,help='用户名验证错误',default="angle")
        # parser.add_argument('password',type=str,help=u'密码验证错误',required=True,trim=True)
        # parser.add_argument('password',type=int,help=u'年龄验证错误')
        # parser.add_argument('gender',type=str,choices=['male','female','secret'],help="性别验证错误")
        args = parser.parse_args()
        print(args)
        return {"username":'angle'}
api.add_resource(LoginView,'/login/')

# with app.test_request_context():
#     print(url_for('index',username='angle'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Flask-restful返回值的规范化

对于一个视图函数，你可以指定好一些字段用于返回。以后使用ORM模型或者自定义的模型的时候，他会自动的获取模型中的相应的字段，生成json数据，然后再返回给客户端。这其中需要导入flask_restful.marshal_with装饰器。并且需要写一个字典，来指示需要返回的字段，以及该字段的数据类型。示例代码如下：

```python
from flask import Flask
import config
from flask_restful import Api,Resource,fields,marshal_with

app = Flask(__name__)
app.config.from_object(config)
api = Api(app)

# 传统方式1: 直接返回字典/JSON数据=========
class ArticleView(Resource):
    def get(self):
        return {"title":"xxx",'content':'xxx'}

# 方式2: 返回值的标准化: ==========
class ArticleView(Resource):
    # 可以渲染指定字段
    # 有了这个中间处理过程, 便可以从数据库中读取数据,处理后(如重命名字段)再返回
    resource_fields = {
        'title':fields.String,
        'content':fields.String,
    }

    # restful规范中要求，被定义的参数
    # 即使这个参数没有值，也应该返回，返回一个None回去
    @marshal_with(resource_fields)
    def get(self):
        return {"title":"xxx"}  # content会返回None

# 方式2: 可以返回模型(数据库): =======
class Article(object):
    def __init__(self,title,content):
        self.title = title
        self.content = content

article = Article(title='angle',content='angle')  # 实例化模型

class ArticleView(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return article  # 可以返回模型

# ==========================
api.add_resource(ArticleView,'/article/',endpoint='article')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
```

- 在get方法中，返回user的时候，flask_restful会自动的读取user模型(数据库)上的username以及age还有school属性。组装成一个json格式的字符串返回给客户端。

- 重命名属性：很多时候你面向公众的属性名(for 网页)称是不同于内部的字段名(for 数据库)。使用 attribute可以配置这种映射。比如现在想要返回user.school中的值，但是在返回给外面的时候，想以education返回回去，那么可以这样写：
    ```python
    resource_fields = {
        'education': fields.String(attribute='school')
    }
    ```
- 默认值：在返回一些字段的时候，有时候可能没有值，那么这时候可以在指定fields的时候给定一个默认值，示例代码如下：
    ```python
    resource_fields = {
        'age': fields.Integer(default=18)
    }
    ```

- 复杂结构：有时候想要在返回的数据格式中，形成比较复杂的结构。那么可以使用一些特殊的字段来实现。比如要在一个字段中放置一个列表，那么可以使用fields.List，比如在一个字段下面又是一个字典，那么可以使用fields.Nested。以下将讲解下复杂结构的用法：

    ```python
    class ArticleView(Resource):

        resource_fields = {
            'aritlce_title':fields.String(attribute='title'),
            'content':fields.String,
            'author': fields.Nested({
                'username': fields.String,
                'email': fields.String
            }),
            'tags': fields.List(fields.Nested({
                'id': fields.Integer,
                'name': fields.String
            })),
            'read_count': fields.Integer(default=80)
        }

        @marshal_with(resource_fields)
        def get(self,article_id):
            article = Article.query.get(article_id)
            return article
    ```

```python
# app.py
from flask import Flask
import config
from flask_restful import Api,Resource,fields,marshal_with
from exts import db
from models import User,Tag,Article

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
api = Api(app)

class ArticleView(Resource):
    resource_fields = {
        # 更换字段名称
        '标题':fields.String(attribute='title'),
        'content':fields.String,
        # 设置默认值
        'age':fields.Integer(default=18),
        'author':fields.Nested({
            'username':fields.String,
            'email':fields.String,
        }),
        'tags':fields.List(fields.Nested({
            'id':fields.Integer,
            'name':fields.String,
        }))
    }
    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Article.query.get(article_id)
        return article
api.add_resource(ArticleView,'/article/<article_id>',endpoint='article')

@app.route('/')
def hello_world():
    user = User(username="angle",email='xxx@qq.com')
    article = Article(title='miku',content='miku')
    article.author = user
    tag1 = Tag(name='C/C++')
    tag2 = Tag(name='Python')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    print(user)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
```

```python
# models.py

from exts import db
# 用户
# 文章
# 关系:1对多
# 标签:多对多

# 文章-标签-中间表
article_tag_table = db.Table(
    'article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    # 定义外键
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    # 关系 一对多
    author = db.relationship("User",backref='articles')
    # 多对多
    tags = db.relationship("Tag",secondary=article_tag_table,backref='tags')

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
```

```python
# manage.py

from flask_script import Manager
from flask_restful_demo2 import app
from flask_migrate import MigrateCommand,Migrate
from exts import db
import models

manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
```

```python
# config.py

DB_USERNAME = 'root'
DB_PASSWORD = '123456'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'flask_restful_demo'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
```

```python
# exts.py

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

### Flask-Restful细节强化

- 在蓝图中，如果使用'flask-restful'，那么创建'Api'对象的时候，就不要再使用'app'了，而是使用蓝图.

    ```python
    article_bp = Blueprint('article',__name__,url_prefix='/article')
    api = Api(article_bp)
    ```
    
- 如果在'flask-restful'的视图中想要返回'html'代码或者是模板，那么就应该使用'api.representation'这个装饰器来定义一个函数，在这个函数中，应该对'html'代码进行一个封装，再返回.

    ```python
    @api.representation('text/html')
    def output_html(data,code,headers):
        print(data)
        # 在representation装饰的函数中，必须返回一个Response对象
        resp = make_response(data)
        return resp

    class ListView(Resource):
        def get(self):
            return render_template('index.html')
    api.add_resource(ListView,'/list/',endpoint='list')
    ```
