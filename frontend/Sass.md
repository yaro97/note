# Less $ SASS

## 概述

现在前端的预处理语言，Less & SASS两家独大，根据StackOverflow的统计数据,SASS的使用者明显更多，不过SASS上面有一个问题，编译SASS需要安装Ruby，而Ruby官网因为众所周知的原因在国内访问不了，因此仅仅就国内来说，很多人因此选择了Less。

## less与Sass的区别

其实他们俩区别真不大，主要的区别如下：

- 编译环境不一样:SASS安装需要Ruby环境；Less需要引入Less.js来处理。
- 变量符不一样:Less :`@`，SASS：`$`。
- 作用域其实也有点不同:Less是存在局部变量这么一说的，SASS则一直都是后面定义的变量会替换掉前面定义的，而不管前面那个变量定义的层级。
- 输出设置:Less没有输出设置。SASS则可以配置输出设置：nested，compact，compressed，expanded，默认nested。
- SASS支持条件判断和循环语句，比如ifelse,for等等。而Less不支持。这一点其实是比较重要的一点，权衡考量使用SASS还是Less，也就在这了。不过这个需求对我来说，一般来说没有或者没这么迫切，对大部分的业务需求来说应该也是吧。

> 所以该选择哪个？ 其实没关系，如果你用Less那就继续Less。功能需求更多，那SASS会更适合你。

## Sass与Scss区别

二者主要是语法的区别;
- Sass采用类似python的缩进的语法; 很多习惯了css的`{}`语法更偏向于less;
- 为了兼容css语法, 官网又推出了支持css`{}`语法的Scss(sassy时髦的 css)
- 个人选择Scss语法;

> 以下内容`Sass`和`Scss`不做区分;

# Sass/Scss的编译

## 编译工具介绍

