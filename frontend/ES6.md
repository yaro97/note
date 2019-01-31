# ES6概述-调试

> 参考
>
> 1. 中文: <http://es6.ruanyifeng.com
> 2. 英文: <http://es6-features.org>

## 概述

### ES6怎么来的	

- CMAScript 和 JavaScript
    - ECMA 是标准，JS语言 是实现(另外一个是ActionScript语言)
    - ECMAScript 简称 ECMA 或 ES
    - ECMA每年更新一个版本
        - 2016->ES7
        - 2017->ES8
- 历史版本
    - 1996, ES1.0 Netscape 将 JS 提交给 ECMA 组织，ES 正式出现
    - 1999, ES3.0 被广泛支持
    - 2011, ES5.1 成为 ISO 国际标准
    - 2015, ES6.0 正式发布

### ES6兼容性	

- S6(ES2015) 支持的环境 IE10+, Chrome, FireFox, 移动端, NodeJS
- 解决不兼容办法，编译、转换
    - 在线转换(不推荐,每次都引入babel)

    ```html
    <!-- 加载 Babel -->
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <!-- 你的脚本代码 -->
    <script type="text/babel">
        const getMessage = () => "Hello World";
        document.getElementById('output').innerHTML = getMessage();
    </script>
    ```

    - 或者提前编译
- Babel 中文网
    - Babel 入门教程 阮一峰
    - Babel 是一个 JavaScript 编译器
    - 一个广泛使用的转码器，可以将ES6代码转为ES5代码，从而在现有环境执行
    - 现在就用 ES6 编写程序，而不用担心现有环境是否支持

## Chrome调试

Chrome新版本支持新版本的ES语法,直接在html中嵌套即可.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <script type="text/javascript">
        var [a,b,c] = [2,3,4];
        console.log(a);
        console.log(b);
        console.log(c);
    </script>
</body>
</html>
```

## Node.js调试

新版本的Node.js也支持ES6语法,直接在命令行输入 node xxx即可.

```js
var [a,b,c] = [1,2,3];
console.log(a);
console.log(b);
console.log(c);
 
var obj1 = {
    a : 1,
    b : 2,
    c : 3
}
 
var obj2 = {
    ...obj1 , 
    b : 8
}
console.log(obj2);
```

## Babel翻译

- 新版本的ES语法用着爽,但是浏览器兼容差;
- 用ES6开发,然后用Babel编译成ES5-的版本,兼容浏览器.
- babel是我们学习的第二个nodejs工作流工具，需要用-g安装（第一个是cnpm）。

> - npm -g install cnpm --registry http://npm.taobao.org/
> - npm -g install babel-cli  #可以使用babel命令(babel --version)
> - cnpm intall --save-dev babel-preset-es2015
> - cnpm install --save-dev babel-plugin-transform-object-rest-spread # 支持扩展运算符

- 使用touch/rename命令在工作目录创建 .babelrc文件：

```json
{
    "presets" : ["es2015"],
    "plugins" : ["transform-object-rest-spread"]
}
```

- 然后就可以使用babel命令翻译了. `babel es6_new.js -o es_old.js`

# let/const命令

## var 的问题

- 可以重复声明，没有报错和警告;
- 大型项目变量太多,很容易重复声明,不报错的话,不易排错

    ```js
    var a = 10
    var a = 5
    alert(a)
    ```

- 无法限制修改

    ```js
    var PI = 3.1415926 //无法限制不修改
    ```

- var没有块级作用域， 只有函数才能创建作用域

    ```js
    if (true) {
        var a = 1
    }
    alert(a) //依然可以访问
    ```

## let命令

### 基本用法

- 用法同var,但是只在let命令的代码块内有效;

    ```js
    {
        let a = 10;
        var b = 1;
    }
    a // ReferenceError: a is not defined.
    b // 1
    ```

- for循环特别适合用let命令:

    ```js
    var a = [];
    for (let i = 0; i < 10; i++) {
        a[i] = function () {
            console.log(i);
        };
    }
    a[6](); // 6
    //上述代码中:i只在本轮循环的{}内有效,每次循环都会生成新的i,JS引擎会记住上一轮循环的值,及所处本轮循环的值
    ```


- 另外，for循环还有一个特别之处，就是设置循环变量的那部分是一个父作用域，而循环体内部是一个单独的子作用域。

    ```js
    for (let i = 0; i < 3; i++) {
        let i = 'abc';
        console.log(i);
    } 
    // abc 
    // abc 
    // abc
    // 输出了 3 次abc。这表明{}内部的变量i与循环变量i不在同一个作用域，有各自单独的作用域。
    ```

### 不存在变量提升

let命令声明的变量一定要在声明后使用，否则报错。

```js
// var 的情况
console.log(foo); // 输出undefined
var foo = 2;
// let 的情况
console.log(bar); // 报错ReferenceError
let bar = 2;
```

### 暂时性死区(TDZ)

- ES6 明确规定，如果区块中存在let和const命令，这个区块对这些命令声明的变量，从一开始就形成了封闭作用域。凡是在声明之前就使用这些变量，就会报错。

    ```js
    if (true) {
        // TDZ开始
        tmp = 'abc'; // ReferenceError
        console.log(tmp); // ReferenceError
        
        let tmp; // TDZ结束
        console.log(tmp); // undefined
        
        tmp = 123;
        console.log(tmp); // 123
    }
    ```

    > 上面代码中，在let命令声明变量tmp之前，都属于变量tmp的“死区”。总之，在代码块内，使用let命令声明变量之前，该变量都是不可用的。这在语法上，称为“暂时性死区”（temporal dead zone，简称 TDZ）。

- “暂时性死区”也意味着typeof不再是一个百分之百安全的操作。

    ```js
    typeof x; // ReferenceError
    let x;

    typeof undeclared_variable // "undefined"
    // 变量x使用let命令声明，所以在声明之前，都属于x的“死区”，只要用到该变量就会报错。因此，typeof运行时就会抛出一个ReferenceError。
    // 如果一个变量根本没有被声明，使用typeof反而不会报错。
    ```

### 不允许重复声明

let不允许在相同作用域内，重复声明同一个变量。

```js
// 报错
function func() {
    let a = 10;
    var a = 1;
}

// 报错
function func() {
    let a = 10;
    let a = 1;
}

function func(arg) {
    let arg; // 报错
}

