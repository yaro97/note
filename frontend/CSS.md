# CSS

## CSS简介

- CSS - Cascading Style      Sheets 层叠样式表
- 起源 - 起初html有少许显示属性，后来随着这些属性的增加，html变得杂乱/臃肿，随之诞生了css。
- 分类：
- ```html
  - 行内样式表：<p style="color: pink;font-size: 1.2em;">行内样式测试</p>
  - 内部样式表：
      <head>
      <style>
          …
      </style>
      </head>
  - 外部样式表：
  	<link rel="stylesheet" href="xxx.css">
  ```

- ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmbfik79qj20mj03ttce.jpg)

- CSS样式规则：**选择器：{属性:值; 属性:值;…}**

## CSS选择器（重点）

 选择器的嵌套层级不应大于3。

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

1. - `[attr]` 带有 attr 属性的元素。
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

1. - a:link 未访问链接，效果同 a ，区别： a:link 只对含有href属性的a标签起作用。

   - a:visited       访问过的链接

   - a:hover       鼠标再连接上

   - a:active       选定的链接

   - 顺序不能颠倒，记忆：LVHA  LoVe HAte 或者 LV HAa好

   - 实际开发实例:

     ```css
     i. a {
         color: #333333;
         text-decoration: none;
         font-size: 25px;
         font-weight: 700;
     }
     a:hover {
         color: #cc0000;
     }
     ```

### 伪元素：

- `::`   两个冒号
- 目的：允许您为元素的某些部分（before/after/first-letter/first-line/selection）设置样式。

### 交集/并集

- div, .red       表示div元素或.red类；
- div.red  表示 div元素且.red类

## CSS字体样式

### Font-size

- 绝对长度单位:

  - **px （常用）** 与屏幕有关，高分辨率的屏幕，一个css像素意味着多个物理像素。
  - mm/cm/in/pt(磅或point)/pc(12pt) 不常用

- 相对长度单位:

  - 相对于父级元素：

  - - **%（常用）**

  - 相对于当前视窗viewport：

  - - vw 当前视窗宽度的1/100；
    - vh 当前视窗高度的1/100；
    - vmin 选取vw，vh中的较小值；
    - vmax 选取vw，vh中的较大值；

  - 相对于字体：

  - - **em （常用）**相对于当前font-size的值；如果对font-size属性的值使用em单位，则继承父元素的font-size值。
    - **rem（常用）** 相对于root（`<html>`）的font-size值；也可以手动指定（适合于响应式布局）。
    - ex 当前字体小写"x"的高度；
    - ch 当前字体"0"(零)的宽度；

> - chrome默认字体为16px/14px（设置中可以查看）；
> - 以前的显示器分辨率低曾经使用过12px；
> - 尽量用偶数，ie6等老浏览器支持奇数会有bug；

### Font-family

- 网页中常用的是："微软雅黑"（"microsoft yahei"）、"宋体"（simsun），照顾所有人电脑上的字体；
- 中文字体需要加引号，带有多个单词的英文字体需要引号；
- 多个字体优先匹配最左边的，无法匹配选择默认字体；
- 中英文字体混用：英文字体写在中文字体前面。

### Unicode字体

- 有些浏览器不认识中文/英文，Unicode字体兼容性更好。

- 使用时需要添加双引号-有反斜杠("\5B8B\4F53")。

  ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmbwgszwcj20d20actce.jpg)

### Font-weight 控制 b/strong的样式

- 实现粗体可以使用 b 和 strong 标签，同样可以用css来实现，但css没有语义；
- Font-weight 可用属性 normal(400)、 bold(700)、 bolder、 lighter、 100-900（没有单位！任何单位都不合适！！）；
- 更习惯用数字400/700，浏览器解析快？

### Font-style 控制 I/em的样式

- I em 可以实现倾斜，css也可实现，但是没有语义；
- 百度搜索的某个关键词，这个关键词会使用em包裹（语义）；再使用font-style:nomal。
- 属性：nomal, italic, oblique(兼容有问题，不常用)；

### Font

- 可以使用 font 一次性设置上述字体的相关属性。
- 顺序不可乱写：选择器{font: font-style  font-weight  font-size/line-height       font-family;}
- 如：css初始化时： body {font: 16px/1.5;} 以后所有的局部内容会继承行高为1.5em（所处环境字体的大小）。
- 必须包含font-size和font-family属性（其余可省略），否则font属性将不起作用。
- 如：font: italic 1.2em "Fira      Sans", serif;

## CSS外观样式

### Color

- 预定义颜色：red, green

- 十六进制：#FF0000(最常用) #f0f

- RGB代码

- - rgb(255,0,0)
  - rgb(100%,0%,0%) 不能省略 % 

### Line-height

- 控制行与行之间的距离（行高）
- 可用单位：px em % ，建议使用px；
- 一般行高比字号大7-8像素。

### Text-align

- 控制盒子中的文本水平对齐
- Left, right, center

### Text-indent

- 控制盒子中的文本首行缩进；
- Text-align: 2em; em为一个字的距离（长度不固定）

### Text-decoration 

> 可以控制u/ins s/del标签的样式

- 文本的修饰，主要修饰链接的样式

- 子属性：~-line/color/style…

- 例子

- - text-decoration:       none/underline;

- - text-decoration: line-through dotted;
  - text-decoration: green wavy       underline;

## 显示模式display

### 块级元素block-level

- `<h1>~<h6>、<p>、<div>、<ul>、<ol>、<li>、dl, hr, address, blockquote, center, dir, fieldset, isindex,menu, noframes, noscript, pre, table`等，其中`<div>`标签是最典型的块元素。总是从新行开始，独占一行；
- 高度，行高、外边距以及内边距都可以控制。
- 默认宽度100%；
- 块级元素可以容纳其他（块级/行内）元素；
- 特殊： p 里面不能放块级元素，同理还有这些标签h1,h2,h3,h4,h5,h6,dt（自定义列表中的dt），他们都是文字类块级标签，里面不能放其他块级元素（浏览器解析有问题）。

### 行内元素inline-level

- `<a>、<strong>、<b>、<em>、<i>、<del>、<s>、<ins>、<u>、<span>,abbr, acronym, bdo, big, br, cite, code, dfn, font, kbd,label, q, s, samp, select, small, strike, sub, sup, textarea, tt, `等，其中`<span>`标签最典型的行内元素。
- 和相邻行内元素同在一行；
- 高、宽设置无效，但水平方向padding/margin可已设置，垂直不可。
- 默认宽度就是它自身内容的宽度。
- 行内元素只能容纳文本/其他行内元素；
- 特殊：a除外，a可以放块级元素。
- 链接里面不能再放链接（浏览器解析有问题）。

