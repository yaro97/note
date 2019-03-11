# jQuery

> jQuery四大特征: 1. 链式调用; 2. 读写二合一; 3. 隐式迭代; 4. 编码函数化;

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

### `$`的本质

- `$` 就是jQuery的简写,  其实就是一个函数名,所以后面记得跟小括号 `$()`
- `$` 的参数不同,功能就不同:
	1. 参数是`DOM对象` -- 如: `$(document)` 把`DOM对象`转变为`jQuery对象`;
	2. 参数是`匿名函数` -->`入口函数`;
	3. 参考是`字符串` -->`定位jQuery对象`;

## jQuery选择/过滤器-遍历

> 请参考 [jQuery cheatsheet](https://oscarotero.com/jquery/)

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

### 三对基本对话

- 三对基本动画
    - Basics--修改宽/高
        [.hide()](https://api.jquery.com/hide/)
        [.show()](https://api.jquery.com/show/)
        [.toggle()](https://api.jquery.com/toggle/)
    - Fading--修改capacity
        [.fadeIn()](https://api.jquery.com/fadeIn/)
        [.fadeOut()](https://api.jquery.com/fadeOut/)
        [.fadeTo()](https://api.jquery.com/fadeTo/)
        [.fadeToggle()](https://api.jquery.com/fadeToggle/)
    - Sliding--修改高
        [.slideDown()](https://api.jquery.com/slideDown/)
        [.slideToggle()](https://api.jquery.com/slideToggle/)
        [.slideUp()](https://api.jquery.com/slideUp/)
- 参数:
	- 空 : 默认速度 normal
	- 参数一:控制动画速度
		- 字符串: slow --600ms; normal --400ms; fast --200ms
		- 数字: 1000 -- ms
	- 参数二: 回调函数,动画执行完后执行的函数(如:下一个动画)
- 案例:
	- 下拉菜单

    ```js
    $(function () {
    //mouseover：鼠标经过事件
    //mouseout:鼠标离开事件
    //mouseenter:鼠标进入事件
    //mouseleave：鼠标离开事件
    var $li = $(".wrap>ul>li");
    //给li注册鼠标经过事件，让自己的ul显示出来
    $li.mouseenter(function () {
            //找到所有的儿子，并且还得是ul
            //stop：停止当前正在执行的动画
            $(this).children("ul").stop().slideDown();
        });
        $li.mouseleave(function () {
            $(this).children("ul").stop().slideUp();
        });
    });
    ```

	- 京东轮播图

    ```js
    $(function () {
        var count = 0;
        $(".arrow-right").click(function () {
            count++;
            if(count == $(".slider li").length){
                count = 0;
            }
            console.log(count);
            //让count渐渐的显示，其他兄弟渐渐的隐藏
            $(".slider li").eq(count).fadeIn().siblings("li").fadeOut();
    });
    
    $(".arrow-left").click(function () {
            count--;
            if(count == -1){
                count = $(".slider li").length - 1;
            }
            console.log(count);
            //让count渐渐的显示，其他兄弟渐渐的隐藏
            $(".slider li").eq(count).fadeIn().siblings("li").fadeOut();
        })
    });
    ```

### 自定义动画

- 类似于自己封装的动画函数,但是更强大
- 语法:   .animate( properties [, duration ] [, easing ] [, complete ] )
- 使用如下: 

    ```js
    $(function () {
        $("input").eq(0).click(function () {
            //第一个参数：对象，里面可以传需要动画的样式
            //第二个参数：speed 动画的执行时间
            //第三个参数：动画的执行效果
            //第四个参数：回调函数
            
            //默认:swing
            $("#box1").animate({left:800}, 8000);
            
            //swing:秋千 摇摆 慢->快->慢
            $("#box2").animate({left:800}, 8000, "swing");
            
            //linear:线性 匀速
            $("#box3").animate({left:800}, 8000, "linear", function () {
            console.log("hahaha");
            });
        })
    });
    ```

### delay方法

delay方法用于在两个动画之间插入时间间隔,让两个动画之间有一定的等待时间;

```js
$(function () {
    //显示2000ms之后再消失
    $("div").fadeIn(1000).delay(2000).fadeOut(1000);
});
```

### 动画队列

- 动画队列
    - 对话队列描述 -- 如下图:

        ```js
        $(function () {
        $("#btn").click(function () {
                //把这些动画存储到一个动画队列里面
                $("div").animate({left: 800})
                .animate({top: 400})
                .animate({width: 300,height: 300})
                .animate({top: 0})
                .animate({left: 0})
                .animate({width: 100,height: 100})
                })
        });
        ```

    > 为一个对象添加了6个动画,这些动画会存放在一个队列(queue)中, 依次执行.

    - 动画队列的优缺点:
        - 优点: 为一个对象添加的多个动画不会丢失,以此有顺序的执行;
        - 缺点:为一个对象添加多个动画, 如何用户多次触发这个动画的话, 动画会"慢慢地依次执行很久".

- stop方法
    - stop方法作用: 用于停止`当前对象`的`当前正在执行`的动画;
    - 使用: 在特定的动画前面调用stop()方法即可 `$("input").stop().animate()` ;
    - 参数:
        - clearQueue(false): 是否清除动画队列 true false
        - jumpToEnd(false): 是否跳转到当前动画的最终效果 true false

## jQuery节点操作

### 创建节点

```js
var $li = $('<a href="http://www.baidu.cn">百度</a>');
```
### clone节点

- clone方法可以克隆节点;
	- 默认值为false --> 深拷贝: 克隆标签和里面的所有内容
    - 如果设置为true -->还拷贝绑定的事件;

### 添加节点

- 用法

    ```js
    //添加到子元素的最后面
    $("div").append($("p"));
    $("p").appendTo("div"); //比上面更方便
    //添加到子元素的最前面
    $("div").prepend($("p"));
    $("p").prependTo("div"); //比上面更方便
    //添加到元素的前面后面(兄弟)
    $('div').after($("p"));
    $("p").insertAfter("div") //比上面更方便
    //添加到元素的前面前面(兄弟)
    $('div').before($("p"));
    $("p").insertBefore("div") //比上面更方便
    ```

- 案例 -- 城市选择

    ```js
    $(function () {
        $("#btn1").click(function () {
            $("#src-city>option").appendTo("#tar-city");
        });
        $("#btn2").click(function () {
            $("#src-city").append($("#tar-city>option"));
        });
        $("#btn3").click(function () {
            $("#src-city>option:selected").appendTo("#tar-city");
        });
        $("#btn4").click(function () {
            $("#src-city").append($("#tar-city>option:selected"));
        });
    });
    ```

- 案例 -- 微博发布

    ```js
    $(function () {
        $("#btn").click(function () {
            if ($("#txt").val().trim().length == 0) {
                return;
            }
            //就是文本框的值
            $("<li></li>").text($("#txt").val()).prependTo("#ul");
            $("#txt").val("");
        })
    });
    ```

### html/text

获取第一个元素, 或设置所有元素的html/text内容

### 删除节点

1. empty方法: 把`所选元素的子元素清空` 
    `$("div").empty();`
2. remove方法: 把`所选元素全部删除`
    `$("div").remove();`
3. detach方法: The .detach() method is the same as .remove(), except that .detach() keeps all jQuery data associated with the removed elements. This method is useful when removed elements are to be reinserted into the DOM at a later time.
4. html方法: `不推荐 <-- 内存泄漏` --  只是里面的内容删除了, 绑定的事件等并没有处理. 一直占用内存(泄漏).

## jQuery特殊属性操作

### val

> 说明: `大部分特殊属性也可以使用attr方法获取/设置`. 但是,使用特殊的方法会更方便.

- `val()`方法: 
    - 操作`表单(input, select and textarea)`的元素的值习惯性用val方法. 
	- 使用方式: 
        - 获取 - 不传参
        - 设置 - 传参
	- 案例: 京东搜索框

        ```js
        $("#txt").focus(function () {
            //如果是默认值，清空内容
            if($(this).val() === "洋酒"){
                $(this).val("");
            }
        });
        
        $("#txt").blur(function () {
            if($(this).val() === ""){
                $(this).val("洋酒");
            }
        });
        ```

### html/text

- html方法相当于innerHTML text方法相当于innerText
- 区别：
	- html方法会识别html标签;
	- text方法会那内容直接当成字符串，并不会识别html标签。

```js
//设置内容
$(“div”).html(“<span>这是一段内容</span>”);
//获取内容
$(“div”).html()

//设置内容
$(“div”).text(“<span>这是一段内容</span>”);
//获取内容
$(“div”).text()
```

### width/height相关

二者用于: 设置或者获取高度

```js
console.log($("div").width()); //width
console.log($("div").innerWidth());//padding+width
console.log($("div").outerWidth());//padding+width+border
console.log($("div").outerWidth(true));//padding+width+border+margin

//带参数表示设置高度
$(“img”).height(200);
//不带参数获取高度
$(“img”).height();
//获取网页可视区宽度
$(window).width();
//获取网页可视区高度
$(window).height();

//需要获取页面可视区的宽度和高度
$(window).resize(function () {
        console.log($(window).width());
        console.log($(window).height());
});
```

### scrollTop/scrollLeft方法

- 设置或者获取垂直滚动条的位置

    ```js
    $(function () {
        $(window).scroll(function () {
            console.log($(window).scrollTop());
            console.log($(window).scrollLeft());
        });
    });
    ```

- 【案例：仿腾讯固定菜单栏案例】

    ```js
    $(function () {
        $(window).scroll(function () {
            //判断卷去的高度超过topPart的高度
            //1. 让navBar有固定定位
            //2. 让mainPart有一个marginTop
            if ($(window).scrollTop() >= $(".top").height()) {
                $(".nav").addClass("fixed");
                $(".main").css("marginTop", $(".nav").height() + 10);
            } else {
                $(".nav").removeClass("fixed");
                $(".main").css("marginTop", 10);
            }
        });
    });
    ```

- 【案例：小火箭返航案例】

    ```js
    //当页面超出去1000px的时候，让小火箭显示出来,如果小于1000，就让小火箭隐藏
    $(window).scroll(function () {
        if ($(window).scrollTop() >= 1000) {
            $(".actGotop").stop().fadeIn(1000);
        } else {
            $(".actGotop").stop().fadeOut(1000);
        }
    });

    /* //为什么使用 $("html,body") 获取对象
    function getScroll(){
        return {
            left:window.pageYOffset || document.documentElement.scrollLeft || document.body.scrollLeft || 0,
            top:window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0
        }
    } */

    //在外面注册
    $(".actGotop").click(function () {
        $("html,body").stop().animate({scrollTop:0},3000);//3s缓慢到顶部
        // $(window).scrollTop(0);//立刻到顶部
        })
    });
    ```

### offset/position方法

```js
//获取元素的相对于document的位置
console.log($(".son").offset());
//获取元素相对于有定位的父元素的位置
console.log($(".son").position());
```

## jQuery事件机制

### jQuery事件发展历程

> JavaScript中已经学习过了事件，但是jQuery对JavaScript事件进行了封装，增加并扩展了事件处理机制。jQuery不仅提供了更加优雅的事件处理语法，而且极大的增强了事件的处理能力。

jQuery事件的进化流程: `简单事件绑定>>bind事件绑定>>delegate事件绑定>>on事件绑定(推荐)`

1. 简单事件绑定

- 优点: 使用方便--直接使用对应的方法即可,如: 
	- `click(handler)`-->单击事件
	- `mouseenter(handler)`-->鼠标进入事件
	- `mouseleave(handler)`-->鼠标离开事件
- 缺点：不能同时注册多个事件

2. bind方式注册事件

- 优点: 可以同时绑定多个事件:
	- 第一个参数：事件类型
	- 第二个参数：事件处理程序

    ```js
    //多个事件->一个处理函数
    $("p").bind("click mouseenter", function () {//});

    //多个事件->多个处理函数
    $("p").bind({
        click: function () {// },
        mouseenter: function () {//}
    });
    ```

- 缺点：不支持动态事件绑定(给div里面通过js新添加一个p,p不会有事件)

3. delegate注册委托事件

- 原理: 委托事件是通过事件冒泡实现的,p虽然没有注册事件,但是点击p会冒泡到父元素div,div注册了事件
- 给`父元素注册delegate委托事件，最终事件(click mouseenter等)还是有子元素`来执行。
	- 第一个参数：selector，要绑定事件的元素
	- 第二个参数：事件类型
	- 第三个参数：事件处理函数
- 优点:能为动态添加到子对象添加事件; 如果有很多个子元素,只需要注册一次,消耗低;
- 缺点:只能注册委托事件,简单的事件不行; --> 接口不统一

    ```js
    //要给div注册一个委托事件,但是最终不是由执行，而是有p执行
    //1. 动态创建的也能有事件 :缺点：只能注册委托事件
    $("#box").delegate("p", "click", function () {
        //alert("呵呵");
        console.log(this);
    });
    ```

4. on注册事件(进化的最终产物)

见下节->

### on方法事件注册

- on注册事件->`最终版`
    - jQuery1.7之后，jQuery用on统一了所有事件的处理方法。
    - 最现代的方式，兼容zepto(移动端类似jQuery的一个库)，强烈建议使用。
    - on方法语法: `$(selector).on(events[,selector][,data],handler)`;
        - 第一个参数：`events`，绑定事件的名称可以是由空格分隔的多个事件（标准事件或者自定义事件）
        - 第二个参数：`selector`, 执行事件的后代元素（可选），如果没有后代元素，那么事件将有自己执行。
        - 第三个参数：`data`，传递给处理函数的数据，事件触发的时候通过event.data来使用（不常使用）
        - 第四个参数：`handler`，事件处理函数
    - 既可以注册简单事件,又可以注册委托事件:
        - on注册简单事件--`无selector参数`

            ```js
            $("#btn").on("click", function () {
                    $("<p>我是新建的p元素</p>").appendTo("div");
            });
            ```

        - on注册委托事件--`有selector参数`

            ```js
            $("div").on("click", "p", function () {
                    alert("呵呵")
            });
            ```

- 事件的执行顺序
    - 事件的执行顺序如下: 
        - 自身直接注册的简单事件
        - 父元素委派的事件
        - 父级元素直接注册的事件(<--冒泡)

        ```js
        //结构: div>p
        // 这个是p自己注册的事件（简单事件）--第一执行
        $("p").on("click", function () {
            alert("呵呵哒");
        });

        //给div自己执行的 第三执行
        $("div").on("click", function () {
            alert("呜呜呜");
        });

        //给div里面的p执行 委托事件 --第二执行
        $("div").on("click", "p", function () {
            alert("嘿嘿嘿")
        });
        ```

### 事件解绑

- unbind方式（不用）	
    - $(selector).unbind(); //解绑所有的事件
    - $(selector).unbind("click"); //解绑指定的事件
		undelegate方式（不用）	
    - $(selector).undelegate(); //解绑所有的delegate事件
    - $(selector).undelegate( “click” ); //解绑所有的click事件
		off方式（`推荐`）	
    - `$(selector).off()`;  // 解绑匹配元素的所有事件
    - `$(selector).off("click")`;  // 解绑匹配元素的click事件

### 触发事件

事件的触发有两种方式

```js
//toggle：切换 trigger：触发
$("#btn").on("click",function () {
    //触发p元素的点击事件
    $("p").click();//方式一
    $("p").trigger("click");//方式二
});
```

### 事件对象

- jQuery事件对象其实就是js事件对象的一个封装，处理了兼容性。
	- screenX和screenY 对应屏幕最左上角的值
	- clientX和clientY 距离页面左上角的位置（忽视滚动条）
	- pageX和pageY 距离页面最顶部的左上角的位置（会计算滚动条的距离）
	
	- event.keyCode 按下的键盘代码
	- event.data 存储绑定事件时传递的附加数据
	
	- event.stopPropagation() 阻止事件冒泡行为
	- event.preventDefault() 阻止浏览器默认行为
	- return false:既能阻止事件冒泡，又能阻止浏览器默认行为。
- event.data解释

    ```js
    //100，注册的时候的时候，把100传到事件里面去。
    var money = 100;
    var di = {
        "name": "yaro",
        "age": 12
    };
    //on(types, selector, data, callback)
    //使用on方法的时候，可以给data参数传一个值，可以在事件里面通过e.data获取到。
    $("div").on("click", di, function (e) {
        console.log(e);
        console.log("哈哈，我有" + e.data);
    });
    ```

- 案例-钢琴版导航（加强）

    ```js
    //按下1-9这几个数字键，能触发对应的mouseenter事件
    $(document).on("keydown", function (e) {
        if(flag) {
            flag = false;
            //获取到按下的键
            var code = e.keyCode;
            if(code >= 49 && code <= 57){
                //触发对应的li的mouseenter事件
                $(".nav li").eq(code - 49).mouseenter();
            }
        }
    });

    $(document).on("keyup", function (e) {
        flag = true;
        //获取到按下的键
        var code = e.keyCode;
        if(code >= 49 && code <= 57){
            //触发对应的li的mouseenter事件
            $(".nav li").eq(code - 49).mouseleave();
        }
    });
    ```

## jQuery知识点补充

### 链式编程

- 通常情况下,"设置"操作返回jQuery对象,可以链式编程;
- 而"获取"操作,会返回获取到的相应的值,无法返回jQuery对象,故不能链式编程;
- end()方法;
	- jQuery链式编程中,每次事件主体(对象)的改变,都会把前一个的对象保存下来prevObj;
	- 通过end()方法,可以切换到前一个对象,方便继续链式编程。
- 【案例：五角星评分案例.html】

    ```html
    <script src="jquery-1.12.4.js"></script>
    <script>
    $(function () {
        //1. 给li注册鼠标经过事件，让自己和前面所有的兄弟都变成实心
        var wjx_k = "☆";
        var wjx_s = "★";
        $(".comment>li").on("mouseenter", function () {
            $(this).text(wjx_s).prevAll().text(wjx_s);
            console.log($(this).text(wjx_s).prevAll().text(wjx_s));
            console.dir($(this).text(wjx_s).prevAll().text(wjx_s));
            $(this).nextAll().text(wjx_k);
        });
        
        //2. 给ul注册鼠标离开时间，让所有的li都变成空心
        $(".comment").on("mouseleave", function () {
            $(this).children().text(wjx_k);
            //再做一件事件，找到current，让current和current前面的变成实心就行。
            $("li.current").text(wjx_s).prevAll().text(wjx_s);
        });
        
        //3. 给li注册点击事件
        $(".comment>li").on("click", function () {
            $(this).addClass("current").siblings().removeClass("current");
        });
    });
    </script>

    <ul class="comment">
        <li>☆</li>
        <li>☆</li>
        <li>☆</li>
        <li>☆</li>
        <li>☆</li>
    </ul>
    ```

### each方法

- jQuery的隐式迭代会对所有的DOM对象设置相同的值，但是如果我们需要给每一个对象设置不同的值的时候，就需要自己进行迭代了。
- 可以手动的通过for循环来遍历/设置(jQuery对象本质上就是DOM对象集合--伪数组);
- jQuery内置的each方法也可以实现遍历jQuery对象集合,为每个匹配的元素执行一个函数.
- 语法: $(selector).each(function(index,element){});
	- 参数一: 表示当前元素在所有匹配元素中的索引号
	- 参数二: 表示当前元素（DOM对象）
	- `JS的数组方法中的foreach的参数刚好和这个反过来foreach(function(element,index)`;

    ```js
    $(function () {
        //for循环--遍历
        for (var i = 0; i < $("li").length; i++) {
            $("li").eq(i).css("opacity", (i + 1) / 10);
        }
        //each方法--遍历
        $("li").each(function (index, element) {
            $(element).css("opacity", (index + 1) / 10);
        })
    });
    ```

### 多库共存

加入$符与别的JS库中的特点标识冲突,可以释放$符,或者重新命名.

```js
//释放$的控制权,可以使用"本体"--jQuery
$.noConflict();
jQuery(function () {});

//也可以自己制定特定的标识符
var my$ = $.noConflict();
my$(function () {});
```

## jQuery插件

> 背景:   • 插件：jquery不可能包含所有的功能，我们可以通过插件扩展jquery的功能。  • jQuery有着丰富的插件，使用这些插件能给jQuery提供一些额外的功能。

### jquery.color.js插件

- jQuery的animate动画不支持颜色的渐变，但是使用了jquery.color.js后，就可以支持颜色的渐变了。
- 使用插件的步骤:
	1. 引入jQuery文件
	2. 引入插件（如果有用到css的话，需要引入css）
    3. 使用插件

### jquery.lazyload.js插件

- 使用场景: 加入一个页面很多屏,而且很多图片, 就没有必要一次性全部加载,只加载当前屏即可.
- 官网: https://github.com/tuupola/jquery_lazyload

```js
<img class="lazy" data-original="02.gif" alt="">

$(function () {
    $("img.lazy").lazyload();
});
```

### jquery.ui.js插件

- jQueryUI专指由jQuery官方维护的UI方向的插件。
- 官方API：http://api.jqueryui.com/category/all/
- 其他教程：jQueryUI教程
- 基本使用:
	1. 引入jQueryUI的样式文件
	2. 引入jQuery
	3. 引入jQueryUI的js文件
	4. 使用jQueryUI功能
- 使用jquery.ui.js实现新闻模块的案例

    ```js
    $(function () {
        $(".drag-wrapper").draggable({
            handle:".drag-bar"
        });
        $(".sort-item").sortable({
            opacity:0.3
        });
        $(".resize-item").resizable({
            handles:"s"
        });
    });
    ```

### 制作jquery插件

- 原理：jquery插件其实说白了就是给jquery原型对象增加一个新的方法，让jquery对象拥有某一个功能。
- jQuery的原型对象prototype的别名为fn --> 更方便书写; 
- 返回this便可以实现链式编程: 

    ```js
    $.fn.bgColor = function (color) {
        //this是一个jq对象
        this.css("backgroundColor", color);
        return this;
    };
    ```

- 方法: 通过给$.fn添加方法就能够扩展jquery对象

    ```js
    $.fn. pluginName = function() {};
    ```

- 制作手风琴插件

    ```js
    $.fn.accordion = function (colors, width) {
        colors = colors || [];
        width = width || 0;
        
        var $li = this.find("li");
        var boxLength = this.width();
        var maxLength = boxLength - ($li.length - 1) * width;
        var avgLength = boxLength / $li.length;
        
        //更改li的颜色
        $li.each(function (i, e) {
            $(e).css("backgroundColor", colors[i]);
        });
        
        //给li注册鼠标经过事件
        $li.on("mouseenter", function () {
            $(this).stop().animate({width: maxLength}).siblings().stop().animate({width: width})
        });
        
        $li.on("mouseleave", function () {
            $li.stop().animate({width: avgLength});
        });
    };

    //插件测试
    <script src="jquery-1.12.4.js"></script>
    <script src="jquery.accordion.js"></script>
    <script>
    $(function () {
        var colors = ["red","yellow","green", "cyan", "pink","hotpink", "blue", "yellowgreen","greenyellow", "skyblue"];
        $("#box").accordion(colors, 20);
    });
    </script>
    ```
