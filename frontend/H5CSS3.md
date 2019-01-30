# H5CSS3

## HTML5新特性

### H5概述

[MDN-HTML5官网](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

- 语义：
    - HTML4.01、XHTML1.0中学习了很多语义的标签，div、p、ul、ol等等。
    - HTML5增加了很多语义的标签、表单标签。今天讲，用巨快速度讲。
-  连通性：
    - web socket ， 服务器和浏览器之间能够通过web socket（网络套接字）来保持持久联通了。
    - HTTP是无连接的，不能使浏览器和服务器之间保持持久连接。比如我们的聊天室，感觉浏览器和服务器有持久连接，感觉别人一说话，你就能看见更新，其实没有持久连接。聊天室的原理就是通过setInterval每1000毫秒发出HTTP请求，查询服务器，渲染DOM页面。实际上没有持久连接的概念。
    - 但是HTML5中提出了一个web socket的概念，能够让浏览器和服务器有持久连接。Node.js课程上看这个东西的神奇威力，联机版的俄罗斯方块。
-  离线 & 存储：
    - 离线：我们之前的网页，一旦脱机（没网）就不能访问了。但是，我们急着上飞机，在空中没有wifi，能不能在机场提前把一个网站的所有网页都离线保存呢？能不能在飞机上继续阅读刚才保存的离线网站呢？HTML5给了我们新的API。
    - 存储：我们之前开发程序，所有的内容持久化都是通过MySQL数据库，所谓的持久化指的就是电脑断电、关机都不丢失的数据。之前我们是无法通过JS来操作数据库的，但是HTML5中提供了JS能够操作的迷你数据库，叫做localStorage、session storage。
-  多媒体
    - 音频视频标签，audio、video 标签。
    - 3D, 图像 & 效果
    - 增加了重要API： canvas、WebGL、svg
    - 水果忍者，就是canvas游戏。我们也要用canvas写俄罗斯方块、天天爱消除、flappy bird、物理游戏。
-  性能 & 集成
    - 增加了web worker能够让js操作线程，之前JS是单线程的，不能操作多线程，HTML5诞生能够让JS操作线程了（现在浏览器支持极差，只有把玩的意义）
    - 增加了新的JS的API：拖放API、全屏API等等
-  设备访问
    - 使用地理位置、摄像头、触控事件、检测设备方向。都是给移动端提供的API
-  样式:CSS3
    - 也就是说HTML5是一个大概念，里面包括了HTML的增强（标签语义化、canvas）、CSS的增强（CSS3）、JS的增强（ECMAScript5、6）、浏览器的API增强（拖放、全屏、摄像头）。

- 兼容问题：ie9 以上的版本；

- 文档类型设定：
    - HTML:        sublime 输入  html:4s
    - XHTML:      sublime 输入  html:xt
    - HTML5        sublime 输入  html:5       <!DOCTYPE html>
- 字符设定：
    - `<meta http-equiv="charset" content="utf-8">`：HTML与XHTML中建议这样去
    - `<meta charset="utf-8">`：HTML5的标签中建议这样去写。

### H5新规范

- 新的骨架

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Document</title>
</head>
<body>

</body>
</html>
```

HTML5的doctype非常简单。表明你的HTML内容使用HTML5，只需要简单的使用：`<!DOCTYPE html>`

> 这个DTD是IE6、7不支持，IE8开始支持。

字符集的设置，现在非常的简单：`<meta charset="UTF-8" />`

> IE8开始支持，为了更多用户的兼容，如果要兼容IE6、7还是要用原来的写法。

- 新的规范

    - 规范都放宽标准了，但是我们还是要保持风骨，以XHTML1.0严格要求自己。XHTML系列，在HTML5诞生之后停止维护了。
    - HTML5中规定标签不一定小写字母了：
        `<DiV>我是一个盒子</DiV>`
    - HTML5中规定自封闭标签不一定有反斜杠了：
        `<img src="images/1.jpg" alt="">`
    - HTML5中规定所有的引号可以不加了：
        `<img src=images/1.jpg alt=我是一个图图 >`
    - HTML5中规定所有的type属性都可以不写了：
        `<link rel="stylesheet" href="1.css">`
    - IE6、7对上面的支持不好。
        但是作为老一代前端工程师，我们要保持风骨，在HTML5中也要用XHTML的规范严格要求自己。

### H5新标签

#### 常用新标签

- header：定义文档的页眉 头部
- nav：定义导航链接的部分
- footer：定义文档或节的页脚 底部
- article：定义文章。
- section：定义文档中的节（section、区段）
- aside：定义其所处内容之外的内容 侧边

```html
<header> 语义 :定义页面的头部  页眉</header>
<nav>  语义 :定义导航栏 </nav> 
<footer> 语义: 定义 页面底部 页脚</footer>
<article> 语义:  定义文章</article>
<section> 语义： 定义区域</section>
<aside> 语义： 定义其所处内容之外的内容 侧边</aside>
```
​
- datalist 标签定义选项列表。请与 input 元素配合使用该元素

```html
<input type="text" value="请输入明星" list="star"/>
<datalist id="star">
    <option value="刘德华">刘德华</option>
    <option value="刘若英">刘若英</option>
    <option value="刘晓庆">刘晓庆</option>
    <option value="戚薇">戚薇</option>
    <option value="戚继光">戚继光</option>
</datalist>
```
​
- fieldset 元素可将表单内的相关元素分组，打包 legend 搭配使用

```html
<fieldset>
    <legend>用户登录</legend>  标题
    用户名: <input type="text"><br /><br />
    密　码: <input type="password">
</fieldset>
```
​
- 其他语义化标签 -- 兼容差
    - 图和它的标题语义：
    
        ```html
        <figure>
        <img src="images/1.jpg" alt="">
        <figcaption>范冰冰和李晨结婚照</figcaption>
        </figure>
        ```
    
    - 进度条语义：`<progress value="60" max="100">60%</progress>`
    
    - 地址语义：`<address>北京市昌平区宏福大厦</address>`
    
    - 高亮语义：`我们一定要<mark>好好学习，天天向上</mark>`
    - 注释语义，拼音语义：

        ```html
        <ruby>
        漢 <rp>(</rp><rt>hàn</rt><rp>)</rp>
        字 <rp>(</rp><rt>zì</rt><rp>)</rp>
        </ruby>
        ```

#### 新增的input type属性值

| 类型****     | 使用示例****            | 含义****             |
| ------------ | ----------------------- | -------------------- |
| email****    | <input type="email">    | 输入邮箱格式         |
| tel****      | <input type="tel">      | 输入手机号码格式     |
| url****      | <input type="url">      | 输入url格式          |
| number****   | <input type="number">   | 输入数字格式         |
| search****   | <input type="search">   | 搜索框（体现语义化） |
| range****    | <input type="range">    | 自由拖动滑块         |
| time****     | <input type="time">     | 小时分钟             |
| date****     | <input type="date">     | 年月日               |
| datetime**** | <input type="datetime"> | 时间                 |
| month****    | <input type="month">    | 月年                 |
| week****     | <input type="week">     | 星期 年              |

#### 表单常用新属性

| 属性****         | 用法****  | 含义****                                                     |
| -------- | --------------- | -------------------- |
| placeholder****  | <input type="text"   placeholder="请输入用户名"> | 占位符 当用户输入的时候 里面的文字消失   删除所有文字，自动返回 |
| autofocus****    | <input type="text" autofocus>                    | 规定当页面加载时 input   元素应该自动获得焦点                |
| multiple****     | <input type="file" multiple>                     | 多文件上传                                                   |
| autocomplete**** | <input type="text"   autocomplete="off">         | 规定表单是否应该启用自动完成功能   有2个值，一个是on 一个是off on 代表记录已经输入的值 1.autocomplete 首先需要提交按钮 2.这个表单您必须给他名字 |
| required****     | <input type="text" required>                     | 必填项 内容不能为空                                          |
| accesskey****    | <input type="text" accesskey="s">                | 规定激活（使元素获得焦点）元素的快捷键   采用 alt + s的形式  |

#### 多媒体标签

- embed（会使用）：标签定义嵌入的内容--HTML4.01想插入音频、视频，都必须借助flash。
    - embed可以用来插入各种多媒体，格式可以是 Midi、Wav、AIFF、AU、MP3等等。url为音频或视频文件及其路径，可以是相对路径或绝对路径。
    - 因为兼容性问题，我们这里只讲解 插入网络视频， 后面H5会讲解 audio 和video 视频多媒体。 
    - 优酷，土豆，爱奇艺，腾讯、乐视：**先上传 - 在分享**
    - `<embed src="http://player.youku.com/player.php/sid/XMTI4MzM2MDIwOA==/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>`

- audio：播放音频
    HTML5通过`<audio>`标签来解决音频播放的问题。
    使用相当简单，如下所示

    ```html
    <!-- 通过src指定音频文件路径即可 -->
    <audio src="./music/xxx.mp3"></audio>
    ```

    - 并且可以通过附加属性可以更友好控制音频的播放，如：
        - autoplay 自动播放
        - controls 是否显不默认播放控件
        - loop 循环播放 如果这个属性不写 默认播放一次 loop 或者 loop = “loop” 表示无限循环
        - 由于版权等原因，不同的浏览器可支持播放的格式是不一样的，如下图供参考

    - 多浏览器支持的方案，如下图
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoe25u0nsj20lt04fgmj.jpg)

    - `<source>` 标签允许您规定可替换的视频/音频文件供浏览器根据它对媒体类型或者编解码器的支持进行选择
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoe2ksfbaj20lc06q79b.jpg)