### 行内块元素（inline-block）

- 行内元素中有几个特殊的标签——`<img />、<input />、<td>`，可以对它们设置宽高和对齐属性，
- 和相邻行内元素（行内块）在一行上,但是之间会有空白缝隙。
- 默认宽度就是它本身内容的宽度。

- 高度，行高、外边距以及内边距都可以控制。
- inline-block包含html空白节点。如果你的html中一系列元素每个元素之间都换行了，当你对这些元素设置inline-block时，这些元素之间就会出现空白。

### 标签显示模式转换 display

- display:inline;
- display:block;
- display:inline-block;
- 行内元素和行内块元素都可以当作文本（text）来看，很多样式（如text-align）对其生效。
- 如：若div包裹p元素，设置div{text-align:center}，p由于继承，p里面的文字也会居中，但是p设置width/height之后，里面的文字便不再居中。
- display: none; 隐藏元素，隐藏后的元素的周边（包括margin）一同消失；

## 关于line-height

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmc3o0x0aj20uk0cxtcx.jpg)

- 中线=（顶线+底线）/ 2 ；
- Line-hight = 两行的基线的间距。即上距离（1/2行距） + （顶线-底线） + 下距离（1/2行距）

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmc42nna7j209k0203yk.jpg)

- Line-height = 盒子高度，即单行文字垂直居中。

## CSS三大特性

- 层叠性
  - 层叠是CSS的一个基本特征，CSS的全称层叠样式表正是强调了这一点。
  - 同优先级时，后面设置的样式会把之前设置的样式覆盖掉。
  - 内部样式和外部样式优先级相同，哪个生效？主要看 link 和 style 标签的书写先后顺序，link相当于把外部样式的内容插入到当前位置！

- 继承性
  - 元素的有些样式会继承与父级元素；
  - 恰当的使用继承可以简化代码，降低css样式的复杂性；
  - 具有继承性的样式大多是字体/文本/颜色相关的样式；如：text-, font-, line- 等开头的或color等。
- 优先级（特殊性Specificity）

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmc5ibw3xj20fu046glm.jpg)

 - | 0 0 0 0 | *选择器,   继承              |
  | ------- | ---------------------------- |
  | 0 0 0 1 | 元素选择器， 伪元素          |
  | 0 0 1 0 | 类选择器， 伪类， 属性选择器 |
  | 0 1 0 0 | ID选择器                     |
  | 1 0 0 0 | 行内样式                     |
  | 无穷大  | !important                   |

   - 配选择符（universal selector）(*), 关系选择符（combinators） (+, >, ~, ' ')  和 否定伪类（negation pseudo-class）(:not()) 对优先级没有影响。（但是，在 :not() 内部声明的选择器是会影响优先级）。

   - 含有id的元素如果使用属性选择器（[id="foo"]而不是#foo）的话，按照属性选择器权重计算。	

   - 权重可以叠加：

    ```css
    div ul  li   ------>      0,0,0,3
    .nav ul li   ------>      0,0,1,2
    a:hover      -----—>      0,0,1,1
    .nav a       ------>      0,0,1,1   
    #nav p       ----->       0,1,0,1
    li.red.level   ----->     0 0 2 1
    ```

   - 数位之间没有进位，高位永远比低位大，如：0 0 1 0  >> 0 0 0 50。

   - 不要轻易使用!important，插件中永远不要使用。

   - div p !important  权重大于 p !important 。

   - 尽量使用类选择器，而不是ID选择器，哪怕时只定位唯一的元素。

   - 举例：

    ```html
    <!-- html: -->
    <div id="box1">
        <div>
            <div id="box3">王聪聪</div>
        </div>
    </div>
    ```

    ```css
    /* CSS: */
    #box1 div {
        color: #0c0;
    }
    div #box3 {
        color: #c00;
    }
    </style>
    ```

    - 结果：

      - 两个选择器都定位到了目标；#box1 div中的div也是定位到“王聪聪”；
      - 所以需要判断优先级，都是：0 1 0 1 。
      - 按照层叠规则，后者生效。

## CSS背景background

### css背景样式

- css可以为目标元素设置背景颜色/背景图片…等各种样式
- background-image背景图片地址；none/url("")
- background-repeat是否平铺：repeat | no-repeat | repeat-x | repeat-y
- background-position背景位置，值的写法很灵活；
- background-attachment滚动/固定：scroll | fixed 

### backgound简写

- background:背景颜色 背景图片地址 背景平铺 背景滚动 背景位置。
- 各值的顺序没有严格规定，建议按照上述顺序。
- 背景可以设置**透明度**：
  - #ff0000 #ff0000ff
  - #0f3 #0f38
  - rgb(ff, ff, 0) rgb(ff, ff, 0, .3) rgb(ff, ff, 0 , 30%)
  - rgb(ff ff 0) rgb(ff ff 0 .3) rgb(ff ff 0 30%)

### 说明

- background-image（CSS3可以多背景）可以和 background-color 连用。 如果图片不重复地话，图片覆盖不到地地方都会被背景色填充。 如果有背景图片平铺，则会覆盖背景颜色。
- url里面的地址路径可以使用双引号，也可省略。
- **通过background-position可以实
现图片精灵的效果(a:hover来改变图片的位置，而不是改变图片的路径)**:smile:.

### img和background-image的区别

- img为插入图片，平时用的最多，如：产品展示…
- 背景图片使用场景：超大图片背景、小的图标背景…
- **img会撑开盒子，而背景不会**。

## 盒子模型（重点1）

### 基本概念：
- 网页的本质：很多盒子堆砌而成
- margin border padding content(width height)；
- 内盒尺寸（元素的实际尺寸）=content + padding + border。
- 外盒尺寸（元素空间的尺寸）
- Width/height仅对block/inline-block元素有效。

### 相关属性
- content
    - 即盒子中的内容区。
    - 通过width height 设置盒子的content。
    - 在指定一个div时，习惯性想到宽度/高度/边框/背景色…

