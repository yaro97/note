# HTML

## 浏览器内核

浏览器内核又可以分成两部分：渲染引擎(layout engineer 或者 Rendering Engine)和 JS 引擎。
最开始渲染引擎和 JS 引擎并没有区分的很明确，后来 JS 引擎越来越独立，内核就倾向于只指渲染引擎。有一个网页标准计划小组制作了一个 ACID 来测试引擎的兼容性和性能。内核的种类很多，如加上没什么人使用的非商业的免费内核，可能会有10多种，但是常见的浏览器内核可以分这四种：Trident、Gecko、Blink、Webkit。

1. Trident(IE内核) 
   国内很多的双核浏览器的其中一核便是 Trident，美其名曰 "兼容模式"。

   代表： IE、傲游、世界之窗浏览器、Avant、腾讯TT、猎豹安全浏览器、360极速浏览器、百度浏览器等。

   Window10 发布后，IE 将其内置浏览器命名为 Edge，Edge 最显著的特点就是新内核 EdgeHTML。

2. Gecko(firefox) 
  Gecko(Firefox 内核)： Mozilla FireFox(火狐浏览器) 采用该内核，Gecko 的特点是代码完全公开，因此，其可开发程度很高，全世界的程序员都可以为其编写代码，增加功能。 可惜这几年已经没落了， 比如 打开速度慢、升级频繁、猪一样的队友flash、神一样的对手chrome。

3. webkit(Safari)  
  Safari 是苹果公司开发的浏览器，所用浏览器内核的名称是大名鼎鼎的 WebKit。

  现在很多人错误地把 webkit 叫做 chrome内核（即使 chrome内核已经是 blink 了），苹果感觉像被别人抢了媳妇，都哭晕再厕所里面了。

  代表浏览器：傲游浏览器3、 Apple Safari (Win/Mac/iPhone/iPad)、Symbian手机浏览器、Android 默认浏览器，

4. Chromium/Blink(chrome) 
  在 Chromium 项目中研发 Blink 渲染引擎（即浏览器核心），内置于 Chrome 浏览器之中。Blink 其实是 WebKit 的分支。 

  大部分国产浏览器最新版都采用Blink内核。二次开发

5. Presto(Opera)
  Presto（已经废弃） 是挪威产浏览器 opera 的 "前任" 内核，为何说是 "前任"，因为最新的 opera 浏览器早已将之抛弃从而投入到了谷歌怀抱了。  

6. 移动端的浏览器内核主要说的是系统内置浏览器的内核。

   Android手机而言，使用率最高的就是Webkit内核，大部分国产浏览器宣称的自己的内核，基本上也是属于webkit二次开发。

   iOS以及WP7平台上，由于系统原因，系统大部分自带浏览器内核，一般是Safari或者IE内核Trident的

## Web标准（重点）

内核不同，工作原理、解析肯定不同，显示就会有差别。

Web标准不是某一个标准，而是由W3C和其他标准化组织制定的一系列标准的集合。

主要包括结构（Structure）、表现（Presentation）和行为（Behavior）三个方面。

	• 结构标准：结构用于对网页元素进行整理和分类，咱们主要学的是HTML。 最重要
	• 表现标准：表现用于设置网页元素的版式、颜色、大小等外观样式，主要指的是CSS。
	• 行为标准：行为是指网页模型的定义及交互的编写，咱们主要学的是 Javascript

理想状态我们的源码： .HTML    .css   .js 

## 文档类型<!DOCTYPE>

<!DOCTYPE html> 

 这句话就是告诉我们使用哪个html版本？  我们使用的是 html 5 的版本。  html有很多版本，那我们应该告诉用户和浏览器我们使用的版本号。

 <!DOCTYPE> 标签位于文档的最前面，用于向浏览器说明当前文档使用哪种 HTML 或 XHTML 标准规范，必需在开头处使用<!DOCTYPE>标签为所有的XHTML文档指定XHTML版本和类型，只有这样浏览器才能按指定的文档类型进行解析。

 注意：  一些老网站可能用的还是老版本的文档类型比如 XHTML之类的，但是我们学的是HTML5,而且HTML5的文档类型兼容很好(向下兼容的原则)，所以大家放心的使用HTML5的文档类型就好了。

## 字符集

- <meta charset="UTF-8" />

- utf-8是目前最常用的字符集编码方式，常用的字符集编码方式还有gbk和gb2312。

- gb2312 简单中文  包括6763个汉字

- BIG5   繁体中文 港澳台等用

- GBK包含全部中文字符    是GB2312的扩展，加入对繁体字的支持，兼容GB2312

- UTF-8则包含全世界所有国家需要用到的字符

- 记住一点，以后我们统统使用UTF-8      字符集, 这样就避免出现字符集不统一而引起乱码的情况了。

## HTML标签的语义化

	• 1. 方便代码的阅读和维护
	• 2. 同时让浏览器或是网络爬虫可以很好地解析，从而更好分析其中的内容 
	• 3. 使用语义化标签会具有更好地搜索引擎优化 

核心：合适的地方给一个最为合理的标签。

语义是否良好： 当我们去掉CSS之后，网页结构依然组织有序，并且有良好的可读性。

遵循的原则：先确定语义的HTML ，再选合适的CSS。

## 排版标签

- <hn>： h1 标签因为重要，尽量少用。 一般h1      都是给logo使用，或者页面中最重要标题信息。
- 段落标签( 熟记)：<p>
- 水平线标签(认识)：<hr />是单标签
- 换行标签(熟记)：`<br />` 单标签
- div span标签(重点)：无语义标签,网页布局主要的2个盒子(css+div)。division/span的缩写。