- video：播放视频
    同音频播放一样，<video>使用也相当简单，如下图

    ```html
    <!-- 通过src指定视频文件路径即可 -->
    <video src="./video/xxx.mp4"></video>
    ```

    同样，通过附加属性可以更友好的控制视频的播放
    - autoplay 自动播放
    - controls 是否显示默认播放控件
    - loop 循环播放
    - width 设置播放窗口宽度
    - height 设置播放窗口的高度

    由于版权等原因，不同的浏览器可支持播放的格式是不一样的，如下图供参考
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoesmfdhlj20m604g79b.jpg)

    多浏览器支持的方案，如下:

    ```html
    <!-- 通过src指定多个视频文件路径即可 -->
    <video src="./video/xxx.ogg"></video>
    <video src="./video/xxx.mp4"></video>
    您的浏览器不支持HTML视频播放功能
    ```

- HTML5提供的audio video标签也提供了JS的API.
    比如监听暂停、播放: 
        - onpause事件
        - onplay事件
    也有控制它的方法：
        - pause()
        - play()

### H5-DOM扩展

- 获取元素

```js
document.getElementsByClassName ('class'); 
//通过类名获取元素，以伪数组形式存在。
document.querySelector('selector');
//通过CSS选择器获取元素，符合匹配条件的第1个元素。
document.querySelectorAll('selector'); 
//通过CSS选择器获取元素，以伪数组形式存在。
```