- border
    1. 盒子边框：
        - border: 2px dotted red; 粗养颜。
        - border-top/right/bottom/left
    2. table边框塌陷：
        - table里面的border由table的边框和td的边框叠加构成（两倍）；
        - table{ border-collapse:collapse; }  设置单倍边框。

- padding
    - padding:2px 3px 4px 5px; 顺时针（上右下左）;
    - 值的数量不一定为四个，可以是1-4个;
    - padding-top/right/bottom/left;
    - 0 可以省略单位。

- margin
    - margin:2px 3px 4px 5px; 顺时针（上右下左）;
    - margin-top/right/bottom/left;
    - 0 可以省略单位;

### 关于居中的问题

1. Text/inline/inline-block水平居中！！
	1. 父元素设置  text-align: center
	2. 对block元素/inline-block元素里面的text文本/inline-block元素生效，（且由于继承，inline-block元素里面的文本/inline-block元素也会居中…）。
	3. inline-block元素可以等价的看成文本内容。
2.  单行文本垂直居中！！
	1. block/inline-block父元素设置的Line-height 等于的自身高度。
	2. 控制block/inline-block元素里面的Text文本垂直居中。
3. 块元素水平居中！！
	- 条件：
		- 子box必须是块级元素（display: block）,inline-block是不行的；
		- 子盒子必须指定了width。
	- 实现方式：
		- 新浏览器：display:flex; justify-content: center;
		- 老浏览器：IE等等。
			- margin:x auto; 通俗写法（核心：左右为auto）。
			- margin-left: auto右对齐; margin-right: auto(左对齐);  高手写法-解析更快（不需要解析上下）。
            - margin: auto; 貌似auto值对top/bottom不起作用

### 清除元素默认内外边距

1. body等元素默认都有margin或者padding值，为了统一规划，实际中常常在初始化css时，清理掉。
2. 清理方式：
	- `*  {padding:0; margin:0}`  实际中不推荐，浏览器需要解析全部标签。
    - `body, ol, ul, h1, h2, h3, h4, h5, h6, p, th, td, dl, dd, form, fieldset, legend, input, textarea, select {margin: 0; padding: 0} ` 推荐，（div没有默认内外边距，不需要清理） 

### 外边距的合并，[参考MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing)

1. 相邻兄弟block元素的垂直外边距合并（或叫做：折叠/塌陷）
	- 条件：上面的元素设置了margin-bottom，下面的元素设置了margin-top；
	- 结果：两者block实际的距离（margin）值并不是二者之和，而是二者中的较大者。
	- 解决：不需要解决，设计时避免即可。
2. 父元素与其第一个或最后一个子元素之间的垂直外边距合并。
	- 条件：父子block元素之间没有boder/ padding/ margin 将二者分开。
	- 结果：子元素的外边距会“溢出到父元素的外边”。
	- 举例：如 上外边距合并：对于两个嵌套关系的块元素，如果父元素没有上内边距及边框，则父元素的上外边距会与子元素的上外边距发生合并，合并后的外边距为两者中的较大者，即使父元素的上外边距为0，也会发生合并。
	- 解决：
		a. 可以为父元素定义1像素的上边框或上内边距。
		b. 可以为父元素添加 overflow:hidden 。
		c. 其他....
3. 空的块级元素
    - 如果一个块级元素中不包含任何内容，并且在其 margin-top 与 margin-bottom 之间没有边框、内边距、行内内容、height、min-height 将两者分开，则该元素的上下外边距会折叠。

### padding不会撑开盒子的情况

- block元素的默认独占一行，宽度为父盒子的100%；
- 如何 子box 没有设定 width 话，对 子盒子设置 padding-left 不会改变 子box 的实际大小。

### 盒子模型布局的稳定性

- 实际布局时，实现一个效果可以有时可以选用width/ padding/ margin 中的任何一个。
- 但是根据稳定性来分，建议：  width >  padding  >   margin   
- 原因：
	1. margin 会有外边距合并 还有 ie6下面margin 加倍的bug（讨厌）所以最后使用。
	2. padding 会影响盒子大小， 需要进行加减计算（麻烦） 其次使用。
    3. width 没有问题（嗨皮）我们经常使用宽度剩余法 高度剩余法来做。

### 圆角边框(CSS3)

- CSS3新加入的。
- `border-radius: 40% 20% 50% 30%;`四个点可以单独设置（顺时针），单位也可以px em 等。
- `border-radius: 20% 50%;`  左上同右下：20%。
- `border-radius: 50%;`   让一个正方形  变成圆。
- 不需要设置border，border只是让边框显示出来即可。背景色也可以看出块的形状。

### box-shadow

- 参考小米官网的阴影：box-shadow: 0 15px 30px rgba(0,0,0,0.1)
- /* offset-x | offset-y | blur-radius | spread-radius | color */ （x/y偏移值必须，其他可选）；

### inline元素的margin和padding

- inline元素也有盒子模型。
- margin值 top right bottom left 都可设置（chrome 调试 能看到设置）。但是 top 和 bottom 无法影响上下盒子的布局；left right 会影响左右盒子的布局。

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmjspbtukj204o03edfm.jpg)

- padding值  top right bottom left 都可设置（chrome 调试 能看到设置），但是 top 和 bottom 无法影响上下盒子的布局；left right 会影响左右盒子的布局。

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmjtaj6g0j204r03egle.jpg)

- Inline 和 inline-block 元素之间会有一定的间隙，可以使用 float 去除。

## 浮动（重点2）

normal flow标准流: 网页中的元素从上到下、从左到右顺序排列，block元素独占一行，inline， inline-block元素行内显示。

### 浮动float

1. 历史：
   - 最初，float用来控制图片，实现文字的环绕图片的效果。
   - 后来，我们发现float可以让任何盒子一行排列，慢慢的就用float来布局了。
2. 理论：
   - 定义：The float CSS property places an element on the left or right side of its container, allowing text and inline elements to wrap around it. The element is removed from the normal flow of the page, though still remaining a part of the flow (in contrast to absolute positioning).
   - values： **left right** none（默认）。
   - **主要目的：让多个block元素一行显示。**
3. 让多个block在同一行为啥不用 display:inline-block;
   - display: inline-block; 同一行的盒子之间由间隙（去除的话需要额外代码）；
   - display: inline-block; 不能实现盒子靠右对齐，float: right; 可以。
