# HTTP相关知识

## GET请求

### 概述

- 定义: 
	- get请求: 向服务器传输请求数据,然后服务器解析该数据,查询数据库,把相关数据返回;
	- post请求: 把本地的数据传输到服务求,服务器解析该数据,并保存;
	- 注意; get/post都是上行数据(向服务器发数据), 只不过`目的分别是get和post`;
- 背景:
	- 以前的只是如何实现和用户交互,并获得数据呢?

        ```js
        //方式一: 在浏览器层面通过js互动
        prompt(“请输入你的年龄”);
        //方式二:通过表单,直接用js读取--也是浏览器页面(客户端)
        var age = ageTxt.value;
        // 以上两种方式都是在本地与用户进行交互的, 服务端如何交互呢?
        ```

- GET请求优缺点:
	- 优点: 便于分享
	- 缺点:
		- 暴露隐私 - 所有的表单字段的值都是通过URL来传输的,明码传输,能够通过浏览器的历史记录查看.
		- 传输的数据内容不能太大,你见过那么长的URL?所有GET请求限制数据大小.

### get请求

- 与服务器交互最简单的方式就是通过url中添加key=value的方式 -- 即get请求方式向服务器传输数据!
    - /http://www.iqianduan.cn/aa/a.html?k=v&k=v&k=v
    > - ? 后面的数据对于用户的访问没有意义;
    > - 主要是给后台语言看的,对前台无用.
- PHP(或其他后台语言)可以通过如下代码获取get请求发过来的数据

    ```php
    <?php
        print_r($_GET);//$_GET是 get请求问号后面的数据组成的数组
        //得到用户输入的年龄、性别

        $nianling = $_GET["nianling"];
        $xingbie = $_GET["xingbie"];
        if($xingbie == "男"){
            //...
        }else{
            //...
        }
    ?>
    ```

### 表单的get请求

- form表单有两个重要的属性
	- `method属性：提交表单的方法，是get还是post`。如果写了get的话，那么提交表单的时候，就会通过URL地址的？来传递参数。
	-  `action属性：处理表单的php程序/url`

        ```html
        <form method="get" action="hahahahah.php">
            <p>
                请输入你的姓名：
                <input type="text" name="xingming" />
            </p>
            <p>
                请输入你的qq号：
                <input type="text" name="qqhao" />
            </p>
            <p>
                请输入你的年龄：
                <input type="text" name="nianling" />
            </p>
            <p>
                <input type="submit" />
            </p>
        </form>
        ```

- get方法提交的表单，html页面就会自动把所有`具有name属性的表单控件`，里面的值用k=v&k=v……`(qqhao=xxx)`, 追加到action那个网址后面:hahahahah.php?qqhao=xxx&xingming=xxx&...

## POST请求

### 概述

- POST请求也可以让用户的数据传输到服务器上,但是不是通过url, 而是利用`HTTP request的报文头`.
	- get请求: 向服务器传输请求数据,然后服务器解析该数据,查询数据库,把相关数据返回;
	- post请求: 把本地的数据传输到服务求,服务器解析该数据,并保存;
	- 注意; get/post都是上行数据(向服务器发数据), 只不过`目的分别是get和post`;
- GET请求非常容易产生,我们每次输入网址打开网站都是一次GET请求; 但是POST请求一般需要借助表单才能产生.
- 背景:
  - 以前的只是如何实现和用户交互,并获得数据呢?

    ```js
    //方式一: 在浏览器层面通过js互动
    prompt(“请输入你的年龄”);
    //方式二:通过表单,直接用js读取--也是浏览器页面(客户端)
    var age = ageTxt.value;
    ```
  > 以上两种方式都是在本地与用户进行交互的, 服务端如何交互呢?
  > ```
  > 
  > ```

- POST请求优缺点:
	- 优点: 
		- 安全, 不会通过网址来暴露我们的表单内容;
		- 内容不限量, POST请求是可以无限量的,表单域填多少内容都可以.
	- 缺点:
		- 地址不可以分享, 很明显POST请求不影响URL;
- GET/POST的使用场景:鉴于二者的优缺点
	- GET请求通常用于提交请求数据,让服务器`检索数据库的某一个条目`;比如: news.php?id=4, 然后返回.
	- POST请求通常用于`提交表单的内容给服务器存储`.