- 类名操作

```js
Node.classList.add('class'); 
//添加class
Node.classList.remove('class'); 
//移除class
Node.classList.toggle('class'); 
//切换class，有则移除，无则添加
Node.classList.contains('class'); 
//检测是否存在class
```

- 自定义属性

> 在HTML5中我们可以自定义属性，其格式如下`data-*=""`

```html
<div id="demo" data-my-name="itcast" data-age="10">
<script>
    // Node.dataset是以对象形式存在的，当我们为同一个DOM节点指定了多个自定义属性时，
    // Node.dataset则存储了所有的自定义属性的值。
    var demo = document.querySelector(反馈);
    //获取
    //注：当我们如下格式设置时，则需要以驼峰格式才能正确获取
    var name = demo.dataset['myName'];
    var age = demo.dataset['age'];
    //设置
    demo.dataset['name'] = 'web developer';
<script/>
```

### H5新增API

- 全屏方法

> HTML5规范允许用户自定义网页上任一元素全屏显示。

- Node.requestFullScreen() 开启全屏显示
- Node.cancelFullScreen() 关闭全屏显示
- 由于其兼容性原因，不同浏览器需要添加前缀如：
    webkit内核浏览器：webkitRequestFullScreen、webkitCancelFullScreen，如chrome浏览器。
    Gecko内核浏览器：mozRequestFullScreen、mozCancelFullScreen，如火狐浏览器。
- document.fullScreen检测当前是否处于全屏
    不同浏览器需要添加前缀
    document.webkitIsFullScreen、document.mozFullScreen

- 多媒体

> 自定义多媒体

**方法**

| 方法           | 描述                                    |
| -------------- | --------------------------------------- |
| addTextTrack() | 向音频/视频添加新的文本轨道             |
| canPlayType()  | 检测浏览器是否能播放指定的音频/视频类型 |
| load()         | 重新加载音频/视频元素                   |
| play()         | 开始播放音频/视频                       |
| pause()        | 暂停当前播放的音频/视频                 |

**属性**

| 属性                | 描述                                                       |
| ------------------- | ---------------------------------------------------------- |
| audioTracks         | 返回表示可用音轨的 AudioTrackList 对象                     |
| autoplay            | 设置或返回是否在加载完成后随即播放音频/视频                |
| buffered            | 返回表示音频/视频已缓冲部分的 TimeRanges 对象              |
| controller          | 返回表示音频/视频当前媒体控制器的 MediaController 对象     |
| controls            | 设置或返回音频/视频是否显示控件（比如播放/暂停等）         |
| crossOrigin         | 设置或返回音频/视频的 CORS 设置                            |
| currentSrc          | 返回当前音频/视频的 URL                                    |
| currentTime         | 设置或返回音频/视频中的当前播放位置（以秒计）              |
| defaultMuted        | 设置或返回音频/视频默认是否静音                            |
| defaultPlaybackRate | 设置或返回音频/视频的默认播放速度                          |
| duration            | 返回当前音频/视频的长度（以秒计）                          |
| ended               | 返回音频/视频的播放是否已结束                              |
| error               | 返回表示音频/视频错误状态的 MediaError 对象                |
| loop                | 设置或返回音频/视频是否应在结束时重新播放                  |
| mediaGroup          | 设置或返回音频/视频所属的组合（用于连接多个音频/视频元素） |
| muted               | 设置或返回音频/视频是否静音                                |
| networkState        | 返回音频/视频的当前网络状态                                |
| paused              | 设置或返回音频/视频是否暂停                                |
| playbackRate        | 设置或返回音频/视频播放的速度                              |
| played              | 返回表示音频/视频已播放部分的 TimeRanges 对象              |
| preload             | 设置或返回音频/视频是否应该在页面加载后进行加载            |
| readyState          | 返回音频/视频当前的就绪状态                                |
| seekable            | 返回表示音频/视频可寻址部分的 TimeRanges 对象              |
| seeking             | 返回用户是否正在音频/视频中进行查找                        |
| src                 | 设置或返回音频/视频元素的当前来源                          |
| startDate           | 返回表示当前时间偏移的 Date 对象                           |
| textTracks          | 返回表示可用文本轨道的 TextTrackList 对象                  |
| videoTracks         | 返回表示可用视频轨道的 VideoTrackList 对象                 |
| volume              | 设置或返回音频/视频的音量                                  |

**事件**