4. 解析：**float 浮 漏 特**
   - 浮：
   - **不完全**脱离标准流，**飘在第二层（可以想象为生成两个文档流：原标准流+浮动的标准流）**，但是原标准流中的文字/img不会被覆盖（**不完全脱标**）。
		- 同级的两个子盒子同时浮动后，**会在生成的“浮动的标准流”正常排序（float的块/行内元素自动具有 inline-block 特性，但不是inline-block）**
   - 漏：
     - 某元素浮动后，**其在原标准流的位置会空（漏）出**，后面的元素按原有规则排列。
   - 特：
    - 浮动的方向要么left，要么right。浮动的边界为**其Parent元素及兄Block元素 确定 内边界（content区域）**；即，如果前面有Child-A**兄Block元素**没有浮动，Child-B的浮动的边界由Parent元素和Child-A元素共同确定。如果Child-A为inline-block 或 inline 元素，会环绕在浮动的Child-B周围。
     - 一个父盒子中，如果其中一个子盒子浮动，其他兄弟盒子都应该浮动，这样才能一行对齐。
     - 浮动后的元素（无论之前是 block， inline-block， inline 元素），**隐形转换成具有 inline-block 特性的元素**；**但是不同的是：inline-block元素仍然在原标准流中。**
5. **正确使用**：
   - 所以一个父盒子中，所有的子盒子要么都浮动，要么都不浮动，哪怕是inline元素也要浮动。
   - 浮动的若干个子盒子通常需要一个标准流中的（指定高度的）父盒子包裹，共同搭配使用。
   - 但是很多时候父盒子是不方便设定明确的高度（里面的内容多少不确定），这个时候需要应用清除浮动。
   - 特别说明：float本意是用来文字环绕的，布局只是GEEK，主要为了让多个Block元素一行显示，其他布局尽量不要刻意使用。很容易出意外（文字/图片出现环绕或者不被覆盖）。
   - 比如：
     - 牵扯到 p 和 img 标签就会会出问题，即使设置 display: block; 文字/图片也会环绕。
     - 即使用 div 标签 包裹 文字/图片 ，div会随标准流布局，里面的 文字/img 也会环绕。

### 清除浮动

- 背景：
  - float最初是用来实现文字混排效果的，用来布局会有很多问题，由于浮动元素不在占用原标准流，就会对后面的元素排版产生影响，这是就需要**清除浮动（造成的影响）**。
  - 多个**浮动的 子box 的 父box，没有指定高度的话（有时候不方便）高度为 0**，（原因：浮动的元素在脱离标准流，不再占用标准流的位置，无法撑开 父box）。

- **清除浮动目的**：解决父级元素因子级浮动引起的内部高度为0的问题，不需要再指定 父box的高度，清除浮动即可！。
- 清除浮动原则：清除影响布局的浮动！不影响的布局的浮动，没必要清除。
- 清除浮动添加对象：可以给父亲添加，也可以给祖先添加。
- 清除浮动常用方法(clear:both[常用],right[用的少], left[从来没见过])：

	1. 额外标签法：
		a. (W3C推荐)，在最后一个浮动元素的末尾添加一个空标签<div style="clear:both"></div>，或者其他标签br等。
		b. 优点：通俗易懂，书写方便；
		c. 缺点：无意义标签，结构化较差。不推荐！！
	2. 父级添加overflow属性法：
		a. 可以给父级添加： overflow为 hidden|auto|scroll  都可以实现。
		b. 原理：通过触发BFC的方式，可以实现清除浮动效果。（BFC后面讲解）
		c. 优点： 代码简洁。
		d. 缺点： 内容增多时候容易造成不会自动换行导致内容被隐藏掉，无法显示需要溢出的元素。
	3. 使用after伪元素法：
		a. :after 方式为空元素的升级版，好处是不用单独加标签了。
		b. 使用方法：

		```css
		//首先, 为需要清除浮动的 父box 添加 clearfix类。
		//然后,
		.clearfix::after {
		content: "";
		display: block;
		height: 0;
		clear: both;
		visibility: hidden;
		}
		//最后,
		.clearfix {*zoom: 1;}    IE6、7 专有，添加 * 的属性只有IE7以下版本识别，其他浏览器忽略。
		```
		c. 优点：符合闭合浮动思想 结构语义化正确。
		d. 缺点：由于IE6-7不支持:after，使用 zoom:1触发 hasLayout。
		e. 代表网站： 百度、淘宝网、网易等。
		f. 注意：尽量使用 content: ""; 而不是 content: ".";

### Inline-block和float的区别

- **文档流（Document flow）**:浮动元素会脱离文档流，并使得周围元素环绕这个元素。而inline-block元素仍在文档流内。因此设置inline-block不需要清除浮动。当然，周围元素不会环绕这个元素，你也不可能通过清除inline-block就让一个元素跑到下面去。
- **水平位置（Horizontal position）**：很明显你不能通过给父元素设置text-align:center让浮动元素居中。事实上定位类属性设置到父元素上，均不会影响父元素内浮动的元素。但是父元素内元素如果设置了display：inline-block，则对父元素设置一些定位属性会影响到子元素。（这还是因为浮动元素脱离文档流的关系）。
- **垂直对齐（Vertical alignment）**：inline-block元素沿着默认的基线对齐。浮动元素紧贴顶部。你可以通过vertical属性设置这个默认基线，但对浮动元素这种方法就不行了。这也是我倾向于inline-block的主要原因。
- **空白（Whitespace）**：inline-block包含html空白节点。如果你的html中一系列元素每个元素之间都换行了，当你对这些元素设置inline-block时，这些元素之间就会出现空白。而浮动元素会忽略空白节点，互相紧贴。

### 版心和布局

- 网页布局的核心就是用CSS来拜访盒子，CSS有三种定位机制：
  - 标准流（普通流）
  - 浮动
  - 定位
- 网页布局概念：
  - 网页布局，类似于报纸，内容多，但是合理排版依然很清晰。
  - 网页布局时，我们主要关心横向布局，纵向根据内容的多少自动下延即可。
  - 版心（可视区）：指网页主题内容所在的区域，一般在浏览器窗口水平显示，常用的宽度有960px， 980px， 1000px， 1200px等。
- 布局流程：
  1. 确定页面的版心（可视区）；
  2. 确定设计稿大的布局结构。
  3. 通过DIV + CSS实现布局框架（css初始化）；
  4. 设计各小模块，首先分析/转换行模块为html，再处理各行中列模块；
