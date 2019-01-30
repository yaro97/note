# jQuery

## jQuery基础知识

### JS框架库

- 原生JS的缺点:
	- 每种空间的操作方式不统一
	- 不同浏览器兼容性处理
- JS框架库:
	- 就是一个JS文件,里面封装了很多函数等功能
	- 兼容多平台/版本浏览器
	- 统一/方便的API接口
- 常见的JS框架库:
	- Prototype
	- YUI-网络反响一般
	- Dojo
	- ExtJS
	- jQuery

### JQuery介绍

- 为啥学习jQuery? --> DOM操作有很多缺点:
	- DOM代码冗余;
	- DOM兼容问题;
	- DOM代码容错性很差(一个地方出现小问题-->不能正常运行);
	- DOM中window.onload只能有一个;
	- 查找元素方法太少/麻烦;
	- 遍历伪数组麻烦;
	- 实现简单的动画效果都会很麻烦;
	- ...
- jQuery是啥?
	- 一个JS框架库,里面封装了很多函数,处理了兼容性,易用的API接口;
	- 并是不代替JS的,使用jQuery/编写jQuery插件还是需要JS技术;
	- 封装了很多函数实现很多功能,但是不可能全部功能,有些功能还需要自己用JS实现;
	- 其实就是个加强版的common.js，学习jQuery，就是学习jQuery这个js文件中封装的方法;
- 特点:
	- 使用简单: Write Less, Do More.
	- 定位元素方式多样/灵活
	- 链式编程
	- 隐式迭代 --> 不需要for循环遍历
	- 实现代码非常简单,且功能强大;
	- 体积小,插件丰富
    - 开源/免费

### jQuery顶级对象

- BOM的顶级对象是window,可以 `.` 出浏览器中的`属性和方法`;
- DOM的顶级对象是document, 可以 `.` 出DOM的`属性和方法`;
- jQuery的顶级对象是jQuery(缩写成 $ ),可以 `.` 出jQuery的`方法`;

### jQuery文件的引入

- 各版本说明:
	- 1.x -- 兼容IE678,使用最为广泛的，官方只做BUG维护，功能不再新增。因此一般项目来说，使用1.x版本就可以了；
	- 2.x -- 不兼容IE678，很少有人使用，官方只做BUG维护，功能不再新增。如果不考虑兼容低版本的浏览器可以使用2.x；
	- 3.x -- 不兼容IE678，只支持最新的浏览器。除非特殊要求，一般不会使用3.x版本的，很多老的jQuery插件不支持这个版本。目前该版本是官方主要更新维护的版本。；