| 事件           | 描述                                         |
| -------------- | -------------------------------------------- |
| abort          | 当音频/视频的加载已放弃时                    |
| canplay        | 当浏览器可以播放音频/视频时                  |
| canplaythrough | 当浏览器可在不因缓冲而停顿的情况下进行播放时 |
| durationchange | 当音频/视频的时长已更改时                    |
| emptied        | 当目前的播放列表为空时                       |
| ended          | 当目前的播放列表已结束时                     |
| error          | 当在音频/视频加载期间发生错误时              |
| loadeddata     | 当浏览器已加载音频/视频的当前帧时            |
| loadedmetadata | 当浏览器已加载音频/视频的元数据时            |
| loadstart      | 当浏览器开始查找音频/视频时                  |
| pause          | 当音频/视频已暂停时                          |
| play           | 当音频/视频已开始或不再暂停时                |
| playing        | 当音频/视频在已因缓冲而暂停或停止后已就绪时  |
| progress       | 当浏览器正在下载音频/视频时                  |
| ratechange     | 当音频/视频的播放速度已更改时                |
| seeked         | 当用户已移动/跳跃到音频/视频中的新位置时     |
| seeking        | 当用户开始移动/跳跃到音频/视频中的新位置时   |
| stalled        | 当浏览器尝试获取媒体数据，但数据不可用时     |
| suspend        | 当浏览器刻意不获取媒体数据时                 |
| timeupdate     | 当目前的播放位置已更改时                     |
| volumechange   | 当音量已更改时                               |
| waiting        | 当视频由于需要缓冲下一帧而停止               |

- 地理定位

    > 在HTML规范中，增加了获取用户地理信息的API，
    > 这样使得我们可以基于用户位置开发互联网应用，
    > 即基于位置服务 (Location Base Service)

    - 获取当前地理信息

    ```
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback) 
    ```

    - 重复获取当前地理信息

    ```
    navigator. geolocation.watchPosition(successCallback, errorCallback)
    ```

    - 当成功获取地理信息后，会调用succssCallback，并返回一个包含位置信息的对象position。
    
    ```
    position.coords.latitude纬度
    position.coords.longitude经度
    position.coords.accuracy精度
    position.coords.altitude海拔高度
    ```

    - 当获取地理信息失败后，会调用`errorCallback`，并返回错误信息`error`
    - 在现实开发中，通过调用第三方API（如百度地图）来实现地理定位信息，这些API都是基于用户当前位置的，并将用位置位置（经/纬度）当做参数传递，就可以实现相应的功能。

- 本地存储

    > 随着互联网的快速发展，基于网页的应用越来越普遍，
    > 同时也变的越来越复杂，为了满足各种各样的需求，会经常性在本地存储大量的数据，
    > HTML5规范提出了相关解决方案。

    - 特性
        - 设置、读取方便
        - 容量较大，sessionStorage约5M、localStorage约20M
        - 只能存储字符串，可以将对象JSON.stringify() 编码后存储
    - window.sessionStorage
        - 生命周期为关闭浏览器窗口
        - 在同一个窗口(页面)下数据可以共享
    - window.localStorage
        - 永久生效，除非手动删除（服务器方式访问然后清除缓存）
        - 可以多窗口（页面）共享
    - 方法
        - setItem(key, value) 设置存储内容
        - getItem(key) 读取存储内容
        - removeItem(key) 删除键值为key的存储内容
        - clear() 清空所有存储内容

- 历史管理

    > 提供window.history，对象我们可以管理历史记录，
    > 可用于单页面应用，Single Page Application，可以无刷新改变网页内容。

    - pushState(data, title, url) 追加一条历史记录  
        - data用于存储自定义数据，通常设为null
        - title网页标题，基本上没有被支持，一般设为空
        - url 以当前域为基础增加一条历史记录，不可跨域设置
    - replaceState(data, title, url) 与pushState()基本相同; 不同之处在于replaceState()，只是替换当前url，不会增加/减少历史记录。
    - onpopstate事件，当前进或后退时则触发  

- 离线应用

    > HTML5中我们可以轻松的构建一个离线（无网络状态）应用，只需要创建一个cache manifest文件。

    - 优势
        - 1、可配置需要缓存的资源
        - 2、网络无连接应用仍可用
        - 3、本地读取缓存资源，提升访问速度，增强用户体验
        - 4、减少请求，缓解服务器负担
    - 缓存清单
        - 一个普通文本文件，其中列出了浏览器应缓存以供离线访问的资源，推荐使用.appcache为后缀名
        - 例如我们创建了一个名为demo.appcache的文件，然后在需要应用缓存在页面的根元素(html)添加属性manifest="demo.appcache"，路径要保证正确。
    - manifest文件格式
        - 1、顶行写CACHE MANIFEST
        - 2、CACHE: 换行 指定我们需要缓存的静态资源，如.css、image、js等
        - 3、NETWORK: 换行 指定需要在线访问的资源，可使用通配符
        - 4、FALLBACK: 换行 当被缓存的文件找不到时的备用资源
    - 其它
        - 1、CACHE: 可以省略，这种情况下将需要缓存的资源写在CACHE MANIFEST
        - 2、可以指定多个CACHE: NETWORK: FALLBACK:，无顺序限制
        - 3、#表示注释，只有当demo.appcache文件内容发生改变时或者手动清除缓存后，才会重新缓存。
        - 4、chrome 可以通过chrome://appcache-internals/工具和离线（offline）模式来调试管理应用缓存

- 文件读取

    HTML5新增内建对象，可以读取本地文件内容。

- 网络状态

    - 我们可以通过window.onLine来检测，用户当前的网络状况，返回一个布尔值
        - window.online用户网络连接时被调用
        - window.offline用户网络断开时被调用