- 常用布局结构：
  - 一列固定宽度居中：最普通，最常用
  ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmnpoq0fnj20hx0gpaaa.jpg)
  - 两列左窄右宽：比如小米  [小米官网](http://www.mi.com)
  ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmnpoj42ej20hx0gp3yu.jpg)
  - 通栏平均分布型:比如锤子  [锤子官网](http://www.smartisan.com/)
  ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmnpokeubj20um0npq3q.jpg)

## 定位（重点3）

### 定位概述

- 定位有两部分构成：**定位方式， 偏移量**：
  - **只要设置 absolute，fixed 定位方式，元素便会脱离标准流，影响标准流后面的元素，元素自身原地待命**。
  - **定位方式、偏移量一起声明才会让定位的元素“移动”**。
- 定位的目的：实现元素的位置移动；
- 定位的分类：
  - static 静态定位（默认的定位方式）
  - relative 相对定位（相对与自己原来的位置）
  - absolute 绝对定位 （相对于自己的已经定位的父元素，逐级往上搜索）
  - fixed 固定定位（相对于浏览器窗口）

### static

- 元素默认的方式；
- 使用场景：**把其他定位的方式取消掉（类似于none）**。

### relative

- 相对自己原来的位置定位；
- **完全“飘起来”，原标准流的文字/img也会被覆盖**，且**完全脱离原来的标准流，但是不释放原来的在标准流的位置**。
- 特殊用法：
  
  ```css
  div:hover {
		border: 1px solid #000;
		position: relative;
	} 
  ```

  - 如下图：让盒子边框重叠时，鼠标悬浮是，飘起来。
  ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmnw60mg5j20n80coa9v.jpg)
  - 如果div本身是 position: relative; ,我们只需要给 div:hover 再添加 z-index: 1; 即可。

### absolute

- **完全“飘起来”，原标准流的文字/img也会被覆盖。且完全脱离原来的标准流，不占有标准流的位置**
- 依据**最近的已经定位（绝对、固定、相对）声明的父元素（祖先）的border边框进行定位。倘若祖先元素都没有定位声明，以浏览器当前屏幕为准定位**(document文档，而不是body标签)。
- “**子绝父相**”，原因如下：
  - “子绝父绝”的话，父元素也会脱离标准流，标准流后面的元素会受影响。
  - “子绝父fixed”的话，父元素也会脱离标准流，标准流后面的元素会受影响。
- **绝对定位盒子居中**：
  - 普通盒子可以通过 左右margin 改为 auto 实现水平居中；
  - 设置 absolute 之后失效；
  - 实现途径：
	- **left： 50%;**
	- **margin-left: - 盒子宽度/2**
	- 垂直居中类似。

### fixed

- **完全“飘起来”**，**原标准流的文字/img也会被覆盖。且完全脱离原来的标准流，不占有标准流的位置**。
- 父亲不需要定位声明，**只参考浏览器的当前窗口定位，不随滚动条滚动，和 body 的 border ， margin也没有关系**。
- ie6等低版本浏览器不支持固定定位。

### 定位时元素模式的隐式转换

- relative不会转换显示模式，**absolute，fixed 会隐式的把元素转变为 具有 inline-block 特性的元素**。
- so，设置absolute，fixed定位后的元素，里面没有内容的话（背景不算），会“消失”，需要指定 `height:xx，width: 100%;` 。

### 四种定位总结

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmo91hodmj20j9066dg8.jpg)

### z-index

- z-index **默认值是0， 取值越大（无单位），叠放顺序居上**；
- 如果取值相同，**后来之居“上”**；
- **只有 absolute relative fixed 定位的元素有此属性，其他 标准流、浮动、静态定位皆无此属性**。

## CSS高级技巧

### 元素的显示和隐藏

- display显示
	- display: none; 隐藏元素，**隐藏后的元素的周边（包括margin）一同消失**；
	- 隐藏后不再占有标准流的位置；
	- 隐藏相反的是 display: block;  除了转换为块级元素外，还有显示元素的意思。
- visibility可见性
	- visibility: visible; 对象可见；
	- visibility: hidden; 对象不可见；
	- 不可见之后，仍然占用标准流的位置。 
- overflow溢出
	- overflow: visible; （默认）**div里面的内容超出后，溢出显示，但是不影响标准流后面元素的布局，只会（被）遮盖而已**；
	- scroll ；始终显示（水平和垂直）滚动条；
	- auto；如果内容溢出，自动显示滚动条；否则，不显示；
- hidden；超出的部分被隐藏掉（**最常用**）。

### CSS用户界面样式

- 鼠标样式cursor：

	```html
	<ul>
		<li style="cursor:default">我是默认箭头</li>
		<li style="cursor:pointer">我是小手（链接）</li>
		<li style="cursor:move">我是移动</li>
		<li style="cursor:text">我是文本</li>
		<li style="cursor:auto">我是自动</li>
	</ul>
	```

	- default全部显示为默认箭头，auto会根据内容自动显示相应的鼠标样式（a标签会当作文本）
	
- 轮廓outline：
	- 和border不同的是：outline不占有盒子尺寸，只是显示而已。
	- 和border相似的是：也有三个分样式（width, style, color)，也可以用 shorthand （粗养颜）；
	- input/textarea等 表单默认都有蓝色的outline；可以用 `outline: 0;` 或者 `outline: none;` 清除。
	- 另外：input...等表单再不同的浏览器会显示不同的初始样式，建议直接初始化：`border: 1px solid #000;` 
- 防止拖拽textarea(文本域)resize：
	- resize可以接受的值：both, horizontal, vertical, none.. 等；
	- 工作时大多直接禁用：`resize: none;` 。 

### vertical-align 

- 以前我们讲过让带有宽度的块级元素居中对齐，是margin: 0 auto; 还讲过让文字居中对齐，是 text-align: center;
![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmofr5birj20l4042409.jpg)
- 主要的属性值有：vertical-align : baseline(默认) |top |middle |bottom 。
- vertical-align 不影响Block元素中的内容对齐，它只针对于 inline或者Inline-block元素，特别是**行内块元素**， 通常用来控制**图片img/表单input与文字**的对齐。
- 比如对和文字同行的img设置：
  - bottom：**图片的bottom和字体的bottom对齐**；
  - top：**图片的top和字体的top对齐**；
  - middle：**图片的middle和`字体的（baseline+x-height）`对齐**。