### 表单发送POST请求

- 表单可以发送POST请求,数据通过请求头发送到服务器;
- 通过表单的method和action属性指定相关POST请求配置

```html
<form method="post" action="10_postchuli.php">
    <p>
        请输入你的姓名：
        <input type="text" name="xingming" />
    </p>
    <p>
        请输入你的qq号：
        <input type="text" name="qqhao" />
    </p>
    <p>
        请输入你的年龄：
        <input type="text" name="nianling" />
    </p>
    <p>
        <input type="submit" />
    </p>
</form>
```

### PHP后台处理

后台接收POST传输过来的数据,进行相关处理

```php
<?php
    $xingming = $_POST["xingming"];
    $qqhao = $_POST["qqhao"];
    $nianling = $_POST["nianling"];
    echo "我们已经妥收您的表单";
    echo $xingming.$qqhao.$nianling;
    //然后插入到数据库
?>
```

## PHP和JSON

- PHP(服务器)如果能够把数据库中的数据处理成JSON, 前端就可以通过AJAX读取到前台,用jS解析并渲染到DOM,实时/异步进行网页的更新.
- PHP中数组可以非常轻松的通过json_encode()来转为JSON：

    ```php
    $a = array("name" => "考拉" , "age" => 12 , "qqhao" => 134324);
    //$a现在就是json格式的字符串了
    ```

# Ajax相关

## Ajax概述

### Ajax简介

- Asynchronous JavaScript and XML （异步JavaScript和XML）
- 实际上现在工作没有一个公司使用XML当做后台、前台的中介文件，都是使用JSON。所以Ajax现在应该改名为Ajaj（Asynchronous JavaScript and JSON），但是大家还是约定俗成起名为Ajax。

### 历史

- AJAX 不是新的编程语言，而是一种原来被人放到角落里，突然被这个哥们推广，它是使用已有标准的新概念。
- 2005年由美国人Jesse James Garrett推广，并取名。神奇的是，这哥们并不是搞程序的，而是搞设计的，是交互设计大师、用户体验大师。甚至是个优秀建筑设计师。
- 在 2005 年，Google 通过其 Google Suggest 使 AJAX 变得流行起来。
- 在今天，很少有哪个网站不使用Ajax技术。
- Ajax技术对智能手机支持非常好。

### Ajax技术三个步骤

1. 带着数据头头上传到服务器(GET或POST, GET是通过URL地址后面的?, POST是通过报文头);
2. 传回JSON数据;
3. 组件DOM, 更新页面.

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzpnmzlnj0j20d607q0st.jpg)


## 基本使用详解

### 快速演示

> Ajax运行在服务器(http协议), 不能是FTP/FILE等协议.


```js
//Ajax的一个固定的模板：
//第1步创建一个xhr对象，使用new关键来调用一个内置构造函数
var xhr = new XMLHttpRequest();
//第2步指定接收回来的内容，怎么处理。监听xhr对象的onreadystatechange事件，这个事件在xhr对象的“就绪状态”改变的时候触发。我们只关心就绪状态为4的时候的事情。
xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
        //接收完文件要做的事情，让h1的内容变为读取的东西
        biaoti.innerHTML = xhr.responseText;
    }
}
//第3步创建一个请求，第一个参数是请求的类型get或者post，第二个参数就是请求的路径，第三个参数叫做是否使用异步机制
xhr.open("get", "a.txt", true);
//第4步发送请求，圆括号里面是请求头内容，get请求没有报文头写null
xhr.send(null);
```

### XHR对象

- 没啥好讲的，Ajax完全依赖XMLHttpRequest对象，字面意思就是“XML文件的HTTP请求”对象。大家一般把new出来的变量叫做xhr。
- 但是, IE6不兼容XMLHttpRequest;
- 高级浏览器是: `new XMLHttpRequest();`
- IE6是：`new ActiveXObject("Microsoft.XMLHTTP");`
- 能力检测/兼容处理：

    ```js
    var httpRequest;
    if (window.XMLHttpRequest) {
        httpRequest = new XMLHttpRequest()
    } else if (window.ActiveXObject) {
        httpRequest = new ActiveXObject()
    }
    ```