## CSS3新选择器/特性

### 概述

- 历史
    - CSS3 是 层叠样式表(Cascading Style Sheets) 语言的最新进展，目的在于扩展 CSS2.1。 它为我们带来了许多期待已久的新特性， 例如圆角，阴影，gradients(渐变)，transitions(过渡) 或 animations(动画) ， 当然还有新的布局如 multi-columns ， flexible box 或 grid layouts。
    - CSS3是一个没有准确边界的一个概念，很难说某一个属性或者某一个选择器是不是CSS3的内容，还是CSS2.1内容。因为都是不同时期被浏览器厂商广泛采用，倒逼W3C把这个属性、选择器定为标准的。
    - CSS3为什么能发展这么快，百花齐放，源于CSS从创立之初就有一个规定，就是遇见不认识的选择器、属性，静默不报错，不影响后面能够识别的语句：

- 兼容性
    CSS3现在主要用于移动端，因为移动端没有IE浏览器，PC端真需要再等两年才能完全使用。

### 选择器

- 回顾

```
### 基础选择器：

1. 标签（或元素）选择器
2. 类选择器：
   - 多类名选择器：<div class="red font20">
   - 等价于 [class~=类名] 可能含有多个类名（空格隔开），所以用 ~
3. id选择器
   - 等价于[id=ID名] ; 
4. 通配符选择器：
   - 代表所有elements，实际开发时不用
   - CSS3中：
     - `ns|*` - 会匹配ns命名空间下的所有元素
     - `*|*` - 会匹配所有命名空间下的所有元素
     - `|*` - 会匹配所有没有命名空间的元素
5. 属性选择器：
   - `[attr]` 带有 attr 属性的元素。
   - `[attr=value] `带 attr 属性，且值为"value"的元素。
   - `[attr~=value]` 带 attr 属性，且值用空格分割后得到的列表中，含有"value"。
   - `[attr|=value]` 带 attr 属性，且值为“value”或是以“value-”为前缀。
   - `[attr^=value]` 带 attr 属性，且值是以"value"开头的元素。
   - `[attr$=value]` 带 attr 属性，且值是以"value"结尾的元素。
   - `[attr*=value] `带 attr 属性，且值包含有"value"的元素。
   - `[attr operator value i]` 带 attr 属性，且值匹配"value" [忽略属性值大小] 的元素。i（或I）。

### 组合选择器

1. （**邻弟**）相邻兄弟选择器 A+B
   - A B为兄弟；
   - 选择的目标为B；
   - A后面紧挨着的B；
2. （兄**弟**）普通兄弟选择器 A ~B
   - A B为兄弟；
   - 选择目标为B；
   - B在A的后面（不一定紧挨）；
3. 子选择器 A > B（用的少）
   - B是A的儿子；
   - 选择目标为B
4. 后代选择器 A B （用的最多）
   - B是A的后代；
   - 选择目标为B；

### 伪类：

- `:`   一个冒号
- 目的：指定要选择的元素的特殊状态（鼠标状态/元素的第n个…）。
- 链接伪类选择器：

   - a:link 未访问链接，效果同 a ，区别： a:link 只对含有href属性的a标签起作用。
   - a:visited       访问过的链接
   - a:hover       鼠标再连接上
   - a:active       选定的链接
   - 顺序不能颠倒，记忆：LVHA  LoVe HAte 或者 LV HAa好
   - 实际开发实例:

     a {
         color: #333333;
         text-decoration: none;
         font-size: 25px;
         font-weight: 700;
     }
     a:hover {
         color: #cc0000;
     }

### 伪元素：

- `::`   两个冒号
- 目的：允许您为元素的某些部分（before/after/first-letter/first-line/selection）设置样式。

### 交集/并集

- div, .red       表示div元素或.red类；
- div.red  表示 div元素且.red类
```

- 伪类选择器(CSS3)

    - :first-child :选取属于其父元素的首个子元素的指定选择器
    - :last-child :选取属于其父元素的最后一个子元素的指定选择器
    - :nth-child(n) ： 匹配属于其父元素的第 N 个子元素，不论元素的类型
    - :nth-last-child(n) ：选择器匹配属于其元素的第 N 个子元素的每个元素，不论元素的类型，从最后一个子元素开始计数。 n 可以是数字、关键词或公式
    - :hover这个选择器，在CSS3中，能够给任何元素使用了。IE7兼容各种元素:hover
    - :focus得到焦点时,当一个表单元素有焦点，那么就能够被:focus伪类选中。
    - :not反着选, 没有.haha类的p  `p:not(.haha)`，IE9兼容 
    -  :only-child 唯一的儿子: `p:only-child` --- 如果一个p是某一个元素的唯一的儿子，那么选择它
    - :empty  空标签, 当一个标签是完全首尾相接，没有任何的空格、tab、换行、文字，就是:empty: `<div></div>`   → 满足div:empty
    -  :checked 选中的,单选按钮、复选框，如果被勾选，那么能被伪类:checked选中 `input[type=”radio”]`:checked
    - :disabled和:enabled   可用不可用的表单 `<input type="text" disabled/>`

