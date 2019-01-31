# 概述

1. 开发中需要引入很多JS文件 -> html页面中有很多<script></script>;
2. 缺点: 加载时间过长, 而且无法知道他们之间的依赖关系;不美观, 维护困难;
3. JS文件合并时(无脑合并),为了防止变量名冲突,每个JS文件需要添加IIFE(立即执行函数表达式)的外壳;
4. So,我们需要一个规范,来管理这些JS文件.

# AMD规范-require.js

## 概述

- Asynchronous Module Defination 异步模块定义。`代表库(貌似唯一)就是require.js`。
- 优点:v
	- JS文件异步加载,避免网页失去响应;
	- 模块之间依赖关系,便于维护;
- 可以参考[阮一峰的require.js](http://www.ruanyifeng.com/blog/2012/11/require_js.html)博客：

为什么叫做AMD规范?

1. AMD规范使用依赖注入的形式，所有的依赖项是同时加载的，没有回来的先后之分，都回来了才执行回调函数。也就是说，回调函数是AMD规范的特征。
2. require()里面的语句是异步语句，把依赖项都加载完毕之后才执行回调函数，此时就是“异步”的由来。
3. AMD规范中，如果两个模块之间有“插件”的关系，彼此依赖，可以用shim中定义这个关系。

AMD现状:

- 很惨!!
- 只有require.js对AMD进行了实现。
- Angular1使用了AMD规范，而Angular2放弃了AMD规范，转入了CMD阵营，Angular4、5都是CMD的。


## 简单的Demo - 使用步骤

1. 首先[下载](https://requirejs.org/docs/download.html)最新版本;
2. 文件目录 

    ```
    ┣  js
    ┃  ┣  lib
    ┃  ┃  ┣  require.js
    ┃  ┣  main.js
    ┣  index.html
    ```
3. 在main.js中写一条语句：`alert("你好")`;
4. index.html中：

    ```html
    <script type="text/javascript" src="js/lib/require.min.js" data-main="js/main"></script>
    ```

    > 引入了库，在这个库的文件的script上，写data-main，路径是主入口的main.js文件，省略了扩展名.js。

## 暴露和引用

- `index文件只需要引入main.js即可,其他JS文件暴露API,main.js通过API直接/间接引用`.
- 我们在js文件夹中创建yuan.js、fang.js的文件：

    ```
    ┣  js
    ┃  ┣  lib
    ┃  ┃  ┣  require.js
    ┃  ┣  main.js
    ┃  ┣  yuan.js
    ┃  ┣  fang.js
    ┣  index.html
    ```

- yuan.js:
    - 我们使用define()来包裹一个函数，define不是ECMAScript的语法，而是require.js的语法。
    - 函数里面可以写任何语句，需要暴露的东西，写return来暴露。

    ```js
    define(function(){
        function mianji(r){
            return 3.14 * r * r;
        }
        return {
            mianji   //k、v相同，省略v
        }
    });
    ```
 
- fang.js:

    ```js
    define(function(){
        function mianji(a,b){
            return a * b;
        }
        return {
            mianji
        }
    });
    ```

- main.js：
    主文件需要使用“依赖注入”（dependencies injection）的方式引入这个模块。

    ```js
    require(['yuan','fang'],function(y,f){
        alert(y.mianji(10));
        alert(f.mianji(10,20));
    });
    // 我们发现，依赖注入的语法是：
    require(["模块1","模块2","模块3"],function(模块1,模块2,模块3){
    });
    ```

- 注意：
	1. 依赖的文件名必须有引号，注入的时候没有引号的；
	2. 注入的时候的名字可以任取，所以require.js是通过依赖注入的顺序来产生对应关系的：
	3. 依赖的时候，没有拓展名，模块的默认名字就是文件名。

## 别名

- 模块的名字默认是文件名。

    ```js
    require(['yuan','fang'],function(y,f){
        alert(y.mianji(10));
        alert(f.mianji(10,20));
    });
    ```

- 如果我们想把依赖的名字改掉，此时可以使用require对象的config方法来配置paths项：

    ```js
    require.config({
        paths: {
            "circle" : "yuan"  //没有.js扩展名
        }
    });
    require(['circle','fang'],function(y,f){
        alert(y.mianji(10));
        alert(f.mianji(10,20));
    });
    ```

## 加载非规范模块

- `AMD规范最强大的事情，就是在于一个普通的JS文件如果不符合AMD规范，可以设置暴露口`。
 
- 什么叫做符合AMD规范：如果一个库在创建的时候有这么一条语句（伪代码）：

    ```js
    if(define){
        define(function(){
            return {
                $
            }
        })
    }
    ```

    > 此时就说明对require.js兼容了，此时叫做符合AMD规范。
 
- 比如我们引入jquery库：

    ```js
    require.config({
        paths: {
            "circle" : "yuan",
            "jq" : "lib/jquery.min"
        }
    });

    require(['circle','fang','jq'],function(y,f,$){
        alert(y.mianji(10));
        alert(f.mianji(10,20));
        $("#box").css("background-color" , "red");
    });
    ```

    > 结果报错：为什么会报错，就是因为jQuery是不符合AMD规范的，天生是没有对define做适配。

- 此时解决办法就是加shim(垫片)：

    ```js
    require.config({
    paths: {
        "circle" : "yuan",
        "jq" : "lib/jquery.min"
        },
        shim: {
            'jq': {exports : '$'}
        }
    });
     
    require(['circle','fang','jq'],function(y,f,$){
        alert(y.mianji(10));
        alert(f.mianji(10,20));
        $("#box").animate({"font-size":400},1000);
    });
    ```

## 引入有依赖的库

- 比如我们引入jquery-ui，很明显jquery-ui是jquery的插件。此时我们说jquery-ui依赖jquery。
- 此时我们要在shim中定义这层关系：

```js
require.config({
    paths: {
        "circle" : "yuan",
        "jq" : "lib/jquery.min",
        "jqui" : "lib/jquery-ui.min"
    },
    shim: {
        'jq': {exports : '$'},
        'jqui': {deps: ['jq']}
    }
});
 
require(['circle','fang','jq','jqui'],function(y,f,$,jqui){
    alert(y.mianji(10));
    alert(f.mianji(10,20));
    $("#box").animate({"font-size":400},1000);
    $("#box").draggable();
});
```

## 多级引用

- main.js可以引用jihe.js,jihe又可以引用yuan.js/fang.js...
- 如此便是多级引用,即任何普通模块也可以有依赖/注入。

    ```
    ┣  js
    ┃  ┣  lib
    ┃  ┃  ┣  require.js
    ┃  ┣  main.js
    ┃  ┣  yuan.js
    ┃  ┣  fang.js
    ┃  ┣  jihe.js
    ┣  index.html
    ```

    ```js
    //jihe.js
    define(["fang","circle"],function(fang,circle){
        return {
            fang,
            circle
        }
    });
    ```

- 主文件的局部：

    ```js
    require(['jihe','jq','jqui'],function(jihe,$,jqui){
        alert(jihe.circle.mianji(10));
        alert(jihe.fang.mianji(10,20));
        $("#box").animate({"font-size":400},1000);
        $("#box").draggable();
    });
    ```

    > 我们的主文件只依赖了jihe（jquery先不考虑），但是由于jihe依赖了fang和yuan，所以fang和yuan都加载了。

# CMD规范

## 概述

- 概述:
    - Common Module Definition，通用模块定义。
    - 它的实现：`common.js、sea.js（淘宝玉伯）、node.js`。
- 总结: 
    1. nodejs是遵循CMD规范的，可以裸奔CMD规范。所以大家已经会了CMD规范了；
    2. `所有的模块`都要用define(function(`require,exports,module`){})包裹，称为“`标准壳`”；
    3. 暴露有两种途径exports.** = ** ; module.exports = ** ;区别见《`nodejs`第1天笔记》；
    4. 引用的时候用`require()`引用，require谁就执行谁，会死等这个文件加载完毕，没有回调函数。
    5. CMD规范中没有node_modules这个神奇的文件夹的概念，是nodejs自己添加的特性。
- 补充: 
    - AMD、CMD规范和业务一点关系没有，就是纯粹的文件组织的形式。
    - 网页DOM开发是不会用AMD、CMD规范的;
    - 现在`学习AMD、CMD规范的意义就是服务于Angular、React、Vue`的。

## 简单Demo

- 我们看看sea.js的简单实现;

- 目录树

    ```
    ┣  js
    ┃  ┣  lib
    ┃  ┃  ┣  sea.js
    ┃  ┣  main.js
    ┃  ┣  yuan.js
    ┃  ┣  fang.js
    ┃  ┣  People.js
    ┣  index.html
    ```

- main.js:

    ```js
    define(function(require,exports,module){
        var yuan = require("./yuan.js");
        var fang = require("./fang.js");
        alert(yuan.mianji(10))
        alert(fang.mianji(10,20))
    });
    ```

- yuan.js:

```js
define(function(require,exports,module){
    function mianji(r){
        return r * r * 3.14;
    }

    exports.mianji = mianji;
});
```

- fang.js:

```js
define(function(require,exports,module){
    function mianji(a,b){
        return a * b;
    }

    exports.mianji = mianji;
});
```

- People.js:

```js
define(function(require,exports,module){
    function People(){
    }

    module.exports = People;
});
```

- index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <script type="text/javascript" src="js/lib/sea.min.js"></script>
    <script type="text/javascript">
        seajs.use("./js/main.js");
    </script>
</body>
</html>
```

# ES6的CMD语法

## 概述

- 参考:[阮一峰Module 的语法](http://es6.ruanyifeng.com/#docs/module)
- `JS一直没有模块体系 -> 大型项目混乱, 于是ES6之前社区制定了一些模块加载方案,主要有`:
	- `CMD - CommonJS/sea.js 主要用于服务器`
	- `AMD - require.js 主要用于浏览器`
- CMD语法是commonjs在2005年左右提出的语法，被nodejs全盘采纳。
- ES6在语言标准层面上,主要参考了python 的模块体系; 完全可以取代之前的规范;
- ES6 模块的设计思想是尽量的静态化，使得编译时就能确定模块的依赖关系，以及输入和输出的变量。CommonJS 和 AMD 模块，都只能在运行时确定这些东西。

    ```js
    // ES6模块
    import { stat, exists, readFile } from 'fs';
    ```

    > - ES6 模块不是对象，而是通过export命令显式指定输出的代码，再通过import命令输入。
    > - 上面代码的实质是从fs模块加载 3 个方法，其他方法不加载。这种加载称为“编译时加载”或者静态加载，即 ES6 可以在编译时就完成模块加载，效率要比 CommonJS 模块的加载方式高。当然，这也导致了没法引用 ES6 模块本身，因为它不是对象。
- webpack支持新标准，webpack在没有babel-loader的存在下，天生能够识别import的导入语法，从而进行智能的文件合并。

## export导出

### 方式1

```js
// profile.js
export var firstName = 'Michael';
export var lastName = 'Jackson';
export var year = 1958;

export function multiply(x, y) {
    return x * y;
};

export class multiply {
    //...
}
```

### 方式2(推荐)

```js
// profile.js
var firstName = 'Michael';
var lastName = 'Jackson';
var year = 1958;

export {firstName, lastName, year};
```

> export写在文件的尾部

### as别名

```js
function v1() { ... }
function v2() { ... }

export {
    v1 as streamV1,
    v2 as streamV2,
    v2 as streamLatestVersion
};
```

### 特别注意

- export命令规定的是对外的`接口`，必须与模块内部的变量建立一一对应关系(而`不是具体的值`)。

    ```js
    // 报错-直接输出1
    export 1;

    // 报错-通过变量间接输出1
    var m = 1;
    export m;

    // 正确
    export var m = 1;

    // 正确-类似于{ m: m }
    var m = 1;
    export {m};

    // 正确-类似于{ m: n }
    var m = 1;
    export {m as n};
    ```

- export语句输出的接口，与其对应的值是`动态绑定关系`，即通过该接口，可以取到`模块内部实时的值`。而CommonJS 模块输出的是值的缓存，不存在动态更新.
- `export命令可以出现在模块的任何位置，只要处于模块顶层就可以(不能在块级作用域)`。

## import导入

### 方式1

```js
// main.js

//类似于 { m: m }
import {m} from './profile.js';
import {firstName, lastName, year} from './profile.js';
```

### as别名

```js
//类似于 { lastName: surname }
import { lastName as surname } from './profile.js';
```

### 特别注意

- import命令输入的变量本质是接口,所以是`只读的`,即使是对象(可以改写属性)也不建议操作.
- import后面的from指定模块文件的位置--可以省略 .js 
- `import命令具有提升效果`，会提升到整个模块的头部，首先执行。
- 由于import是静态执行，所以不能使用表达式和变量.

    ```js
    // 报错
    import { 'f' + 'oo' } from 'my_module';
    ```

- import语句会执行所加载的模块,多次重复执行同一句import语句，那么只会执行一次.

## *导入所有

```js
//从'./circle'中引入所有的接口,附着则circle对象上
import * as circle from './circle';

circle.area(5);//使用
```

## export default导出默认

### 说明

- export default命令用于指定模块的`默认输出`,显然,一个模块只能有一个默认输出,所以,`该命令只能用一次`.
- export default本质上就是输出一个叫做default的变量/方法,系统允许你改名.

### 基本使用

```js
//// modules.js////
export default function foo() {
    console.log('foo');
}

// 或者写成
function foo() {
	console.log('foo');
}
export default foo;
// 等同于
export {foo as default};

//// app.js////
import { default as foo } from 'modules';
// 等同于
import foo from 'modules'; //注意没有 { }
```

### 特别注意

- export default命令`只能导出一个变量`;
- **对应的import不能使用 `{}`**;
- `export default命令的本质是将后面的值赋值给default`,所以有:

    ```js
    // 正确
    export default 42;
    // 报错
    export 42;
    ```

    >上面代码中，后一句报错是因为没有指定对外的接口，而前一句指定对外接口为default。
- 如果想在一条import语句中，同时输入默认方法和其他接口，可以写成下面这样:

    ```js
    import _, { each, forEach } from 'lodash';
    ```

## 中转模块



- 情况一(转发): B模块负责从C模块导入foo bar,然后再导出到A模块.

    ```js
    export { foo, bar } from 'my_module';

    // 可以简单理解为
    import { foo, bar } from 'my_module';
    export { foo, bar };

    // 整体输出
    export * from 'my_module';

    // default输出
    export { default } from 'foo';
    ```

    > 但B模块不能使用 foo 和bar

- 情况二(接口改名):B模块负责从C模块导入foo bar,同时把名称修改为FOO BAR,然后再导出到A模块;

    ```js
    //改名
    export { foo as FOO } from 'my_module';

    //具名接口改为默认接口
    export { es6 as default } from './someModule';
    // 等同于
    import { es6 } from './someModule';
    export default es6;

    //默认接口也可以改名为具名接口。
    export { default as es6 } from './someModule';
    ```

## 跨模块常量

const命令声明的常量只能在当前代码块有效,如果要被多个模块(文件)共享可以如下操作:

```js
// constants.js 模块
export const A = 1;
// test1.js 模块
import * as constants from './constants';
console.log(constants.A); // 1
// test2.js 模块
import {A} from './constants';
console.log(A); // 1
```

> 更多[参考](http://es6.ruanyifeng.com/#docs/module#%E8%B7%A8%E6%A8%A1%E5%9D%97%E5%B8%B8%E9%87%8F):