### open()方法

open()方法表示让xhr对象配置一个请求，open字面意思是打开，就是打开一个请求。open之后并没有真正的发送请求，send()方法才会正式发送请求.
- 第一个参数: 要么是'get',要么是post;
- 第二个参数:就是处理这个请求的php/java/python路径
- 第三个参数:true表示异步,false表示通过,没得选--只能是true(可以省略);
- 另外: JS中很多都是异步操作, 如: 读取文件, 读取数据库, setInterval(定时器),所有的事件监听, 其实Ajax也是事件监听(onreadystatechange事件). 

### send()方法

- send方法就是发送请求，里面的参数表示http requset报头里面携带内容。
- get请求报头里面没有内容，post请求有内容。
- get请求：`xhr.send(null);`
- post请求，写的也是类似于get请求的参数字符串：`xhr.send("name=kaola&age=18");`

### encodeURIComponent()

- 语法：`encodeURIComponent("我是一个文本");`
- 请求尽量不要有中文，如果要传输中文为了防止服务器上错乱，我们前端一般要进行encodeURIComponent处理。
- 据我所知，高级后台程序语言，都能够自动处理转译。
- get请求、post请求如果要用中文，一般要将中文转为URI标准字符。
- 世界上所有的文字都有URI编码，根据你的HTML页面的字符集不同，URI编码也不同。

### post请求必须setRequestHeader一下

- POST请求在服务器端比较难处理，需要用服务器写对应“流处理”程序。为什么？POST请求参数的尺寸可以无限大，所以post请求也是一段一段上去的。（node.js中我们将遇见这个datachuck）。
- 比如$_POST[] 接收会报错。
- 但是，如果是表单提交，那么PHP内置了相应处理程序。Ajax如果需要模拟表单提交，那么需要在send前设置：

```js
xhr.open("post","do2.php",true);
//如果用post发送请求，那么必须写一句话，模拟成form表单提交：
xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
xhr.send("xingming="+encodeURIComponent("考拉")+"&age=18");
```

### readystatechange事件

- xhr对象一旦开始open，就有了readyState属性，readyState属性一旦发生改变，就能够触发onreadystatechange事件。
- xhr对象的readyState属性的值有0、1、2、3、4，一共五个值：

    | Value | State            | Description                                                 |
    | ----- | ---------------- | ------------------------------------------------------------ |
    | 0     | UNSENT           | Client   has been created. open() not called yet.            |
    | 1     | OPENED           | open() has   been called.                                    |
    | 2     | HEADERS_RECEIVED | send() has   been called, and headers and status are available. |
    | 3     | LOADING          | Downloading; responseText holds   partial data.              |
    | 4     | DONE             | The   operation is complete.                                 |

From <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState> 

> - 0:  UNSENT                 open()还没有被调用
> - 1:  OPENED                    调用send()
> - 2:  HEADERS_RECEIVED     头部已经被服务器接收
> - 3:  LOADING                开始接收服务器的返回的东西，还没有接收完全
> - 4:  DONE                    完成
> - 工程上，我们只关心4这个状态。

- xhr.responseText就表示接收回来的文本。是一个string类型。

### HTTP状态码

- 每一次http请求，会根据请求是否成功，有不同的状态码。
- 常见状态码：
	- 200		ok，成功
	- 304 	not modified ，文件没有改变。浏览器会比对你请求的文件，和已经在缓存文件夹中的文件，如果相同，不再请求。这就是为啥第二次访问网站，速度更快的原因。
	- 404		not found	，没有找到文件