- 下载地址: [官网](https://code.jquery.com/jquery/) + [Bootstrap](https://www.bootcdn.cn/) 
- 版本选择:
	- 开发环境 -- 普通版-->方便调试(跳转到函数方便阅读);
	- 生产环境--压缩版-->网络宽带
- 文件的引入
	- JS引入文件, 务必使用单独的一对<script></script>标签.
	- 额外使用一对<script></script>标签书写内容.

### jQuery语法

- 基础语法：`$(selector).action()`
- `$` === `jQuery`
- `选择符（selector）` 定位 HTML 元素
- jQuery 的 `action()` 执行对元素的操作

### jQuery入口函数(页面加载事件)

1. 传统JS页面加载事件(只能写一个)

```js
window.onload = function () { //失效
    console.log("Hello World 1");
};
window.onload = function () {
    console.log("Hello World 2"); //只有这个有效 
};
```

2. jQuery页面加载事件(可以写多个)
    - 方法一: 所有内容(标签/文字/图片...)加载完再执行
    
    ```js
    $(window).load(function () {
        console.log("Hello World 1"); //两个都会执行
    });
    $(window).load(function () {
        console.log("Hello World 2"); //两个都会执行
    });
    ```
    
    - 方法二: 基本的标签加载完就执行(**推荐**)
    
    ```js
    $(document).ready(function () {
        console.log("Hello World 1");
    });
    //更简单的写法(推荐)
    $(function () { //$可以用jQuery替换
        console.log("Hello World 1");
    });
    ```

### DOM对象 VS jQuery对象

- 二者的区别
	- DOM对象：使用JavaScript中的方法获取页面中的元素返回的对象就是dom对象。
	- jQuery对象：jquery对象就是使用jquery的方法获取页面中的元素返回的对象就是jQuery对象。
	- jQuery对象其实就是DOM对象的包装集（包装了`DOM对象的集合（伪数组）`）
	- DOM对象与jQuery对象的方法不能混用。
- 转换的意义:
	- DOM对象->jQuery对象: jQuery对象操作方便;
	- jQuery对象->DOM对象: jQuery不是万能的,有时候还需要原生JS;
- 如何互相转换:
	1. DOM对象->jQuery对象: domObj -> $(domObj)

        ```js
        //DOM-->jquery对象
        $(function () {
            var btnObj = document.getElementById("btn");//DOM对象
            $(btnObj).click(function () {//DOM对象转换为jQuery对象
                $(this).css("background-color", "red");//DOM中的this转换为jQuery对象
            });
        });
        ```
    
	2. jQuery对象->DOM对象: jQueryObj -> jQueryObj.get(0)/或jQueryObj[0]

        ```js
        //jQuery对象->DOM对象
        $(function () {
            $("#btn1").get(0).onclick = function () { //jQuery对象->DOM对象
            // $("#btn1")[0].onclick = function () {
                this.style.backgroundColor = "red";
            };
        });
        ```

### `$` 的本质

- `$` 就是jQuery的简写,  其实就是一个函数名,所以后面记得跟小括号 `$()`
- `$` 的参数不同,功能就不同:
	1. 参数是`DOM对象` -- 如: `$(document)` 把`DOM对象`转变为`jQuery对象`;
	2. 参数是`匿名函数` -->`入口函数`;
	3. 参考是`字符串` -->`定位jQuery对象`;

## jQuery选择/过滤器-遍历

### 概述

- jQuery选择器是jQuery为我们提供的一组方法，让我们更加方便的获取到页面中的元素。注意：jQuery选择器返回的是jQuery对象。
- jQuery选择器有很多，基本兼容了CSS1到CSS3所有的选择器，并且jQuery还添加了很多更加复杂的选择器。
- jQuery选择器虽然很多，但是选择器之间可以相互替代，就是说获取一个元素，你会有很多种方法获取到。所以我们平时真正能用到的只是少数的最常用的选择器。

### 基本选择器

| 名称       | 用法               | 描述                                |
| ---------- | ------------------ | ------------------------------------ |
| ID选择器   | $(“#id”);          | 获取指定ID的元素                     |
| 类选择器   | $(“.class”);       | 获取同一类class的元素                |
| 标签选择器 | $(“div”);          | 获取同一类标签的所有元素             |
| 并集选择器 | $(“div,p,li”);     | 使用逗号分隔，只要符合条件之一就可。 |
| 交集选择器 | $(“div.redClass”); | 获取class为redClass的div元素         |

> 总结：跟css的选择器用法一模一样。

### 层级选择器(组合选择器)

| 名称       | 用法        | 描述                                                       |
| ---------- | ----------- | ----------------------------------------------------------- |
| 子代选择器 | $(“ul>li”); | 使用>号，获取儿子层级的元素，注意，并不会获取孙子层级的元素 |
| 后代选择器 | $(“ul li”); | 使用空格，代表后代选择器，获取ul下的所有li元素，包括孙子等  |

> 总结：跟css的选择器用法一模一样。

### 基本过滤器

> 这类选择器都带冒号:

| 名称         | 用法                                | 描述                                                        |
| ------------ | ------------------------------------ | ----------------------------------------------------------- |
| :eq（index） | $(“li:eq(2)”).css(“color”,   ”red”); | 获取到的li元素中，选择索引号为2的元素，索引号index从0开始。 |
| :odd         | $(“li:odd”).css(“color”,   ”red”);   | 获取到的li元素中，选择索引号为奇数的元素                    |
| :even        | $(“li:even”).css(“color”,   ”red”);  | 获取到的li元素中，选择索引号为偶数的元素                    |
- 【案例：隔行变色】

### 筛选方法(属于遍历--根据已定位元素找其他元素)

> 筛选选择器的功能与过滤选择器有点类似，但是用法不一样，筛选选择器主要是方法。

| 名称               | 用法                       | 描述                             |
| ------------------ | --------------------------- | -------------------------------- |
| children(selector) | $(“ul”).children(“li”)      | 相当于$(“ul>li”)，子类选择器     |
| find(selector)     | $(“ul”).find(“li”);         | 相当于$(“ul li”),后代选择器      |
| siblings(selector) | $(“#first”).siblings(“li”); | 查找兄弟节点，不包括自己本身。   |
| parent()           | $(“#first”).parent();       | 查找父亲                         |
| eq(index)          | $(“li”).eq(2);              | 相当于$(“li:eq(2)”),index从0开始 |
| next()             | $(“li”).next()              | 找下一个兄弟                     |
| prev()             | $(“li”).prev()              | 找上一次兄弟                     |

- 【案例：下拉菜单】this+children+mouseenter+mouseleave

    ```js
    $(function () {
        var $li = $(".wrap>ul>li");
        //给li注册鼠标经过事件，让自己的ul显示出来
        $li.mouseenter(function () {
            //找到所有的儿子，并且还得是ul
            $(this).children("ul").show();
        });
        $li.mouseleave(function () {
            $(this).children("ul").hide();
        });
    });
    ```

- 【案例：突出展示-京剧脸谱】siblings+find

    ```js
    $(function () {
        $(".wrap>ul>li").mouseenter(function () {
            $(this).css("opacity", "1").siblings().css("opacity", "0.4");
        });
        $(".wrap").mouseleave(function () {
            $(this).find('li').css("opacity", 1);
        });
    });
    ```

- 【案例：手风琴】next+parent

    ```js
    $(function () {
        //思路分析：
        //1. 给所有的span注册点击事件，让当前span的兄弟div显示出来
        $(".groupTitle").click(function () {
            //下一个兄弟：nextElementSibling
            //链式编程：在jQuery里面，方法可以一直调用下去。
            $(this).next().slideDown(200).parent().siblings().children("div").slideUp(200);
        });
    });
    ```

- 【案例：淘宝精品】index+eq

    ```js
    $(function () {
        $("#left>li").mouseenter(function () {
            $("#center>li:eq(" + $(this).index() + ")").show().siblings().hide();
        });
        $("#right>li").mouseenter(function () {
            $("#center>li").eq($(this).index() + 9).show().siblings().hide();
        });
    })
    ```

### index()方法

- HTML 代码:

    ```html
    <ul>
    <li id="foo">foo</li>
    <li id="bar">bar</li>
    <li id="baz">baz</li>
    </ul>
    ```
- jQuery 代码:

    ```js
    $('li').index(document.getElementById('bar')); //1，传递一个DOM对象，返回这个对象在原先集合中的索引位置
    $('li').index($('#bar')); //1，传递一个jQuery对象
    $('li').index($('li:gt(0)')); //1，传递一组jQuery对象，返回这个对象中第一个元素在原先集合中的索引位置
    $('#bar').index('li'); //1，传递一个选择器，返回#bar在所有li中的做引位置
    $('#bar').index(); //1，不传递参数，返回这个元素在同辈中的索引位置。  
    ```

### siblings()方法

选择所有的兄弟元素(除自己)

### mouseover /mouseenter 

- 不论鼠标指针穿过被选元素或其子元素，都会触发 mouseover- mouseout事件。
- 只有在鼠标指针穿过被选元素时，才会触发 mouseenter-mouseleave 事件(推荐)。

### 选择器Reference --直接定位某个某元素

Basics基础选择器

- [*](https://api.jquery.com/all-selector/)
- [.class](https://api.jquery.com/class-selector/)
- [element](https://api.jquery.com/element-selector/)
- [#id](https://api.jquery.com/id-selector/)
- [selector1, selectorN, ...](https://api.jquery.com/multiple-selector/)

Hierarchy层级选择器

- [parent > child](https://api.jquery.com/child-selector/)
- [ancestor descendant](https://api.jquery.com/descendant-selector/)
- [prev + next](https://api.jquery.com/next-adjacent-Selector/)
- [prev ~ siblings](https://api.jquery.com/next-siblings-selector/)

Basic Filters基本过滤器

- [:animated](https://api.jquery.com/animated-selector/)
- [:eq()](https://api.jquery.com/eq-selector/)
- [:even](https://api.jquery.com/even-selector/)
- [:first](https://api.jquery.com/first-selector/)
- [:gt()](https://api.jquery.com/gt-selector/)
- [:header](https://api.jquery.com/header-selector/)
- [:lang()](https://api.jquery.com/lang-selector/)
- [:last](https://api.jquery.com/last-selector/)
- [:lt()](https://api.jquery.com/lt-selector/)
- [:not()](https://api.jquery.com/not-selector/)
- [:odd](https://api.jquery.com/odd-selector/)
- [:root](https://api.jquery.com/root-selector/)
- [:target](https://api.jquery.com/target-selector/)

Content Filters内容过滤器

- [:contains()](https://api.jquery.com/contains-selector/)
- [:empty](https://api.jquery.com/empty-selector/)
- [:has()](https://api.jquery.com/has-selector/)
- [:parent](https://api.jquery.com/parent-selector/)

Visibility Filters

- [:hidden](https://api.jquery.com/hidden-selector/)
- [:visible](https://api.jquery.com/visible-selector/)

Attribute属性选择器--css3+

- [[name|="value"\]](https://api.jquery.com/attribute-contains-prefix-selector/)
- [[name*="value"\]](https://api.jquery.com/attribute-contains-selector/)
- [[name~="value"\]](https://api.jquery.com/attribute-contains-word-selector/)
- [[name$="value"\]](https://api.jquery.com/attribute-ends-with-selector/)
- [[name="value"\]](https://api.jquery.com/attribute-equals-selector/)
- [[name!="value"\]](https://api.jquery.com/attribute-not-equal-selector/)
- [[name^="value"\]](https://api.jquery.com/attribute-starts-with-selector/)
- [[name\]](https://api.jquery.com/has-attribute-selector/)
- [[name="value"\][name2="value2"]](https://api.jquery.com/multiple-attribute-selector/)

Child Filters--css3+

- [:first-child](https://api.jquery.com/first-child-selector/)
- [:first-of-type](https://api.jquery.com/first-of-type-selector/)
- [:last-child](https://api.jquery.com/last-child-selector/)
- [:last-of-type](https://api.jquery.com/last-of-type-selector/)
- [:nth-child()](https://api.jquery.com/nth-child-selector/)
- [:nth-last-child()](https://api.jquery.com/nth-last-child-selector/)
- [:nth-last-of-type()](https://api.jquery.com/nth-last-of-type-selector/)
- [:nth-of-type()](https://api.jquery.com/nth-of-type-selector/)
- [:only-child](https://api.jquery.com/only-child-selector/)
- [:only-of-type()](https://api.jquery.com/only-of-type-selector/)

Forms表单专用

- [:button](https://api.jquery.com/button-selector/)
- [:checkbox](https://api.jquery.com/checkbox-selector/)
- [:checked](https://api.jquery.com/checked-selector/)
- [:disabled](https://api.jquery.com/disabled-selector/)
- [:enabled](https://api.jquery.com/enabled-selector/)
- [:focus](https://api.jquery.com/focus-selector/)
- [:file](https://api.jquery.com/file-selector/)
- [:image](https://api.jquery.com/image-selector/)
- [:input](https://api.jquery.com/input-selector/)
- [:password](https://api.jquery.com/password-selector/)
- [:radio](https://api.jquery.com/radio-selector/)
- [:reset](https://api.jquery.com/reset-selector/)
- [:selected](https://api.jquery.com/selected-selector/)
- [:submit](https://api.jquery.com/submit-selector/)
- [:text](https://api.jquery.com/text-selector/)

From <<https://oscarotero.com/jquery/>> 

### TRAVERSING遍历

Filtering筛选/过滤

- [.eq()](https://api.jquery.com/eq/)
- [.filter()](https://api.jquery.com/filter/)
- [.first()](https://api.jquery.com/first/)
- [.has()](https://api.jquery.com/has/)
- [.is()](https://api.jquery.com/is/)
- [.last()](https://api.jquery.com/last/)
- [.map()](https://api.jquery.com/map/)
- [.not()](https://api.jquery.com/not/)
- [.slice()](https://api.jquery.com/slice/)

Miscellaneous Traversing杂项遍历

- [.add()](https://api.jquery.com/add/)
- [.addBack()](https://api.jquery.com/addBack/)
- [.andSelf()](https://api.jquery.com/andSelf/)
- [.contents()](https://api.jquery.com/contents/)
- [.each()](https://api.jquery.com/each/)
- [.end()](https://api.jquery.com/end/)

Tree Traversal树遍历

- [.children()](https://api.jquery.com/children/)
- [.closest()](https://api.jquery.com/closest/)
- [.find()](https://api.jquery.com/find/)
- [.next()](https://api.jquery.com/next/)
- [.nextAll()](https://api.jquery.com/nextAll/)
- [.nextUntil()](https://api.jquery.com/nextUntil/)
- [.parent()](https://api.jquery.com/parent/)
- [.parents()](https://api.jquery.com/parents/)
- [.parentsUntil()](https://api.jquery.com/parentsUntil/)
- [.prev()](https://api.jquery.com/prev/)
- [.prevAll()](https://api.jquery.com/prevAll/)
- [.prevUntil()](https://api.jquery.com/prevUntil/)
- [.siblings()](https://api.jquery.com/siblings/)

From <<https://oscarotero.com/jquery/>> 

## jQuery样式

### CSS操作

- 隐式迭代说明	
    - 设置操作,如果是多个元素,所有元素都设置;
    - 获取操作,如果是多个元素,只返回第一个;
- css方法操作
    - 获取样式:`console.log($("div").css("background-color"))`;
    - 设置一个/多个样式:

        ```js
        $("#one").css("background", "gray");
        $("#one").css({
            "background": "gray",
            "width": "400px",
            "height": "200px"
        });
        ```

### Class操作

- class相关操作

    > 说明: class/id 也是attribute的一种,也可以用attr方法来操作,只不过习惯上不这么干.

    1. 判断是否有 - `$(“div”).hasClass(“one”)`;
    2. 添加类 - `$(“div”).addClass(“one”)`; 
    3. 移除类 - `$(“div”).removeClass(“one”)`;
    4. 切换 - `$(“div”).toggleClass(“one”)`; 有则删除,无则添加
    - **Note**:
        - 类名称不需要加点,即不需要".one", 直接用 "one" ;
        - addClass(“one”),追加类, 不会覆盖掉之前的类;
        - 添加多个类,addClass(“one two”);
    - 案例 --> tab 栏切换

        ```js
        $(function () {
            $(".tab-item").mouseenter(function () {
                //两件事件
                $(this).addClass("active").siblings().removeClass("active");
                var idx = $(this).index();
                $(".main").eq(idx).addClass("selected").siblings().removeClass("selected");
            });
        });
        ```

- CSS Reference

    - [.addClass()](https://api.jquery.com/addClass/)
    - [.css()](https://api.jquery.com/css/)
    - [jQuery.cssHooks](https://api.jquery.com/jQuery.cssHooks/)
    - [jQuery.cssNumber](https://api.jquery.com/jQuery.cssNumber/)
    - [jQuery.escapeSelector()](https://api.jquery.com/jQuery.escapeSelector/)
    - [.hasClass()](https://api.jquery.com/hasClass/)
    - [.removeClass()](https://api.jquery.com/removeClass/)
    - [.toggleClass()](https://api.jquery.com/toggleClass/)

    From <<https://oscarotero.com/jquery/>> 

## jQuery属性

### 属性和样式的区别

- 样式：在style里面写的，用css来操作
- 属性：在里面里面写的，用attr方法操作 -- 表单的相关属性用 prop方法操作;

### attr方法

> 说明: class/id 也是attribute的一种,也可以用attr方法来操作,只不过习惯上不这么干.

- 获取属性: `console.log($("img").attr("alt"))`;
- 设置一个/多个/自定义属性

    ```js
    $("img").attr("alt", "图破了");
    $("img").attr("title", "错错错错");
    //设置多个属性
    $("img").attr({
        alt: "图破了",
        title: "错错错",
        aa: "bb" //jquery可以设置自定义属性
    })
    ```

- 案例-美女相册

    ```js
    $(function () {
        //1. 给所有的a注册点击事件
        $("#imagegallery a").click(function () {
            var href = $(this).attr("href");
            $("#image").attr("src", href);
            
            var title = $(this).attr("title");
            $("#des").text(title);
            
            return false;
        });
    });
    ```

### prop方法

- attributes和properties区别
	- attributes 是 HTML 元素（标签）的属性,--编写的html，
	- properties 是 DOM 对象的属性 -- 浏览器解析时创建的DOM。
- attr和prop的区别
	- attr: 
		- attr源码中通过setAttitude实现;
		- 目的: 检索/设置HTML文档节点属性;
		- 可以设置的自定义属性-->能够在html中体现.
		- 标签中没写该 attributes, 获取时会返回 undefined;
	- prop:
		- prop源码中通过 = 等号赋值实现;
		- 目的:检索/设置DOM对象的属性;
- 官方使用建议：**`值为 true 和 false 属性，如 checked, selected 或者 disabled 使用prop()，其他的使用 attr()`**;
- 案例-点菜表格

    ```js
    $(function () {
        $("#j_cbAll").click(function () {
            //修改下面的哪些checkbox
            $("#j_tb input").prop("checked", $(this).prop("checked"));
        });
        $("#j_tb input").click(function () {
            if($("#j_tb input:checked").length == $("#j_tb input").length){
                $("#j_cbAll").prop("checked", true)
            }else {
                $("#j_cbAll").prop("checked", false)
            }
        });
    });
    ```

### ATTRIBUTES Reference

- Attributes
	- `.attr()`
	- `.prop()`
	- `.removeAttr()` 移除属性
	- `.removeProp()` 移除属性
	- `.val()`

From <https://oscarotero.com/jquery/> 

## jQuery动画
## jQuery节点操作
## jQuery特殊属性操作
## jQuery事件机制
## jQuery知识点补充
## jQuery插件