function func(arg) {
    {
        let arg; // 不报错-新的子作用域
    }
}
```

## 块级作用域

### 为什么需要块级作用域

- `ES5只有全局作用域和函数作用域`,这引起很多不合理的场景:
- 场景一:内层变量可能会覆盖外层变量

    ```js
    var tmp = new Date();
    function f() {
        console.log(tmp);
        if (false) {
            var tmp = 'hello world'; //使用了var->变量提升
        }
    }
    f(); // undefined
    // 原因在于变量提升，导致内层的tmp变量覆盖了外层的tmp变量。
    ```
- 场景二:用来计数的循环变量泄漏为全局变量

    ```js
    var s = 'hello';
        for (var i = 0; i < s.length; i++) {
        console.log(s[i]);
    }
    console.log(i); // 5
    // 变量i只用来控制循环，但是循环结束后，它并没有消失，泄露成了全局变量。
    ```

### ES6 的块级作用域

- let和{}实现ES6的块级作用域

    ```js
    function f1() {
        let n = 5;
        if (true) {
            let n = 10;
        }
        console.log(n); // 5
    }
    ```

- 块级作用域可以无限嵌套, 内部层可以访问外层,外层不能内层;不同块级作用域变量可以同名

    ```js
    {{{{
        {let insane = 'Hello World'}
        console.log(insane); // 报错
    }}}};
    {{{{
        let insane = 'Hello World';
        {let insane = 'Hello World'}
    }}}};
    ```

- 不再需要以前用的自执行函数/立即执行函数表达式（IIFE）--沙箱

    ```js
    // IIFE 写法
    (function () {
        var tmp = ...;
        ...
    }());

    // 块级作用域写法
    {
        let tmp = ...;
        ...
    }
    ```

### 块级作用域与函数声明

- ES5 规定，函数只能在顶层作用域和函数作用域之中声明，不能在块级作用域声明。

    ```js
    // 情况一
    if (true) {
        function f() {}
    }

    // 情况二
    try {
        function f() {}
    } catch (e) {
    // ...
    }
    // 上面两种函数声明，根据 ES5 的规定都是非法的。
    ```

- 但是，浏览器没有遵守这个规定，为了兼容以前的旧代码，还是支持在块级作用域之中声明函数，因此上面两种情况实际都能运行，不会报错。
- ES6 引入了块级作用域，明确允许在块级作用域之中声明函数。ES6 规定，块级作用域之中，函数声明语句的行为类似于let，在块级作用域之外不可引用。
- 为了减轻因此产生的不兼容问题，ES6 在附录 B里面规定，浏览器的实现可以不遵守上面的规定，有自己的行为方式。
- 考虑到环境导致的行为差异太大，`应该避免在块级作用域内声明函数。如果确实需要，也应该写成函数表达式，而不是函数声明语句`。

    ```js
    // 函数声明语句
    {
        let a = 'secret';
        function f() {
            return a;
        }
    }
    // 函数表达式
    {
        let a = 'secret';
        let f = function () {
            return a;
        };
    }
    ```

## const命令

### 基本用法

- const声明的变量不得改变值，这意味着，const一旦声明变量，就必须立即初始化，不能留到以后赋值。

    ```js
    const PI = 3.1415;
    PI // 3.1415
    PI = 3; //不能修改
    // TypeError: Assignment to constant variable.

    const foo; //声明时必须初始化
    // SyntaxError: Missing initializer in const declaration
    ```

- const其他特性同let命令:
    - 只在声明的块级作用域内有效;
    - 声明的常量不提升;
    - 同样存在暂时性死区->只能先声明后使用;
    - 不可重复声明:

    ```js
    var message = "Hello!";
    let age = 25;
    // 以下两行都会报错
    const message = "Goodbye!";
    const age = 30;
    ```

### 本质

- const实际上保证的，并不是变量的值不得改动，而是变量指向的那个内存地址所保存的数据不得改动。
- 对于简单类型的数据（数值、字符串、布尔值），值就保存在变量指向的那个内存地址，因此等同于常量。
- 但对于复合类型的数据（主要是对象和数组），变量指向的内存地址，保存的只是一个指向实际数据的指针，const只能保证这个指针是固定的，至于它指向的数据结构就完全不能控制了。

    ```js
    const foo = {}; //对象

    // 为 foo 添加一个属性，可以成功
    foo.prop = 123;
    foo.prop // 123

    // 将 foo 指向另一个对象，就会报错
    foo = {}; // TypeError: "foo" is read-only

    //=========
    const a = []; //数组

    a.push('Hello'); // 可执行
    a.length = 0; // 可执行

    a = ['Dave']; // 报错
    ```

- 如果真的想将对象冻结，应该使用Object.freeze方法。

    ```js
    const foo = Object.freeze({});
    // 常规模式时，下面一行不起作用；
    // 严格模式时，该行会报错
    foo.prop = 123;
    ```

- 除了将对象本身冻结，对象的属性也应该冻结。下面是一个将对象彻底冻结的函数。

    ```js
    var constantize = (obj) => {
        Object.freeze(obj);
        Object.keys(obj).forEach((key, i) => {
            if (typeof obj[key] === 'object') {
                constantize(obj[key]);
            }
        });
    };
    ```

### ES6 声明变量的六种方法

- `ES5` 只有两种声明变量的方法：`var命令和function命令`。
- `ES6` 除了添加let和const命令，后面章节还会提到，另外两种声明变量的方法：import命令和class命令。
- 所以，`ES6 一共有 6 种声明变量的方法`。

## 顶层对象的属性

### ES5的现状

- 顶层对象，在浏览器环境指的是window对象，在 Node 指的是global对象。
- ES5 之中，顶层对象的属性与全局变量是等价的。

    ```js
    window.a = 1;
    a // 1
    a = 2;
    window.a // 2
    ```

- 顶层对象的属性与全局变量挂钩，被认为是JS最大的设计败笔之一,问题有:
    - 首先是没法在编译时就报出变量未声明的错误，只有运行时才能知道（因为全局变量可能是顶层对象的属性创造的，而属性的创造是动态的）；
    - 其次，程序员很容易不知不觉地就创建了全局变量（比如打字出错）；
    - 最后，顶层对象的属性是到处可以读写的，这非常不利于模块化编程。
    - 另一方面，window对象有实体含义，指的是浏览器的窗口对象，顶层对象是一个有实体含义的对象，也是不合适的。

### ES6的改进

- 一方面规定，为了保持兼容性，var命令和function命令声明的全局变量，依旧是顶层对象的属性；
- 另一方面规定，let命令、const命令、class命令声明的全局变量，不属于顶层对象的属性。
- 也就是说，从 ES6 开始，全局变量将逐步与顶层对象的属性脱钩。

    ```js
    var a = 1;
    // 如果在 Node 的 REPL 环境，可以写成 global.a
    // 或者采用通用方法，写成 this.a
    window.a // 1
    let b = 1;
    window.b // undefined
    //上面代码中，全局变量a由var命令声明，所以它是顶层对象的属性；全局变量b由let命令声明，所以它不是顶层对象的属性，返回undefined。
    ```

## global对象

- ES5 的顶层对象，本身也是一个问题，因为它在各种实现里面是不统一的。
    - 浏览器里面，顶层对象是window，但 Node 和 Web Worker 没有window。
    - 浏览器和 Web Worker 里面，self也指向顶层对象，但是 Node 没有self。
    - Node 里面，顶层对象是global，但其他环境都不支持。
- 同一段代码为了能够在各种环境，都能取到顶层对象，现在一般是使用this变量，但是有局限性。
    - 全局环境中，this会返回顶层对象。但是，Node 模块和 ES6 模块中，this返回的是当前模块。
    - 函数里面的this，如果函数不是作为对象的方法运行，而是单纯作为函数运行，this会指向顶层对象。但是，严格模式下，这时this会返回undefined。
    - 不管是严格模式，还是普通模式，new Function('return this')()，总是会返回全局对象。但是，如果浏览器用了 CSP（Content Security Policy，内容安全策略），那么eval、new Function这些方法都可能无法使用。
- 综上所述，很难找到一种方法，可以在所有情况下，都取到顶层对象。

# 扩展运算符

## 作用

1. 收集`剩余参数(rest参数)`--必须是充当最后一个参数.
2. `数组<->非数组` 之间的转换;
    - 展开数组相当于,把数组两边的方括号去掉.
    - 常用的非数组有:字符串, 伪数组(函数参数/获取的DOM对象...),

    ```js
    //数组变成非数组
    let arr = [1, 2, 3]
    console.log(...arr)

    //字符串变成数组
    let str = 'abcd'
    console.log([...str])

    //将伪数组变成数组
    function fn() {
        return [...arguments].sort((a, b) => a - b)
    }
    console.log(fn(2, 45, 6, 7, 8, 14, 6))
    ```

## 应用

- Math.max 函数的参数只能是N多个数,不能是数组->如何传入数组?

    ```js
    Math.max.apply(null, [1, 2, 3]) //旧方法
    Math.max(...[1, 2, 3]) //新方法
    ```

- `apply([thisObj[,argArray]])` 方法的作用-- 调用函数，并用指定对象替换函数的 this 值，`同时用指定数组替换函数的参数`。
- 复制数组/合并数组/与解构赋值结合使用/把 具有Iterator 接口的对象转变成数组
- 对象的"继承"

    ```js
    obj1 = {
        a: 1,
        b: 2,
        c: 3
    };
    obj2 = {
        ...obj1,
        b: 8
    }
    console.log(obj2);
    ```

- 数组的拼接

    ```js
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    arr1.concat(arr2) //旧方法
    [...arr1, ...arr2] //新方法
    ```

# 解构赋值

## 概述

**定义:** ES6 允许按照一定模式，从数组和对象中提取值，对变量进行赋值，这被称为解构（Destructuring）。

**前提: **
- 左右两个边结构必须一样
- 右边必须是:数组/对象/其他可迭代对象
- 声明和赋值赋值不能分开，必须在一条语句中;

```js
let [a, b, c] = [1, 2, 3]
console.log(a, b, c)
let {x, y, z} = {x: 1, y: 2, z: 3}
console.log(x, y, z)
let [json, arr, num, str] = [{ a: 1, b: 2 }, [1, 2, 3], 8, 'str']
console.log(json, arr, num, str)
```

## 数组的解构赋值

### 基本使用

- 匹配的原则如下: 
    - 两边结构匹配 -> 对应赋值;
    - 左少右多 -> 解构成功(不完全解构);
    - 左多右少 -> 左边多余的变量值为undefined;
    - 解构的颗粒度可以自由控制;
    - 可以使用扩展运算符...

    ```js
    let [foo, [[bar], baz]] = [1, [[2], 3]];
    foo // 1
    bar // 2
    baz // 3

    let [ , , third] = ["foo", "bar", "baz"];
    third // "baz"

    let [x, , y] = [1, 2, 3];
    x // 1
    y // 3

    let [head, ...tail] = [1, 2, 3, 4];
    head // 1
    tail // [2, 3, 4]

    let [x, y, ...z] = ['a'];
    x // "a"
    y // undefined
    z // []

    let [a, [b], d] = [1, [2, 3], 4];
    a // 1
    b // 2
    d // 4
    ```

- 右边必须是可迭代对象(具备 Iterator 接口)

    ```js
    // 报错
    let [foo] = 1;
    let [foo] = false;
    let [foo] = NaN;
    let [foo] = undefined;
    let [foo] = null;
    let [foo] = {};

    //对于 Set 结构，也可以使用数组的解构赋值。
    let [x, y, z] = new Set(['a', 'b', 'c']);
    x // "a"

    //Generator函数也具有Iterator接口
    function* fibs() {
        let a = 0;
        let b = 1;
        while (true) {
            yield a;
            [a, b] = [b, a + b];
        }
    }
    let [first, second, third, fourth, fifth, sixth] = fibs();
    sixth // 5
    ```

### 可以指定默认值

- ES6内部使用严格等于===,只有右边的值===undefined,才会使用默认值

    ```js
    let [x, y = 'b'] = ['a']; // x='a', y='b'
    let [x, y = 'b'] = ['a', undefined]; // x='a', y='b'

    let [x = 1] = [undefined];
    x // 1
    let [x = 1] = [null];
    x // null <-不是undefined
    ```

- 如果默认值是一个表达式，那么这个表达式是惰性求值的，即只有在用到的时候，才会求值。

    ```js
    function f() {
    console.log('aaa');//返回undefined
    }
    let [x = f()] = [1];//因为能取到1,所以f()不会执行
    ```

- 默认值可以引用解构赋值的其他变量,但是该变量必须已经声明

    ```js
    let [x = 1, y = x] = []; // x=1; y=1
    let [x = 1, y = x] = [2]; // x=2; y=2
    let [x = 1, y = x] = [1, 2]; // x=1; y=2
    let [x = y, y = 1] = []; // ReferenceError: y is not defined
    // 上面最后一个表达式之所以会报错，是因为x用y做默认值时，y还没有声明。
    ```

## 对象的解构赋值

### 与数组解构赋值的区别

- 对象的解构与数组有一个重要的不同。数组的元素是按次序排列的，变量的取值由它的位置决定；而对象的属性没有次序，变量必须与属性同名，才能取到正确的值。

    ```js
    let { bar, foo } = { foo: "aaa", bar: "bbb" };
    foo // "aaa"
    bar // "bbb"
    let { baz } = { foo: "aaa", bar: "bbb" };
    baz // undefined
    ```

- 如果变量名与属性名不一致，必须写成下面这样。

    ```js
    let { foo: baz } = { foo: 'aaa', bar: 'bbb' };
    baz // "aaa"
    let obj = { first: 'hello', last: 'world' };
    let { first: f, last: l } = obj;
    f // 'hello'
    l // 'world'

    //这实际上说明，对象的解构赋值是下面形式的简写（参见《对象的扩展》一章）。
    let { foo: foo, bar: bar } = { foo: "aaa", bar: "bbb" };
    ```

    > 也就是说，对象的解构赋值的内部机制，是先找到同名属性，然后再赋给对应的变量。真正被赋值的是后者，而不是前者。

### 对象解构赋值指定默认值

默认值生效的条件是对象的属性值===undefined

```js
var {x = 3} = {};
x // 3
var {x, y = 5} = {x: 1};
x // 1
y // 5
var {x: y = 3} = {};
y // 3
var {x: y = 3} = {x: 5};
y // 5
var { message: msg = 'Something went wrong' } = {};
msg // "Something went wrong"