- 使用命令行工具;
    - Sass使用Ruby语言编写,所以可以使用Ruby的`gen`工具安装`sass`;
    - 为了其他语言的可以使用Sass,发行了Sass的引擎`LibSass`(C/C++);
    - LibSass is just a library. 为了其他语言使用Sass,需要包裹成[相应的Wrappers](https://sass-lang.com/libsass);
    - Node.js下的wrapper是`node-sass`;
- 使用Sublime/Vscode插件;
- 自动化工具:Gulp/Grunt/Webpack等
- 使用考拉(Koala)等UI软件;
- 其他

## node-sass使用介绍

个人不希望在安装一个Ruby, 所以算则Node.js的Wrapper:`node-sass`

- 安装
    - npm i nrm -g
    - nrm use taobao
    - npm i -g node-sass
    - node-sass -v
- 使用
    - node-sass --help
    - 编译显示到屏幕上: node-sass xxx.scss
    - 编译到css文件: node-sass xxx.scss xxx.css
    - 监视文件(夹): 
        ```sh
        node-sass --watch src/test.scss dist/output.css # 监视文件
        # node-sass -w test.scss dist/output.css --output-style compact
        node-sass -wr scss\ -o css\ --output-style expanded # 监视文件夹
        # watch 文件夹, 且只编译入口文件, 忽略Partial文件
        # -r, --recursive -o, --output  
        node-sass -wr scss\ -o css\ --output-style expanded --indent-width 4 # Tab=4
        ```
- `--output-style`四种格式:
    - nested(默认):
        ```css
        body {
            color: #666; }
            body h1 {
                background-color: #666; }
        ```
    - expanded(平时手写的样式)
        ```css
        body {
            color: #666;
        }

        body h1 {
            background-color: #666;
        }
        ```
    - compact
        ```css
        body { color: #666; }

        body h1 { background-color: #666; }
        ```
    - compressed(生产环境)
        ```css
        body{color:#666}body h1{background-color:#666}
        ```

# 语法

## 变量

```scss
$primary-color: #1269b5;
$primary-border: 1px solid $primary-color;

div.box {
    background-color: $primary-color;
}

h1.page-header {
    border: 1px solid $primary-border;
}
// 变量的定义/引用中 - 和 _ 可以混着用, 但是建议统一
```

## 嵌套(选择器/属性)

- 基本使用

    ```scss
    .nav {
        height: 100px;
        ul {
            margin: 0;
            li {
                float: left;
                list-style: none;
                padding: 5px;
            }
        }
    }
    ```

- 父选择器的调用

    以上代码会组成如下选择器: `.nav ul li`, 但是类似`:hover`的选择器就需要添加`&`如下:

    ```scss
    a {
        display: block;
        color: #000;
        &:hover {
            color: #c00;
        }
    }
    ```

    这里的`&`表示父选择器`a`, 再如:

    ```scss
    .nav {
        height: 100px;
        ul {
            margin: 0;
            li {
                float: left;
            }
        }
        & &-text {
            font-size: 15px;
        }
    }
    ```

    这里的`&`表示父选择器`.div`, `& &-text`代表`.nav .nav-text`

- 属性的嵌套

    使用`属性前缀:`实现嵌套,如:

    ```scss
    body {
        font: {
            family: Helvetica, Arial, sans-serif;
            size: 15px;
            weight: normal;
        }
    }

    .nav {
        border: 1px solid #000 {
            left: 0;
            right: 0;
        }
    }
    ```

## Mixin混合

- Minxin概述: 
    - 有名字的一堆样式(宏/代码块/函数...);
    - 实现代码(块)的复用;
    - 可以传参(可以指定默认值),使用起来更灵活;

- 语法: 
    - 定义: `@mixin 名字($参数1, $参数2, ...) { ... }`
    - 调用: `@include 名字`或`@include 名字($a, $b, ...)`

- 基本使用:

    ```scss
    @mixin alert {
        color: #8a6b3a;
        background-color: #fcf8e3;
    }

    .alert-warning {
        @include alert; //无参数, 不建议 alert()
    }
    ```

- 可以嵌套:

    ```scss
    @mixin alert {
        color: #8a6b3a;
        background-color: #fcf8e3;
        a {
            color: #158f70;
        }
    }

    .alert-warning {
        @include alert; //无参数, 不建议 alert()
    }
    ```

    > 生成 `.alert-warning a { color: #158f70; }`

- 传参(位置参数/命名参数)

    ```scss
    @mixin alert($t-color, $b-color) {
        color: $t-color;
        background-color: $b-color;

        a {
            color: darken($t-color, 10%); //调用内置函数
        }
    }

    .alert-warning {
        @include alert(#8a6d3f, #fcf8e2); //位置参数传参
    }

    .alert-info {
        @include alert($b-color: #19b340, $t-color: #b62f82); //命名参数传参
    }
    ```

## 继承(扩展)

- 概述
    - 让一个选择器里面的样式继承另一个的所有样式;
    - `@extend`的意思是:**所有带有被继承的选择, 都会被copy一份**

- 语法: `@extend 选择器`

- 基本使用
    ```scss
    .alert {
        padding: 15px;
    }

    .alert a {
        font-weight: bold;
    }
    // 与 .alert 相关选择器的样式,也会被继承!! -> .alert-info a

    .alert-info {
        @extend .alert;
        background-color: #d9edf7;
    }
    ```

    编译的结果如下:

    ```css
    .alert, .alert-info {
        padding: 15px;
    }

    .alert a, .alert-info a {
        font-weight: bold;
    }

    .alert-info {
        background-color: #d9edf7;
    }
    ```

    > 所有`.alert`相关的选择器,都会被`.alert-info`替换并copy一份

## Partials与`@import`

- 概述:
    - css也带有`@import`语句, 但是每次import都会引发http请求,进而影响页面加载速度;
    - Scss可以实现开发时样式模块化, 最终编译成一个css文件上线;
    - Scss规定每个Partial的文件名以`_`开头;
    - 监视一个文件夹时,只编译`入口文件`, Partial文件不会被编译;
    - Partial文件引入时:如`_base.scss`只需要`@import 'base';`

## 注释comment

Scss支持三种类型的注释:
- 单行: 编译结果**不保留**(`// ...`);
    ```scss
    // 单行注释
    ```
- 多行: **除了**`compressed`编译, 编译结果中会**保留**(`/* ... */`);
    ```scss
    /*
    * 天王盖地虎
    * 小鸡炖蘑菇
    */
    ```
- 强制: 编译结果中**保留**(`/*! ... */`, 首字符为`!`)；
    ```scss
    /*!
    * 天王盖地虎
    * 小鸡炖蘑菇
    */
    ```

## Scss的数据类型(Data Type)

### 概述

`sass`提供了交互的shell(`sass -i`)用于测试, 但是`node-sass`貌似没有提供;

但是可以使用如下方式,变相的实现:

```scss
$var: type-of(5); //number
$var: type-of(5px); //number
$var: type-of(hello); //string
$var: type-of('hello'); //string
$var: type-of(1px solid #000); //list
$var: type-of(5px 10px); //list
$var: type-of(#ff0000); //color
$var: type-of(red); //color
$var: type-of(rgb(255, 0, 0)); //color
$var: type-of(hsl(0, 100%, 50%)); //color

p:before {
    content: $var;
}
```

### number

- 基本计算如下:

    ```scss
    $var: 2 + 8; //10
    $var: 2 * 8; //16
    $var: 8 / 2; //8/2  会保留原来的格式;
    $var: (8 / 2); //4  添加括号强制计算
    $var: (8px / 2px); //4
    $var: (8px + 2); //10px
    $var: (8px * 2px); //报错 16px*px
    $var: (3 + 2 * 5px); //13px
    $var: ((3 + 2) * 5px); //25px

    p:before {
        content: $var;
    }
    ```

- scss自带number相关函数:

    ```scss
    $var: abs(-10); //10
    $var: abs(-10px); //10px
    $var: (10px / 4); //2.5px
    $var: round(10px / 4); //3px 四舍五入
    $var: ceil(9px / 4); //3px 向上取整
    $var: floor(11.5px / 4); //2px 向下取整
    $var: percentage(650px / 1000px); //65%
    $var: min(1, 2, 3px); //1
    $var: min(1px, 2, 3px); //1px
    $var: max(1px, 2, 3em); //3em

    p:before {
        content: $var;
    }
    ```

### string

> Scss中字符串,可以带引号(单双都可),也可以不带引号; 引号里面的字符串可以包含空格;

- 基本计算如下:

    ```scss
    $var: hello + " world"; //hello world
    $var: hello + "world"; //helloworld
    $var: hello + 8080; //hello8080
    $var: hello - world; //hello-world
    // $var: hello * 2; //报错
    $var: hello / world; //hello/world

    p:before {
        content: $var;
    }
    ```

- scss自带string相关函数:

    ```scss
    $var1: greeting; 
    $var2: GREETING; 
    $var: greeting; //greeting
    $var: to-upper-case($var1); //GREETING
    $var: to-lower-case($var2); //greeting
    $var: str-length($var1); //8
    $var: str-index($var1, "greet"); //1
    $var: str-index($var1, "reet");
    $var: greeting;
    $var: str-insert($var, ".net" , 9); //greeting.net

    p:before {
        content: $var;
    }
    ```

### color

CSS中表示颜色的方式有: HEX/RGB/RGBA/HSL/String

- 基本计算如下:
    ```scss
        $var: rgb(255, 0, 0); //red
    $var: rgb(100%, 0, 0); //red
    $var: rgb(255, 100, 0); //#ff6400
    $var: rgba(255, 100, 0, 0.8); //rgba(255, 100, 0, 0.8)
    $var: hsl(0, 100%, 50%); //red
    $var: hsl(60, 100%, 50%); //yellow
    $var: hsla(60, 100%, 50%, 0.5); //rgba(255, 255, 0, 0.5);
    ```

- scss自带的color相关函数
    ```scss
    $base-color: #ff0000;
    $base-color-hsl: hsl(0, 100, 50%);
    $var: adjust-hue($base-color, 137deg); //#00ff48 色相
    $var: adjust-hue($base-color-hsl, 137deg); //#00ff48
    $var: lighten($base-color, 30%); //变亮
    $var: darken($base-color, 30%); //变暗
    $var: saturate($base-color, 30%); //饱和度+
    $var: desaturate($base-color, 30%); //饱和度-
    $var: opacify($base-color, 0.3); //不透明度+
    $var: transparentize($base-color, 0.2); //不透明度-

    p:before {
        content: $var;
    }
    ```

### list

list是用`空格`或`,`分割的一系列数据, 如: `border: 1px solid red`和`font-family: Courier, "Lucida Console`;

- list也可以包含其他list,如:
    - `padding: 5px 10px, 5px 0`包含两个用`,`分割列表;
    - `padding: (5px 10px) (5px 0)`也包含两个列表;

- scss自带的color相关函数:

    ```scss
    $var: length(5px 10px); //2
    $var: length(5px 10px 5px 0);//4 
    $var: nth(5px 10px, 1); //5px
    $var: nth(5px 10px, 2); //10px
    $var: index(1px solid red, solid); //2
    $var: append(1px 2px 3px, 4px); //1px 2px 3px 4px
    $var: append(1px 2px 3px, 4px, comma); //1px, 2px, 3px, 4px
    $var: join(1px 2px, 3px 5px);//1px 2px 3px 5px
    $var: join(1px 2px, 3px 5px, space);//1px 2px 3px 5px

    p:before {
        content: $var;
    }
    ```

### map

map - 键值对的列表: `$map: (key1: value1, key2: value2, key3: value3)`;

- scss自带的color相关函数:

    ```scss
    $colors: (light: #ffffff, dark: #000000);
    $var: length($colors); //2
    $var: nth($colors, 1); //light #ffffff
    // map是键值对组成的list, 所有list相关的函数map都能用;
    $var: map-get($colors, dark); //#000000
    $var: map-get($colors, light); //#ffffff
    $var: map-keys($colors); //light, dark
    $var: map-values($colors); // #ffffff, #000000
    $var: map-has-key($colors, light); //true
    $var: map-merge($colors, (gray: #e5e5e5)); //(light: #ffffff, dark: #000000, gray: #e5e5e5)
    $var: map-remove($var, light, gray); //dark: #000000

    p:before {
        content: $var;
    }
    ```

### boolean

布尔值(true/false)

- scss自带的boolean相关函数

    ```scss
    $var: 5px > 3px; //true
    $var: 5px > 30px; //false
    $var: 5px <= 30px; //true
    $var: 5px <= 30px or 1px > 5px; //true
    $var: (5px <= 30px) and (1px > 5px); //false
    $var: not(5px > 30px);//true
    $var: not (5px > 30px);//true

    p:before {
        content: $var;
    }
    ```

### interpolation(插入)

> interpolation[ɪnˌtɜ:pə'leɪʃn]: 
> The interpolation appears to have been inserted very soon after the original text was finished.	
> 插补文字似乎是在原文完成后不久被补充进来的。

- 使用场景: 在`注释`/`选择器`/`属性`中使用变量时,就需要`interpolation`;
- 语法: `#{变量}`
- 基本使用:

    ```scss
    $version: '0.0.1';
    /* 项目当前的版本为: #{$version} */

    $name: "info";
    $attr: "border";

    .alert-#{$name} {
        #{$attr}-color: #ccc;
    }
    ```

## Control Directives 控制指令


### `@if`, `@else if`, `@else`指令

- 语法: `@if 条件 {...}`
- 基本使用:

    ```scss
    $theme: white;
    $use-prefixes: true;

    body {
        @if $theme==black {
            background-color: #000;
        }

        @else if $theme==white {
            background-color: #fff;
        }

        @else {
            background-color: #ccc;
        }
    }


    .rounded {
        @if $use-prefixes {
            -webkit-border-radius: 5px;
            -moz-border-radius: 5px;
            -ms-border-radius: 5px;
            -o-border-radius: 5px;
        }

        border-radius: 5px;
    }
    ```

### `@for`指令

- 语法: 
    - 1-9:`@for $var from 1 to 10 {...}`
    - 1-10: `@for $var from 1 through 10 {...}`

- 基本使用:

    ```scss
    $columns: 4;

    @for $i from 1 through $columns {
        .col-#{$i} {
            width: 100% / $columns * $i;
        }
    }
    ```

    编译结果如下:

    ```css
    .col-1 {
        width: 25%;
    }

    .col-2 {
        width: 50%;
    }

    .col-3 {
        width: 75%;
    }

    .col-4 {
        width: 100%;
    }
    ```

### `@each`指令

- 语法: `@each $li in $list {...}`
- 基本使用:

    ```scss
    $icons: success error warning;

    @each $icon in $icons {
        .icon-#{$icon} {
            background-image: url("../images/icons/#{$icon}.png");
        }
    }
    ```

    编译生成:

    ```css
    .icon-success {
        background-image: url("../images/icons/success.png");
    }

    .icon-error {
        background-image: url("../images/icons/error.png");
    }

    .icon-warning {
        background-image: url("../images/icons/warning.png");
    }
    ```

### `@while`指令

- 语法: `@while 条件 {...}`
- 基本使用:

    ```scss
    $i: 6;

    @while $i>0 {
        .item-#{$i} {
            width: 5px * $i;
        }

        $i: $i - 2;
    }
    ```

    编译生成

    ```css
        .item-6 {
            width: 30px;
        }

        .item-4 {
            width: 20px;
        }

        .item-2 {
            width: 10px;
        }
    ```

### 用户自定义函数

上面我们使用了很多Scss内置的函数,我们还可以自己自定义函数;

- 语法: `function 函数名(参数1, 参数2){...}`
- 基本使用:

    ```scss
    $colors: (light: #fff, dark: #000);

    @function color($colors, $key) { //定义函数
        @return map-get($colors, $key);
    }

    body {
        background-color: color($colors, "dark"); //调用函数
    }
    ```

    编译生成

    ```css
    body {
        background-color: #000;
    }

    ```

### 警告与错误

在我们自定义的`mixin`和`function`中,可以包含一些警告/错误信息;当不正确使用时可以看到这些提示信息;

上面我们使用了很多Scss内置的函数,我们还可以自己自定义函数;

- 语法: 
    - `@warn "警告的提示信息";`
    - `@error "错误的提示信息";`
- 基本使用:

    ```scss
    $colors: (light: #fff, dark: #000);

    @function color($colors, $key) {
        @if not map-has-key($colors, $key) {
            @warn "在 $colors 中没有 #{$key}";
            // @error "在 $colors 中没有 #{$key}";
        }
        @return map-get($colors, $key);
    }

    body {
        background-color: color($colors, "gray"); //错误调用:没有grap这个key
    }
    ```

    如此便会在CMD显示相关`警告`/`错误`信息;
