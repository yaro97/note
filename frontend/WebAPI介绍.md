# WebAPI介绍

## 概述

- API概念
    API（Application Programming Interface,应用程序编程接口）是一些预先定义的函数，目的是提供应用程序与开发人员基于某软件或硬件得以访问一组例程的能力，而又无需访问源码，或理解内部工作机制的细节。
    - 任何开发语言都有自己的API
    - API的特征输入和输出(I/O)
    - API的使用方法(console.log())

- WebAPI概念
    - 浏览器提供的一套操作浏览器和页面元素的API(BOM和DOM)
    - 此处的Web API特指浏览器提供的API(一组方法)，Web API在后面的课程中有其它含义

- 常见浏览器提供的API
    [MDN-Web API](https://developer.mozilla.org/zh-CN/docs/Web/API)

- JS组成
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoh1m4kvgj20gw06pmx5.jpg)
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoh1tmj5pj209u08k0sx.jpg)
    - ECMAScript - JavaScript的核心 
    定义了javascript的语法规范
    JavaScript的核心，描述了语言的基本语法和数据类型，ECMAScript是一套标准，定义了一种语言的标准与具体实现无关
    - BOM - 浏览器对象模型
    一套操作浏览器功能的API
    通过BOM可以操作浏览器窗口，比如：弹出框、控制浏览器跳转、获取分辨率等
    - DOM - 文档对象模型
    一套操作页面元素的API
    DOM可以把HTML看做是文档树，通过DOM提供的API可以对树上的节点进行操作

## DOM

### 节点>元素

- 背景知识

    - 相关背景：
        - DOM（Document Object Model）是W3C组织推荐的处理可扩展标志语言的标准编程接口。在网页上，组织页面（或文档）的对象被组织在一个树形结构中，用来表示文档中对象的标准模型就称为DOM。
        - **DOM作用：操作页面内容。**
        - 文档：把一个html文件看成是一个文档，由于万物皆对象，so，把这个文档看成是一个对象；文档中**每个的tag都是一个元素，也可以看成对象**。同tag，元素也可以嵌套。
        - 同样，xml文档及里面的元素也可以看成是对象。**html侧重于展示数据；xml侧重于存储数据。**
    - DOM又称为文档树模型（**DOM树**）
        ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoh4wza4kj20di07e3yc.jpg)

- 节点>元素

    - 概述:
        - document对象是DOM的顶级对象.
        - window对象是BOM中的顶级对象.document也属于window,JS中的变量/函数/定时器都是window的属性.
        - DOM/BOM中一切对象.比如页面中的标签, 属性, 文本, 注释, 空格...
        - 节点对象(node)：**页面中的所有内容都是节点（包含:`标签+属性+文本+注释`等）,其中文本包括:`文字/换行/空格/回车`**...
        - 元素对象(element)：(标签=元素)页面中的`标签(tag)`。
        - `so,对元素的操作具有局限性,由于节点的概念更大,对节点的操作更具在灵活性`.
            ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoh79xh5mj20la0fh3z1.jpg)
    - 节点类型nodeType:
	    - 1代表 标签节点,
	    - 2代表 属性节点,
	    - 3代表 文本节点
    - 节点名称nodeName:
	    - 标签节点--大写的标签名字,
	    - 属性节点---小写的属性名字,
	    - 文本节点---#text
    - 节点的值nodeValue:
	    - 标签节点---null,
	    - 属性节点---属性的值,
	    - 文本节点---文本内容
	    ```js
        if (node.nodeType == 1 && node.nodeName == "P") {
            // ...
        }
        ```

### 节点获取/操作

- DOM常用操作(CRUD)
	1. 获取元素(定位);
	2. 操作元素(增加/删除/更改);
    3. 注册事件,添加时间处理函数;

- 获取元素/节点

1. 获取目标节点/元素
    > 特殊节点: `document.body/documentElement/title...`

    ```js
    //A.根据id获取元素(单个元素)
    var div = document.getElementById('main');
    console.log(div);

    //B.​根据标签名获取元素(伪数组)
    var divs = document.getElementsByTagName('div');
    for (var i = 0; i < divs.length; i++) {
    var div = divs[i];
    console.log(div);
    }

    //以下方法有兼容问题
    //C.根据类名获取元素(伪数组) 
    var mains = document.getElementsByClassName('main');
    for (var i = 0; i < mains.length; i++) {
    var main = mains[i];
    console.log(main);
    }

    //D.根据name获取元素(表单元素, 伪数组) 
    var inputs = document.getElementsByName('hobby');
    for (var i = 0; i < inputs.length; i++) {
    var input = inputs[i];
    console.log(input);
    }

    //E.根据CSS选择器获取单个元素(如果选择多个元素, 只返回第一个元素对象)
    document.querySelector();

    //F.根据CSS选择器获取多个元素(即使是一个对象,也返回伪数组)
    document.querySelectorAll();
    ```

2. (根据目标节点)获取周边节点
    - 节点层级属性 -- 相关节点/元素对象的获取
	    > `**记忆技巧**: 元素对象都含有Element, 除了children`.
        
        ```js
        console.log(ulObj.parentNode);//父节点
        console.log(ulObj.parentElement);//父元素
        console.log(ulObj.childNodes);//子节点
        console.log(ulObj.children);//子元素

        //以下IE8兼容有问题:不支持获取element的方法,
        // 获取node的方法,默认搜索节点,如果节点为空(换行等),会获取Element.
        console.log(ulObj.firstChild);//first子节点-最前面一个
        console.log(ulObj.firstElementChild);//first子元素-最前面一个
        console.log(ulObj.lastChild);//last子节点-最后面一个
        console.log(ulObj.lastElementChild);//last子元素-最后面一个
        console.log(ulObj.previousSibling);//pre子节点-前一个
        console.log(ulObj.previousElementSibling);//pre子元素-前一个
        console.log(ulObj.nextSibling);//next子节点-后一个
        console.log(ulObj.nextElementSibling);//next子元素-后一个
        ```
    
    - 获取第一个/最后一个子元素**兼容代码**:

        ```js
        //获取任意一个父级元素的第一个子级元素
        function getFirstElementChild(element) {
            if(element.firstElementChild){//true--->支持
                return element.firstElementChild;
            }else{
                var node=element.firstChild;//第一个节点
                while (node&&node.nodeType!=1){
                    node=node.nextSibling;
                }
                return node;
            }
        }
        //获取任意一个父级元素的最后一个子级元素
        function getLastElementChild(element) {
            if(element.lastElementChild){//true--->支持
                return element.lastElementChild;
            }else{
                var node=element.lastChild;//第一个节点
                while (node&&node.nodeType!=1){
                node=node.previousSibling;
                }
                return node;
            }
        }
        ```