## 文本格式化标签(熟记)

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmapq0l53j20ta0c23yz.jpg)

注：建议使用长的标签-具有语义化，小标签经常在购物车的数量等地方起点缀作用。

## 图像标签img（重点）

`<img src="图像URL" />`
常用属性如下：

- src url 图片的路径
- alt 文本 图像不能显示时的替换文本（SEO/盲人）
- title 文本 鼠标悬停时显示的内容；
- width 像素 设置图片宽度（宽高只需要设置一个）
- height 像素 高度

- border 数字 设置图片边框的宽度

## 链接标签（重点）

- ` <a href="跳转目标" target="目标窗口的弹出方式">文本或图像</a>`
- 锚点定位：结合 id 通过 # 来定位到网页中的某个位置；
- base标签：设置整体链接的打开状态 ，写到 `<head>...</head>`之间；把所有的连接 都默认添加 target="_blank"。

## 特殊字符标签 （理解）

```html
&lt;	<	小于号或显示标记
&gt;	>	大于号或显示标记
&amp;	&	可用于显示其它特殊字符
&quot;	"	引号
&reg;	®	已注册
&copy;	©	版权
&trade;	™	商标
&ensp;	 	半个空白位
&emsp;	 	一个空白位
&nbsp;	 	不断行的空白
```

## 注释标签

```html
<!-- 注释语句 -->   ctrl + /       或者 ctrl +shift + / 
```

## 列表标签

```
• ul（重点）：和li配对使用；li中可以放其他标签；
• ol（了解）：和li配对使用；使用场景：金牌榜；
• dl（理解）：和dt/dd配合使用，一个dl多个dt，每个dt多个dd；使用场景：页面最下面-帮助/服务等。
```

## 路径(重点、难点)

- 相对路径（相对于当前文件：css和html文件引用图片时，相对路径可能不同）：a.jpg       img/b.jpg  ../../c.jpg
- 绝对都路径：C:/…/mydir/a.jpg(不推荐)  <http://www.abc.com/b.jpg>

## 标签属性

<标签名 属性1="属性值1" 属性2="属性值2" …> 内容 </标签名>

注：属性之间部分先后，任何标签都有默认值，不建议使用样式属性-用css替代。

## 表格 table(会使用)

- 以前用来网站布局，现在放弃；
- 使用场景：存放数据；
- 要求：能手写表格结构/合并单元格。
- Table tr td/th  配对，其他内容放在 td 中，没有列;
- 第一行/第一列可以设置 th 标签：默认居中加粗；

```html
<table width="500" border="1" align="center" cellspacing="0" cellpadding="5">
```

- 三参（ border cellspacing cellpadding）为零；
- Tr td 的align属性控制控制td里面对应的文字是否居中。当然通过css直接可以控制所有tr中的所有td中的文字居中；
- 可以 紧挨着 table 标签下方 添加 caption 标签(表格标题)；
- 表格结构（理解）：table 下级 应该具有 caption thead tbody 结构（上面没有设置的话，默认会把所有的tr/th放在tbody中）；表格结构的页面布局时有用。
- 单元格合并：
  - 定位左/上角的单元格对应的代码;
  - 对应 td 中添加属性：水平合并n个colspan="n" 垂直合并n个rowspan="n" ；
  - 并手动把被合并n-1个单元格对应的代码删除掉！



## 表单标签（掌握）

作用：交互，收集用户信息；

组成：表单控件（也称表单元素）、提示信息、表单域；

- input控件（重点）- 单标签：

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmaytodlaj20ka09qtce.jpg)

```html
<td><input type="text" value="北京"></td> 在表格中布局表单
<input type="password" name="" id="">
女<input type="radio" name="sex" id="" /> name为组名-必须
小鲜肉<input type="checkbox" name="love" id=""> name为组名
<input type="button" value="免费注册">
<input type="submit" value="提交">
<input type="reset" value="重置">
<input type="image" src="./img/submit.jpg" alt="">
<input type="file" name="" id="">
<input type="radio" checked="checked"> 还可用于checkbox属性
<input type="text" maxlength="6"> 最多输入6个字符
```

- label标签（理解）

  ```html
  <label>用户名<input type="text"></label>
  点击“用户名”也可以进入输入框，用户体验更好！；
  <label for="pwd">123</label>  
  用户名<input type="text">  
  密码<input type="password" id="pwd"> 
  点击 123 进入 id 为 pwd 的输入框。可以在不同的td中指定id。
  ```

- textarea控件(文本域)

  ```html
  <textarea name="" id="" cols="30" rows="10">不支持富文本</textarea>
  上一行中的 cols 和 rows 为列/行中的字符数，实际中通过css控制。
  ```

- select下拉菜单

  ```html
  <select name="" id="">
      <option value="">选择年份</option>
      <option value="">2001</option>
      <option value="">2002</option>
  </select>
  <option value="" selected="selected">2001</option> 默认被选。
  ```

- form表单域

  ```html
  一个表单域中所有的表单一次性提交；
  <form action="url地址" method="提交方式" name="表单名称">
      用户名：<input type="text" name="username"> <br><br>
      密　码：<input type="password" name="passwd"><br><br>
      <input type="submit" value="提交">
      <input type="reset" value="重置">
  </form>
  Action：url指定接受/处理表单数据的服务器地址；
  method：指定数据的提交方式（get/post）。
  name：指定表单的名称，区分一个页面中的多个表单。
  每个表单都应该有自己的表单域。
  ```