- 去**除图片底部的空白缝隙**：由于img/表单默认是baseline（图片没有baseline，用bottom）和父级盒子的基线baseline对齐，会导致图片底侧会有一个空白缝隙，
  - 解决办法1：`CSS初始化时添加—— img { vertical-align: top; border: 0;}` 。
  - 解决办法2：display：block; 不推荐，会影响后面元素的布局。
- 更深入的解释见[MDN官网](https://developer.mozilla.org/zh-CN/docs/Web/CSS/vertical-align)。

## 溢出的文字隐藏

### white-space

- 用来设置如何处理元素中的空白。通常我们使用于强制一行显示内容。
- normal : 　默认处理方式 ，自动换行（`连续的空白符会被合并，换行符会被当作空白符来处理。填充line盒子时，必要的话会换行。`）。
- nowrap : 　强制在同一行内显示所有文本，直到文本结束或者遭遇br标签对象才换行（`和 normal 一样，连续的空白符会被合并。但文本内的换行无效。`）。
- 可以处理中文

### text-overflow

- 设置或检索是否使用一个省略标记（...）标示对象内文本的溢出。
- clip : 　不显示省略标记（...），而是简单的裁切 。
- ellipsis : 　当对象内文本溢出时显示省略标记（...）。
- **注意要与下面两个一起用:**
  - 首先强制一行内显示white-space:nowrap;
  - 再次和overflow:hidden属性 搭配使用。

## 图片精灵sprite

### 产生背景

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmolz4sdaj20ll0720ud.jpg)

- 当用户访问一个网站时，需要向服务器发送请求，网页上的每张图像都要经过一次请求。
- 但是，网页往往有很多小**背景图像**，服务器就会频繁地接受和发送请求，这将大大增加服务器负担和带宽的占用，进而降低页面的加载速度。因此，出现了CSS精灵技术（也称CSS Sprites、CSS雪碧）

### 本质

- CSS精灵是一种处理网页背景图像的方式。它将一个页面涉及到的所有零星**背景图像**都集中到一张大图中去，然后将大图应用于网页，这样.
- 当用户访问该页面时，只需向服务发送一次请求，网页中的背景图像即可全部展示出来。通常情况下，这个由很多小的背景图像合成的大图被称为**精灵图（雪碧图）**。

### 实现

- CSS 精灵其实是将网页中的一些背景图像整合到一张大图中（精灵图），然而，各个网页元素通常只需要精灵图中不同位置的某个小图，要想精确定位到精灵图中的某个小图，就需要使用CSS的background-image、background-repeat和background-position属性进行背景定位，其中最关键的是使用background-position属性精确地定位。

### 制作

- CSS 精灵其实是将网页中的一些背景图像整合到一张大图中，具体而言，就是把小图拼合成一张大图。大部分情况下，精灵图都是网页美工做。
- 我们精灵图上放的都是小的装饰性质的**背景(backgroud)图片**。 **插入图片(img)**不能往上放。
- 我们精灵图的宽度取决于最宽的那个背景。 
- 我们可以横向摆放也可以纵向摆放，但是**每个图片之间，间隔至少隔开偶数像素合适**。
- 在我们**精灵图的最底端，留一片空隙**，方便我们以后添加其他精灵图。

### 结束语

- **小公司，背景图片很少的情况，没有必要使用精灵技术，维护成本太高**。 如果是背景图片比较多，可以建议使用精灵技术。

## 滑动门

### 出现背景

- 制作网页时，为了美观，常常需要为网页元素设置特殊形状的背景，比如微信导航栏，有凸起和凹下去的感觉，最大的问题是里面的字数不一样多，咋办？
- 为了使各种特殊形状的背景能够自适应元素中文本内容的多少，出现了CSS滑动门技术。它从新的角度构建页面，使各种特殊形状的背景能够自由拉伸滑动，以适应元素内部的文本内容，可用性更强。 最常见于各种导航栏的滑动门。

### 核心技术

- 核心技术就是利用CSS精灵（主要是背景位置）和盒子padding撑开宽度, 以便能适应不同字数的导航栏。
- 一般的经典布局都是这样的：

  ```html
	<li>
		<a href="#">
		<span>导航栏内容</span>
		</a>
	</li>
  ```

### 总结

- a 设置 背景left(默认)，padding撑开合适宽度。 
- span 设置背景(right)， padding撑开合适宽度 剩下由文字继续撑开宽度。
- 之所以a包含span就是因为 整个导航都是可以点击的(`.nav a:hover span`)。

## web字体

### 字体格式

- 不同浏览器所支持的字体格式是不一样的：
	- TureType(.ttf)格式：.ttf字体是Windows和Mac的最常见的字体，是一种RAW格式，支持这种字体的浏览器有IE9+、Firefox3.5+、Chrome4+、Safari3+、Opera10+、iOS Mobile、Safari4.2+；
	- OpenType(.otf)格式：.otf字体被认为是一种原始的字体格式，其内置在TureType的基础上，支持这种字体的浏览器有Firefox3.5+、Chrome4.0+、Safari3.1+、Opera10.0+、iOS Mobile、Safari4.2+；
	- Web Open Font Format(.woff)格式：woff字体是Web字体中最佳格式，他是一个开放的TrueType/OpenType的压缩版本，同时也支持元数据包的分离，支持这种字体的浏览器有IE9+、Firefox3.5+、Chrome6+、Safari3.6+、Opera11.1+；
	- Embedded Open Type(.eot)格式：.eot字体是IE专用字体，可以从TrueType创建此格式字体，支持这种字体的浏览器有IE4+；
	- SVG(.svg)格式：.svg字体是基于SVG字体渲染的一种格式，支持这种字体的浏览器有Chrome4+、Safari3.1+、Opera10.0+、iOS Mobile Safari3.2+；
- 了解了上面的知识后，我们就需要为不同的浏览器准备不同格式的字体，通常我们会通过字体生成工具帮我们生成各种格式的字体，因此无需过于在意字体格式间的区别差异。

### 字体图标

- 介绍：图片是有诸多优点的，但是缺点很明显，比如图片不但增加了总文件的大小，还增加了很多额外的"http请求"，这都会大大降低网页的性能的。更重要的是图片不能很好的进行“缩放”，因为图片放大和缩小会失真。 我们后面会学习移动端响应式，很多情况下希望我们的图标是可以缩放的。此时，一个非常重要的技术出现了，额不是出现了，是以前就有，是被从新"宠幸"啦。。 这就是字体图标（iconfont).
- 字体图标优点：
  1. 可以做出跟图片一样可以做的事情,改变透明度、旋转度，等..
  2. 但是本质其实是文字，可以很随意的改变颜色、产生阴影、透明效果等等...
  3. 本身体积更小，但携带的信息并没有削减。
  4. 几乎支持所有的浏览器
  5. 移动端设备必备良药...