var {x = 3} = {x: undefined};
x // 3
var {x = 3} = {x: null};
x // null
```

## 字符串的解构赋值

- 字符串也可以解构赋值。这是因为此时，字符串被转换成了一个类似数组的对象。

```js
const [a, b, c, d, e] = 'hello';
a // "h"
b // "e"
c // "l"
d // "l"
e // "o"
```

- 类似数组的对象都有一个length属性，因此还可以对这个属性解构赋值。

```js
let {length : len} = 'hello';
len // 5
```

## 数值和布尔值的解构赋值

- 解构赋值时，如果等号右边是数值和布尔值，则会先转为对象。

    ```js
    let {toString: s} = 123;
    s === Number.prototype.toString // true
    let {toString: s} = true;
    s === Boolean.prototype.toString // true
    ```

    > 上面代码中，数值和布尔值的包装对象都有toString属性，因此变量s都能取到值。

- 解构赋值的规则是:只要等号右边的值不是对象或数组，就先将其转为对象。由于undefined和null无法转为对象，所以对它们进行解构赋值，都会报错。

    ```js
    let { prop: x } = undefined; // TypeError
    let { prop: y } = null; // TypeError
    ```

## 函数参数的解构赋值

- 函数的参数也可以使用解构赋值。

    ```js
    function add([x, y]){
        return x + y;
    }
    add([1, 2]); // 3

    //另一个例子
    [[1, 2], [3, 4]].map(([a, b]) => a + b);
    // [ 3, 7 ]
    ```

    > 上面代码中，函数add的参数表面上是一个数组，但在传入参数的那一刻，数组参数就被解构成变量x和y。对于函数内部的代码来说，它们能感受到的参数就是x和y。

- 函数参数的解构也可以使用默认值

    ```js
    function move({x = 0, y = 0} = {}) {
        return [x, y];
    }
    move({x: 3, y: 8}); // [3, 8]
    move({x: 3}); // [3, 0]
    move({}); // [0, 0]
    move(); // [0, 0]
    ```

    > 上面代码中，函数move的参数是一个对象，通过对这个对象进行解构，得到变量x和y的值。如果解构失败，x和y等于默认值。

## 用途


### 交换变量的值

    ```js
    let x = 1;
    let y = 2;
    [x, y] = [y, x];
    Nice: 简单,易读
    ```

### 从函数返回多个值

    ```js
    // 返回一个数组
    function example() {
        return [1, 2, 3];
    }
    let [a, b, c] = example();
    
    // 返回一个对象
    function example() {
        return {
            foo: 1,
            bar: 2
        };
    }
    let { foo, bar } = example();
    // 函数只能返回一个值，如果要返回多个值，只能将它们放在数组或对象里返回。有了解构赋值，取出这些值就非常方便。
    ```

### 函数参数的定义

    ```js
    // 参数是一组有次序的值
    function f([x, y, z]) { ... }
    f([1, 2, 3]);
    
    // 参数是一组无次序的值
    function f({x, y, z}) { ... }
    f({z: 3, y: 2, x: 1});
    // 解构赋值可以方便地将一组参数与变量名对应起来。
    ```

### 提取JSON数据

    ```js
    let jsonData = {
        id: 42,
        status: "OK",
        data: [867, 5309]
    };
    
    let { id, status, data: number } = jsonData;
    console.log(id, status, number);
    // 42, "OK", [867, 5309]
    // 解构赋值对提取JSON对象中的数据,尤其有用
    ```

### 函数参数的默认值

    ```js
    jQuery.ajax = function (url, {
        async = true,
        beforeSend = function () {},
        cache = true,
        complete = function () {},
        crossDomain = false,
        global = true,
        // ... more config
    } = {}) {
        // ... do stuff
    };
    // 指定参数的默认值，就避免了在函数体内部再写var foo = config.foo || 'default foo';这样的语句。
    ```

### 遍历Map结构

    ```js
    const map = new Map();
    map.set('first', 'hello');
    map.set('second', 'world');
    
    for (let [key, value] of map) {
        console.log(key + " is " + value);
    }
    // first is hello
    // second is world
    
    //如果只想获取键名，或者只想获取键值，可以写成下面这样。
    // 获取键名
    for (let [key] of map) {
        // ...
    }
    
    // 获取键值
    for (let [,value] of map) {
            // ...
    }
    ```
    
    > 任何部署了 Iterator 接口的对象，都可以用for...of循环遍历。Map 结构原生支持 Iterator 接口，配合变量的解构赋值，获取键名和键值就非常方便。

### 输入模块的指定方法

    ```js
    const { SourceMapConsumer, SourceNode } = require("source-map");
    ```
    > 加载模块时，往往需要指定输入哪些方法。解构赋值使得输入语句非常清晰。

# 字符串扩展

## 旧版本常用方法

> 字符串所有的方法，都不会修改字符串本身(字符串是不可变的)，操作完成会返回一个新的字符串。

1. 字符方法
    - charAt() //获取指定位置处字符,无参数默认为index=0，超出索引返回空字符串;
    - charCodeAt() //获取指定位置处字符的ASCII码
    - str[0]  //HTML5，IE8+支持 和charAt()等效
2. 字符串操作方法
    - concat() //拼接字符串，等效于+，+更常用
    - slice()    //arr.slice([begin[, end]]) 一个参数会截取到最后,并返回截取的字符串
    - substring() //基本同slice,区别见
    - substr()   //从start位置开始，截取length个字符
3. 位置方法
    - indexOf(searchvalue,fromindex) //返回指定内容在元字符串中的位置,找不到返回-1
    - lastIndexOf() //从后往前找，只找第一个匹配的
4. 去除空白   
    - trim() //只能去除字符串 前后 的空白
5. 大小写转换方法
    - to(Locale)UpperCase() //转换大写
    - to(Locale)LowerCase() //转换小写
    
    > 注：大多数情况下，toLocaleUpperCase()方法与 toUpperCase() 会产生相同的值，但是对于一些语言（locale）,例如土耳其语，因为它们的大小写映射规则与Unicode默认的映射规则不同，所以调用这两个方法将会产生不同的结果。

    From <https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase> 
6. 其它(参考:JS高级->正则)
    - search()
    - match()
    - replace()
    - split()
    - fromCharCode()
    // `String.fromCharCode(83, 79, 83)`;   //把ASCII码转换成字符串

## ES6新增的方法

- 可以使用 `for of` 遍历  <-  增加了Iterator接口
- `includes()`, `startsWith()`, `endsWith()`
    三者都接收第二个参数n, endsWith为针对前n个字符, 其他两个为从第n个字符开始.
- `repeat()` -- 重复多少次,可以接收:小数, 字符串'5' ...
- `padStart(20,'abc')`，`padEnd()`  -- 用'abc'在前面/后面(重复)填充长度为20个,如果原字符串少于20无效.

## 模板字符串

- 之前字符串的拼接用加号(+) 很麻烦,ES6引入了模板字符串template string;
- 模板字符串  `  `  
    - **可以多行(回车)**;
    - **可以使用变量 `${}`**
    - **`${}` 内部可以是JS表达式, 可以运算,调用函数...**;

# 正则扩展

## y修饰符

ES6 还为正则表达式添加了y修饰符，叫做“粘连”（sticky）修饰符。和g的区别: 

- g修饰符只要剩余位置中`存在匹配(不一定要挨着上一次匹配成功的位置)`就可.
- 而y修饰符确保匹配必须从`剩余的第一个位置开始`，这也就是“`粘连`”的涵义

## s修饰符-dotAll

- 之前正则中的点(.)不能匹配终止符和四个字节的UTF-16字符.所谓行终止符，就是该字符表示一行的终结。以下四个字符属于”行终止符“。
    - U+000A 换行符（\n）
    - U+000D 回车符（\r）
    - U+2028 行分隔符（line separator）
    - U+2029 段分隔符（paragraph separator
- ES2018引入 s修饰符 , 点(.) 可以代表一切

## 支持反向断言

之前的ES不支持反向断言,ES2018(chrome62+)开始支持反向断言

```js
var reg = /(?:x)/; //非捕获组 - 
var reg = /x(?=y)/; //x后面必须紧跟着y,才匹配x - 正向肯定查找
var reg = /x(!?=y)/; //x后面必须不紧跟着y,才匹配x - 正向否定查找
var reg = /x(?=y)/; //x前面必须紧跟着y,才匹配x - 反向肯定查找-JS不支持
var reg = /x(!?=y)/; //x前面必须不紧跟着y,才匹配x - 反向否定查找-JS不支持
var reg = /([a-z])\1{1,2}/; //小写字母,而且,重复出现2到3词,如 aab foo
```

## 具名组

ES2018可以使用具名组-为组起个名字.

```js
const RE_DATE = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
const matchObj = RE_DATE.exec('1999-12-31');
const year = matchObj.groups.year; // 1999
const month = matchObj.groups.month; // 12
const day = matchObj.groups.day; // 31
```

> 上面代码中，“具名组匹配”在圆括号内部，模式的头部添加“问号 + 尖括号 + 组名”（?<year>），然后就可以在exec方法返回结果的groups属性上引用该组名。同时，数字序号（matchObj[1]）依然有效。

# 数组扩展

## 旧版本常用方法

- toString()/valueOf()
    - toString() 方法返回一个新的 Array Iterator 对象，该对象包含数组每个索引的值
    - valueOf() 返回数组对象本身
- 数组常用方法
    1. 栈操作(先进后出)
        - push()    //在末尾追加元素，返回新数组长度
        - pop()       //删除末尾元素，并返回该元素
    2. 队列操作(先进先出)
        - push()
        - shift()     //删除头部元素，并返回该元素
        - unshift()   //在头部追加元素，返回新数组长度
    3. 排序方法
        - reverse()   //翻转数组 --> 修改原数组
        - sort();     //排序，排序后的数组。请注意，数组已原地排序，并且不进行复制。但是sort不稳定，需要传输回调函数，参考MDN写法。
    4. 操作方法
        - concat()    //var new_array = old_array.concat([...])  合并两个数组 -> 返回新数组
    5. slice()     //arr.slice([begin[, end]]) 截取 -> 返回新数组，原数组不变，包括前，不包括后。
    6. splice()    //array.splice(start[, deleteCount[, item1[, item2[, ...]]]]) 从start开始,删除几个,添加几个 -> 改变原数组。
    7. 位置方法
        - indexOf()、lastIndexOf()   //如果没找到返回-1
    8. 迭代方法 不会修改原数组(可选)
        - every()  //arr.every(callback[, thisArg]) 所有元素满足回调函数里面的条件（return ele.length>4;），返回true；
    9. some()  //只要有元素满足fallback(返回true), 则返回true
    10. join("|") //用"|"连接各元素，返回字符串。
- 清空数组
    - 方式1(推荐): `arr = [];`
    - 方式2: `arr.length = 0;`
    - 方式3: `arr.splice(0, arr.length);`

## forEach/map/filter/reduce

### forEach方法

- array.forEach(callback(currentValue, index, array){
    //do something
}, this)
- forEach() 方法对数组的每个元素执行一次提供的函数。
- `返回值都是undefined`;
- `原数组也不改变;`
- `只是遍历`, 类似以前的for循环遍历数组

```js
const items = ['item1', 'item2', 'item3'];
const copy = [];
items.forEach(function (item) {
    console.log(item)
    copy.push(item)
});
```

### map方法

- 语法

    ```js
    var new_array = arr.map(function callback(currentValue[, index[, array]]) {
        // Return element for new_array
    }[, thisArg])
    ```

- 创建一个新数组，其结果是该数组中的每个元素都调用一个提供的函数后返回的结果。
- 原数组不变, `新数组的个数个原数组一样`.

```js
var array1 = [1, 4, 9, 16];
// pass a function to map
const map1 = array1.map(x => x * 2);
console.log(map1);
// expected output: Array [2, 8, 18, 32]
```

### filter方法

- 语法: `var newArray = arr.filter(callback(element[, index[, array]])[, thisArg])`
- The filter() method creates a new array with all elements that pass the test implemented by the provided function.
- 创建一个新数组,原数组不变,新数组的成员是筛选过的原成员.

```js
var words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter(word => word.length > 6);
console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]
```

### reduce方法

- 语法: `arr.reduce(callback[,initialValue])`
- initialValue--作为第一次调用 callback函数时的第一个参数的值。 如果没有提供初始值，则将使用数组中的第一个元素。
- callback函数需要三个参数:
    - `accumulator`-累计器累计回调的返回值; 它是上一次调用回调时返回的累积值，或initialValue。
    - `currentValue`-数组中正在处理的元素。
    - currentIndex可选-数组中正在处理的当前元素的索引。 如果提供了initialValue，则起始索引号为0，否则为1。
    - array可选-调用reduce()的数组
- 执行过程: 
    1. `callback函数处理initialValue(若没提供使用第一个元素)和第二个元素,返回值作为accumulator`;
    2. 函数继续处理accumulator和第三个元素,返回值作为accumulator;
    3. 函数继续处理accumulator和第四个元素,返回值作为accumulator;
    4. ...
    5. 函数继续处理accumulator和最后一个元素,`返回值作为函数返回值`;

```js
//计算数组中所有元素的和
var total = [0, 1, 2, 3].reduce(
    (acc, cur) => acc + cur,
    0
); //6
//累加对象数组里的值
var initialValue = 0;
var sum = [{x: 1}, {x: 2}, {x: 3}].reduce(
    (accumulator, currentValue) => accumulator + currentValue.x, initialValue
);
console.log(sum) // logs 6
```

## Array.of()

- 之前的new Array()构造函数创建数组的时候,参数为一个数字n时,返回的是一个内容为empty*n的数组.
- 而Array.of()的行为更统一,无论传几个参数,返回值都是一个数组.

```js
let a = new Array(4)
console.log(a) //[empty × 4]