- [更多状态码](http://tool.oschina.net/commons?type=5)

### Ajax异步的细节：

1. 浏览器执行到Ajax代码这行语句，发出了一个HTTP请求，欲请求服务器上的数据a.txt。服务器的此时开始I/O，所谓的I/O就是磁盘读取，需要花一些时间，所以不会立即产生下行HTTP报文。
2. 由于Ajax是异步的，所以本地的JavaScript程序不会停止运行，页面不会假死，不会傻等下行HTTP报文的出现。后面的JavaScript语句将继续运行。进程不阻塞。
3. 服务器I/O结束，将下行HTTP报文发送到本地。此时，回调函数将执行。回调函数中，将使用DOM更改页面内容。

## Ajax函数封装

### api设计

```js
myajax.get(“check.php”, {“ xingming”: ”考拉”, ”age”: 18 }, function(err, data) {
  });

//唯一向外暴露的顶层变量
var myajax = window.myajax = {};
myajax.get = function() {}
myajax.post = function() {}
```

### 函数主体

```js
function ajax(method, url, body, doneFn) {
    var xhr = new XMLHttpRequest()
    method = method.toUpperCase()
    //参数为对象
    if (typeof body === 'object') {
        var tempArr = []
        for (var key in body) {
            tempArr.push(key + '=' + body[key])
            //tempArr => ['key1=value1','key2=value2']
            body = tempArr.join('&')
        }
    }
    //GET方式也可以接受body
    if (method === 'GET') {
        url += '?' + body
    }
    xhr.open(method, url)
    //如果是POST方式,设置请求头
    var data = null
    if (method === 'POST') {
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
        data = body
    }
    xhr.send(data)
    xhr.onreadystatechange = function() {
        if (this.readyState) return
        // return this.responseText 
        // 外部函数没有返回值; 
        // 如果外部函数var res = null, 内部改变, 会因为异步执行,res的结果一直是null
        //只能使用回调函数=>闭包的思维
        // JS --> 最核心的就是 回调函数 
        //异步编程中,回调用的很多
        //委托的思维->调用者使用/委托封装的函数处理某件事-->应该告诉它怎么处理返回的结果
        //封装的函数/方法处理完数据之后,不应该自己处理->接收一个函数告诉他怎么处理.
        //调用者在使用封装的函数时,应该直接如何处理结果(回调函数)
        doneFn(this.responseText)
    }
}
fn = function() {
    //pass
}
ajax('GET', 'time.php', 'id=1', fn)
ajax('GET', 'time.php', { 'id': 1 }, fn)
ajax('POST', 'add.php', 'key1=value1$key2=value2', fn)
ajax('POST', 'add.php', { 'key1': 'value1', 'key2': 'value2' }, fn)
```

## 表单序列化

- 表单中的每个控件，都有name属性，值却是千差万别的，radio、checkbox、select甚至需要迭代才能得到他们的值。不方便，并且用ajax提交表单的时候，要手工序列化。
- 你填的表单，最终要变为：`name=考拉&age=18&sex=男&hobby=篮球&hooby=足球`, 这个就叫做表单序列化。
- 经典面试题，写一个表单序列化函数。
- DOM提供了一个非常简单的一个属性，所有的表单元素都可以用elements来获得里面的所有控件。`var elems = biaodan.elements;`
- 元素的类型，input元素的type属性就是自己的type，而select的type属性是select-one, `elems[0].type`

```html
<body>
    <form id="biaodan">
        <p>
            请输入姓名：
            <input type="text" name="xingming" />
        </p>
        <p>
            请选择性别：
            <input type="radio" name="sex" value="男" /> 男
            <input type="radio" name="sex" value="女" /> 女
            <input type="radio" name="sex" value="保密" /> 保密
        </p>
        <p>
            请选择国籍：
            <input type="radio" name="nationality" value="中国" /> 中国
            <input type="radio" name="nationality" value="外国" /> 外国
        </p>
        <p>
            请选择你的爱好：
            <input type="checkbox" name="hobby" value="足球" /> 足球
            <input type="checkbox" name="hobby" value="篮球" /> 篮球
            <input type="checkbox" name="hobby" value="吃饭" /> 吃饭
            <input type="checkbox" name="hobby" value="睡觉" /> 睡觉
            <input type="checkbox" name="hobby" value="打豆豆" /> 打豆豆
        </p>
        <p>
            选择你的省份：
            <select name="hometown">
                <option value="北京">北京</option>
                <option value="上海">上海</option>
                <option value="东莞">东莞</option>
                <option value="广州">广州</option>
            </select>
        </p>
        <p>
            密码：
            <input type="password" name="password" />
        </p>
        <p>
            留言：
            <textarea name="message" id="" cols="30" rows="10"></textarea>
        </p>
        <p>
            <input type="button" value="点击提交" id="btn" />
        </p>
    </form>
    <script type="text/javascript" src="js/myajax.js"></script>
    <script type="text/javascript">
        var biaodan = document.getElementById("biaodan");
        var btn = document.getElementById("btn");
        btn.onclick = function() {
            //得到表单中的所有控件
            var elems = biaodan.elements;
            //结果数组
            var arr = [];
            //遍历所有的控件
            for (var i = 0; i < elems.length; i++) {
                //当前遍历的小元素
                var e = elems[i];
                //分类讨论：
                switch (e.type) {
                    //如果控件的类型是个按钮，那么没有任何返回值
                    case "button":
                    case "submit":
                    case "reset":
                        break;
                    case "text":
                    case "password":
                    case "textarea":
                        arr.push(e.name + "=" + e.value);
                        break;
                    case "radio":
                    case "checkbox":
                        e.checked && arr.push(e.name + "=" + e.value);
                        break;
                    case "select-one":
                        var options = e.getElementsByTagName("option");
                        console.log(options);
                        for (var j = 0; j < options.length; j++) {
                            if (options[j].selected) {
                                arr.push(e.name + "=" + options[j].value);
                            }
                        }
                        break;
                }
            }
            console.log(arr.join("&"));
        }
    </script>
</body>
```

## JSON字符串->对象

### 概述

- 对于前端开发工程师来说，主要的工作：
	1. 准确发出请求，之前讲的事情都是发请求
	2. 根据收到的JSON进行处理
- 从服务器接收到的东西，永远是string，无论它长得多么像JSON。
- 所以,第一步: 把JSON字符串转换为对象, 有如下三个方法;

### eval语句

- eval语句很神奇，能够识别字符串，并把字符串当做JS语句执行。
    先来说eval是什么：
    
    ```js
    var a = "alert(1+2+3)";
    eval(a);
    ```

- 一个字符串被eval之后，能够把字符串当做语句来执行。`eval语句一般用于奇淫技巧。`
 
- 现在回到Ajax，data是一个string，可以用eval转为json，需要注意的是，json先通过圆括号的拼接，变为表达式：

    ```js
    var json = eval("(" + data + ")");
    console.log(json);
    ```

### new Function()

- 语法: `new Function ([arg1[, arg2[, ...argN]],] functionBody)`
- 描述: 前面是参数, 最后一个是函数体, 二者都是字符串; 如果`只有functionBody`, 便可以把 `JSON字符串` 转换为 `JS的对象`;

    ```js
    var data = new Function("return " + data)();
    console.log(data);
    ```

### JSON.parse()内置函数

- JSON对象注意，不是一个构造函数，就是一个内置对象。这个对象有两个方法
- `JSON.parse`:  字符串 → JSON
- `JSON.stringify`： JSON → 字符串 

    ```js
    var obj = JSON.parse(data);
    alert(obj.result[0].name);
    ```

> Note: 
> - IE6、7不兼容
> - “老道”JSON作者帮我们写了一个shim。shim就是桌角垫，计算机世界中就是指本身没有这个功能，利用现有功能模拟一个这个功能。IE8、9、高级浏览器有内置JSON对象，而IE6、7没有，就可以用现有功能去模拟JSON对象。
https://github.com/douglascrockford/JSON-js


# jQuery中的Ajax

## 概述

- 原生的Ajax这套“佛经”要非常熟悉，面试的时候笔试都有可能。
var xhr = new XMLHttpRequest();    //不兼容，能力检测

```js
xhr.onreadystatechange = function(){
    if(xhr.readyState == 4){
        if(xhr.status >= 200 && xhr.status < 300 || xhr.status == 304){
            //正面的HTTP状态码
            alert(xhr.responseText);
        }
    }
}

xhr.open("post","check.php",true);
xhr.send("id=" + id + "&name=" + encodingURIComponent(name));
```
 
- jQuery很重要，千万不要被忽悠，有些机构就宣称jQuery臃肿，很多公司不用，胡扯！！小公司自己如果有框架，也是模拟jQuery，没有时间成本培训员工，所以jQuery已经是事实上的标准了，大家都会jQuery，所以就当做面试的要求，进入公司之后就不用培训框架了。
- 大公司装×，自己的库，比如kissy、tangram，API都和jQuery很像。
- 组件开发中，组件可以脱离运动框架，可以自己内部有小的运动函数，是个例外。通常情况下，一个jQuery压缩包只有90k，您一个图片都200k。
- 把精力放在业务上。

## `$.get()`方法

```js
// 方法一
$.get("a.json"  ,   {"id":1,"name":"考拉"}  ,  function(text){
    alert(typeof text);
});

// 方法二: jQuery中get方法还可以这样使用两个参数：
$.get("a.json?id=1&name=考拉"  , function(text){
	alert(typeof text);
});
```

jQuery默默的帮我们：
- encodingURIComponent中文了；
- 如果请求是404等错误状态，不会执行回调函数；
- jQuery识别传回来的东西像JSON，已经帮我们转JSON了，

## `$.post()`方法

```js
 $.post("a.json",{"id":1,"name":"考拉"},function(data){
    alert(typeof data);
    alert(data.content[2].id);
});
```

## `$.ajax()`方法

> $.get/$.post方法更便捷; $.ajax方法更底层,可定制化更高.

`ajax()方法`配置信息非常多，写在json里面进行配置：

```js
$.ajax("b.json",{
    //请求类型
    "type": "get",
    //传到服务器上的数据
    "data": {
        "name":"xiaoming",
        "age" :10
    },
    //成功做的事情
    "success" : function(data){
        alert(typeof data);
    },
    //错误做的事情
    "error": function(XMLHttpRequest, textStatus, errorThrown){
        alert(errorThrown);
    }
});
```

## `serialize()`方法

jQuery封装了表单序列化方法

```js
var str = $("#biaodan").serialize();
```

> 注意能够调用srialize的元素，一般来说一定是form标签。

# 缓存问题解决

## 概述

- Ajax缓存极其严重，如果两次get、post都是通往同一个URL的，并且携带的参数一样，即使服务器返回200的状态码，也会被当做304那样有缓存。这样就会表现出内容更改不及时，后台的文件已经更改了，但是前台由于有缓存就不会变化。
- 篮球比赛图文直播就是Ajax做的，你想想看如果有缓存，后台已经比赛进行到了10分钟了，你这里还在开球呢。

## 法一:随机数

- 只要更改参数，就不会有缓存！所以我们受此启发， 可以为我们的URL后面添加不影响页面使用的随机数。 

    ```js
    xhr.open("get","a.txt?z=" + Math.random(),true);
    ```

- 甚至可以不写k：

    ```js
    xhr.open("get","a.txt?" + Math.random(),true);
    ```
 
- jQuery中：

    ```js
    $.get(“a.txt”,{“z”:Math.random()},true);
    ```

## 法二:时间戳

- Date是系统内置的构造函数，new Date()就能产生一个日期时间对象，输出之后就是一个当前系统时间。
- Date.parse(日期时间对象)就能产生一个时间戳，是从1970年1月1日到现在这一时刻的毫秒数。 

    ```js
    xhr.open("get","a.txt?z=" + Date.parse(new Date()),true);
    ```

# 模板引擎-原理

> 通过js/jQuery读取的大量JSON数据, 需要配合模板引擎才能方便的渲染到DOM中.

- 拼接字符串很不爽，还容易出错。
- 所以就有工程师在大量的实践中，提出了模板引擎的概念，就是在一个完整的字符串中，把未定的量用特殊的语法(比如：`@xinqing@`)来表示。然后把数据替换这些标记，这个操作叫做数据绑定。

    ```js
    //模板
    var str = "好@xinqing@啊，我买了一个@dongxi@，花了@qian@元钱";
     
    //字典，数据
    var dictionary = {
        "xinqing" : "高兴",
        "dongxi" : "vivo手机",
        "qian" : 7000
    }
     
    //数据绑定
    str = str.replace(/\@([a-z]+)\@/g , function(match,$1,index,string){
        return dictionary[$1];
    });
     
    console.log(str);
    ```

- 模板一般都放在页面的`<script type=”text/template”><script>`标签对儿里面。
- 字典都是从Ajax读来的。

```js 
function compile(templateString , dictionary){
    return templateString.replace(/\@([a-z]+)\@/g , function(match,$1,index,string){
        return dictionary[$1];
    });
}
```

# underscore - 模板引擎的一种实现

## 概述

> - underscore提供了很多方便的函数, 更方便的实现函数式编程; lodash是underscore的升级版(功能更强, 性能更高), 二者都包含模板引擎;
> - 还有很多其他模板引擎: Handlebarsjs, Mustache, ejs, Jade等...

- underscore手册： http://www.css88.com/doc/underscore/#reduce
- 先回忆一下jQuery是干嘛的？jQuery解决了DOM开发中的问题，比如选择元素难、事件绑定不能批量、animate难的问题、浏览器兼容问题太多。jQuery是DOM编程界的霸主。jQuery离开DOM开发就是渣渣，比如用jQuery你不能开发canvas游戏，不能开发node.js。
- underscore不限制使用场景，我们canvas游戏真得靠它，node.js里面都能够用它。underscore封装了一堆实用函数，这些实用函数基本都是针对数组、对象、函数的。这些小功能，都不复杂，但是我们自己写挺麻烦的。所以就是屌人集合在了一起，叫做underscore。 

## 基本使用

- 熟练知道：

    ```js
    _.max();
    _.min();
    _.without();
    ```

- underscore中内置了一个模板引擎： 

    ```js
    //模板字符串
    var templateString = "好<%= xinqing %>啊，今天我买了<%= dongxi%>，花了<%=qian%>元";
     
    //通过模板字符串生成一个数据绑定函数
    var compile = _.template(templateString);
     
    //字典
    var dictionary = {
        "xinqing" : "高兴",
        "dongxi" : "vivo手机",
        "qian" : 7000
    }

    //调用数据绑定函数完成数据绑定，只需要传一个参数，就是字典。
    console.log( compile(dictionary) );
    ```
 
- 大量公司在把underscore当做事实上的标准。

# JSONP

## Ajax不能跨域

- Ajax不能跨域，比如您是www.baidu.com，您就不能请求www.163.com的文件。但您可以请求www.baidu.com/1.json、  ent.baidu.com/1.json。
- 同样的127.0.0.1 和 127.23.2.4 都是本地服务器(localhost)的地址,也属于跨域
- 这是因为安全原因，对于任何后台语言来说、服务器程序来说，所有的XHR类型的请求，如果来自其他的服务器，将不予应答。
- 浏览器也不予发送前往不同服务器的XHR类型请求。
- 无法用XMLHttpRequest对象请求其他服务器的内容。这个现象持续到了2008年。
- 2008年有一个天才、或者是疯子，发明了一个东西，震惊了全球。叫做JSONP。

## JSONP原理

- 我们平时引用jquery等库, 函数都是定义在外部, 引入后在内部调用;
- JSONP刚好反过来: `函数在内部定义, 然后在外部调用`(通过`script标签--可以跨域`);
- 外部文件中存放的是一个函数的调用，实参是我们需要的数据，一般来说是JSON：

    ```js
    fun({
        "result" : [
            {
                "name" : "小明",
                "age" : 12,
                "sex" : "男"
            },
            {
                "name" : "小红",
                "age" : 13,
                "sex" : "女"
            }
    ]
    });
    ```
- 绿色部分是JSON，外面的fun();是函数的调用，是`padding`补充部分。所以JSON+Padding： JSONP
 
- HTML文件中定义函数:

    ```js
    //定义函数
    function fun(obj){
        alert(obj.result[1].name);
    }
    ```

- 尤其是要注意，在HTML内部中一定要先定义函数，然后再引包。

## 点击按钮发送JSONP请求

按钮事件处理函数：

```js
//创建一个script标签，孤儿节点
var scriptObj = document.createElement("script");
//追加这个script节点
document.body.appendChild(scriptObj);
//一个script标签如果没有src属性，将什么都不做
//一个script标签如果一旦设置src属性，那么将立即发出HTTP请求。
scriptObj.src = "jsonp.txt";
//删除这个script节点
document.body.removeChild(scriptObj);
```

## jsonp实用轮子的封装

- jsonp的使用非常拧巴，要先定义函数，然后创建script标签，设置script标签的src属性发出请求。
- 所以拧巴，不是“正向编程”。
- 那么我们就要封装一个实用轮子，解决这个事情，最最重要的语句，就是在window中注册一个传进来的函数名字，函数的名字指向你传进来的回调函数。

```js
myajax.jsonp = function(URL,queryJSON,callbackname,callback){
    //在window对象上强行增加一个属性，这个属性就是全局变量，是一个函数的名字，值是一个函数
    window[callbackname] = callback;
    //创建节点
    var scriptObj = document.createElement("script");
    //添加节点
    document.body.appendChild(scriptObj);
    //拼接字符串
    var querystring = myajax._queryjson2querystring(queryJSON);
    //设置新创建的script标签的src属性，HTTP上行请求将发出
    scriptObj.src = querystring ? (URL + "?" + querystring) : URL;
    //删除这个script标签
    document.body.removeChild(scriptObj);
}
```

- 这样就能够正向编程：

    ```js
    myajax.jsonp(url,{},”kaola”,function(data){
    });
    ```

## jQuery中的JSONP

- jQuery用同样的原理帮我们实现了框架正向编程。创建script标签，添加src，注册系统的全局的函数名。

    ```js
    $.ajax({
        "dataType" : "jsonp",
        "url" : "www.163.com",    //jsonp的网址
        "jsonpCallback" : "haha",     //jsonp的网址是一句调用，所以这里要在window对象上注册一个函数，和jsonp那个调用同名。
        "success" : function(data){   //成功的回调函数
            console.log(data);
        }
    });
    ```

- JSONP如果没听懂，也必须懂两个事儿：
	1. 原理
	2.  jQuery实现
- 用什么(get、post、jsonp)要看服务器给你什么.

# PHP/Python偷数据(爬虫)

> 所谓偷数据就是爬虫;

- 经典Ajax面试题，如何实现跨域？标准答案：两个方法，
	- 第一个方法: 使用JSONP，要求服务器上是JSONP的形式，如果服务器上提供的不是JSONP而是JSON，不能用JSONP方法跨域；
	- 第二种方法: PHP偷数据，有的服务器进行的限制，也透不过来。
- 使用PHP中的一条函数，交租file_get_contents就能够将那个网址的HTML源代码原封不动的抄过来。

    ```php
    $a = file_get_contents("http://www.sohu.com");
    ```

- 偷数据是后台哥哥做的事情，我们只需要关心数据得到之后的JSON解析就行了。

# Ajax应用-瀑布流

## 概述

- 提到Ajax，首先想到瀑布流，永远拉不到底，图片一张一张列出来。
- 瀑布流是2011年出现的，北欧的一个设计师发明的。
 
- 瀑布流(waterfall)是一列一列的，列的宽度是固定的（定列宽瀑布流），每个列里面是小grid，每个grid都不一样高。为什么不一样高，因为里面的内容不一样高，图片不一样高。

## 算法

- 瀑布流的原理就是绝对定位，每个grid有不同的绝对定位的top、left值。
- 其中每个grid的top值，都是它上面的grid的height的累加。每个grid的left值，都是自己(序号%3)*270。
 
- 瀑布流实现有很多种算法：绝对定位、浮动。
- 绝对定位原理，有两大种小算法区别：

    ```
    1）   
    0  1  2
	3  4  5
	6  7  8
	9  10 11
	这种排序的方法，有一个非常大的毛病，就是一列可能有多个瘦子、矮子。让列非常难看，底部，高矮不齐。

    2）
    每个格格不一定往自己序号%3这个列插入，看哪个列目前最矮，插在哪里。
    ```

## 原理-案例代码

见百度网盘: `全部文件>others>编程-源文件>waterfall.zip`

# fetch()

- fetch是ES8中定稿的一个功能，是一个Ajax函数的升级版。天生可以跨域(需要设置跨域头)，不需要jQuery。
- fetch()函数的最大优点是天生封装了Promise对象的工厂函数,返回一个Promise对象，所以就可以结合then()、async、await轻松解决回调套回调的问题。
兼容性较差

```js
// fetch实现ajax
async function main(){
	//1.txt文件格式: {"key":"value1"} --json字符串
	var data1 = await fetch('./txt/1.txt').then(data=>data.json());
	var data2 = await fetch('./txt/2.txt').then(data=>data.json());
	var data3 = await fetch('./txt/3.txt').then(data=>data.json());
	console.log(data1);
	console.log(data2);
	console.log(data3);
}

main();
```