- 操作节点
    - 操作内置属性(内置属性可以使用"`点`"运算读取/设置)
        1. 非表单元素属性:
            > href、title、id、src、alt、className属性

		    - 案例:点击按钮，显示图片 --  imgObj.src = "";
		    - 案例:点击按钮修改p标签内容：--  **成对tag，使用innerText 设置中间的内容**。
		    - 案例:点击按钮修改所有p标签内容 --遍历.
		2. 表单元素属性:
		    > value 用于大部分表单元素的内容获取(option除外)
		    > type 可以获取input标签的类型(输入框或复选框等)
		    > disabled 禁用属性
		    > checked 复选框选中属性
		    > selected 下拉菜单选中属性
		    > name,readonly 等

		    - 案例: 点击按钮修改所有文本框内容（除自己）,可以用innerText,但是建议用value,毕竟是表单
		    - 案例:点击按钮，修改按钮本身的属性(**this指代紧挨着方法前的对象**)

    - 操作自定义属性(**如 index =1,非系统自带属性,不能使用"点"运算读取/设置**)
        > 通过"`.`"方式添加/获取的自定义属性,**只是添加到DOM树的对象上,HTML元素并没有生效.**若想在HTML中生效,应该使用DOM对象内置的getAttribute/ setAttribute/removeAttribute 方法. 

        a. `getAttribute()` 获取标签行内属性;
		b. `setAttribute()` 设置标签行内属性;
		c. `removeAttribute()` 移除标签行内属性;
        > 注: 上述三个方法也可用于内置属性获取/设置/移除, 当然,"点"运算符更方便。

    - 操作标签的内容(innerHTML和innerText)
        1. 设置时:想要设置标签内容,使用innerHTML,想要设置文本内容,innerText或者textContent,或者innerHTML,推荐用innerHTML.
        2. 获取时:innerText可以获取标签中间的文本内容,但是标签中如果还有标签,那么最里面的标签的文本内容也能获取;innerHTML才是真正的获取标签中间的所有内容.
        3. 兼容:ie中不支持innerText,支持textContent.**兼容代码**如下:

            ```js
            //设置任意的标签中间的任意文本内容
            function setInnerText(element,text) {
                //判断浏览器是否支持这个属性
                if(element.textContent){//不支持
                    element.innerText=text;
                }else{//支持这个属性
                    element.textContent=text;
                }
            }
            //获取任意标签中间的文本内容
            function getInnerText(element) {
                if(element.textContent){
                    return element.innerText;
                }else{
                    return element.textContent;
                }
            }
            ```

    - 操作样式
        1. style方式设置样式:单个设置.

        ```js
        var box = document.getElementById('box');
        box.style.width = '100px';
        box.style.backgroundColor = 'red';
        ```

        2. className方式追加css类:批量在CSS中添加样式.

        ```js
        box.className= "clearFix";
        ```

    - 创建节点的三种方法:
        1. `document.write()` -- 覆盖原来的内容

        ```js
		document.write('新设置的内容<p>标签也可以生成</p>');
        ```

		2. `innerHTML`

        ```js
		var box = document.getElementById('box');
		box.innerHTML = '新内容<p>新标签</p>';
        ```

		3. `document.createElement()`

        ```js
		var div = document.createElement('div');
		document.body.appendChild(div);
        ```

		**性能问题**
		- innerHTML方法由于会对字符串进行解析，需要避免在循环内多次使用。
		- 可以借助字符串或数组的方式进行替换，再设置给innerHTML
		- 优化后与document.createElement性能相近

    - 追加/移除节点的方法
        1. `appendChild()` 追加到最后一个子元素的后面;

        ```js
		//创建元素的
		var pObj = document.createElement("p");
		//在p中添加内容(使用兼容代码)
		setInnnerText(pObj, "这是一个p");
		//把创建后的子元素追加到最后一个子元素后面
		my$("dv").appendChild(pObj);
        ```

		2. `insertBefore()` 插入指定元素的前面;

        ```js
		//把新的子元素插入到第一个子元素的前面
		my$("dv").insertBefore(obj, my$("dv").firstElementChild);
        ```

		3. `removeChild()` 删除第一个子元素,可以用while循环,删除所有子元素
		
        ```js
        my$("btn3").onclick = function () {
		        //点击按钮删除div中所有的子级元素
		        //判断父级元素中有没有第一个子元素
		        while (my$("dv").firstElementChild) {
		                my$("dv").removeChild(my$("dv").firstElementChild);
		        }
		};
        ```

		4. `replaceChild()`

        ```js
		//返回旧节点
		replacedNode = parentNode.replaceChild(newChild, oldChild);
        ```

### 事件

#### Event对象

- Event 对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。
- 事件通常与函数结合使用，函数不会在事件发生前被执行！

#### 注册事件

- 过程: **注册事件-->添加事件处理函数**
- 事件：发生在 HTML 元素上的事情,HTML事件可以是用户行为（例如鼠标或键盘事件），也可以是浏览器行为。
- 事件三要素:
	1. `事件源`: 被添加触发事件的元素
	2. `事件类型`: 事件的触发方式(例如鼠标点击或键盘点击)-多以on_开头(由于IE的历史传统),标准的名称没有on,
	3. `事件处理程序`: 事件触发后要执行的代码(函数形式)
- 注册事件的三种方式:
	1. `element.onclick=function () {};`
	2. `element.addEventListener(type,fnName,false);`
		- addEventListener中第三个参数是控制事件阶段的;
		- false指事件冒泡阶段,true为事件捕获阶段;
		- 一般默认都是冒泡阶段,很少用捕获阶段
	3. `element.attachEvent("on"+type,fnName);` ---  IE浏览器
        > 注意: 
        > - 方法2/3,可以为同一对象注册多个(相同的)事件,同时触发. 方法1如果为同一对象绑定多个相同事件(如 onclick),前面的会被覆盖.
        > - for循环中的应该使用命名处理函数,防止创建多个匿名函数,节约内存空间.
- 解绑事件的三种方式:
	> 注意: a.用什么方式注册事件,就用什么方式解绑事件. b.解除需要命名函数.
	1. `element.onclick=null;`
	2. `element.removeEventListener(type,fnName,false);`
	3. `element.detachEvent("onclick",fnName);`  ---  IE浏览器
- 注册/解绑事件兼容代码:
    ```js
    //绑定事件的兼容
    function addEventListener(element,type,fn) {
        if(element.addEventListener){
            element.addEventListener(type,fnName,false);
        }else if(element.attachEvent){
            element.attachEvent("on"+type,fnName);
        }else{
            element["on"+type]=fnName;
        }
    }
    //解绑事件的兼容
    //为任意的一个元素,解绑对应的事件
    function removeEventListener(element,type,fnName) {
        if(element.removeEventListener){
            element.removeEventListener(type,fnName,false);
        }else if(element.detachEvent){
            element.detachEvent("on"+type,fnName);
        }else{
            element["on"+type]=null;
        }
    }
    ```

#### 事件详解

- 事件的三个阶段
	1. 事件捕获阶段: 从外向内.
	2. 事件目标阶段: 最开始选择的那个元素.
	3. 事件冒泡阶段: 从内向外(如:onclick-点击内部的元素,外部的元素也会触发).
	> 注：事件对象.eventPhase属性可以查看事件触发时所处的阶段
- 事件处理函数的参数
	- 又称: 事件对象, 以参数的形式传递给事件处理函数;
	- 事件对象内保存了所有的事件相关的信息.

        ```js
        my$("dv3").onclick = function (event) {
            console.log(event);
            console.log(this.id);
        };
        ```

	- event参数具有很多属性,其中event.eventPhase指示当前事件的阶段,如果这个属性的值是:
        1---->捕获阶段
        2---->目标阶段
        3---->冒泡
	- 其他事件对象的属性和方法
		- `event.type` 获取事件类型(不带"on");
		- `event.clientX/clientY` 所有浏览器都支持，窗口位置;
		- `event.pageX/pageY` IE8以前不支持，页面位置;
		- `event.target || event.srcElement` 用于获取触发事件的元素;
		- `event.preventDefault()` 取消默认行为;
		- 案例 - 为同一个元素绑定多个不同的事件,指向相同的事件处理函数

	        ```js
            //为同一个元素绑定多个不同的事件,指向相同的事件处理函数
            my$("btn").onclick = f1;
            my$("btn").onmouseover = f1;
            my$("btn").onmouseout = f1;
            function f1(e) {
                switch (e.type) {
                    case "click":
                        alert("好帅哦");
                        break;
                    case "mouseover":
                        this.style.backgroundColor = "red";
                        break;
                    case "mouseout":
                        this.style.backgroundColor = "green";
                        break;
                }
            }
            ```

- 阻止事件的默认行为:`return false;`

    ```js
    <a href="http://www.baidu.com" id="ak">百度</a>
    document.getElementById("ak").onclick=function () {
            alert("嘎嘎");
            return false;
    };
    ```

- 阻止事件冒泡(传播):
    - 大部分时候,事件冒泡是有必要的,但是,有时候我们不需要事件冒泡,就需要阻止.

    ```js
    //window.event.cancelBubble=true;//IE特有的,谷歌支持,
    };

    my$("dv3").onclick = function (event) {
        console.log(this.id);
        //event.stopPropagation(); //火狐特有,谷歌支持,
        console.log(event);
    };
    //IE低版本 event.cancelBubble = true; 标准中已废弃
    ```

    - 阻止事件冒泡**兼容代码**:
    
    ```js
    //window.event ? window.event.cancelBubble = true : e.stopPropagation();
    function cancelBubble(e) {
        //如果提供了事件对象，则这是一个非IE浏览器 
        if (e && e.stopPropagation) {
            //因此它支持W3C的stopPropagation()方法 
            e.stopPropagation();
        } else {
            //否则，我们需要使用IE的方式来取消事件冒泡 
            window.event.cancelBubble = true;
        }
    }
    ```

#### 事件句柄(EventHandlers)