Array.of(4) //[4]
//其他和Array一样
```

## Array.from()

### 作用

- 把伪数组/可遍历对象(字符串/Set/Map...)/NodeList对象转化为数组.
- 还可以接受第二个参数(回调函数),类似于数组的map方法.

```js
Array.from(arrayLike, x => x * x);
// 等同于
Array.from(arrayLike).map(x => x * x);
Array.from([1, 2, 3], (x) => x * x)
// [1, 4, 9]
```

### 和扩展运算符的区别

- 扩展运算符(spread)也可以将某些数据结构转为数组,扩展运算符背后调用的是遍历器接口（Symbol.iterator）,如果一个对象没有部署这个接口，就无法转换。
- Array.from方法还支持类似数组(具有length属性的对象)转化为数组。扩展运算符做不到.

    ```js
    let arrayLike = {
        '0': 'a',
        '1': 'b',
        '2': 'c',
        length: 3
    };

    // ES5的写法
    var arr1 = [].slice.call(arrayLike); // ['a', 'b', 'c']

    // ES6的写法
    let arr2 = Array.from(arrayLike); // ['a', 'b', 'c']
    ```

## includes()

- 语法: `arr.includes(searchElement[, fromIndex])`
- 作用: The includes() method determines whether an array includes a certain element, returning true or false as appropriate.

```js
var array1 = [1, 2, 3];
console.log(array1.includes(2));
// expected output: true
var pets = ['cat', 'dog', 'bat'];
console.log(pets.includes('cat'));
// expected output: true
```

## entries/keys/values() 

- 作用: 三者都返回一个可迭代(Iterator)对象, 可以用for...of循环进行遍历;
- 区别是keys()是对index的遍历、values()是对item的遍历，entries()是对[index, item]的遍历。

```js
for (let index of ['a', 'b'].keys()) {
    console.log(index);
}
// 0
// 1
for (let elem of ['a', 'b'].values()) {
    console.log(elem);
}
// 'a'
// 'b'
for (let [index, elem] of ['a', 'b'].entries()) {
    console.log(index, elem);
}
// 0 "a"
// 1 "b"
```

## copyWithin()

- 语法: Array.prototype.copyWithin(target, start = 0, end = this.length)
- 作用: "复制"数组的一部分,覆盖另一部分
- 参数:
    - target（必需）：从该位置开始替换数据。如果为负值，表示倒数。
    - start（可选）：从该位置开始读取数据，默认为 0。如果为负值，表示倒数。
    - end（可选）：到该位置前停止读取数据，默认等于数组长度。如果为负值，表示倒数
- 返回值: 修改原来的数组

```js
var arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr.copyWithin(0, -2) //[8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(arr)
//"复制" -2到最后(最后两位),从第0位开始覆盖

var arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr.copyWithin(1, -4, -1) //[0, 6, 7, 8, 4, 5, 6, 7, 8, 9]
console.log(arr)
//"复制" -4到-1(不包含),从第1位开始覆盖

var arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr.copyWithin(1, 5, 6) //[0, 5, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(arr)
//"复制" 5到6(不包含),从第1位开始覆盖
```

## find() 和 findIndex()

- find()
    - 语法: `arr.find(callback(element[, index[, array]])[, thisArg])`
    - 作用: 遍历数组的元素,一旦callback (testing function) 返回true,停止并返回当前element;否则返回undefined

        ```js
        [1, 5, 10, 15].find(function (value, index, arr) {
            return value > 9;
        }) // 10
        ```

- findIndex()
    - 语法: `arr.findIndex(callback(element[, index[, array]])[, thisArg])`
    - 作用类似于find(), 不同的是找到的话, 返回当前index;否则返回-1

## fill()

- arr.fill(value[, start[, end]])
- The fill() method fills all the elements of an array from a start index to an end index with a static value. The end index is not included.

```js
var array1 = [1, 2, 3, 4];
// fill with 0 from position 2 until position 4

console.log(array1.fill(0, 2, 4));
// expected output: [1, 2, 0, 0]
// fill with 5 from position 1