- 字体图标使用流程：

	![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmp433bblj20xt0a8409.jpg)
	
	1. 设计字体图标：
     - 假如图标是我们公司单独设计，那就需要第一步了，这个属于UI设计人员的工作， 他们在 illustrator 或 Sketch 这类矢量图形软件里创建 icon图标， 比如下图：
     ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmpa3083yj20dc05w76c.jpg)
     - 之后保存为svg格式，然后给我们前端人员就好了。 其实第一步，我们不需要关心，只需要给我们这些图标就可以了，如果图标是大众的，网上本来就有的，可以直接跳过第一步，进入第三步。
	2. 上传生成字体包：
     - 当UI设计人员给我们svg文件的时候，我们需要转换成我们页面能使用的字体文件， 而且需要生成的是兼容性的适合各个浏览器的。
       - icomoon字库
       推荐网站： http://icomoon.io
       IcoMoon成立于2011年，推出的第一个自定义图标字体生成器，它允许用户选择他们所需要的图标，使它们成一字型。 内容种类繁多，非常全面，唯一的遗憾是国外服务器，打开网速较慢。
       - 阿里icon font字库
       http://www.iconfont.cn/
       这个是阿里妈妈M2UX的一个icon font字体图标字库，包含了淘宝图标库和阿里妈妈图标库。可以使用AI制作图标上传生成。 一个字，免费，免费！！
       - fontello
       http://fontello.com/
       在线定制你自己的icon font字体图标字库，也可以直接从GitHub下载整个图标集，该项目也是开源的。
       - Font-Awesome
       http://fortawesome.github.io/Font-Awesome/
       这是我最喜欢的字库之一了，更新比较快。目前已经有369个图标了。
       - Glyphicon Halflings
       http://glyphicons.com/
       这个字体图标可以在Bootstrap下免费使用。自带了200多个图标。
       - Icons8
       https://icons8.com/
       提供PNG免费下载，像素大能到500PX
     3. 下载兼容字体包：
     刚才上传完毕， 网站会给我们把UI做的svg图片转换为我们的字体格式， 然后下载下来就好了。当然，我们不需要自己专门的图标，是想网上找几个图标使用，以上2步可以直接省略了， 直接到刚才的网站上找喜欢的下载使用吧。
     4. 引入字体到html：
     得到压缩包之后，最后一步，是最重要的一步了， 就是字体文件已经有了，我们需要引入到我们页面中。
        - 首先把 以下4个文件放入到 fonts文件夹里面。 通俗的做法
        - 在样式里面声明字体： 告诉别人我们自己定义的字体
        @font-face {  font-family: 'icomoon'; ...}
        - 盒子里面添加结构  span::before { content: "\e900";} 或者  <span></span>  
        - 给盒子使用字体  span {font-family: "icomoon"; }
	5. 追加新图标到原来库里面：
		如果工作中，原来的字体图标不够用了，我们需要添加新的字体图标，但是原来的不能删除，继续使用，此时我们需要这样做：把压缩包里面的selection.json 从新上传，然后，选中自己想要新的图标，从新下载压缩包，替换原来文件即可。

## JD京东项目

### 目标

初步了解兼容，熟悉css/div布局， 了解电商类网站布局， 为后期移动端做铺垫， 理解BFC， 了解优雅降级/渐进增强，了解CSS压缩和验证工具;

### 思考

- 开发工具:PS，webstorm， VScode， 各种浏览器。
- CSS Reset 类库：为跨浏览器兼容做准备(也可以直接运用jd网站的初始化)
normalize.css   只是一个很小的CSS文件，但它在默认的HTML元素样式上提供了跨浏览器的高度一致性。相比于传统的CSS reset，Normalize.css是一种现代的、为HTML5准备的优质替代方案。Normalize.css现在已经被用于Twitter Bootstrap、HTML5 Boilerplate、GOV.UK、Rdio、CSS Tricks 以及许许多多其他框架、工具和网站上。 你值得拥有。

  - 保护有用的浏览器默认样式而不是完全去掉它们；
  - 一般化的样式：为大部分HTML元素提供；
  - 修复浏览器自身的bug并保证各浏览器的一致性；
  - 优化CSS可用性：用一些小技巧；
  - 解释代码：用注释和详细的文档来；