- 伪元素选择器(css3)

    > 之所以被称为伪元素，是因为他们不是真正的页面元素，html没有对应的元素，但是其所有用法和表现行为与真正的页面元素一样，可以对其使用诸如页面元素一样的css样式，表面上看上去貌似是页面的某些元素来展现，实际上是css样式展现的行为，因此被称为伪元素。
    - E::first-letter文本的第一个单词或字（如中文、日文、韩文等）
    - E::first-line 文本第一行；
    - E::selection 可改变**文本被选中的样式**；
    - E::before和E::after
    - 在E元素内部的开始位置和结束位创建一个元素，**该元素为行内元素**，且**必须要结合content属性使用（哪怕为空 "" ）**。

### 基础效果

#### 圆角边框

- border-radius属性，值可以是一个px为单位的数值，也可以是%为单位的百分比数值。
    > IE9开始兼容

    ```css
    div:nth-child(1){
        width: 200px;
        height: 200px;
        border: 1px solid #000;
        border-radius: 20px;
    }
    ```
 
- 如果border-radius足够大，是宽度、高度的一半，就是正圆。

    ```css
    div:nth-child(3){
        width: 600px;
        height: 200px;
        border: 1px solid #000;
        border-radius: 100px;
    }
    ```
 
- 可以分别描述四个角：

    ```css
    border-radius: 20px 40px 60px 80px;
    // 分别是左上角、右上角、右下角、左下角
    ```

- 也可以是三个数值：

    ```css
    border-radius: 20px 60px 80px;
    // 分别是：左上角、右上角和左下角、右下角
    ```
 
- 也可以通过小属性来层叠：

    ```css
    border-top-left-radius: 60px;
    border-top-right-radius: 60px;
    border-bottom-right-radius: 100px;
    border-bottom-left-radius:50px;
    ```
 
- 用百分比来设置border-radius不一样，可以综合设置圆弧占了直边的百分之几。

    ```css
    border-radius: 0% 100%;
    ```

#### 盒模型

- 盒子相关值： content padding border margin；
- 之前的盒模型设置 width / height 为content的宽/高，但是盒子在文档流中实际占用的位置（包括 padding，border）;
- 新的盒模型设置 width / height 为盒子在文档流中实际的宽/高（包括 padding，border）。
- 为了兼容之前的盒模型：增加 box-sizing 属性:
    - 默认值为 content-box(兼容之前的盒模型)；
    - 若设值为border-box（css3新盒模型）
- 优点：不需要设置盒子宽/高后，由于padding值的改变（撑开盒子），重新调整盒子的宽/高。

#### 前缀

- -webkit-	Google Chrome, Safari, Android Browser
- -moz-	Firefox
- -o-	Opera
- -ms-	Internet Explorer, Edge
- -khtml-	Konqueror


#### 阴影

- box-shadow

    - 标准的是5个参数，IE9开始兼容。

    ```css
    /*向右的偏移值、向下的偏移值、模糊半径、延展宽度、颜色。*/
    box-shadow: 2px 2px 2px 2px black;
    /*可以省略参数：*/
    box-shadow: 2px 2px 2px black; /*没有延展值。*/
    ```
    
    - 一个盒子可以有多个阴影，用逗号隔开：

    ```css
    box-shadow: 0px 0px 12px 10px red , 0px 0px 20px 20px blue ;
    ```
     
    - 通过写inset，表示内阴影：
    
    ```css
    box-shadow: inset 0px 0px 10px red;
    ```
     
    - 内阴影也可以有多个：
    
    ```css
    box-shadow: inset 0px 0px 10px red,
    inset 0px 0px 20px blue,
    0px 0px 10px green,
    0px 0px 20px orange;
    ```

- text-shadow

    text-shadow是文字阴影，只有四个参数，少了延展值，IE10开始兼容。
    
    ```css
    text-shadow: 1px 1px 1px red;
    ```

#### 背景

- 背景渐变
    - 兼容性问题很严重，我们这里之讲解线性渐变。
    - 语法格式：
        1. `background:-webkit-linear-gradient(渐变的起始位置， 起始颜色， 结束颜色)`；
        2. `background:-webkit-linear-gradient(渐变的起始位置， 颜色 位置， 颜色位置....)`；

- 前缀
    - 私有前缀：浏览器厂商把一些还处于实验性质的css属性，都加上了自己的前缀。
        - hrome的是-webkit-
        - 火狐是-moz-
        - E是-ms-
        - 欧朋是-o-
     
    - 所以一条属性要写很多个私有前缀的写法：
        ```css
        background-image: -webkit-linear-gradient(top,red,blue);
        background-image: -moz-linear-gradient(top,red,blue);
        background-image: -o-linear-gradient(top,red,blue);
        background-image: -ms-linear-gradient(top,red,blue);
        background-image: linear-gradient(top,red,blue);
        ```

- 背景缩放(CSS3)
    - background-size设置背景图片的尺寸，就像我们设置img的尺寸一样，在移动Web开发中做屏幕适配应用非常广泛。
    - 参数如下：
        1. 可以设置长度单位(px)或百分比（设置百分比时，参照盒子的宽高）；
        2. 设置为cover：短边缩放到盒子大小，长边按尺寸缩放（溢出部分隐藏），平时用cover 最多；
        3. 设置为contain：长边缩放到盒子大小，短边按尺寸缩放。