console.log(array1.fill(5, 1));
// expected output: [1, 5, 5, 5]
```

## flat/flatMap()

- flat()
    - var newArray = `arr.flat([depth])`;
    - 作用:The flat() method creates a new array with all sub-array elements concatenated into it recursively up to the specified depth.

        ```js
        var arr1 = [1, 2, [3, 4]];
        arr1.flat();
        // [1, 2, 3, 4]

        var arr2 = [1, 2, [3, 4, [5, 6]]];
        arr2.flat();
        // [1, 2, 3, 4, [5, 6]]

        var arr3 = [1, 2, [3, 4, [5, 6]]];
        arr3.flat(2);
        // [1, 2, 3, 4, 5, 6]
        ```

- flatMap()
    - var new_array = arr.flatMap(function callback(currentValue[, index[, array]]) {
        // return element for new_array
    }[, thisArg])
    - 作用:The flatMap() method first maps each element using a mapping function, then flattens the result into a new array. It is identical to a map followed by a flat of depth 1, but flatMap is often quite useful, as merging both into one method is slightly more efficient.

        ```js
        let arr1 = [1, 2, 3, 4];

        arr1.map(x => [x * 2]);
        // [[2], [4], [6], [8]]

        arr1.flatMap(x => [x * 2]);
        // [2, 4, 6, 8]

        // only one level is flattened
        arr1.flatMap(x => [[x * 2]]);
        // [[2], [4], [6], [8]]

        //另一个例子
        let arr1 = ["it's Sunny in", "", "California"];

        arr1.map(x => x.split(" "));
        // [["it's","Sunny","in"],[""],["California"]]

        arr1.flatMap(x => x.split(" "));
        // ["it's","Sunny","in", "", "California"]
        ```

## 数组空位

- 数组的空位指，数组的某一个位置没有任何值。比如，Array构造函数返回的数组都是空位。
- 注意，空位不是undefined，一个位置的值等于undefined，依然是有值的。空位是没有任何值，in运算符可以说明这一点。

    ```js
    0 in [undefined, undefined, undefined] // true
    0 in [, , ,] // false
    // in运算符,是判断某个对象是否具有某个属性
    ```

    > 上面代码说明，第一个数组的 0 号位置是有值的，第二个数组的 0 号位置没有值。

- ES5 对空位的处理，已经很不一致了，大多数情况下会忽略空位。
- ES6 则是明确将空位转为undefined。
- 由于空位的处理规则非常不统一，所以建议避免出现空位。

# 函数扩展

## rest参数

具体见扩展运算符

```js
function add(...values) {
    let sum = 0;
    for (var val of values) {
        sum += val;
    }
    return sum;
}
add(2, 5, 3) // 10
```

## 默认值

### 基本使用

- ES5之前没有默认值,只能变通的实现

    ```js
    //之前的写法
    function log(x, y) {
        y = y || 'World';
        console.log(x, y);
    }

    //ES6的写法
    function log(x, y = 'World') {
            console.log(x, y);
    }
    log('Hello') // Hello World
    log('Hello', 'China') // Hello China
    ```

- 注意事项:
    1. 函数的参数变量默认是声明的,不能再函数内部使用let/const再次声明;
    2. 函数的默认值是惰性求值(每次调用的时候,如果传入的是undefined才会计算)

        ```js
        let x = 99;
            function foo(p = x + 1) {
            console.log(p);
        }
        foo() // 100
        x = 100;
        foo() // 101
        ```

    3. **定义了默认值的参数应该在函数参数的尾部**;

### 对函数length属性的影响

`函数对象的length属性不包含指定了默认值的参数,如果设置了默认值的参数不是尾参数，那么length属性也不再计入后面的参数了。`

```js
(function (a) {}).length // 1
(function (a = 5) {}).length // 0
(function (a, b, c = 5) {}).length // 2
```

### 作用域

- 一旦设置了参数的默认值，函数进行声明初始化时，`参数会形成一个单独的作用域（context）`。等到初始化结束，这个作用域就会消失。
- 外部作用域 -> 默认参数形成的作用域 -> 函数内部作用域;

    ```js
    let m = 20 //外部作用域
    function fn(x = m, y = x) { //默认参数形成的作用域
        let m = 50 //函数内部作用域
        console.log(x, y);
    }
    fn()
    ```

    > 上面代码中，参数y的默认值等于变量x。调用函数f时，参数形成一个单独的作用域。在这个作用域里面，默认值变量x指向第一个参数x，而不是全局变量x，所以输出是2。

## 箭头函数

### 基本使用

- 箭头函数,就是函数的简写,方便有些地方的使用.
- 缩写的情况:
    1. `如果有且仅有一个参数，() 可以省`;
    2. `如果有且仅有return一行，return 和 {}可以省`;

    ```js
    // 普通函数
    let arr = [5, 3, 6, 8, 4, 1, 9, 10]
    arr.sort(function (a, b) { //排序
            return a - b
    })
    // 箭头函数，去掉 function， 加上 =>
    let arr2 = arr.map(value => value * 2) //全部*2
    arr.sort((a, b) => a - b) //排序
    ```

- 箭头函数使用注意事项:
    1. `箭头函数只是函数的简写,同样具有作用域`。
    2. 不可以当作构造函数，也就是说，不可以使用new命令，否则会抛出一个错误。
    3. 不可以使用arguments对象，该对象在函数体内不存在。如果要用，可以用 rest 参数代替。
    4. 不可以使用yield命令，因此箭头函数不能用作 Generator 函数。

### 之前的this总结

- 函数中`this的指向`与`函数定义时无关`, 而是`取决于函数调用的上下文环境 -> 是动态的`;

```js
a = 2
var obj = {
    a: 1,
    b: function () {
        console.log(this.a)
    }
};

obj.b(); //1 上下文是obj

let bb = obj.b;
bb() //2 上下文是window
```

- 不同场景下this的指向

    | 调用方式         | 非严格模式     | 备注                                      |
    | ---------------- | -------------- | ------------------------------------------ |
    | 普通函数调用     | window         | 严格模式下是 undefined                     |
    | 构造函数调用     | 实例对象       | 原型方法中 this 也是实例对象               |
    | 原型中添加的方法 | 实例对象       | Obj.prototype.method()最终还是实例对象调用 |
    | 对象方法调用     | 该方法所属对象 | 紧挨着的对象                               |
    | 事件绑定方法     | 绑定事件对象   |                                            |
    | 定时器函数       | window         | window.setInterval();                      |

- 根本准则: 函数/方法 "`.`" 前面紧挨着的对象.

### 箭头函数this 的问题

- `箭头函数的this`的指向只取决于`箭头函数定义的上下文` -> 是静态的 -> 与函数调用的上下文环境无关,
- 由于箭头函数没有自己的this,函数的call/apply/bind方法也无法指定箭头函数的上下文环境;
- **`箭头函数不会创建自己的this,它只会从自己的作用域链的上一层继承this, 上一层如果还是箭头函数,再往上找`。**

```js
let obj = {
    fn: function () {
        console.log(this) //当前作用域的this===obj
        let f = () => {
            console.log(this) //上一级作用域的 obj
        }
        f()
    },
    fn1: () => {
        console.log(this) //上一级的window
    }
}
obj.fn()
obj.fn1()
```

> - 以上说明: 箭头函数没有产生新的上下文, 即箭头函数定义时的上下文环境为上一级上下文环境;
> - 并且this的指向是静态的--保持定义是的上下文环境,与调用时的上下文无关;

## 函数的name

- 函数(对象)的name属性早就被广泛支持,直到ES6才被写入标准.
- 和ES5还是有所不同, ES6的结果如下:

    ```js
    let fn = function () {}
    console.log(fn.name); //fn

    console.log((function () {}).name) //空字符串

    //bind
    var fn1 = fn.bind({}) //传入一个空对象
    console.log(fn1.name) //bound fn

    //new Function
    let foo = new Function('m', 'return m')
    console.log(foo.name) //anonymous
    ```

# 对象扩展

## 简写属性

当对象的某个k,v相同(k的名字和v的变量名相同),可以省略v.

```js
var a = 1;
var b = 2;
var c = 3;
var obj = {
    a ,
    b ,
    c
}
console.log(obj); //{ a: 1, b: 2, c: 3 }
```

## 简写方法

```js
//以前的写法
var obj = {
    a : 1,
    fn : function(){
        console.log(this.a);
    }
}
obj.fn();
//现在可以简写
var obj = {
    a : 1,
    fn(){
        console.log(this.a);
    }
}
obj.fn();
```

## Object.is()

ES5 比较两个值是否相等，只有两个运算符：相等运算符（==）和严格相等运算符（===）。它们都有缺点，前者会自动转换数据类型，后者的NaN不等于自身，以及+0等于-0。JavaScript 缺乏一种运算，在所有环境中，只要两个值是一样的，它们就应该相等。

```js
+0 === -0 //true
NaN === NaN // false

Object.is(+0, -0) // false
Object.is(NaN, NaN) // true
```

## Object.assign()

- 语法: `Object.assign(target, ...sources)`
- 作用: 把多个对象的all enumerable own properties复制到第一个对象,修改第一个对象, 被返回第一个对象.

## Object.keys/values/entries() 

分别获取对象自身的(非集成)keys/values/entries,返回值为数组.

```js
var obj = { foo: 'bar', baz: 42 };
Object.keys(obj)
// ["foo", "baz"]

const obj = { foo: 'bar', baz: 42 };
Object.values(obj)
// ["bar", 42]