| 属性                                                         | 此事件发生在何时...                  |
| ------------------------------------------------------------ | ------------------------------------ |
| [onabort](http://www.w3school.com.cn/jsref/event_onabort.asp) | 图像的加载被中断。                   |
| [onblur](http://www.w3school.com.cn/jsref/event_onblur.asp)  | 元素失去焦点                         |
| [onchange](http://www.w3school.com.cn/jsref/event_onchange.asp) | 域的内容被改变。                     |
| [onclick](http://www.w3school.com.cn/jsref/event_onclick.asp) | 当用户点击某个对象时调用的事件句柄。 |
| [ondblclick](http://www.w3school.com.cn/jsref/event_ondblclick.asp) | 当用户双击某个对象时调用的事件句柄。 |
| [onerror](http://www.w3school.com.cn/jsref/event_onerror.asp) | 在加载文档或图像时发生错误。         |
| [onfocus](http://www.w3school.com.cn/jsref/event_onfocus.asp) | 元素获得焦点。                       |
| [onkeydown](http://www.w3school.com.cn/jsref/event_onkeydown.asp) | 某个键盘按键被按下。                 |
| [onkeypress](http://www.w3school.com.cn/jsref/event_onkeypress.asp) | 某个键盘按键被按下并松开。           |
| [onkeyup](http://www.w3school.com.cn/jsref/event_onkeyup.asp) | 某个键盘按键被松开。                 |
| [onload](http://www.w3school.com.cn/jsref/event_onload.asp)  | 一张页面或一幅图像完成加载。         |
| [onmousedown](http://www.w3school.com.cn/jsref/event_onmousedown.asp) | 鼠标按钮被按下。                     |
| [onmousemove](http://www.w3school.com.cn/jsref/event_onmousemove.asp) | 鼠标被移动。                         |
| [onmouseout](http://www.w3school.com.cn/jsref/event_onmouseout.asp) | 鼠标从某元素移开。                   |
| [onmouseover](http://www.w3school.com.cn/jsref/event_onmouseover.asp) | 鼠标移到某元素之上。                 |
| [onmouseup](http://www.w3school.com.cn/jsref/event_onmouseup.asp) | 鼠标按键被松开。                     |
| [onreset](http://www.w3school.com.cn/jsref/event_onreset.asp) | 重置按钮被点击。                     |
| [onresize](http://www.w3school.com.cn/jsref/event_onresize.asp) | 窗口或框架被重新调整大小。           |
| [onselect](http://www.w3school.com.cn/jsref/event_onselect.asp) | 文本被选中。                         |
| [onsubmit](http://www.w3school.com.cn/jsref/event_onsubmit.asp) | 确认按钮被点击。                     |
| [onunload](http://www.w3school.com.cn/jsref/event_onunload.asp) | 用户退出页面。                       |

#### 鼠标/键盘属性

| 属性                                                         | 描述                                         |
| ------------------------------------------------------------ | -------------------------------------------- |
| [altKey](http://www.w3school.com.cn/jsref/event_altkey.asp)  | 返回当事件被触发时，"ALT" 是否被按下。       |
| [button](http://www.w3school.com.cn/jsref/event_button.asp)  | 返回当事件被触发时，哪个鼠标按钮被点击。     |
| [clientX](http://www.w3school.com.cn/jsref/event_clientx.asp) | 返回当事件被触发时，鼠标指针的水平坐标。     |
| [clientY](http://www.w3school.com.cn/jsref/event_clienty.asp) | 返回当事件被触发时，鼠标指针的垂直坐标。     |
| [ctrlKey](http://www.w3school.com.cn/jsref/event_ctrlkey.asp) | 返回当事件被触发时，"CTRL" 键是否被按下。    |
| [metaKey](http://www.w3school.com.cn/jsref/event_metakey.asp) | 返回当事件被触发时，"meta" 键是否被按下。    |
| [relatedTarget](http://www.w3school.com.cn/jsref/event_relatedtarget.asp) | 返回与事件的目标节点相关的节点。             |
| [screenX](http://www.w3school.com.cn/jsref/event_screenx.asp) | 返回当某个事件被触发时，鼠标指针的水平坐标。 |
| [screenY](http://www.w3school.com.cn/jsref/event_screeny.asp) | 返回当某个事件被触发时，鼠标指针的垂直坐标。 |
| [shiftKey](http://www.w3school.com.cn/jsref/event_shiftkey.asp) | 返回当事件被触发时，"SHIFT" 键是否被按下。   |

#### IE属性

除了上面的鼠标/事件属性，IE 浏览器还支持下面的属性：

| 属性            | 描述                                                         |
| :-------------- | ------------------------------------------------------------ |
| cancelBubble    | 如果事件句柄想阻止事件传播到包容对象，必须把该属性设为 true。 |
| fromElement     | 对于 mouseover 和 mouseout 事件，fromElement 引用移出鼠标的元素。 |
| keyCode         | 对于 keypress 事件，该属性声明了被敲击的键生成的 Unicode 字符码。对于 keydown 和 keyup 事件，它指定了被敲击的键的虚拟键盘码。虚拟键盘码可能和使用的键盘的布局相关。 |
| offsetX,offsetY | 发生事件的地点在事件源元素的坐标系统中的   x 坐标和 y 坐标。 |
| returnValue     | 如果设置了该属性，它的值比事件句柄的返回值优先级高。把这个属性设置为 fasle，可以取消发生事件的源元素的默认动作。 |
| srcElement      | 对于生成事件的   Window 对象、Document 对象或 Element 对象的引用。 |
| toElement       | 对于 mouseover 和 mouseout 事件，该属性引用移入鼠标的元素。  |
| x,y             | 事件发生的位置的 x 坐标和 y 坐标，它们相对于用CSS动态定位的最内层包容元素。 |

#### 标准Event属性

下面列出了 2 级 DOM 事件标准定义的属性。

| 属性                                                         | 描述                                           |
| ------------------------------------------------------------ | ---------------------------------------------- |
| [bubbles](http://www.w3school.com.cn/jsref/event_bubbles.asp) | 返回布尔值，指示事件是否是起泡事件类型。       |
| [cancelable](http://www.w3school.com.cn/jsref/event_cancelable.asp) | 返回布尔值，指示事件是否可拥可取消的默认动作。 |
| [currentTarget](http://www.w3school.com.cn/jsref/event_currenttarget.asp) | 返回其事件监听器触发该事件的元素。             |
| [eventPhase](http://www.w3school.com.cn/jsref/event_eventphase.asp) | 返回事件传播的当前阶段。                       |
| [target](http://www.w3school.com.cn/jsref/event_target.asp)  | 返回触发此事件的元素（事件的目标节点）。       |
| [timeStamp](http://www.w3school.com.cn/jsref/event_timestamp.asp) | 返回事件生成的日期和时间。                     |
| [type](http://www.w3school.com.cn/jsref/event_type.asp)      | 返回当前   Event 对象表示的事件的名称。        |

#### 标准Event方法

下面列出了 2 级 DOM 事件标准定义的方法。IE 的事件模型不支持这些方法：

| 方法                                                         | 描述                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| [initEvent()](http://www.w3school.com.cn/jsref/event_initevent.asp) | 初始化新创建的   Event 对象的属性。      |
| [preventDefault()](http://www.w3school.com.cn/jsref/event_preventdefault.asp) | 通知浏览器不要执行与事件关联的默认动作。 |
| [stopPropagation()](http://www.w3school.com.cn/jsref/event_stoppropagation.asp) | 不再派发事件。                           |

### 案例

> 声明: 以下案例中的 my$(); 记得引入 common.js 文件

- 根据 节点名/类型 过滤节点

    ```js
    my$("btn").onclick = function () {
        //先获取div
        var dvObj = my$("dv");
        //获取里面所有的子节点
        var nodes = dvObj.childNodes;
        //循环遍历所有的子节点
        for (var i = 0; i < nodes.length; i++) {
            //判断这个子节点是不是p标签
            if (nodes[i].nodeType == 1 && nodes[i].nodeName == "P") {
                nodes[i].style.backgroundColor = "red";
            }
        }
    };
    ```

- 排他功能：点谁谁怀孕。

    ```js
    //获取所有的按钮,分别注册点击事件
    var btnObjs = document.getElementsByTagName("input");
    //循环遍历所有的按钮
    for (var i = 0; i < btnObjs.length; i++) {
        //为每个按钮都要注册点击事件
            btnObjs[i].onclick = function () {
            //把所有的按钮的value值设置为默认的值:没怀孕
            for (var j = 0; j < btnObjs.length; j++) {
                btnObjs[j].value = "没怀孕";
            }
            //当前被点击的按钮设置为:怀孕了
            this.value = "怀孕了";
        };
    }
    ```

- 美女相册(阻止事件默认行为).

    ```js
    //点击a标签,把a标签中的href的属性值给id为image的src属性
    //把a的title属性的值给id为des的p标签赋值
    //从ul中标签获取获取所有的a标签
    var aObjs=my$("imagegallery").getElementsByTagName("a");
    //循环遍历所有的a标签
    for(var i=0;i<aObjs.length;i++){
        //为每个a标签注册点击事件
        aObjs[i].onclick=function () {
            //为id为image的标签的src赋值
            my$("image").src=this.href;
            //为p标签赋值
            my$("des").innerText=this.title;
            
            //阻止超链接默认的跳转
            return false;
        };
    }
    ```

- 切换背景图片

    ```js
    var imgObjs=my$("mask").children;//获取的所有的子元素
    //循环遍历所有img,注册点击事件
    for(var i=0;i<imgObjs.length;i++){
        imgObjs[i].onclick=function () {
            document.body.style.backgroundImage="url("+this.src+")";
        };
    }
    ```

- 模拟搜索框onfocus, onblur

    ```js
    //注册获取焦点的事件
    my$("txt").onfocus = function () {
        //判断文本框的内容是不是默认的内容
        if (this.value == "请输入搜索内容") {
            this.value = ""; //清空文本框
            this.style.color = "black";
        }
    };
    //注册失去焦点的事件
    my$("txt").onblur = function () {
        if (this.value.length == 0) {
            this.value = "请输入搜索内容";
            this.style.color = "gray";
        }
    };
    ```

- Tab切换

    ```js
    //获取最外面的div
    var box = my$("box");
    //获取的是里面的第一个div
    var hd = box.getElementsByTagName("div")[0];
    //获取的是里面的第二个div
    var bd = box.getElementsByTagName("div")[1];
    //获取所有的li标签
    var list = bd.getElementsByTagName("li"); 
    //获取所有的span标签
    var spans = hd.getElementsByTagName("span");
    //循环遍历的方式,添加点击事件
    for (var i = 0; i < spans.length; i++) {
        //在点击之前就把索引保存在span标签中
        spans[i].setAttribute("index", i); 
        spans[i].onclick = function () {
            //第一件事,所有的span的类样式全部移除
            for (var j = 0; j < spans.length; j++) {
                spans[j].removeAttribute("class");
            }
            
            //第二件事,当前被点击的span应用类样式
            this.className = "current";
            //span被点击的时候获取存储的索引值
            //alert(this.getAttribute("index"));
            var num = this.getAttribute("index"); 
            //获取所有的li标签,每个li标签先全部隐藏
            for (var k = 0; k < list.length; k++) {
                list[k].removeAttribute("class");
            }
            //当前被点击的span对应的li标签显示
            list[num].className = "current";
        };
    }
    ```

- 点菜:全选/全不选

    ```js
    //获取全选的这个复选框
    var ckAll = my$("j_cbAll");
    //获取tbody中所有的小复选框
    var cks = my$("j_tb").getElementsByTagName("input");
    //点击全选的这个复选框,获取他当前的状态,然后设置tbody中所有复选框的状态
    ckAll.onclick = function () {
        //console.log(this.checked);
        for (var i = 0; i < cks.length; i++) {
            cks[i].checked = this.checked;
        }
    };
    //获取tbody中所有的复选框,分别注册点击事件
    for (var i = 0; i < cks.length; i++) {
        cks[i].onclick = function () {
            var flag = true; //默认都被选中了
            //判断是否所有的复选框都选中
            for (var j = 0; j < cks.length; j++) {
                if (!cks[j].checked) {
                //没选中就进来了
                flag = false;
                break;
                }
            }
            //全选的这个复选框的状态就是flag这个变量的值
            ckAll.checked = flag;
        };
    }
    ```

- 创建表格

    ```js
    var arr=[
        {name:"百度",href:"http://www.baidu.com"},
        {name:"谷歌",href:"http://www.google.com"},
        {name:"优酷",href:"http://www.youku.com"},
        {name:"土豆",href:"http://www.tudou.com"},
        {name:"快播",href:"http://www.kuaibo.com"},
        {name:"爱奇艺",href:"http://www.aiqiyi.com"}
    ];

    //点击按钮创建表格
    my$("btn").onclick=function () {
        //创建table加入到div中
        var tableObj=document.createElement("table");
        tableObj.border="1";
        tableObj.cellPadding="0";
        tableObj.cellSpacing="0";
        my$("dv").appendChild(tableObj);
        //创建行,把行加入到table中
        for(var i=0;i<arr.length;i++){
            var dt=arr[i];//每个对象
            var trObj=document.createElement("tr");
            tableObj.appendChild(trObj);
            //创建第一个列,然后加入到行中
            var td1=document.createElement("td");
            td1.innerText=dt.name;
            trObj.appendChild(td1);
            //创建第二个列
            var td2=document.createElement("td");
            td2.innerHTML="<a href="+dt.href+">"+dt.name+"</a>";
            trObj.appendChild(td2);
        }
    };
    ```

- 模拟百度搜索框-自动提示

    ```js
    var keyWords = ["小杨才是最纯洁的", "小杨才是最帅的", "小段是最猥琐的", "小超是最龌龊的", "传智播客是一个培训机构", "传说在传智有个很帅很纯洁的小杨", "苹果好吃",
    "苹果此次召回还是没有中国"];

    //获取文本框注册键盘抬起事件
    my$("txt").onkeyup = function () {

        //每一次的键盘抬起都判断页面中有没有这个div
        if (my$("dv")) {
            //删除一次
            my$("box").removeChild(my$("dv"));
        }
        //获取文本框输入的内容
        var text = this.value;
        //临时数组--空数组------->存放对应上的数据
        var tempArr = [];
        //把文本框输入的内容和数组中的每个数据对比
        for (var i = 0; i < keyWords.length; i++) {
            //是否是最开始出现的
            if (keyWords[i].indexOf(text) == 0) {
                tempArr.push(keyWords[i]); //追加
            }
        }
        
        //如果文本框是空的,临时数组是空的,不用创建div
        if (this.value.length == 0 || tempArr.length == 0) {
            //如果页面中有这个div,删除这个div
            if (my$("dv")) {
                my$("box").removeChild(my$("dv"));
            }
            return;
        }
        
        //创建div,把div加入id为box的div中
        var dvObj = document.createElement("div");
        my$("box").appendChild(dvObj);
        dvObj.id = "dv";
        dvObj.style.width = "350px";
        //dvObj.style.height="100px";//肯定是不需要的------
        dvObj.style.border = "1px solid green";
        //循环遍历临时数组,创建对应的p标签
        for (var i = 0; i < tempArr.length; i++) {
            //创建p标签
            var pObj = document.createElement("p");
            //把p加到div中
            dvObj.appendChild(pObj);
            setInnerText(pObj, tempArr[i]);
            pObj.style.margin = 0;
            pObj.style.padding = 0;
            pObj.style.cursor = "pointer";
            pObj.style.marginTop = "5px";
            pObj.style.marginLeft = "5px";
            //鼠标进入
            pObj.onmouseover = function () {
                this.style.backgroundColor = "yellow";
            };
            //鼠标离开
            pObj.onmouseout = function () {
                this.style.backgroundColor = "";
            };
        }
    };
    ```

## BOM

### 概述

- BOM(Browser Object Model) 是指浏览器对象模型，浏览器对象模型提供了独立于内容的、可以与浏览器窗口进行互动的对象结构。BOM由多个对象组成，其中代表浏览器窗口的Window对象是BOM的顶层对象，其他对象都是该对象的子对象。
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzor5wa1i4j20qo0k0q3j.jpg)
- BOM作用：**操作浏览器**。
    > 我们在浏览器中的一些操作都可以使用BOM的方式进行编程处理; 比如：刷新浏览器、后退、前进、在浏览器中输入URL等
- window是浏览器的顶级对象: 
    - 当调用window下的属性和方法时，可以省略window 注意：window下一个特殊的属性 window.name
    - 变量/普通函数函数等都是window的属性/方法,使用时,window可以省略; 普通函数里的this指的即使window对象;
    - 计时器也是window对象的方法,里面的this也是值window对象;

### Window

- Window 对象描述

    - Window 对象表示浏览器中打开的窗口。
    - 如果文档包含框架（frame 或 iframe 标签），浏览器会为 HTML 文档创建一个 window 对象，并为每个框架创建一个额外的 window 对象。

- Window 对象属性

    | 属性                                                         | 描述                                                         |
    | :----------------------------------------------------------- | :----------------------------------------------------------- |
    | [closed](http://www.w3school.com.cn/jsref/prop_win_closed.asp) | 返回窗口是否已被关闭。                 |
    | [defaultStatus](http://www.w3school.com.cn/jsref/prop_win_defaultstatus.asp) | 设置或返回窗口状态栏中的默认文本。     |
    | [document](http://www.w3school.com.cn/jsref/dom_obj_document.asp) | 对 Document 对象的只读引用。请参阅 [Document 对象](http://www.w3school.com.cn/jsref/dom_obj_document.asp)。 |
    | [history](http://www.w3school.com.cn/jsref/dom_obj_history.asp) | 对 History 对象的只读引用。请参数 [History   对象](http://www.w3school.com.cn/jsref/dom_obj_history.asp)。 |
    | [innerheight](http://www.w3school.com.cn/jsref/prop_win_innerheight_innerwidth.asp) | 返回窗口的文档显示区的高度。           |
    | [innerwidth](http://www.w3school.com.cn/jsref/prop_win_innerheight_innerwidth.asp) | 返回窗口的文档显示区的宽度。           |
    | length           | 设置或返回窗口中的框架数量。           |
    | [location](http://www.w3school.com.cn/jsref/dom_obj_location.asp) | 用于窗口或框架的 Location 对象。请参阅 [Location 对象](http://www.w3school.com.cn/jsref/dom_obj_location.asp)。 |
    | [name](http://www.w3school.com.cn/jsref/prop_win_name.asp)   | 设置或返回窗口的名称。                 |
    | [Navigator](http://www.w3school.com.cn/jsref/dom_obj_navigator.asp) | 对 Navigator 对象的只读引用。请参数 [Navigator 对象](http://www.w3school.com.cn/jsref/dom_obj_navigator.asp)。 |
    | [opener](http://www.w3school.com.cn/jsref/prop_win_opener.asp) | 返回对创建此窗口的窗口的引用。         |
    | [outerheight](http://www.w3school.com.cn/jsref/prop_win_outerheight.asp) | 返回窗口的外部高度。                   |
    | [outerwidth](http://www.w3school.com.cn/jsref/prop_win_outerwidth.asp) | 返回窗口的外部宽度。                   |
    | pageXOffset      | 设置或返回当前页面相对于窗口显示区左上角的   X 位置。        |
    | pageYOffset      | 设置或返回当前页面相对于窗口显示区左上角的   Y 位置。        |
    | parent           | 返回父窗口。     |
    | [Screen](http://www.w3school.com.cn/jsref/dom_obj_screen.asp) | 对 Screen 对象的只读引用。请参数 [Screen   对象](http://www.w3school.com.cn/jsref/dom_obj_screen.asp)。 |
    | [self](http://www.w3school.com.cn/jsref/prop_win_self.asp)   | 返回对当前窗口的引用。等价于   Window 属性。                 |
    | [status](http://www.w3school.com.cn/jsref/prop_win_status.asp) | 设置窗口状态栏的文本。                 |
    | [top](http://www.w3school.com.cn/jsref/prop_win_top.asp)     | 返回最顶层的先辈窗口。                 |
    | window           | window 属性等价于 self 属性，它包含了对窗口自身的引用。      |
    | screenLeft/screenTop/ screenX/screenY  | 只读整数。声明了窗口的左上角在屏幕上的的   x 坐标和 y 坐标。IE、Safari 和 Opera 支持 screenLeft 和 s |

- Window 对象方法

    | 方法                                                         | 描述                                               |
    | :----------------------------------------------------------- | -------------------------------------------------- |
    | [alert()](http://www.w3school.com.cn/jsref/met_win_alert.asp) | 显示带有一段消息和一个确认按钮的警告框。|
    | [blur()](http://www.w3school.com.cn/jsref/met_win_blur.asp)  | 把键盘焦点从顶层窗口移开。   |
    | [clearInterval()](http://www.w3school.com.cn/jsref/met_win_clearinterval.asp) | 取消由   setInterval() 设置的 timeout。 |
    | [clearTimeout()](http://www.w3school.com.cn/jsref/met_win_cleartimeout.asp) | 取消由   setTimeout() 方法设置的 timeout。         |
    | [close()](http://www.w3school.com.cn/jsref/met_win_close.asp) | 关闭浏览器窗口。  |
    | [confirm()](http://www.w3school.com.cn/jsref/met_win_confirm.asp) | 显示带有一段消息以及确认按钮和取消按钮的对话框。   |
    | [createPopup()](http://www.w3school.com.cn/jsref/met_win_createpopup.asp) | 创建一个   pop-up 窗口。     |
    | [focus()](http://www.w3school.com.cn/jsref/met_win_focus.asp) | 把键盘焦点给予一个窗口。     |
    | [moveBy()](http://www.w3school.com.cn/jsref/met_win_moveby.asp) | 可相对窗口的当前坐标把它移动指定的像素。|
    | [moveTo()](http://www.w3school.com.cn/jsref/met_win_moveto.asp) | 把窗口的左上角移动到一个指定的坐标。    |
    | [open()](http://www.w3school.com.cn/jsref/met_win_open.asp)  | 打开一个新的浏览器窗口或查找一个已命名的窗口。     |
    | [print()](http://www.w3school.com.cn/jsref/met_win_print.asp) | 打印当前窗口的内容。         |
    | [prompt()](http://www.w3school.com.cn/jsref/met_win_prompt.asp) | 显示可提示用户输入的对话框。 |
    | [resizeBy()](http://www.w3school.com.cn/jsref/met_win_resizeby.asp) | 按照指定的像素调整窗口的大小。          |
    | [resizeTo()](http://www.w3school.com.cn/jsref/met_win_resizeto.asp) | 把窗口的大小调整到指定的宽度和高度。    |
    | [scrollBy()](http://www.w3school.com.cn/jsref/met_win_scrollby.asp) | 按照指定的像素值来滚动内容。 |
    | [scrollTo()](http://www.w3school.com.cn/jsref/met_win_scrollto.asp) | 把内容滚动到指定的坐标。     |
    | [setInterval()](http://www.w3school.com.cn/jsref/met_win_setinterval.asp) | 按照指定的周期（以毫秒计）来调用函数或计算表达式。 |
    | [setTimeout()](http://www.w3school.com.cn/jsref/met_win_settimeout.asp) | 在指定的毫秒数后调用函数或计算表达式。  |

    - 弹框的区别
	    - `alert()`  警告,无返回值
	    - `prompt()`  参数1:提示信息; 参数2:输入框的默认内容; 返回值:用户输入的内容,如果用户点击取消,返回null
	    - `confirm()` 参数:提示框信息, 返回值: 确定-->true 取消-->false
    - 定时器区别
        - `setInterval()`和`clearInterval()`
            定时调用的函数，可以按照给定的时间(单位毫秒)周期调用函数

            ```js
            // 创建一个定时器，每隔1秒调用一次
            var timerId = setInterval(function () {
                    var date = new Date();
                    console.log(date.toLocaleTimeString());
            }, 1000);​
            // 清理定时器
            clearInterval(timerId);
            ```

        - `setTimeout()`和`clearTimeout()`
            在指定的毫秒数到达之后执行指定的函数，只执行一次
            
            ```js
            // 创建一个定时器，1000毫秒后执行，返回定时器的标示
            var timerId = setTimeout(function () {
                    console.log('Hello World');
            }, 1000);​
            // 清理定时器(虽然是一次性定时器,还是要清理,否则会占用内存空间)
            clearTimeout(timerId);
            ```

- 页面加载事件
    - onload

        ```js
        window.onload = function () {
         // 当页面加载完成执行
         // 当页面完全加载所有内容（包括图像、脚本文件、CSS 文件等）执行
        }
        ```

    - onunload
    
        ```js
        window.onunload = function () {
         // 当用户退出页面时执行
        }
        ```

- 定时器案例
    - 一闪一闪亮晶晶

        ```js
        my$("btn").onclick = function () {
            setInterval(function () {
                my$("dv").innerHTML = "<span>★</span>";
                var x = parseInt(Math.random() * 600 + 1);
                var y = parseInt(Math.random() * 600 + 1);
                my$("dv").firstElementChild.style.left = x + "px";
                my$("dv").firstElementChild.style.top = y + "px";
            }, 5);
        };
        ```

    - 美女时钟
        > 前提: 准备1440张照片(只有 小时和秒  12 * 12)
        ```html
        <img src="" alt="" id="im" />
        <script>
            function f1() {
                //获取当前时间
                var dt = new Date();
                //获取小时
                var hour = dt.getHours();
                //获取秒
                var second = dt.getSeconds();
                hour = hour < 10 ? "0" + hour : hour;
                second = second < 10 ? "0" + second : second;
                my$("im").src = "meimei/" + hour + "_" + second + ".jpg";
            }
            f1();
            //页面加载完毕后,过了1秒才执行函数的代码
            setInterval(f1, 1000);
        </script>
        ```

### Location

- Location 对象描述: location对象可以获取或者设置浏览器地址栏的URL

- Location 对象属性

    | 属性                                                         | 描述                                  |
    | ------------------------------------------------------------ | --------------------------------------------- |
    | [hash](http://www.w3school.com.cn/jsref/prop_loc_hash.asp)   | 设置或返回从井号 (#) 开始的 URL（锚）。  |
    | [host](http://www.w3school.com.cn/jsref/prop_loc_host.asp)   | 设置或返回主机名和当前   URL 的端口号。  |
    | [hostname](http://www.w3school.com.cn/jsref/prop_loc_hostname.asp) | 设置或返回当前   URL 的主机名。  |
    | [href](http://www.w3school.com.cn/jsref/prop_loc_href.asp)   | 设置或返回完整的   URL。 |
    | [pathname](http://www.w3school.com.cn/jsref/prop_loc_pathname.asp) | 设置或返回当前   URL 的路径部分。|
    | [port](http://www.w3school.com.cn/jsref/prop_loc_port.asp)   | 设置或返回当前   URL 的端口号。  |
    | [protocol](http://www.w3school.com.cn/jsref/prop_loc_protocol.asp) | 设置或返回当前   URL 的协议。 |
    | [search](http://www.w3school.com.cn/jsref/prop_loc_search.asp) | 设置或返回从问号 (?) 开始的 URL（查询部分）。 |

- Location 对象方法

    | 属性                                                    | 描述                     |
    | ------------------------------------------------------------ | ------------------------ |
    | [assign()](http://www.w3school.com.cn/jsref/met_loc_assign.asp) | 加载新的文档。           |
    | [reload()](http://www.w3school.com.cn/jsref/met_loc_reload.asp) | 重新加载当前文档。       |
    | [replace()](http://www.w3school.com.cn/jsref/met_loc_replace.asp) | 用新的文档替换当前文档。 |

    > href 和 assign() 跳转之后,历史记录会保存(可以返回),replace()跳转之后,不能返回.

### Navigator

- Navigator对象描述
    - Navigator 对象包含有关浏览器的信息。可以使用这些属性进行平台专用的配置。
    - 虽然这个对象的名称显而易见的是 Netscape 的 Navigator 浏览器，但其他实现了 JavaScript 的浏览器也支持这个对象。
    - Navigator 对象的实例是唯一的，可以用 Window 对象的 navigator 属性来引用它。

- Navigator 对象属性

    | 属性                                            | 描述                                |
    | ------------------------------------------------------------ | ------------------------------------------------ |
    | [appCodeName](http://www.w3school.com.cn/jsref/prop_nav_appcodename.asp) | 返回浏览器的代码名。                             |
    | [appMinorVersion](http://www.w3school.com.cn/jsref/prop_nav_appminorversion.asp) | 返回浏览器的次级版本。                           |
    | [appName](http://www.w3school.com.cn/jsref/prop_nav_appname.asp) | 返回浏览器的名称。                               |
    | [appVersion](http://www.w3school.com.cn/jsref/prop_nav_appversion.asp) | 返回浏览器的平台和版本信息。                     |
    | [browserLanguage](http://www.w3school.com.cn/jsref/prop_nav_browserlanguage.asp) | 返回当前浏览器的语言。                           |
    | [cookieEnabled](http://www.w3school.com.cn/jsref/prop_nav_cookieenabled.asp) | 返回指明浏览器中是否启用   cookie 的布尔值。     |
    | [cpuClass](http://www.w3school.com.cn/jsref/prop_nav_cpuclass.asp) | 返回浏览器系统的   CPU 等级。                    |
    | [onLine](http://www.w3school.com.cn/jsref/prop_nav_online.asp) | 返回指明系统是否处于脱机模式的布尔值。           |
    | [platform](http://www.w3school.com.cn/jsref/prop_nav_platform.asp) | 返回运行浏览器的操作系统平台。                   |
    | [systemLanguage](http://www.w3school.com.cn/jsref/prop_nav_systemlanguage.asp) | 返回 OS   使用的默认语言。                       |
    | [userAgent](http://www.w3school.com.cn/jsref/prop_nav_useragent.asp) | 返回由客户机发送服务器的   user-agent 头部的值。 |
    | [userLanguage](http://www.w3school.com.cn/jsref/prop_nav_userlanguage.asp) | 返回 OS   的自然语言设置。                       |

- Navigator 对象方法

    | 方法                                                 | 描述                                   |
    | ------------------------------------------------------------ | ---------------------------------------------- |
    | [javaEnabled()](http://www.w3school.com.cn/jsref/met_nav_javaenabled.asp) | 规定浏览器是否启用   Java。                    |
    | [taintEnabled()](http://www.w3school.com.cn/jsref/met_nav_taintenabled.asp) | 规定浏览器是否启用数据污点   (data tainting)。 |

### History

- History 对象描述
    - History 对象最初设计来表示窗口的浏览历史。
    - 但出于隐私方面的原因，History 对象不再允许脚本访问已经访问过的实际 URL。唯一保持使用的功能只有 back()、forward() 和 go() 方法。

- History 对象属性

    | 属性                                                        | 描述                                |
    | ------------------------------------------------------------ | ----------------------------------- |
    | [length](http://www.w3school.com.cn/jsref/prop_his_length.asp) | 返回浏览器历史列表中的   URL 数量。 |

- History 对象方法

    | 方法                                                        | 描述                                                         |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | [back()](http://www.w3school.com.cn/jsref/met_his_back.asp)  | 加载   history 列表中的前一个 URL。                          |
    | [forward()](http://www.w3school.com.cn/jsref/met_his_forward.asp) | 加载   history 列表中的下一个 URL。                          |
    | [go()](http://www.w3school.com.cn/jsref/met_his_go.asp)      | 加载 history 列表中的某个具体页面。+n表示n次向前.空/0表示刷新 |

### Screen

- Screen 对象描述: Screen 对象包含有关客户端显示屏幕的信息。

- Screen 对象属性

    | 属性                                                         | 描述                                          |
    | ------------------------------------------------------------ | ---------------------------------------------- |
    | [availHeight](http://www.w3school.com.cn/jsref/prop_screen_availheight.asp) | 返回显示屏幕的高度   (除 Windows 任务栏之外)。 |
    | [availWidth](http://www.w3school.com.cn/jsref/prop_screen_availwidth.asp) | 返回显示屏幕的宽度   (除 Windows 任务栏之外)。 |
    | [bufferDepth](http://www.w3school.com.cn/jsref/prop_screen_bufferdepth.asp) | 设置或返回调色板的比特深度。                   |
    | [colorDepth](http://www.w3school.com.cn/jsref/prop_screen_colordepth.asp) | 返回目标设备或缓冲器上的调色板的比特深度。     |
    | [deviceXDPI](http://www.w3school.com.cn/jsref/prop_screen_devicexdpi.asp) | 返回显示屏幕的每英寸水平点数。                 |
    | [deviceYDPI](http://www.w3school.com.cn/jsref/prop_screen_deviceydpi.asp) | 返回显示屏幕的每英寸垂直点数。                 |
    | [fontSmoothingEnabled](http://www.w3school.com.cn/jsref/prop_screen_fontsmoothingenabled.asp) | 返回用户是否在显示控制面板中启用了字体平滑。   |
    | [height](http://www.w3school.com.cn/jsref/prop_screen_height.asp) | 返回显示屏幕的高度。                           |
    | [logicalXDPI](http://www.w3school.com.cn/jsref/prop_screen_logicalxdpi.asp) | 返回显示屏幕每英寸的水平方向的常规点数。       |
    | [logicalYDPI](http://www.w3school.com.cn/jsref/prop_screen_logicalydpi.asp) | 返回显示屏幕每英寸的垂直方向的常规点数。       |
    | [pixelDepth](http://www.w3school.com.cn/jsref/prop_screen_pixeldepth.asp) | 返回显示屏幕的颜色分辨率（比特每像素）。       |
    | [updateInterval](http://www.w3school.com.cn/jsref/prop_screen_updateinterval.asp) | 设置或返回屏幕的刷新率。                       |
    | [width](http://www.w3school.com.cn/jsref/prop_screen_width.asp) | 返回显示器屏幕的宽度。                         |

## 特效

### 三大系列
1. offset系列:偏移量
    - (父级元素margin+父级元素padding+父级元素border+自己的margin)
    - offsetLeft:元素距离左边位置的值
    - offsetTop:元素距离上面位置的值
    - offsetWidth:获取元素的宽度(有边框)
    - offsetHeight:获取元素的高度(有边框)
    - offsetParent:获取该元素中有定位的最近父级元素(找不到为body)
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzorwm57fqj20lg0cn3zt.jpg)
2. scroll系列:卷曲/滚动偏移
    - scrollLeft:元素向左卷曲出去的距离
    - scrollTop:元素向上卷曲出去的距离
    - scrollWidth:元素中内容的实际的宽度,如果没有内容,或者内容很少,元素的宽度
    - scrollHeight:元素中内容的实际的高度,如果没有内容,或者内容很少,元素的高度
3. client系列:客户区
    - clientWidth:可视区域的宽度,没有边框
    - clientHeight:可视区域的高度,没有边框
    - clientLeft:左边框的宽度
    - clientTop:上边框的宽度
    - clientX:可视区域的横坐标
    - clientY:可视区域的纵坐标
- 图片跟着鼠标-三大系列兼容
  
    ```js
    //图片跟着鼠标飞,可以在任何的浏览器中实现
    //window.event和事件参数对象e的兼容
    //clientX和clientY单独的使用的兼容代码
    //scrollLeft和scrollTop的兼容代码
    //pageX,pageY和clientX+scrollLeft 和clientY+scrollTop

    //把代码封装放在一个对象中
    var evt = {
        //window.event和事件参数对象e的兼容
        getEvent: function (evt) {
            return window.event || evt;
        },
        //可视区域的横坐标的兼容代码
        getClientX: function (evt) {
            return this.getEvent(evt).clientX;
        },
        //可视区域的纵坐标的兼容代码
        getClientY: function (evt) {
            return this.getEvent(evt).clientY;
        },
        //页面向左卷曲出去的横坐标
        getScrollLeft: function () {
            return window.pageXOffset || document.body.scrollLeft || document.documentElement.scrollLeft || 0;
        },
        //页面向上卷曲出去的纵坐标
        getScrollTop: function () {
            return window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop || 0;
        },
        //相对于页面的横坐标(pageX或者是clientX+scrollLeft)
        getPageX: function (evt) {
            return this.getEvent(evt).pageX ? this.getEvent(evt).pageX : this.getClientX(evt) + this.getScrollLeft();
        },
        //相对于页面的纵坐标(pageY或者是clientY+scrollTop)
        getPageY: function (evt) {
            return this.getEvent(evt).pageY ? this.getEvent(evt).pageY : this.getClientY(evt) + this.getScrollTop();
        }
    };

    //最终的代码
    //需要注意图片本身的margin-top/left,最终位置相应的加减;
    document.onmousemove = function (e) {
        my$("im").style.left = evt.getPageX(e) + "px";
        my$("im").style.top = evt.getPageY(e) + "px";
    };
    ```

### 特效案例
- 相关配套源文件:  见`百度网盘 > 全部文件 > others > 编程-源文件 > 特效源文件-含(最终common.js).7z`
- "阅读协议"禁用5s

    ```js
    var time = 5;
    var timeId = setInterval(function () {
        time--;
        my$("btn").value = "请仔细阅读协议(" + time + ")";
        if (time <= 0) {
            //停止定时器就可以
            clearInterval(timeId);
            //按钮可以被点击了
            my$("btn").disabled = false;
            my$("btn").value = "同意";
        }
    }, 1000);
    ```

- 表格各行变色

    ```js
    //先获取所有的行
    var trs = my$("j_tb").getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        trs[i].style.backgroundColor = i % 2 == 0 ? "red" : "yellow";
        //鼠标进入
        trs[i].onmouseover = mouseoverHandle;
        //鼠标离开
        trs[i].onmouseout = mouseoutHandle;
    }
    
    //当鼠标进入的时候,先把设置后的颜色保存起来,等到鼠标离开再恢复即可
    var lastColor = "";
    function mouseoverHandle() { //鼠标进入
        lastColor = this.style.backgroundColor;
        this.style.backgroundColor = "green";
    }
    function mouseoutHandle() { //鼠标离开
        this.style.backgroundColor = lastColor;
    }
    ```

- 大量字符串拼接

    ```js
    //推荐使用数组的方式拼接大量的字符串
    document.getElementById("btn").onclick = function () {
        var str = [];
        //获取所有的文本框
        var inputs = document.getElementsByTagName("input");
        //每个文本框的value属性值
        for (var i = 0; i < inputs.length; i++) {
            if (inputs[i].type != "button") {
            str.push(inputs[i].value);
            }
        }
        console.log(str.join("|"));//把数组元素拼接成字符串
    };
    ```

- 轮播图

    ```js
    var box = my$("box"); //获取最外面的div
    var screen = box.children[0]; //获取相框
    var imgWidth = screen.offsetWidth; //获取相框的宽度
    var ulObj = screen.children[0]; //获取ul
    var list = ulObj.children; //获取ul中的所有的li
    var olObj = screen.children[1]; //获取ol
    var arr = my$("arr"); //焦点的div
    var pic = 0; //全局变量
    
    //创建小按钮----根据ul中的li个数
    for (var i = 0; i < list.length; i++) {
        //创建li标签,加入到ol中
        var liObj = document.createElement("li");
        olObj.appendChild(liObj);
        liObj.innerHTML = (i + 1);
        //在每个ol中的li标签上添加一个自定义属性,存储索引值
        liObj.setAttribute("index", i);
        //注册鼠标进入事件
        liObj.onmouseover = function () {
            //先干掉所有的ol中的li的背景颜色
            for (var j = 0; j < olObj.children.length; j++) {
                olObj.children[j].removeAttribute("class");
            }
            //设置当前鼠标进来的li的背景颜色
            this.className = "current";
            //获取鼠标进入的li的当前索引值
            pic = this.getAttribute("index");
            //移动ul--匀速动画函数
            animate(ulObj, -pic * imgWidth);
        };
    }
    
    //设置ol中第一个li有背景颜色
    olObj.children[0].className = "current";
    //克隆一个ul中第一个li,加入到ul中的最后=====克隆
    ulObj.appendChild(ulObj.children[0].cloneNode(true));
    //自动播放
    var timeId = setInterval(clickHandle, 1000);
    //鼠标进入到box的div显示左右焦点的div
    box.onmouseover = function () {
        arr.style.display = "block";
        //鼠标进入废掉之前的定时器
        clearInterval(timeId);
    };
    //鼠标离开到box的div隐藏左右焦点的div
    box.onmouseout = function () {
        arr.style.display = "none";
        //鼠标离开自动播放
        timeId = setInterval(clickHandle, 1000);
    };
    
    //右边按钮
    my$("right").onclick = clickHandle;
    function clickHandle() {
        //如果pic的值是5,恰巧是ul中li的个数-1的值,此时页面显示第六个图片,而用户会认为这是第一个图,
        //所以,如果用户再次点击按钮,用户应该看到第二个图片
        if (pic == list.length - 1) {
            //如何从第6个图,跳转到第一个图
            pic = 0; //先设置pic=0
            ulObj.style.left = 0 + "px"; //把ul的位置还原成开始的默认位置
        }
        pic++; //立刻设置pic加1,那么此时用户就会看到第二个图片了
        animate(ulObj, -pic * imgWidth); //pic从0的值加1之后,pic的值是1,然后ul移动出去一个图片
        //如果pic==5说明,此时显示第6个图(内容是第一张图片),第一个小按钮有颜色,
        if (pic == list.length - 1) {
            //第五个按钮颜色干掉
            olObj.children[olObj.children.length - 1].className = "";
            //第一个按钮颜色设置上
            olObj.children[0].className = "current";
        } else {
            //干掉所有的小按钮的背景颜色
            for (var i = 0; i < olObj.children.length; i++) {
                olObj.children[i].removeAttribute("class");
            }
            olObj.children[pic].className = "current";
        }
    };
    
    //左边按钮
    my$("left").onclick = function () {
    if (pic == 0) {
    pic = 5;
    ulObj.style.left = -pic * imgWidth + "px";
    }
    pic--;
    animate(ulObj, -pic * imgWidth); //匀速动画函数
    //设置小按钮的颜色---所有的小按钮干掉颜色
    for (var i = 0; i < olObj.children.length; i++) {
    olObj.children[i].removeAttribute("class");
    }
    //当前的pic索引对应的按钮设置颜色
    olObj.children[pic].className = "current";
    };
    ```

- 固定顶部导航栏
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzos3qv133j20f801q3zt.jpg)

    ```js
    //获取页面向上或者向左卷曲出去的距离的值
    function getScroll() {
        return {
            left: window.pageXOffset || document.documentElement.scrollLeft || document.body.scrollLeft || 0,
            top: window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0
        };
    }
    //滚动事件
    window.onscroll = function () {
        //向上卷曲出去的距离和最上面的div的高度对比
        if (getScroll().top >= my$("topPart").offsetHeight) {
            //设置第二个div的类样式
            my$("navBar").className = "nav fixed";
            //设置第三个div的marginTop的值
            my$("mainPart").style.marginTop = my$("navBar").offsetHeight + "px";
            } else {
            my$("navBar").className = "nav";
            my$("mainPart").style.marginTop = "10px";
        }
    };
    ```

- 筋斗云导航栏
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzos4seb0ej20dr00z3zt.jpg)

    ```js
    //获取云彩
    var cloud = my$("cloud");
    //获取所有的li标签
    var list = my$("navBar").children;
    //循环遍历分别注册鼠标进入,鼠标离开,点击事件
    for (var i = 0; i < list.length; i++) {
        //鼠标进入事件
        list[i].onmouseover = mouseoverHandle;
        //点击事件
        list[i].onclick = clickHandle;
        //鼠标离开事件
        list[i].onmouseout = mouseoutHandle;
    }
    function mouseoverHandle() { //进入
        //移动到鼠标此次进入的li的位置--匀速动画函数
        animate(cloud, this.offsetLeft);
    }
    //点击的时候,记录此次点击的位置
    var lastPosition = 0;
    
    function clickHandle() { //点击
        lastPosition = this.offsetLeft;
    }
    function mouseoutHandle() { //离开--匀速动画函数
        animate(cloud, lastPosition);
    }
    ```

- 手风琴案例
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzos5nx9w1j20gk02x3zt.jpg)

    ```js
    //先获取所有的li标签
    var list = my$("box").getElementsByTagName("li");
    for (var i = 0; i < list.length; i++) {
        list[i].style.backgroundImage = "url(images/" + (i + 1) + ".jpg)";
        //鼠标进入
        list[i].onmouseover = mouseoverHandle;
        //鼠标离开
        list[i].onmouseout = mouseoutHandle;
    }
    //进入
    function mouseoverHandle() {
        for (var j = 0; j < list.length; j++) {
            animate(list[j], {
                "width": 100
            }); //动画效果--万能动画函数
        }
        animate(this, {
        "width": 800
        });
    }
    //离开
    function mouseoutHandle() {
        for (var j = 0; j < list.length; j++) {
            animate(list[j], {
                "width": 240
            }); //动画效果--万能动画函数
        }
    }
    ```

- 360弹框关闭动画
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzos6dkbnaj207c05b3zt.jpg)

    ```js
    my$("closeButton").onclick=function () {
        //设置最下面的div的高渐渐的变成0
        //万能动画函数
        animate(my$("bottomPart"),{"height":0},function () {
            animate(my$("box"),{"width":0});
        });
    };
    ```

- 旋转木马

    ```js
    var flag=true;//假设所有的动画执行完毕了---锁============
    var list = my$("slide").getElementsByTagName("li");
    
    //1---图片散开
    function assign() {
        for (var i = 0; i < list.length; i++) {
            //设置每个li,都要把宽,层级,透明度,left,top到达指定的目标位置
            animate(list[i], config[i],function () {
                flag=true;//==============================
            });
        }
    }
    assign();
    
    //右边按钮
    my$("arrRight").onclick = function () {
        if(flag){//======================
            flag=false;
            config.push(config.shift());
            assign();//重新分配
        }
    };
    
    //左边按钮
    my$("arrLeft").onclick = function () {
        if(flag){//====================
            flag=false;
            config.unshift(config.pop());
            assign();
        }
    };
    
    //鼠标进入,左右焦点的div显示
    my$("slide").onmouseover = function () {
        animate(my$("arrow"), {"opacity": 1});
    };
    
    //鼠标离开,左右焦点的div隐藏
    my$("slide").onmouseout = function () {
        animate(my$("arrow"), {"opacity": 0});
    };
    ```

- 图片跟着鼠标走最终兼容版本

    ```js
    //图片跟着鼠标飞,可以在任何的浏览器中实现
    //window.event和事件参数对象e的兼容
    //clientX和clientY单独的使用的兼容代码
    //scrollLeft和scrollTop的兼容代码
    //pageX,pageY和clientX+scrollLeft 和clientY+scrollTop
    
    //把代码封装放在一个对象中
    var evt = {
    //window.event和事件参数对象e的兼容
    getEvent: function (evt) {
        return window.event || evt;
    },
    //可视区域的横坐标的兼容代码
    getClientX: function (evt) {
        return this.getEvent(evt).clientX;
    },
    //可视区域的纵坐标的兼容代码
    getClientY: function (evt) {
        return this.getEvent(evt).clientY;
    },
    //页面向左卷曲出去的横坐标
    getScrollLeft: function () {
        return window.pageXOffset || document.body.scrollLeft || document.documentElement.scrollLeft || 0;
    },
    //页面向上卷曲出去的纵坐标
    getScrollTop: function () {
        return window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop || 0;
    },
    //相对于页面的横坐标(pageX或者是clientX+scrollLeft)
    getPageX: function (evt) {
        return this.getEvent(evt).pageX ? this.getEvent(evt).pageX : this.getClientX(evt) + this.getScrollLeft();
    },
    //相对于页面的纵坐标(pageY或者是clientY+scrollTop)
    getPageY: function (evt) {
        return this.getEvent(evt).pageY ? this.getEvent(evt).pageY : this.getClientY(evt) + this.getScrollTop();
    }
    };
    
    //最终的代码
    //需要注意图片本身的margin-top/left,最终位置相应的加减;
    document.onmousemove = function (e) {
        my$("im").style.left = evt.getPageX(e) + "px";
        my$("im").style.top = evt.getPageY(e) + "px";
    };
    ```

- 鼠标拖拽对话框

    ```js
    //获取超链接,注册点击事件,显示登录框和遮挡层
    my$("link").onclick = function () {
        my$("login").style.display = "block";
        my$("bg").style.display = "block";
    };
    
    //获取关闭,注册点击事件,隐藏登录框和遮挡层
    my$("closeBtn").onclick = function () {
        my$("login").style.display = "none";
        my$("bg").style.display = "none";
    };
    
    //按下鼠标,移动鼠标,移动登录框
    my$("title").onmousedown = function (e) {
        //获取此时的可视区域的横坐标-此时登录框距离左侧页面的横坐标
        var spaceX = e.clientX - my$("login").offsetLeft;
        var spaceY = e.clientY - my$("login").offsetTop;
        //移动的事件
        document.onmousemove = function (e) {
            //新的可视区域的横坐标-spaceX====>新的值--->登录框的left属性
            var x = e.clientX - spaceX+250;
            var y = e.clientY - spaceY-140;
            my$("login").style.left = x + "px";
            my$("login").style.top = y + "px";
        }
    };
    
    //松开鼠标
    document.onmouseup=function () {
        document.onmousemove=null;//当鼠标抬起的时候,把鼠标移动事件干掉
    };
    ```

- 京东主图放大镜

    ```js
    var box = my$("box"); //获取需要的元素
    var small = box.children[0]; //获取小图的div
    var mask = small.children[1]; //遮挡层
    var big = box.children[1]; //获取大图的div
    var bigImg = big.children[0]; //获取大图
    
    //鼠标进入显示遮挡层和大图的div
    box.onmouseover = function () {
        mask.style.display = "block";
        big.style.display = "block";
    };
    //鼠标离开隐藏遮挡层和大图的div
    box.onmouseout = function () {
        mask.style.display = "none";
        big.style.display = "none";
    };
    
    //鼠标的移动事件---鼠标是在小层上移动
    small.onmousemove = function (e) {
        //鼠标此时的可视区域的横坐标和纵坐标
        //主要是设置鼠标在遮挡层的中间显示
        var x = e.clientX - mask.offsetWidth / 2;
        var y = e.clientY - mask.offsetHeight / 2;
        //主要是margin的100px的问题
        x = x - 100;
        y = y - 100;
        //横坐标的最小值
        x = x < 0 ? 0 : x;
        //纵坐标的最小值
        y = y < 0 ? 0 : y;
        //横坐标的最大值
        x = x > small.offsetWidth - mask.offsetWidth ? small.offsetWidth - mask.offsetWidth : x;
        //纵坐标的最大值
        y = y > small.offsetHeight - mask.offsetHeight ? small.offsetHeight - mask.offsetHeight : y;
        //为遮挡层的left和top赋值
        mask.style.left = x + "px";
        mask.style.top = y + "px";
        
        //遮挡层的移动距离/大图的移动距离=遮挡层的最大移动距离/大图的最大移动距离
        //大图的移动距离=遮挡层的移动距离*大图的最大移动距离/遮挡层的最大移动距离
        
        //大图的横向的最大移动距离
        var maxX = bigImg.offsetWidth - big.offsetWidth;
        //大图的纵向的最大移动距离
        //var maxY = bigImg.offsetHeight - big.offsetHeight;
        //大图的横向移动的坐标
        var bigImgMoveX = x * maxX / (small.offsetWidth - mask.offsetWidth);
        //大图的纵向移动的坐标
        var bigImgMoveY = y * maxX / (small.offsetWidth - mask.offsetWidth);
        
        //设置图片移动
        bigImg.style.marginLeft = -bigImgMoveX + "px";
        bigImg.style.marginTop = -bigImgMoveY + "px";
    };
    ```

- 滚动条案例

    ```js
    var box = my$("box"); //最外面的div
    var content = my$("content"); //文字div
    var scroll = my$("scroll"); //装滚动条的div---容器
    var bar = my$("bar"); //滚动条
    
    //设置滚动条的高度
    //滚动条的高/装滚动条的div的高=box的高/文字div的高
    //滚动条的高=装滚动条的div的高*box的高/文字div的高
    var height = scroll.offsetHeight * box.offsetHeight / content.offsetHeight;
    bar.style.height = height + "px";
    
    //移动滚动条
    bar.onmousedown = function (e) {
        var spaceY = e.clientY - bar.offsetTop;
        document.onmousemove = function (e) { //移动事件
            var y = e.clientY - spaceY;
            y = y < 0 ? 0 : y; //最小值
            y = y > scroll.offsetHeight - bar.offsetHeight ? scroll.offsetHeight - bar.offsetHeight : y;
            bar.style.top = y + "px";
            //设置鼠标移动的时候,文字不被选中
            window.getSelection ? window.getSelection().removeAllRanges() : document.selection.empty();
            //滚动条的移动距离/文字div的移动距离=滚动条最大的移动距离/文字div的最大移动距离
            //文字div的移动距离=滚动条的移动距离*文字div的最大移动距离/滚动条最大的移动距离
            var moveY = y * (content.offsetHeight - box.offsetHeight) / (scroll.offsetHeight - bar.offsetHeight);
            //设置文字div的移动距离
            content.style.marginTop = -moveY + "px";
        };
    };
    
    document.onmouseup = function () {
        //鼠标抬起的时候,把移动事件干掉
        document.onmousemove = null;
    };
    ```

- 无刷新评论

    ```js
    //获取按钮,注册点击事件
    document.getElementById("btn").onclick = function () {
        //获取昵称的元素
        var userName = my$("userName");
        //获取评论的元素
        var tt = my$("tt");
        //创建行
        var tr = document.createElement("tr");
        //行加到tbody中
        my$("tbd").appendChild(tr);
        //创建列
        var td1 = document.createElement("td");
        tr.appendChild(td1);
        td1.innerHTML = userName.value;
        //创建列
        var td2 = document.createElement("td");
        tr.appendChild(td2);
        td2.innerHTML = tt.value;
        //清空
        userName.value = "";
        tt.value = "";
    };
    ```