- 技术栈：HTML + CSS
- 为低版本浏览器单独制作[跳转页面](https://h5.m.jd.com/dev/3dm8aE4LDBNMkDfcCaRxLnVQ7rqo/index.html)：

### 目录

| 名称   | 说明                       |
| ------ | -------------------------- |
| css    | 用于存放CSS文件            |
| images | 用于存放图片               |
| index  | 京东首页 HTML              |
| js     | 用于后期存放javascript文件 |

### 运用知识点

1. 引入ico图标 
 - 代码：`<link rel="shortcut icon" href="favicon.ico"  type="image/x-icon"/> `
 - 注意： 
	- 她(它)不是iconfont字体哦 也不是图片。
	- 位置是放到 head 标签中间。
	- 后面的type="image/x-icon" 属性可以省略。（我相信你也愿意省略。）
	- 为了兼容性，请将favicon.ico 这个图标放到根目录下。（我们就不要任性了，听话放位置，省很多麻烦。。你好，我也好）
2. 转换ICO图标：在线转换。
3. 网页三大标签（SEO）：
 - 网页title 标题
	- title具有不可替代性，是我们的内页第一个重要标签，是搜索引擎了解网页的入口，和对网页主题归属的最佳判断点。

	- 建议：首页标题：网站名（产品名）- 网站的介绍 
	- 例如：京东(JD.COM)-综合网购首选-正品低价、品质保障、配送及时、轻松购物！
	小米商城 - 小米5s、红米Note 4、小米MIX、小米笔记本官方网站
 - Description 网站说明
	- 对于关键词的作用明显降低，但由于很多搜索引擎，仍然大量采用网页的MATA标签中描述部分作为搜索结果的“内容摘要”。 
	- 就是简要说明我们网站的主要做什么的。 我们提倡，Description作为网站的总体业务和主题概括，多采用“我们是…”“我们提供…”“×××网作为…”“电话：010…”之类语句。
	- 京东网：`<meta name="description" content="京东JD.COM-专业的综合网上购物商城,销售家电、数码通讯、电脑、家居百货、服装服饰、母婴、图书、食品等数万个品牌优质商品.便捷、诚信的服务，为您提供愉悦的网上购物体验!" />`
	- 注意点：
		a. 描述中出现关键词，与正文内容相关，这部分内容是给人看的，所以要写的很详细，让人感兴趣， 吸引用户点击。
		b. 同样遵循简短原则，字符数含空格在内不要超过 120 个汉字。
		c. 补充在 title 和 keywords 中未能充分表述的说明.
		d. 用英文逗号隔开： 关键词1,关键词2
`		<meta name="description" content="小米商城直营小米公司旗下所有产品，囊括小米手机系列小米MIX、小米Note 2，红米手机系列红米Note 4、红米4，智能硬件，配件及小米生活周边，同时提供小米客户服务及售后支持。" />`
 - Keywords 关键字
	- Keywords是页面关键词，是搜索引擎关注点之一。Keywords应该限制在6～8个关键词左右，电商类网站可以多 少许。
	- 京东网：`<meta name="Keywords" content="网上购物,网上商城,手机,笔记本,电脑,MP3,CD,VCD,DV,相机,数码,配件,手表,存储卡,京东" />`
	- 小米网：
	`<meta name="keywords" content="小米,小米6,红米Note4,小米MIX,小米商城" />`

### 顶部（快捷菜单）所用知识点

| 知识点                                 | 说明                                                                                   |
| -------------------------------------- | -------------------------------------------------------------------------------------- |
| 通栏的盒子                             | 不用给宽度 默认为 100% 但是加了浮动和定位的盒子需要 添加 100%                          |
| 盒子居中对齐                           | margin: auto; 注意必须有宽度的块级元素，文字水平居中对齐是 text-align:center;          |
| 行高会继承                             | 文字性质的，比如 颜色、文字大小、字体、行高等会继承父级元素                            |
| 浮动元素、固定定位，绝对定位会模式转换 | 具有行内块特性，比如一行放多个，有高度和宽度，如果没有指定宽度，则会根据内容多少撑开。 |

### logo 和搜索 header 区域所用知识点

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmpl0f5h6j20k60kqq5t.jpg)

### nav导航栏所用知识点

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmplnh2gwj20kh0g3gmg.jpg)

### 页面底部所用知识点

- 绝对定位的盒子居中对齐: 盒子 left 50% 然后通过 margin 负值自己的宽度一半（固定定位也是如此）

### 焦点图部分所用知识点

- 圆角矩形: border-radius: 左上角 右上角 右下角 左下角。
  > 负值自己的宽度一半（固定定位也是如此）

### 背景半透明

1. 强烈推荐：  background: rgba(r,g,b,alpha);​  r,g,b 是红绿蓝的颜色，alpha 是透明度的意思，取值范围是 0~1 之间。
2. 了解ie低版本浏览器 半透明：

	```
	filter:Alpha(opacity=50) ；   // opacity值为0 到 100；但是 此属性是盒子半透明，不是背景半透明哦，因为里面的内容也一起半透明了；
	因此，低版本的 ie6.7浏览器，我们不需要透明了，直接采用优雅降级的做法。
	background: gary;
	background: rgba(0,0,0,.2);
	写上两句 背景， 低版本ie只执行gray， 其他浏览器执行 半透明下面这一句。
	```

### CSS W3C统一验证工具

1. [CssStats](http://www.cssstats.com/) 是一个在线的 CSS 代码分析工具
如果你想要更全面的，这个神奇，你值得拥有：
2. W3C 统一验证工具：    http://validator.w3.org/unicorn/  ☆☆☆☆☆
因为它可以检测本地文件哦！！
3. [css 代码压缩](http://tool.chinaz.com/Tools/CssFormat.aspx)

## BFC（块级格式化上下文）

### 概述

- BFC(Block formatting context)，直译为"块级格式化上下文"。
- 元素的显示模式（display）：
	![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmpq4oznnj20a508t76c.jpg)

### 哪些元素可能触发BFC

- 不是所有模式的元素都能产生BFC，w3c 规范： 
	- display 属性为 block, list-item, table 的元素，会产生BFC.
	- 大家有么有发现这个三个都是用来布局最为合理的元素，因为他们就是用来可视化布局。
	- 注意其他的，display属性，比如 line 等等，他们创建的是 IFC ，我们暂且不研究。
- 这个BFC 有着具体的布局特性： 
  ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzmpr1asmcj20be0cd76c.jpg)

### 触发元素BFC的条件

- float属性不为none
- position为absolute或fixed
- display为inline-block, table-cell, table-caption, flex, inline-flex
- overflow不为visible。

### BFC元素具有的特性

- 在BFC中，盒子从顶端开始垂直地一个接一个地排列.
- 盒子垂直方向的距离由margin决定。属于同一个BFC的两个相邻盒子的margin会发生重叠
- 在BFC中，每一个盒子的左外边缘（margin-left）会触碰到容器的左边缘(border-left)（对于从右到左的格式来说，则触碰到右边缘）。
	- BFC的区域不会与浮动盒子产生交集，而是紧贴浮动边缘。
	- 计算BFC的高度时，自然也会检测浮动或者定位的盒子高度。
- 它是一个独立的渲染区域，只有Block-level box参与， 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干。

### FC的主要用途

1. 清除元素内部浮动：
	- 只要把父元素设为BFC就可以清理子元素的浮动了，最常见的用法就是在父元素上设置overflow: hidden样式，对于IE6加上zoom:1就可以了。
	- 主要用到 ：计算BFC的高度时，自然也会检测浮动或者定位的盒子高度。
2. 解决外边距合并问题：
	- 主要用到 ：属于同一个BFC的两个相邻盒子的margin会发生重叠，那么我们创建不属于同一个BFC，就不会发生margin重叠了。
3. 制作右侧自适应的盒子问题：
	- 主要用到：普通流体元素BFC后，为了和浮动元素不产生任何交集，顺着浮动边缘形成自己的封闭上下文。

### BFC 总结

- BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素。反之也如此。包括浮动，和外边距合并等等，因此，有了这个特性，我们布局的时候就不会出现意外情况了。