- 多背景(CSS3)
    - 以逗号分隔可以设置多背景，可用于自适应布局  做法就是 用逗号隔开就好了。
        - 一个元素可以设置多重背景图像。 
        - 每组属性间使用逗号分隔。 
        - 如果设置的多重背景图之间存在着交集（即存在着重叠关系），前面的背景图会覆盖在后面的背景图之上。
    - 如：`url(test1.jpg) no-repeat scroll 10px 20px/70px 90px ,url(test1.jpg) no-repeat scroll 10px 20px/110px 130px #aaa;`

### 高级效果

#### 过渡

- 过渡(css3)

    ```css
    div {
	width:100px;
	transition: width 2s;
	-webkit- sition: width 2s; /* Safari */
    }
    div:hover {
        width:300px;
    }
    ```

    - 过渡（transition)是CSS3中具有颠覆性的特征之一，我们可以在不使用 Flash 动画或 JavaScript 的情况下，当元素从一种样式变换为另一种样式时为元素添加效果
    - 帧动画：通过一帧一帧的画面按照固定顺序和速度播放。如电影胶片
    - 在CSS3里使用transition可以实现补间动画（过渡效果），并且当前元素只要有“属性”发生变化时即存在两种状态(我们用A和B代指），就可以实现平滑的过渡，为了方便演示采用hover切换两种状态，但是并不仅仅局限于hover状态来实现过渡。
    - 语法：`transition: 要过渡的属性  花费时间  运动曲线  何时开始;`
        > 如果有多组属性变化，还是用逗号隔开。

        ```
        - transition	简写属性，用于在一个属性中设置四个过渡属性。
        - transition-property	规定应用过渡的 CSS 属性的名称。
        - transition-duration	定义过渡效果花费的时间。默认是 0。
        - transition-timing-function	规定过渡效果的时间曲线。默认是 "ease"。
        - transition-delay	规定过渡效果何时开始。默认是 0。
        ```
    - 如果想要所有的属性都变化过渡， 写一个all 就可以(all 可以省略)transition-duration 运动曲线示意图：
    
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzogcwgrswj20ko07e79b.jpg)

- 什么属性都可以过渡?

- 基本所有属性都能过渡：
    background-color、background-position、background-image、border-radius、border、padding、font-size等等。
- 不能过渡的：
    渐变色、float

- 什么时候触发过渡?

    - 任何对元素的CSS改变都能触发过渡。
        - 不要认为只有:hover能够触发过渡。任何造成元素的改变，都会引发过渡。
        - 比如元素的类名改变，能够触发过渡。
        - 比如直接用JS来设置属性，也能够触发过渡。

    - transition就像护身符一样，任何人胆敢改我的css样式，一定是动画实现的。并且动画效率比setInterval还高。
    - 用过渡来实现动画，早晚有一天要替代setInterval()原理。
    - 明天很爽：过渡做点东西、变形、3D、滚滚屏、元素进出。

#### 2D变形(transform)

transform是CSS3中具有颠覆性的特征之一，可以实现元素的位移、旋转、倾斜、缩放，甚至支持矩阵方式，配合过渡和即将学习的动画知识，可以取代大量之前只能靠Flash才可以实现的效果。

- 移动 `translate(x, y)`  
    - translate(x,y)水平方向和垂直方向同时移动（也就是X轴和Y轴同时移动）
    - translateX(x)仅水平方向移动（X轴移动）
    - translateY(Y)仅垂直方向移动（Y轴移动）
    - 可以利用translate实现定位盒子的对齐：
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzogi31am8j20d505t79b.jpg)
    
- 缩放 `scale(x, y)` ：默认值为 1.0
    - scale(X,Y)使元素水平方向和垂直方向同时缩放（也就是X轴和Y轴同时缩放）
    - scaleX(x)元素仅水平方向缩放（X轴缩放）
    - scaleY(y)元素仅垂直方向缩放（Y轴缩放）
- 旋转 `rotate(deg)` 
    - 可以对元素进行旋转，正值为顺时针，负值为逆时针；
    - `transform:rotate(45deg);`
- `transform-origin`可以调整元素转换变形的原点
    - `div{transform-origin: left top;transform: rotate(45deg); } ` /* 改变元素原点到左上角，然后进行顺时旋转45度 */    
    -  `div{transform-origin: 10px 10px;transform: rotate(45deg); } ` /* 改变元素原点到x 为10  y 为10，然后进行顺时旋转45度 */ 
- 倾斜 `skew(deg, deg)` 
    - `transform:skew(30deg,0deg);`
    - 可以使元素按一定的角度进行倾斜，可为负值，第二个参数不写默认为0。

#### 3D变形(transform)

- rotateX() ：沿X轴旋转：`img {  transition:all 0.5s ease 0s;}img:hove {  transform:rotateX(180deg);}`
- rotateY()：沿着y轴进行旋转：`img {  transition:all 0.5s ease 0s;}img:hove {  transform:rotateX(180deg);}`
- rotateZ()：沿着z轴进行旋转：`img {  transition:all .25s ease-in 0s;}img:hover { transform:rotateZ(180deg);}`
- 透视(perspective)：
	- 电脑显示屏是一个2D平面，图像之所以具有立体感（3D效果），其实只是一种视觉呈现，通过透视可以实现此目的。透视可以将一个2D平面，在转换的过程当中，呈现3D效果。
	- 透视原理： 近大远小 。
	- 浏览器透视：把近大远小的所有图像，透视在屏幕上。
	- perspective：视距，表示视点距离屏幕的长短。视点，用于模拟透视效果时人眼的位置
	- 注：并非任何情况下需要透视效果，根据开发需要进行设置。
	- perspective 一般作为一个属性，设置给父元素，作用于所有3D转换的子元素