const obj = { foo: 'bar', baz: 42 };
Object.entries(obj)
// [ ["foo", "bar"], ["baz", 42] ]
```

## 属性表达式

ES6可以在字面量声明对象是,在对象的属性中使用表达式.

```js
let propKey = 'foo';
let obj = {
[propKey]: true,
['a' + 'bc']: 123
};
console.log(obj) //{ foo: true, abc: 123 }
```

## super关键字

this指向函数所在的当前对象, ES6新增的super指向当前对象的原型对象.

## 对象中的扩展运算符

### 解构赋值

```js
let { x, y, ...z } = { x: 1, y: 2, a: 3, b: 4 };
x // 1
y // 2
z // { a: 3, b: 4 }
```

### 属性的拷贝

对象的扩展运算符（...）用于取出参数对象的所有可遍历属性，拷贝到当前对象之中。

```js
let o = { a: 3, b: 4 };
let n = { ...o, c: 5 };
console.log(n) //{ a: 3, b: 4, c: 5 }
```

## 属性的遍历/可枚举性

### 属性的遍历

ES6中有5中方法可以遍历对象的属性
- for...in循环遍历对象自身的和继承的可枚举属性（不含 Symbol 属性）。

- Object.keys返回一个数组，包括对象自身的（不含继承的）所有可枚举属性（不含 Symbol 属性）的键名。

- Object.getOwnPropertyNames返回一个数组，包含对象自身的所有属性（不含 Symbol 属性，但是包括不可枚举属性）的键名。

- Object.getOwnPropertySymbols返回一个数组，包含对象自身的所有 Symbol 属性的键名。

- Reflect.ownKeys返回一个数组，包含对象自身的所有键名，不管键名是 Symbol 或字符串，也不管是否可枚举。

以上的 5 种方法遍历对象的键名，都遵守同样的属性遍历的次序规则。
- 首先遍历所有数值键，按照数值升序排列。
- 其次遍历所有字符串键，按照加入时间升序排列。
- 最后遍历所有 Symbol 键，按照加入时间升序排列。

### 可枚举性

- 描述对象的enumerable属性，称为”可枚举性“，如果该属性为false，就表示某些操作会忽略当前属性

    ```js
    let obj = { foo: 123 };
    Object.getOwnPropertyDescriptor(obj, 'foo')
    // {
    // value: 123,
    // writable: true,
    // enumerable: true,
    // configurable: true
    // }
    ```

- 目前，有四个操作会忽略enumerable为false的属性。
	1. for...in循环：只遍历对象自身的和继承的可枚举的属性。
	2. Object.keys()：返回对象自身的所有可枚举的属性的键名。
	3. JSON.stringify()：只串行化对象自身的可枚举的属性。
	4. Object.assign()： 忽略enumerable为false的属性，只拷贝对象自身的可枚举的属性。

# Class类

## 新的写法

- JS还是没有类,只是基于类,以前用构造函数实现类的功能.
- ES6新增了class关键字,刚能模仿类的概念. 也仅仅是语法上的模仿.
- ES6依然很多功能没有实现,如:私有方法/属性...最新写法如下:

    ```js
    class Foo {
        count = 0; //实例属性-类的顶部,不需要this
        
        constructor(name, age) { //实例属性-构造器中
            this.name = name;
            this.age = age;
        }
        
        goDie() { //实例方法
            console.log(this.name + '挂了');
        }
        
        static classMethod() { //静态方法
            return 'hello';
        }
        static newProp = 2; //静态属性- 提案而已,没有实现
    }
    Foo.prop = 1; //静态属性 - ES6规定只能这样定义静态属性
    ```

    > - `类名后面没有圆括号`;
    > - `方法可以简写`;

## 继承

- 之前JS通过构造函数实现类属性的继承,通过原型实现方法的继承,写法很不优雅;
- ES6通过extends/super关键字使得类的继承更优雅;

```js
class People{
    constructor(name , age , sex){
        this.name = name;
        this.age = age;
        this.sex = sex;
    }
    changge(){
        console.log("我是一个" + this.name + "今年" + this.age + "岁啦！！");
    }
    goDie(){
        console.log("死啦");
    }
}

// 注意语法
class Student extends People{
    constructor(name , age , sex , xuehao , banji){
        super(name , age , sex);     //调用超类的构造器
        this.xuehao = xuehao;
        this.banji = banji;
    }
    kaoshi(){
        console.log(`${this.name}在考试`);
    }
}

var xiaohua = new Student("小花",12,"女",10001,"1班");
xiaohua.changge();
xiaohua.kaoshi();
```

# Set/Map

## Set

### 概述

- 类似于python 的集合, 没有重复值;
- Set的遍历顺序就是插入顺序;

### 基本使用

```js
//创建方法一
const s = new Set();
[2, 3, 5, 4, 5, 2, 2].forEach(x => s.add(x));//去重

//创建方法二: 通过可遍历对象
const set = new Set([1, 2, 3, 4, 4]);//去重

//集合转换为数组 [1, 2, 3, 4]
[...set] 

