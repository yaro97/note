# mdx/mdict源码文件格式

本文适用于MdxBuilder软件制作mdx文件。

请仔细阅读文件夹下面的`manual.txt`文件，基本格式如下：

每个词条基本设置如下：

```xml
English
English test
</>
中文
中文测试
</>
```

> 上述代码中，最上面时索引，中间是具体内容，最后是分割符。

当然可以使用内置css和标签属性，设置相应样式。

```xml
Whole
<font size=5>whole</font>
<br>
<font face="Kingsoft Phonetic Plain, Tahoma">(hol,hJl; houl)</font>
</>
```

还可以额外添加图片和音频。

**还是推荐使用外部css和js文件，需要在基本设置的基础额外设置如下（样本格式）：**

```xml
hypergol
<link rel="stylesheet"href="WKT.css"type="text/css"><div class="wic"><a href="https://en.wiktionary.org/wiki/hypergol#English"target="_new"><img src="x.png" class="qkx"></a><h1 id="firstHeading" class="bxr"><span class="gec">hypergol</span></h1><h3><span class="vbz" id="Noun">Noun </span><p class="aak">(<i>plural</i> <span class="apd"><b class="nyr">hypergols</b></span>)</p></h3><ol class="p3i"><li>Any <a href="entry://hypergolic">hypergolic</a> <a href="entry://propellant">propellant</a>.</li></ol></div>
</>
```

> 上述代码中依然是三行，最上面时索引，中间是具体内容，最后是分割符。

为了更清晰结构，结构化如下（只为了分析，具体使用时依然是**三行**）：

```xml
hypergol
<link rel="stylesheet" href="WKT.css" type="text/css">
<div class="wic">
    <a href="https://en.wiktionary.org/wiki/hypergol#English" target="_new">
        <img src="x.png" class="qkx">
    </a>
    <h1 id="firstHeading" class="bxr">
        <span class="gec">hypergol</span>
    </h1>
    <h3>
        <span class="vbz" id="Noun">Noun </span>
        <p class="aak">(
            <i>plural</i>
            <span class="apd">
                <b class="nyr">hypergols</b>
            </span>)</p>
    </h3>
    <ol class="p3i">
        <li>Any
            <a href="entry://hypergolic">hypergolic</a>
            <a href="entry://propellant">propellant</a>.</li>
    </ol>
</div>
</>
```