- translateX(x)：仅水平方向移动**（X轴移动）
- translateY(y)：仅垂直方向移动（Y轴移动）
- translateZ(z)：transformZ的直观表现形式就是大小变化，实质是XY平面相对于视点的远近变化（说远近就一定会说到离什么参照物远或近，在这里参照物就是perspective属性）。比如设置了`perspective为200px;`那么transformZ的值越接近200，就是离的越近，看上去也就越大，超过200就看不到了，因为相当于跑到后脑勺去了，我相信你正常情况下，是看不到自己的后脑勺的。
- `translate3d(x,y,z)`：[注意]其中，x和y可以是长度值，也可以是百分比，百分比是相对于其本身元素水平方向的宽度和垂直方向的高度和；z只能设置长度值
- `backface-visibility` ：`backface-visibility` 属性定义当元素不面向屏幕时是否可见。
- 翻转盒子案例：
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzogky3cy3j208n0cz79b.jpg)

#### 动画(animation)

- 动画是CSS3中具有颠覆性的特征之一，可通过设置多个节点来精确控制一个或一组动画，常用来实现复杂的动画效果。
- animation的使用方式类似于函数：需要先用 “`@keyframes`” 定义，然后调用。
- 语法格式：`animation:动画名称 花费时间 运动曲线  何时开始  播放次数  是否反方向;`
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzogmwtisej20mr0b23zb.jpg)
- 关于几个值的顺序，除了名字，动画时间，延时有严格顺序要求其它随意;
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzognavwzrj20mk05zjrf.jpg)
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzognhbwxxj20e50iy75b.jpg)

### 伸缩布局

- CSS3在布局方面做了非常大的改进，使得我们对块级元素的布局排列变得十分灵活，适应性非常强，其强大的伸缩性，在响应式开中可以发挥极大的作用。
- 主轴：Flex容器的主轴主要用来配置Flex项目，默认是水平方向
- 侧轴：与主轴垂直的轴称作侧轴，默认是垂直方向的
- 方向：默认主轴从左向右，侧轴默认从上到下
- 主轴和侧轴并不是固定不变的，通过flex-direction可以互换。
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzogp0uspqj20je08i3zx.jpg)
- Flex布局的语法规范经过几年发生了很大的变化，也给Flexbox的使用带来一定的局限性，因为语法规范版本众多，浏览器支持不一致，致使Flexbox布局使用不多
- 各属性详解：
    - flex子项目在主轴的缩放比例，不指定flex属性，则不参与伸缩分配。
        a. min-width 最小值 min-width: 280px 最小宽度 不能小于 280；
        b. max-width: 1280px 最大宽度 不能大于 1280；
    - flex-direction调整主轴方向（默认为水平方向）。
        a. flex-direction: column 垂直排列；
        b. flex-direction: row 水平排列；
        c. http://m.ctrip.com/html5/ 携程网手机端地址；

## 优雅降级/渐进增强

- 优雅降级 graceful degradation：	
    - 一开始就构建完整的功能，然后再针对低版本浏览器进行兼容。
	- 高级浏览器很炫酷，低级浏览器看不见炫酷的效果，页面结构稳定、骨架稳定、该显示的东西都有。CSS的兼容策略，基本都是平稳退化。
	- 比如你现在用一个border-radius:15px;  那么IE6、7、8是没有圆角的，ok，你心想没有圆角就没有了吧，因为盒子稳定，只不过就是美观性差了点，这就是平稳退化的思路。平稳退化就是放低低端用户，低端用户在审美上上就有一些瑕疵。
- 渐进增强 progressive enhancement：
	针对低版本浏览器进行构建页面，保证最基本的功能，然后再针对高级浏览器进行效果、交互等改进和追加功能达到更好的用户体验。
- 区别: 渐进增强是向上兼容，优雅降级是向下兼容。
- 建议: 
    - 现在互联网发展很快， 连微软公司都抛弃了ie浏览器，转而支持 edge这样的高版本浏览器，我们很多情况下没有必要再时刻想着低版本浏览器了，而是一开始就构建完整的效果，根据实际情况，修补低版本浏览器问题。
    - 优雅降级和渐进增强（取决于客户需求）	
- 破罐破摔: 还有一个更经常使用的策略，就是破罐破摔，就是不让低版本浏览器用户看到这个页面，强行跳转：

	```
    <!--[if lte IE9]>
	        <script type="text/javascript">
	        window.location = "error.html";
	        </script>
	<![endif]-->
    ```

	- IE6、7、8都不认识新标签，比如header、section。
	- 有神人帮你写了一个js，叫做html5shiv，能够把所有新标签换成div来解析。
- 总结: 平稳退化和渐进渐强哲学上都是一致的：放弃低端用户，只给低端用户足够的使用性，但是美观、易用程度上有瑕疵。平稳退化先以高版本思考问题，低版本用户就不兼容就算了，因为已经足够能使用这个页面了；渐进渐强是对自己的严格要求，给高级浏览器用户更多的功能。