// 去除数组的重复成员
[...new Set([1, 2, 3, 4, 4])

// 去除字符串的重复成员
[...new Set('ababbc')].join('')
```

### Set实例的属性/方法

- 属性。
	- Set.prototype.constructor：构造函数，默认就是Set函数。
	- Set.prototype.size：返回Set实例的成员总数。
- 操作方法（用于操作数据）和。下面先介绍四个操作方法。
	- add(value)：添加某个值，返回 Set 结构本身。
	- delete(value)：删除某个值，返回一个布尔值，表示删除是否成功。
	- has(value)：返回一个布尔值，表示该值是否为Set的成员。
	- clear()：清除所有成员，没有返回值。
- 遍历方法（用于遍历成员）
	- keys()：返回键名的遍历器
	- values()：返回键值的遍历器
	- entries()：返回键值对的遍历器
	- forEach()：使用回调函数遍历每个成员

## Map

### 概述

- JavaScript 的对象（Object），本质上是键值对的集合（Hash 结构），但是传统上只能用字符串当作键。这给它的使用带来了很大的限制。
- ES6 提供了 Map 数据结构。但是各种类型的值（包括对象）都可以充当“键”。如果你需要“键值对”的数据结构，Map 比 Object 更合适。

### 基本使用

```js
const m = new Map();
const o = { p: 'Hello World' };

m.set(o, 'content')
m.get(o) // "content"
m.has(o) // true
m.delete(o) // true
m.has(o) // false

//任何具有 Iterator 接口、且每个成员都是一个双元素的数组
const map = new Map([
    ['name', '张三'],
    ['title', 'Author']
]);

map.size // 2

```
### Map实例的属性/方法

- 属性
	- size属性返回 Map 结构的成员总数。
- 操作方法
	- set(key, value)- 返回的是当前的Map对象，因此可以采用链式写法。
	- get(key)--读取key对应的键值，如果找不到key，返回undefined。
	- has(key)--返回一个布尔值，表示某个键是否在当前 Map 对象之中。
	- delete(key)--删除某个键，返回true。如果删除失败，返回false。
	- clear()--清除所有成员，没有返回值。
- 遍历方法
	- keys()：返回键名的遍历器。
	- values()：返回键值的遍历器。
	- entries()：返回所有成员的遍历器。
	- forEach()：遍历 Map 的所有成员。

# 异步相关

## 回调地狱

### 概述

- 为了拿到异步请求的数据,我们需要回调函数(闭包);
- 既然是异步(各自执行),我们便无法控制各个任务先后顺序;
- 为了让异步请求顺序执行(一个异步任务需要另一的结果),我们需要回调里面再回调;
- 于是就形成了回调地狱(callback hell) 或 回调黑洞(callback blackhole);
- 回调地狱的代码不友好,我们还是习惯"同步式"的代码.

### 顺序读取文件

```js
import { readFile } from 'fs';

function duwenjian(url, callback) {
    readFile(url, (err, data) => {
        if (err) {
            console.log('出错了');
        }
        callback(data)
    }); //end readFile
} //end duweijian

//顺序读取三个文件
duwenjian('./1.txt', function(data){
    console.log(data);
    duwenjian('./2.txt', function(data){
        console.log(data);
        duwenjian('./2.txt', function(data){
            console.log(data);
        })
    })
})
```

### 顺序发送Ajax请求

```js
<script src="jquery1.12.4.js"></script>
<script>
    function duweijian(url, callback) {
        $.get(url, function(data) {
            callback(data);
        })
    }

    duweijian('txt/1.txt', function(data) {
        console.log(data);
        duweijian('txt/2.txt', function(data) {
            console.log(data);
            duweijian('txt/3.txt', function(data) {
                console.log(data);
            });
        });
    });
</script>
```

### 顺序做动画

```js
<body>
    <div class="dv1"></div>
    <div class="dv2"></div>
    <div class="dv3"></div>
    <div class="dv4"></div>
</body>

<script>
    //四个函数实现顺序移动->回调地狱hell
    $(function () {
        $('.dv1').animate({left: 1000}, 1000,function(){
            $('.dv2').animate({left: 1000}, 1000,function(){
                $('.dv3').animate({left: 1000}, 1000,function(){
                    $('.dv4').animate({left: 1000}, 1000);
                });
            });
        });
    })
</script>
```

## Promise

### Promise简介

- Promise 是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。它由社区最早提出和实现，ES6 将其写进了语言标准，统一了用法，原生提供了Promise对象。
- 所谓Promise，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。
- 有了Promise对象，就可以将异步操作以同步操作的流程表达出来，避免了层层嵌套的回调函数。
- Promise对象的then方法返回的是一个新的Promise实例（注意，不是原来那个Promise实例）。因此可以采用链式写法，即then方法后面再调用另一个then方法。
- [更多参考](http://es6.ruanyifeng.com/#docs/promise):

    ```js
    const promise = new Promise(function(resolve, reject) {
        // ... some code
        
        if (/* 异步操作成功 */){
            resolve(value);
        } else {
            reject(error);
        }
    });
    ```

    > Promise构造函数`接受一个函数作为参数，该函数的两个参数分别是resolve和reject。它们是两个函数，由 JavaScript 引擎提供，不用自己部署`。
    > resolve函数的作用是，将Promise对象的状态从“未完成”变为“成功”（即从 pending 变为 resolved），在异步操作成功时调用，并将异步操作的结果，作为参数传递出去；reject函数的作用是，将Promise对象的状态从“未完成”变为“失败”（即从 pending 变为 rejected），在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。
    > Promise实例生成以后，可以用then方法分别指定resolved状态和rejected状态的回调函数。

    ```js
    promise.then(function(value) {
        // success
    }, function(error) {
        // failure
    });
    ```

    > then方法可以接受两个回调函数作为参数。第一个回调函数是Promise对象的状态变为resolved时调用，第二个回调函数是Promise对象的状态变为rejected时调用。其中，第二个函数是可选的，不一定要提供。这两个函数都接受Promise对象传出的值作为参数

### 顺序读取文件

```js
var fs = require('fs');

function duwenjian(url) {
    //提供原材料, 构建一个Promise对象并返回
    return new Promise(
        //Promise的参数为一个异步任务(函数),来处理原材料
        //该异步任务有两个结果:成功/失败;
        //需要传入两个函数把异步的成功/失败数据拿出去.
        (resolve, reject) => {
            fs.readFile(
                url,
                (err, data) => {
                    if (err) {
                        reject(err)
                        return;
                    }
                    resolve(data)
                }
            ); //end readFile
        }
    ) //end Promise对象
} //end duweijian

duwenjian('./txt/1.txt') //创建一个Promise对象
    .then( //调用 Promise 对象的then方法
        //这个函数用于把成功时的数据拿出来,并处理
        (data) => {
            console.log(data.toString());
            return duwenjian('./txt/2.txt'); //返回一个Promise对象->链式编程
        },
        //这个函数用于把失败时的数据那处理,并处理
        (err) => {
            console.log(err);
            console.log('读文件1.txt失败');
        }
    )
    .then(
        (data) => {
            console.log(data.toString());
            return duwenjian('./txt/3.txt');
        },
        (err) => {
            console.log('读文件2.txt失败');
        }
    ).then(
        (data) => {
            console.log(data.toString());
            // return duwenjian('./txt/2.txt');
        },
        (err) => {
            console.log('读文件3.txt失败');
        }
    )
```

### 顺序发送Ajax

```html
<script src="jquery1.12.4.js"></script>
<script>
    function duweijian(url) {
        return new Promise((resolve, reject) => {
            $.get(url, function (data) {
                resolve(data);
            });
        });
    }
    
    duweijian('txt/1.txt')
        .then((data) => {
            console.log(data);
            return duweijian('txt/2.txt');
        })
        .then((data) => {
            console.log(data);
            return duweijian('txt/3.txt');
        })
        .then((data) => {
            console.log(data);
        })
</script>
```

## Generator/yield

- ES8实现了生成器, yield, * ;
-  Promise 的写法比回调函数的写法大大改进，但是一眼看上去，代码完全都是 Promise 的 API（then、catch等等），操作本身的语义反而不容易看出来。
- 于是Generator边进行了改进;

## async/await

### async简介

- ES2017 标准引入了 async 函数，使得异步操作变得更加方便。
- 本质:他是Generator函数的语法糖;
- async实现异步编程比其他方式更优雅,语言更明确.

### 使用

- `需要一个返回Promise对象的函数`;
- 定义主函数,在前面添加async关键字,`表示这个函数里面有异步语句`需要等待;
- 异步语句的前面添加await关键字,`表示这条语句是异步语句`,后面的语句需要等待我完成.

### 顺序读文件

```js
var fs = require('fs');

function duwenjian(url) {
    //提供原材料, 构建一个Promise对象并返回
    return new Promise(
        //Promise的参数为一个异步任务(函数),来处理原材料
        //该异步任务有两个结果:成功/失败;
        //需要传入两个函数把异步的成功/失败数据拿出去.
        (resolve, reject) => {
            fs.readFile(
                url,
            (err, data) => {
                    if (err) {
                        reject(err)
                        return;
                    }
                    resolve(data.toString())
                }
            ); //end readFile
        }
    ) //end Promise对象
} //end duweijian

//异步函数
async function main() {
    var data1 = await duwenjian('./txt/1.txt');
    //await只能在async函数中使用
    //await表示后面的语句是异步语句->这个异步语句完成再执行其他
    //返回值是resolve从异步任务中传出来的值
    console.log(data1);
    var data2 = await duwenjian('./txt/2.txt');
    console.log(data2);
    var data3 = await duwenjian('./txt/3.txt');
    console.log(data3);
}
main();
```

### 顺序Ajax

```js
function duweijian(url) {
    return new Promise((resolve, reject) => {
        $.get(url, function (data) {
            resolve(JSON.parse(data));
        });
    });
}

async function main() {
    //duweijian函数会把resolve函数中的参数返回
    //执行异步语句后,再执行then -> 把json数据的value提取
    var data1 = await duweijian('txt/1.txt').then(data=>data.key);
    var data2 = await duweijian('txt/2.txt').then(data=>data.key);
    var data3 = await duweijian('txt/3.txt').then(data=>data.key);
    console.log(data1);
    console.log(data2);
    console.log(data3);
}
main();
```

### 顺序做动画

```html
<div class="dv1"></div>
<div class="dv2"></div>
<div class="dv3"></div>
<div class="dv4"></div>

<script>
    //async实现动画的以此执行
    function dong(class_name) {
            return new Promise((resolve) => {
                $(class_name).animate({ left: 1000 }, 1000, resolve);
                //如果第一个动画执行成功了,执行resolve,没有传参
            });
        }
        async function main() {
        //await只能在async函数中使用
        await dong('.dv1');//await表示后面为异步语句,后面的等待
        await dong('.dv2');
        await dong('.dv3');
        await dong('.dv4');
    }
    
    main();
</script>
```

# 其他

## symbol对象

- The original motivation for introducing symbols to Javascript was to enable private properties.
最初的目的是为了实现私有属性

- Unfortunately, they ended up being severely downgraded. They are no longer private, since you can find them via reflection, for example, using Object.getOwnPropertySymbols or proxies.
不幸的是:没有实现,可以通过proxy/reflection来访问

- They are now known as unique symbols and their only intended use is to avoid name clashes between properties. For example, ECMAScript itself can now introduce extension hooks via certain methods that you can put on objects (e.g. to define their iteration protocol) without risking them to clash with user names.
现在,被当做唯一的标识符来使用,防止属性的重名/冲突,比如:ECMA自己通过某种访问引入某个钩子,你也可以放进对象中(通过迭代),而不用担心他会和用户的命名冲突

- Whether that is strong enough a motivation to add symbols to the language is debatable.
是否应该添加这个symbols依然很受争议.

## proxy/reflect

- proxy是es6的新特性，简单来讲，即是对目标对象的属性读取、设置，亦或函数调用等操作进行拦截（处理）。
`let proxy = new Proxy(target,handle)`

- reflect与ES5的Object有点类似，包含了对象语言内部的方法，Reflect也有13种方法，与proxy中的方法一一对应。Proxy相当于去修改设置对象的属性行为，而Reflect则是获取对象的这些行为。