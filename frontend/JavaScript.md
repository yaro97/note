# JavaScript教程

后端可以选择的语言很多，前端没得选，只有js语言；Web时代，掌握js还是很有必要的。

js上手容易，深入难，编写高质量的js代码更是难上加难，

## JS简介

### 概述

- JS的创始人：Brendan Eich 布兰登-艾奇 10天就把js搞出来了。
- Netscape在最初将其脚本语言命名为LiveScript，后来Netscape在与Sun合作之后将其改名为JavaScript。JavaScript最初受Java启发而开始设计的，目的之一就是“看上去像Java”，因此语法上有类似之处，一些名称和命名规范也借自Java。JavaScript与Java名称上的近似，是当时Netscape为了营销考虑与Sun微系统达成协议的结果。Java和JavaScript的关系就像张雨和张雨生的关系，只是名字很像。
- Java 服务器端的编程语言
- JavaScript 运行在客户端(浏览器)的编程语言

	> JavaScript是一种运行在客户端 的脚本语言 JavaScript的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，最早是在HTML（标准通用标记语言下的一个应用）网页上使用，用来给HTML网页增加动态功能。

- JavaScript最初的目的

演示：[http://baixiu.uieee.com/admin/login.php ](http://baixiu.uieee.com/admin/login.php)最初的目的是为了处理表单的验证操作。

- JavaScrpt现在的意义(应用场景)

JavaScript 发展到现在几乎无所不能。

1. 网页特效
2. 服务端开发(Node.js)
3. 命令行工具(Node.js)
4. 桌面程序(Electron)
5. App(Cordova)
6. 控制硬件-物联网(Ruff)
7. 游戏开发(cocos2d-js)

- JavaScript和HTML、CSS的区别

  1. HTML：提供网页的结构，提供网页中的内容
  2. CSS: 用来美化网页
  3. JavaScript: 可以用来控制网页内容，给网页增加动态的效果

- JS是一门什么样的语言：

  1. 是一门解释性语言；
  2. 是一门脚本语言；
  3. 是一门弱类型语言，声明变量都用var；
  4. 是一门基于对象的语言；
  5. 是一门动态类型语言（代码执行时才知道变量的类型；可以为对象通过"点语法"动态的添加属性/方法；动态改变变量的值/类型）。

### JS组成

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzn6xw8srvj20gt06pdif.jpg)
![](http://ww1.sinaimg.cn/large/48356ef5ly1fzn6y6sz0hj209u08kdif.jpg)

- ECMAScript - JavaScript的核心 

  - ECMA 欧洲计算机制造联合会
  - 网景：JavaScript
  - 微软：JScript
  - 定义了JavaScript的语法规范 
  - JavaScript的核心，描述了语言的基本语法和数据类型，ECMAScript是一套标准，定义了一种语言的标准与具体实现无关

- BOM - 浏览器对象模型

  - 一套操作浏览器功能的API
  - 通过BOM可以操作浏览器窗口，比如：弹出框、控制浏览器跳转、获取分辨率等

- DOM - 文档对象模型

  - 一套操作页面元素的API
  - DOM可以把HTML看做是文档树，通过DOM提供的API可以对树上的节点进行操作

### JS书写位置

- CSS：行内样式、嵌入样式、外部样式

1. 写在行内

```html
<input type="button" value="按钮" onclick="alert('Hello World')" />
```
2. 写在script标签中

```html
<head>
 <script>
   alert('Hello World!');
 </script>
</head>
```

3. 写在外部js文件中，在页面引入

```html
<script src="main.js"></script>
```

> **注意点:**
> **script要么用于引入外部JS文件, 要么用于书写JS代码, 不可混用**
> 本地运行js代码没有问题，但由于浏览器的限制，以`file://`开头的地址无法执行如联网等js代码，所以本地搭建Web服务器很有必要，然后以`http://`开头的地址来正常执行所有js代码。

### JS代码注意的问题

1. script标签在页面中可以出现多对；
2. 在一对script的标签中有错误的js代码,那么该错误的代码后面的js代码不会执行；
3. 如果第一对的script标签中有错误,不会影响后面的script标签中的js代码执行；
4. script的标签中可以写什么内容`type="text/javascript"`是标准写法或者写`language="JavaScript"`都可以。
   - 但是,目前在我们的html页面中,type和language都可以省略,原因:html是遵循h5的标准。
   - 有可能会出现这种情况:script标签中可能同时出现type和language的写法.       
5. script标签一般是放在body的标签的最后的,有的时候会在head标签中,但是放在最后有利于页面的加载。
6. 如果script标签用于引用外部js，script标签内部不能写代码。 

## 基本语法

### 语法

JavaScript的语法和Java语言类似，每个**语句**以`;`结束，**语句块**用`{...}`。但是，JavaScript并不强制要求在每个语句的结尾加`;`，浏览器中负责执行JavaScript代码的引擎会自动在每个语句的结尾补上`;`。

> 注意：让JavaScript引擎自动加分号在某些情况下会改变程序的语义，导致运行结果与期望不一致。在本教程中，我们不会省略`;`，所有语句都会添加`;`。

**多个语句可以写在一行，但是不建议**。

**语句块**用`{...}`内的语句具有**缩进**，缩进不是js语法要求必须的，但是有助于我们理解代码的层次；

**语句块**用`{...}`还可以嵌套，形成层级结构，js本身对嵌套的层级没有限制，但是过多嵌套不利于理解代码。遇到这种情况，需要把部分代码抽出来，作为**函数**来调用。

### 注释

以`//`开头直到行末的字符被视为**行注释** ；

用`/*...*/`把多行字符包裹起来，为**“块”注释**；

> 注释是给开发人员看到，js引擎会自动忽略。

### 大小写

js严格区分大小写，切记！

## 数值类型

> 计算机：做数学计算的机器，因此计算机程序理所当然可以处理各种数值。但是计算机能处理的不只是数值，还可以出来文本、图像、音频、视频、网页等各种数据，不同数据，需要定义不同的数据类型，js定义了如下几种数据类型：

js中有六种数据类型：
- 包括五种基本数据类型（Number,String,Boolean,Undefined,Null）；
- 和一种复杂数据类型（Object）。

### Number

- js不区分整数和浮点数，统一用Number表示：

```javascript
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
```

> 计算机使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制以`0x`前缀表示, 如: `var num = 0xA;`。

- Number可以直接做四则运算，规则和数学一致：

```javascript
1 + 2; // 3
(1 + 2) * 5 / 2; // 7.5
2 / 0; // Infinity
0 / 0; // NaN
10 % 3; // 1
10.5 % 3; // 1.5
```

- 数值范围

	- 最小值：Number.MIN_VALUE，这个值为： 5e-324
	- 最大值：Number.MAX_VALUE，这个值为： 1.7976931348623157e+308
	- 无穷大：Infinity
	- 无穷小：-Infinity

- 数值判断

	- NaN：not a number
	  - NaN 与任何值都不相等，包括他本身
	- isNaN: is not a number

### 字符串

- 字符以`单引号''`或`双引号""`括起来的任何文本，习惯用单引号即可。

- 转义符

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzn7l0selhj20kq08gdif.jpg)

- 字符串长度

	- length属性用来获取字符串的长度
	- var str = '黑马程序猿 Hello World';
	- console.log(str.length);

- 字符串拼接

```js
//字符串拼接使用 + 连接
console.log(11 + 11);
console.log('hello' + ' world');
console.log('100' + '100');
console.log('11' + 11);
console.log('male:' + true);
```

> 两边只要有一个是字符串，那么+就是字符串拼接功能
> 两边如果都是数字，那么就是算术功能。

### 布尔值

布尔值和布尔代数的表示完全一致，一个布尔值只有`true`、`false`两种值，要么是`true`，要么是`false`，可以直接用`true`、`false`表示布尔值，也可以通过布尔运算计算出来：

```javascript
true; // 这是一个true值
false; // 这是一个false值
2 > 1; // 这是一个true值
2 >= 3; // 这是一个false值
false && true && false; // 这个&&语句计算结果为false
false || true || false; // 这个||语句计算结果为true
! (2 > 5); // 结果为true
```

布尔值经常用在条件判断中，比如：

```javascript
var age = 15;
if (age >= 18) {
	alert('adult');
} else {
	alert('teenager');
}
```

### null和undefined

- undefined表示一个声明了没有赋值的变量，变量只声明的时候值默认是undefined
- null表示一个空，变量的值如果想为null，必须手动设置

`null`表示一个“空”的值，它和`0`以及空字符串`''`不同，`0`是一个数值，`''`表示长度为0的字符串，而`null`表示“空”。

在其他语言中，也有类似JavaScript的`null`的表示，例如Java也用`null`，Swift用`nil`，Python用`None`表示。但是，在JavaScript中，还有一个和`null`类似的`undefined`，它表示“未定义”。

JavaScript的设计者希望用`null`表示一个空的值，而`undefined`表示值未定义。事实证明，这并没有什么卵用，区分两者的意义不大。大多数情况下，我们都应该用`null`。`undefined`仅仅在判断函数参数是否传递的情况下有用。

### 对象

JavaScript的对象是一组由键-值对组成的无序集合，例如：

```javascript
var person = {
	name: 'Bob',
	age: 20,
	tags: ['js', 'web', 'mobile'],
	city: 'Beijing',
	hasCar: true,
	zipcode: null
};
```

JavaScript对象的键都是字符串类型，值可以是任意数据类型。上述`person`对象一共定义了6个键值对，其中每个键又称为对象的属性，例如，`person`的`name`属性为`'Bob'`，`zipcode`属性为`null`。

要获取一个对象的属性，我们用`对象变量.属性名`的方式：

```javascript
person.name; // 'Bob'
person.zipcode; // null
```

## 数据类型转换

### chrome不同类型的显示颜色

- 字符串的颜色是黑色的，
- 数值/布尔类型是蓝色的，
- undefined和null是灰色的。

### 转换成字符串类型

- toString()
	var num = 5;
	console.log(num.toString());
- String()
	String()函数存在的意义：有些值没有toString()，这个时候可以使用String()。比如：undefined和null
- 拼接字符串方式
	num + ""，当 + 两边一个操作符是字符串类型，一个操作符是其它类型的时候，会先把其它类型转换成字符串再进行字符串拼接，返回字符串

### 转换成数值类型

- Number()
	Number()可以把任意值转换成数值，如果要转换的字符串中有一个不是数值的字符，返回NaN
- parseInt()

```js
var num1 = parseInt("12.3abc");  // 返回12，如果第一个字符是数字会解析直到遇到非数字结束
var num2 = parseInt("abc123");   // 返回NaN，如果第一个字符不是数字或者符号就返回NaN
```

- parseFloat()

```js
parseFloat() // 把字符串转换成浮点数
// 和parseInt非常相似，不同之处在: parseFloat会解析第一个. 遇到第二个.或者非数字结束
// 如果解析的内容里只有整数，解析成整数
```
- +，-0等运算

```js
var str = '500';
console.log(+str); // 取正
console.log(-str); // 取负
console.log(str - 0);
```

### 转换成布尔类型

```js
• Boolean()
// 0 ''(空字符串) null undefined NaN 会转换成false 其它都会转换成true
```

## 变量

### 什么是变量

  - 什么是变量
	变量是计算机内存中存储数据的标识符，根据变量名称可以获取到内存中存储的数据
  - 为什么要使用变量
	使用变量可以方便的获取或者修改内存中的数据

### 变量的声明/赋值

```javascript
var a; // 申明了变量a，此时a的值为undefined
var $b = 1; // 申明了变量$b，同时给$b赋值，此时$b的值为1
var s_007 = '007'; // s_007是一个字符串
var Answer = true; // Answer是一个布尔值true
var t = null; // t的值是null
var age = 10, name = 'zs';  // 同时声明多个变量并赋值
var age, name, sex; // 同时声明多个变量
age = 10; // 赋值
```

### 变量的命名

- 规则 - 必须遵守的，不遵守会报错
	- 由字母、数字、下划线、$符号组成，不能以数字开头
	- 不能是关键字和保留字，例如：for、while。
	- 区分大小写
- 规范 - 建议遵守的，不遵守不会报错
	- 变量名必须有意义
	- 遵守驼峰命名法。首字母小写，后面单词的首字母需要大写。例如：userName、userPassword

> 变量名也可以用中文，但是，请不要给自己找麻烦。

### 静态/动态语言

在JavaScript中，使用等号`=`对变量进行赋值。可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，但是要注意只能用`var`申明一次，例如：

```javascript
var a = 123; // a的值是整数123
a = 'ABC'; // a变为字符串
```

这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下：

```c++
int a = 123; // a是整数类型变量，类型用int申明
a = "ABC"; // 错误：不能把字符串赋给整型变量
```

和静态语言相比，动态语言更灵活，就是这个原因。

### 获取变量的类型

typeof有两种写法：
	- typeof(xxx);
	- typeof xxx;

### strict模式

JavaScript在设计之初，为了方便初学者学习，并不强制要求用`var`申明变量。这个设计错误带来了严重的后果：如果一个变量没有通过`var`申明就被使用，那么该变量就自动被申明为全局变量：

```javascript
i = 10; // i现在是全局变量
```

在同一个页面的不同的JavaScript文件中，如果都不用`var`申明，恰好都使用了变量`i`，将造成变量`i`互相影响，产生难以调试的错误结果。

使用`var`申明的变量则不是全局变量，它的范围被限制在该变量被申明的函数体内（函数的概念将稍后讲解），同名变量在不同的函数体内互不冲突。

为了修补JavaScript这一严重设计缺陷，ECMA在后续规范中推出了strict模式，在strict模式下运行的JavaScript代码，强制通过`var`申明变量，未使用`var`申明变量就使用的，将导致运行错误。

启用strict模式的方法是在JavaScript代码的第一行写上：

```javascript
'use strict';
```

这是一个字符串，不支持strict模式的浏览器会把它当做一个字符串语句执行，支持strict模式的浏览器将开启strict模式运行JavaScript。

来测试一下你的浏览器是否能支持strict模式：

```javascript
'use strict';
// 如果浏览器支持strict模式，
// 下面的代码将报ReferenceError错误:
abc = 'Hello, world';
alert(abc);
```

运行代码，如果浏览器报错，请修复后再运行。如果浏览器不报错，说明你的浏览器太古老了，需要尽快升级。

不用`var`申明的变量会被视为全局变量，为了避免这一缺陷，所有的JavaScript代码都应该使用strict模式。我们在后面编写的JavaScript代码将全部采用strict模式。

## 操作符

#### 算术运算符

`+ - * / %`

#### 一元运算符

- 一元运算符：只有一个操作数的运算符
  1. 前置++ 后置++
  2. 前置-- 后置--

```js
var a = 1; var b = ++a + ++a; console.log(b);    
var a = 1; var b = a++ + ++a; console.log(b);    
var a = 1; var b = a++ + a++; console.log(b);    
var a = 1; var b = ++a + a++; console.log(b);  
```

- 总结 如果**不参与运算，前置/后置没有区别**。如果参与运算，前置是先自增/减后运算；后置式先运算后自增/减。

#### 逻辑(布尔)运算符

- `&&` 与 两个操作数同时为true，结果为true，否则都是false
- `||` 或 两个操作数有一个为true，结果为true，否则为false
- `!`  非  取反

#### 关系(比较)运算符

- <    >    >=    <=   ==    !=     ===     !==
- `==`与`===`的区别：`==`只进行值得比较，`===`类型和值同时相等，则相等
​
```js
var result = '55' == 55;    // true
var result = '55' === 55;   // false 值相等，类型不相等
var result = 55 === 55;     // true
```

#### 赋值运算符

- =    +=    -=    *=    /=    %=

```js
// 例如：
var num = 0;
num += 5;   //相当于  num = num + 5;
```

#### 运算符优先级

- 优先级从高到底
	1. ()  优先级最高
	2. 一元运算符  ++   --   !
	3. 算数运算符  先*  /  %   后 +   -
	4. 关系运算符  >   >=   <   <=
	5. 相等运算符   ==   !=    ===    !==
	6. 逻辑运算符 先&&   后||
	7. 赋值运算符

- 练习：
- 
```js
4 >= 6 || '人' != '阿凡达' && !(12 * 2 == 144) && true

var num = 10;
5 == num / 2 && (2 + 2 * num).toString() === '22'
```

## 表达式和语句

- 表达式
	**一个表达式可以产生一个值**，有可能是运算、函数调用、有可能是字面量。表达式可以放在任何需要值的地方。

- 语句
	**语句可以理解为一个行为**，循环语句和判断语句就是典型的语句。一个程序有很多个语句组成，一般情况下;分割一个一个的语句

## 流程控制

- 程序的流程有三种结构:
 - 顺序结构
	从上到下执行的代码就是顺序结构，程序默认就是由上到下顺序执行的；
 - 分支结构 
	根据不同的情况，执行对应代码；
 - 循环结构
	循环结构：重复做一件事情；

### 分支结构

JS中有三种分支结构: `if`, `三元`, `switch`

1. if语句

	```js
	// ***单分支***
	if (/* 条件表达式 */) {
	 // 执行语句
	}
	// ***双分支​***
	if (/* 条件表达式 */){
	 // 成立执行语句
	} else {
	 // 否则执行语句
	}
	// ***多分支***
	if (/* 条件1 */){
	 // 成立执行语句
	} else if (/* 条件2 */){
	 // 成立执行语句
	} else if (/* 条件3 */){
	 // 成立执行语句
	} else {
	 // 最后默认执行语句
	}
	```

2. 三元运算符

	> 可以用来替换if - esle 的双分支, 是对if……else语句的一种简化写法.

	- 语法: `表达式1 ? 表达式2 : 表达式3`
	- 如果表达式1成立, 返回表达式2, 否则返回表达式3.

3. switch语句

	> 可以和if语句的多分支替换。switch case习惯上用于点的分支判断；if esle 习惯上用于范围的分支判断。

	- 语法格式:

	```js
	switch (expression) {
		 case 常量1:
		   语句;
		   break;
		 case 常量2:
		   语句;
		   break;
		 …
		 case 常量n:
		   语句;
		   break;
		 default:
		   语句;
		   break;
		}
	```
	- 说明: 
	  - break可以省略，如果省略，代码会继续执行下一个case（不判断case，遇到下一个break为止。）；
	  - default可省略；
	  - switch 语句在比较值时使用的是全等操作符(===), 因此不会发生类型转换（例如，字符串'10' 不等于数值 10）。
	  - 案例： 显示星期几 素质教育（把分数变成ABCDE）千万不要写100个case哟

- 布尔类型的隐式转换

	- 流程控制语句会把后面的值隐式转换成布尔类型
	  - 转换为true   非空字符串  非0数字  true 任何对象
	  - 转换成false  空字符串  0  false  null  undefined

	```js
	// 结果是什么？
	var a = !!'123';

	//案例
	var message;
	// 会自动把message转换成false
	if (message) {     
	 // todo...
	}
	```

### 循环结构

JS中, 循环运距有三种: `while`, `do...while`, `for` 循环

1. while语句

   - 基本语法：
   
   ```js
   // 当循环条件为true时，执行循环体，
   // 当循环条件为false时，结束循环。
   while (循环条件) {
   //循环体
   }
   ```

   - 代码示例：
   
   ```js
   // 计算1-100之间所有数的和
   // 初始化变量
   var i = 1;
   var sum = 0;
   // 判断条件
   while (i <= 100) {
    // 循环体
    sum += i;
    // 自增
    i++;
   }
   console.log(sum);
   ```
   
   - 案例： 打印100以内 7的倍数, 打印100以内所有偶数, 打印100以内所有偶数的和

2. do...while语句

    > do..while循环和while循环非常像，二者经常可以相互替代，但是do..while的特点是不管条件成不成立，都会执行一次。
    > **注意while的语句结尾有个分号**.
    
    - 基础语法：
    
    ```js
    do {
     // 循环体;
    } while (循环条件);
    ```

    - 代码示例：
    
    ```js
    // 初始化变量
    var i = 1;
    var sum = 0;
    do {
     sum += i;//循环体
     i++;//自增
    } while (i <= 100);//循环条件
    ```

    - 案例：求100以内所有3的倍数的和。使用do-while循环：输出询问“我爱你，嫁给我吧？”，选择“你喜欢我吗？(y/n):"，如果输入为y则打印”我们形影不离“，若输入为n,则继续询问 

3. for语句

    > while和do...while一般用来解决无法确认次数的循环。for循环一般在循环次数确定的时候比较方便.
    > for循环可以理解为来源于while，因为while的计数器、初始值、判断条件分开写不方便/易忘，所以for循环把这几个条件写在一起。
    
    - for循环语法：
    
    ```js
    // for循环的表达式之间用的是;号分隔的，千万不要写成,
    for (初始化表达式1; 判断表达式2; 自增表达式3) {
     // 循环体4
    }
    ```

    - 执行顺序：1243 ---- 243 -----243(直到循环条件变成false)
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fznp3yeqwsj209g035dfu.jpg)
      1. 初始化表达式
      2. 判断表达式
      3. 自增表达式
      4. 循环体
    
    - 案例：
        - 打印1-100之间所有数
        - 求1-100之间所有数的和
        - 求1-100之间所有数的平均值
        - 求1-100之间所有偶数的和
        - 同时求1-100之间所有偶数和奇数的和
    
    ```js
    // ****打印正方形
    // 使用拼字符串的方法的原因
    // console.log 输出重复内容的问题
    // console.log 默认输出内容介绍后有换行
    var start = '';
    for (var i = 0; i < 10; i++) {
     for (var j = 0; j < 10; j++) {
       start += '* ';
    }
     start += '\n';
    }
    console.log(start);
    
    // ****打印直角三角形
    var start = '';
    for (var i = 0; i < 10; i++) {
     for (var j = i; j < 10; j++) {
       start += '* ';
    }
     start += '\n';
    }
    console.log(start);
    ​
    // ****打印9*9乘法表
    var str = '';
    for (var i = 1; i <= 9; i++) {
     for (var j = i; j <=9; j++) {
       str += i + ' * ' + j + ' = ' + i * j + '\t';
    }
     str += '\n';
    }
    console.log(str);
    ```

### continue和break

- break:立即跳出当前的整个循环（不能跳出嵌套的循环），即循环结束，开始执行循环后面的内容（直接跳到大括号）。
- continue:立即跳出当前循环（当前循环continue后面的语句不执行，for循环执行i++），继续下一次循环。
- 案例：
    求整数1～100的累加值，但要求碰到个位为3的数则停止累加。
    求整数1～100的累加值，但要求跳过所有个位为3的数。
- 作业：
    求1-100之间不能被7整除的整数的和（用continue） 求200-300之间所有的奇数的和（用continue） 求200-300之间第一个能被7整数的数（break）。

### 调试

- 过去调试JavaScript的方式
    - alert()
    - console.log()
- 断点调试
断点调试是指自己在程序的某一行设置一个断点，调试时，程序运行到这一行就会停住，然后你可以一步一步往下调试，调试过程中可以看各个变量当前的值，出错的话，调试到出错的代码行即显示错误，停下。
- 调试步骤
浏览器中按F12-->sources-->找到需要调试的文件-->在程序的某一行设置断点
- 调试中的相关操作
    - Watch: 监视，通过watch可以监视变量的值的变化，非常的常用。
    - F10: 程序单步执行，让程序一行一行的执行，这个时候，观察watch中变量的值的变化。
    - F8：跳到下一个断点处，如果后面没有断点了，则程序执行结束。
    > tips: 监视变量，不要监视表达式，因为监视了表达式，那么这个表达式也会执行。
    > 1. 代码调试的能力非常重要，只有学会了代码调试，才能学会自己解决bug的能力。初学者不要觉得调试代码麻烦就不去调试，知识点花点功夫肯定学的会，但是代码调试这个东西，自己不去练，永远都学不会。
    > 2. 今天学的代码调试非常的简单，只要求同学们记住代码调试的这几个按钮的作用即可，后面还会学到很多的代码调试技巧。

## 数组

### 概述

- 之前学习的数据类型，只能存储一个值(比如：Number/String。我们想存储班级中所有学生的姓名，此时该如何存储？
- 所谓数组，就是将多个元素（通常是同一类型）按一定顺序排列放到一个集合中，那么这个集合我们就称之为数组。

### 数组的定义

> 数组是一个有序的列表，可以在数组中存放任意的数据，并且数组的长度可以动态的调整。

1. 通过数组字面量创建数组

	```js
	// 创建一个空数组
	var arr1 = []; 
	// 创建一个包含3个数值的数组，多个数组项以逗号隔开
	var arr2 = [1, 3, 4]; 
	// 创建一个包含2个字符串的数组
	var arr3 = ['a', 'c']; 
	// 可以通过数组的length属性获取数组的长度
	console.log(arr3.length);
	// 可以设置length属性改变数组中元素的个数
	arr3.length = 0;
	```

2. 通过构造函数创建数组

	```js
	var arr=new Array();//创建一个空数组
	var arr=new Array(5);//创建长度为5，类型为undifined的元素的数组。
	var arr=new Array(1,2);//创建长度为2，元素分别为1，2的数组。
	```

### 获取数组元素

- 格式：数组名[下标]   下标又称索引
- 功能：获取数组对应下标的那个值，如果下标不存在，则返回undefined。

```js
var arr = ['red',, 'green', 'blue'];
arr[0]; // red
arr[2]; // blue
arr[3]; // 这个数组的最大下标为2,因此返回undefined
```

### 遍历数组

> 遍历：遍及所有，对数组的每一个元素都访问一次就叫遍历。

```js
for(var i = 0; i < arr.length; i++) {
// 数组遍历的固定结构
}
```

### 新增元素

- 格式：数组名[下标/索引] = 值;
- 如果下标有对应的值，会把原来的值覆盖，如果下标不存在，会给数组新增一个元素。

```js
var arr = ["red", "green", "blue"];
// 把red替换成了yellow
arr[0] = "yellow";
// 给数组新增加了一个pink的值
arr[3] = "pink";
```

### 案例

- 求一组数中的所有数的和和平均值
- 求一组数中的最大值和最小值，以及所在位置
- 将字符串数组用|或其他符号分割
- 要求将数组中的0项去掉，将不为0的值存入一个新的数组，生成新的数组

	```js
	var arr1=[1,2,0,3,0,4,5,7,6,];
	var arr2=[];
	//var j=0;
	for(var i=0;i<arr1.length;i++){
		if(arr1[i]!==0){
			arr2[arr2.length]=arr1[i];//巧妙！！
			//j++;
		}
	}
	console.log(arr2);
	```

- 翻转数组

	```js
	var arr=[1,2,0,3,0,4,5,6,7];
	var temp;
	for(var i=0;i<arr.length/2;i++){
		temp=arr[i];
		arr[i]=arr[arr.length-i-1];
		arr[arr.length-i-1]=temp;
	}
	console.log(arr);
	```

- 冒泡排序，从小到大

	```js
	var arr=[1,10,0,3,0,9,5,6,7];
	var temp;
	for(vari=0;i<arr.length-1;i++){
		//控制比较的轮数
		for(var j=0;j<arr.length-1-i;j++){
			//控制每一轮比较的次数
			if(arr[j]>arr[j+1]){
				temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
		}
	}
	console.log(arr);
	```

## 函数

### 概述

- 背景：如果要在多个地方求1-100之间所有数的和，应该怎么做？
- 把一段相对独立的具有特定功能的代码块封装起来，形成一个独立实体，就是函数，起个名字（函数名），在后续开发中可以反复调用。
- 函数的作用就是封装一段代码，将来可以重复使用。
- **一个函数最好只封装一个功能**。

### 函数的定义

- 函数声明

	```js
	function 函数名 () {
	 // 函数体
	}
	```

- 函数表达式(匿名函数)

	```js
	var fn = function () {
	 // 函数体
	};
	```

- 特点：

	函数声明的时候，函数体并不会执行，只要当函数被调用的时候才会执行。 函数一般都用来干一件事情，需用使用动词+名词，表示做一件事情 `tellStory` `sayHello`等

### 函数的调用

- 语法: `funName()`
- 特点: 函数体只有在调用的时候才会执行，调用需要()进行调用。 可以调用多次(重复使用)

### 函数的参数

- 为什么要有参数

	```js
	function getSum() {
	 var sum = 0;
	 for (var i = 1; i <= 100; i++) {
	   sum += i;
	}
	 console.log();
	}
	// 虽然上面代码可以重复调用，但是只能计算1-100之间的值
	// 如果想要计算n-m之间所有数的和，应该怎么办呢？
	```
- 语法：

	```js
	// 函数内部是一个封闭的环境，可以通过参数的方式，把外部的值传递给函数内部，函数参数不需要var 声明。
	// 带参数的函数声明
	function 函数名(形参1, 形参2, 形参...){
	 // 函数体
	}

	// 带参数的函数调用
	函数名(实参1, 实参2, 实参3);
	```

- 形参和实参

	1. 形式参数：在声明一个函数的时候，为了函数的功能更加灵活，有些值是固定不了的，对于这些固定不了的值。我们可以给函数设置参数。这个参数没有具体的值，仅仅起到一个占位置的作用，我们通常称之为形式参数，也叫形参。
	2. 实际参数：如果函数在声明时，设置了形参，那么在函数调用的时候就需要传入对应的参数，我们把传入的参数叫做实际参数，也叫实参。
		
		```js
		var x = 5, y = 6;
		fn(x,y); 
		function fn(a, b) {
		 console.log(a + b);
		}
		//x,y实参，有具体的值。函数执行的时候会把x,y复制一份给函数内部的a和b，函数内部的值是复制的新值，无法修改外部的x,y
		```
	3. 形参、实参 的个数 可以不一致，对应接受即可。

- 案例

	- 求1-n之间所有数的和
	- 求n-m之间所有数额和
	- 圆的面积
	- 求2个数中的最大值
	- 求3个数中的最大值
	- 判断一个数是否是素数

### 函数的返回值

- 当函数执行完的时候，并不是所有时候都要把结果打印。我们期望函数给我一些反馈（比如计算的结果返回进行后续的运算），这个时候可以让函数返回一些东西。也就是返回值。函数通过return返回一个返回值
- 返回值语法：
	
	```js
	//声明一个带返回值的函数
	function 函数名(形参1, 形参2, 形参...){
	 //函数体
	 return 返回值;
	}
	​
	//可以通过变量来接收这个返回值
	var 变量 = 函数名(实参1, 实参2, 实参3);
	```
- 函数的调用结果就是返回值，因此我们可以直接对函数调用结果进行操作。
- 返回值详解： 
	- 如果函数没有显示的使用 return语句 ，**那么函数有默认的返回值：undefined**。
	- 如果函数使用 return语句，那么跟在return后面的值，就成了函数的返回值。 
	- 如果函数使用 return语句，但是return后面没有任何值，那么函数的返回值也是：undefined 
	- 函数使用return语句后，这个函数会在执行完 return 语句之后停止并立即退出，也就是说return后面的所有其他代码都不会再执行。 
	- **推荐的做法是要么让函数始终都返回一个值，要么永远都不要返回值**。

- 案例
	- 求阶乘
	- 求1!+2!+3!+....+n!
	- 求一组数中的最大值
	- 求一组数中的最小值

### arguments的使用

- JavaScript中，arguments对象是比较特别的一个对象，实际上是当前函数的一个内置属性。也就是说所有函数都内置了一个arguments对象，arguments对象中存储了传递的所有的实参。arguments是一个伪数组，因此及可以进行遍历
- 案例
	- 求任意个数的最大值
	- 求任意个数的和
		```js
		// 计算个数不固定的所有参数的和
		function () {
			let sum = 0
			console.log(arguments)
			console.log(arguments.length)
			for (let i = 0; i < arguments.length; i++) {
				sum += arguments[i]
			}
			console.log(sum)
		}
		```

### 函数综合案例

- 求斐波那契数列Fibonacci中的第n个数是多少？      1 1 2 3 5 8 13 21...
- 翻转数组，返回一个新数组
- 对数组排序，从小到大
- 输入一个年份，判断是否是闰年[闰年：能被4整数并且不能被100整数，或者能被400整数]
- 输入某年某月某日，判断这一天是这一年的第几天？

### 函数的其他

1. **匿名函数** <-> 命名函数
	- 匿名函数：没有名字的函数
	- 匿名函数如何使用：
	- 将匿名函数赋值给一个变量，这样就可以通过变量进行调用
	- 匿名函数自调用
	- 关于自执行函数（匿名函数自调用）的作用：防止全局变量污染。
2. 自调用函数（一次性--最安全--不冲突）
	匿名函数不能通过直接调用来执行，因此可以通过匿名函数的自调用的方式来执行

	```js
	(function () {
	 alert(123);
	})();
	```

3. 函数是一种数据类型

	```js
	function fn() {}
	console.log(typeof fn);  //function
	```

4. 函数作为参数
	因为函数也是一种类型，可以把函数作为两一个函数的参数，在另一个函数中调用。当作参数的函数叫做回调函数callback。
5. 函数做为返回值
	因为函数是一种类型，所以可以把函数可以作为返回值从函数内部返回，这种用法在后面很常见。

	```js
	function fn(b) {
		 var a = 10;
		 return function () {
		   alert(a+b);
		}
	}
	fn(15)();
	```

6. 代码规范
	- 命名规范  
	- 变量规范: `var name = 'zs'`    
	- 注释规范: `// 这里是注释`
	- 空格规范
	- 换行规范
		
		```js
		var arr = [1, 2, 3, 4];
		if (a > b) {
		     
		}
		for(var i = 0; i < 10; i++) {
		     
		}
		function fn() {
		     
		}
		```

## 对象

### 概述

- 为什么要有对象

	```js
	function printPerson(name, age, sex....) {
	}
	// 函数的参数如果特别多的话，可以使用对象简化
	function printPerson(person) {
	 console.log(person.name);
	 ……
	}
	```

- 什么是对象
	- 现实生活中：万物皆对象，对象是一个**具体的事物**，一个具体的事物就会有**行为和特征**。
	- 举例： 一部车，一个手机
	- 车是一类事物，门口停的那辆车才是对象
		- 特征：红色、四个轮子
		- 行为：驾驶、刹车
- JS和面向对象：
	- 面向对象的特性：封装、继承、多态、（抽象性）。
	- **JS没有“类”的概念，所以没有“继承”、“多态”的特性，所以JS不是面向对象的语言**。
	- **JS是一门基于对象的语言（内置了很多对象，直接用）**；（由于现在很多语言都是面向对象），JS可以模拟面向对象的思想。
- JavaScript中的对象
	- JavaScript中的对象其实就是生活中对象的一个抽象；
	- JavaScript的对象是**无序属性的集合**。其属性可以包含基本值、对象或函数。对象就是一组没有顺序的值。
	- 我们可以把JavaScript中的对象想象成**键值对**，其中值可以是数据和函数。
	- 对象的行为和特征
		- **特征---属性（变量）：事物的特征在对象中用属性来表示**。
		- **行为---方法（函数）：事物的行为在对象中用方法来表示**。
- JS中对象的属性/方法可以通过`点语法`或`[]`的方式来获取/修改。**后者更通用（如array等），前置更方便**。

### 对象的创建方式

1. 方法一：调用系统构造函数Object创建（=实例化）对象，Object为系统构造函数。
	
	```js
	var person = new Object();
	 person.name = 'lisi';
	 person.age = 35;
	 person.job = 'actor';
	 person.sayHi = function () {
	 console.log('Hello,everyBody');
	};
	```

	1.1、**工厂函数创建对象**：系统的Object构造函数每创建一个对象，都要重复写一遍相应的属性，所以可以借用函数，复用重复代码。

	```js
	function createObj(name, age) {
		let obj = new Object()
		// add props
		obj.name = name
		obj.age = age
		// add methods
		obj.sayHi = function () {
			console.log("你好, 我叫" + this.name + "年龄" + this.age)
		}
		return obj
	}
	
	// 调用工厂函数->创建对象
	let per1 = createObj('小芳', 20)
	per1.sayHi()
	```

2. 方法二：**自定义构造函数**创建对象（传值灵活，创建不同对象）：
	- 函数和构造函数的“**约定**”表象区别是：**构造函数名的首字母大写**，告诉其他程序员，这不是普通函数；
	- 函数和构造函数的“**约定**”用途区别：**普通函数是用来调用的，构造函数是用来创建对象的**。
		
		```js
		// 先定义一个构造函数
		function Person(name, age) {
			this.name = name
			this.age = age
			this.sayHi = function () {
				console.log("你好, 我叫" + this.name + "年龄" + this.age)
			}
		}

		// 调用构造函数->创建对象
		let per1 = new Person('小明', 10)
		per1.sayHi()
		```

	- 自定义构造函数，其实就是再工厂函数的基础上，省略了var this=new Object() 和 return this;
	- 用自定义构造函数创建对象时(var per1 = new Person(...))，new在执行时做了四件事（参考工厂函数）：
		a. **在内存中申请一块空闲空间，存储创建的新对象；**
		b. **把当前对象赋值给this；**
		c. **设置this对象的属性和方法；**
		d. **把this这个对象返回。**

3. 方法三：**字面量**创建对象（无法传值：一次性对象）
	
	```js
	// 原始写法
	let obj = {}
	obj.name = '小白'
	obj.age = 23
	obj.sayHi = function () {
		console.log("你好, 我叫" + this.name + "年龄" + this.age)
	}
	obj.sayHi() // 调用

	// 优化后的写法
	let obj = {
		name: '小明',
		age: 20,
		sayHi: function () {
			console.log("你好, 我叫" + this.name + "年龄" + this.age)
		}
	}
	obj.sayHi() // 调用
	```

### new关键字

**构造函数**：是一种特殊的函数。主要用来在创建对象时初始化对象， 即为对象成员变量赋初始值，总与new运算符一起使用在创建对象的语句中。

1. 构造函数用于创建一类对象，首字母要大写。
2. 构造函数要和new一起使用才有意义。

### this详解

JavaScript中的this指向问题，有时候会让人难以捉摸，随着学习的深入，我们可以逐渐了解，现在我们需要掌握函数内部的this几个特点：
1. 函数在定义的时候this是不确定的，只有在调用的时候才可以确定
2. 一般函数直接执行，内部this指向全局window
3. 函数作为一个对象的方法，被该对象所调用，那么this指向的是该对象
4. 构造函数中的this其实是一个隐式对象，类似一个初始化的模型，所有方法和属性都挂载到了这个隐式对象身上，后续通过new关键字来调用，从而实现实例化

### 属性和方法

- 如果一个变量属于一个对象所有，那么该变量就可以称之为该对象的一个属性，属性一般是名词，用来描述事物的特征；
- 如果一个函数属于一个对象所有，那么该函数就可以称之为该对象的一个方法，方法是动词，描述事物的行为和功能。
- 扩展：JS对象是无序属性的集合。==》**JSON**
	- 对象的内容为属性:值（**键值对**）；
	- 方法/属性都是广义的属性；
	- 数， 布尔，数组，函数，对象...都类型可以作为值；

### `点语法` 和 `[]` 语法

- “[""]”语法更通用（如array也可以访问属性/元素），“点语法”更简单。
- 由于JS是动态语言，访问对象没有的某个属性（如：obj.noname），会提示 undefined ，只要“点语法”访问了就相当于用var声明了。obj.noname = "yaro" 声明并赋值了。
- 对象中有xxx属性，可以使用“点语法”访问；没有xxx属性的话，使用“点语法”会有声明的效果，应该使用“[""]”语法读取里面的值。例子如下：

### JSON(JS object Notation)

- JSON数据本质：格式化后的一组字符串数据，方便交换数据。
- Json也是一个对象，但是，和字面量方式的区别为：key value 都是用双引号括起来。
- 遍历json对象使用 for in 循环；不能使用“点语法”。

	```js
	//JS 对象
	let obj = {
		name: '小明',
		age: 10
	}
	//JSON  - 键值都要双引号 && 不能有注释
	let json = {
		"name": "小明",
		"age": "10",
		"sex": "男"
	}
	//遍历JSON
	for (let key in json) {
		console.log(json.key) // 错误(不是对象), 会显示undefined
		console.log(json[key]) // 正确
	}
	```

| 区别| Json| Javascript对象|
| ----| ----- | ------- |
| 含义| 仅仅是一种数据格式| 对象的实例|
| 传输| 可以跨平台数据传输，速度快| 不能传输|
| 表现| 1. 键值对   2.   键必须加双引号   3.   值不能为方法函数/undefined/NaN|1.键值对   2.值可以是函数、对象、字符串、数字、boolean   等|
| 相互转换| Json →   JS 对象：   1. var obj = JSON.parse(jsonstring);   2. var obj = eval("("+jsonstring+")");| JS 对象 →   Json：   JSON.stringify(obj); |

From <<https://segmentfault.com/a/1190000005943794>> 

### JS对象属性的遍历/删除

- JS对象属性的遍历(同JSON对象的遍历)
	通过for..in语法可以遍历一个对象
	
	```js
	for(var key in obj) {
	 console.log(key + "==" + obj[key]); //不能使用"点语法"
	}
	```

	> `for in `还可以遍历 `array string` ，`for(var key in xxx）`中的`key` 都是 `index`索引/对象的键。

- 对象属性的删除

	```js
	function Fun() { 
	 this.name = 'mm';
	}
	var obj = new Fun(); 
	console.log(obj.name); // mm 
	delete obj.name;  //删除属性
	console.log(obj.name); // undefined
	```

### 堆(heap)和栈(stack)

- 这里指 Application Memory 相关的概念，和数据结构里面的概念有所不同。
- 堆栈空间分配区别：
	1. 栈（操作系统）：由操作系统自动分配释放 ，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈；
	2. 堆（操作系统）： 存储复杂类型(对象)，一般由程序员分配释放， 若程序员不释放，由垃圾回收机制回收，分配方式倒是类似于链表。

> 注意：**JavaScript中没有堆和栈的概念，此处我们用堆和栈来讲解，目的方便理解和方便以后的学习**。

- 不同的编程语言执行时，内存分配可能不同？？？
	1. C语言：C语言compile后，会把机器语言代码，加载到code区，供CPU取指令执行；
	![](http://ww1.sinaimg.cn/large/48356ef5ly1fznt36hi9cj20id0aa403.jpg)
	2. JS和java类似：
	![](http://ww1.sinaimg.cn/large/48356ef5ly1fznt3mq6fpj20ge0bswgj.jpg)

### JS不同数据类型的存储及值的传递

- 总的来说：**原始数据类型有**：number, string, boolean, undefined, null, object。
- 细分的话：
	- 值类型（又叫简单数据类型，基本数据类型）：number, string, boolean。在存储时，变量中存储的是值本身，因此叫做值类型；。
	- 引用类型（又叫复杂数据类型）：object。在存储时，变量中存储的仅仅是地址（引用），因此叫做引用数据类型。
	- 空类型：undefined, null。
- **值类型在栈中存储**。
- **引用类型在栈和堆中存储**：对象在堆中存储，**对象在堆中的地址在栈中存储**。
- 值类型之间传递，传递（复制）的是值；值类型作为函数的参数，传递的是值。
- 引用类型之间传递，传递（复制）的是地址（引用）；引用类型所谓函数的参数，传递的是地址。

1. 基本类型在内存中的存储（在栈中复制数据的值）
![](http://ww1.sinaimg.cn/large/48356ef5ly1fznt5u572tj20ge0bswgj.jpg)
2. 复杂类型在内存中的存储（在栈中复制obj的地址）
![](http://ww1.sinaimg.cn/large/48356ef5ly1fznt6gj46vj20gb07dt9p.jpg)
3. 基本类型作为函数的参数（在栈中传递(复制)数据的值）
![](http://ww1.sinaimg.cn/large/48356ef5ly1fznt6xg3szj20bv07kaaf.jpg)
4. 复杂类型作为函数的参数（在栈中传递(复制)obj的地址）
![](http://ww1.sinaimg.cn/large/48356ef5ly1fznt7jjtbxj20ex09emxv.jpg)
- 一个综合的练习。
![](http://ww1.sinaimg.cn/large/48356ef5ly1fznt8bbrcjj20l10a6aer.jpg)

## 内置对象 - 概述

- JavaScript中的对象分为3种：**内置对象**、**浏览器对象**、**自定义对象**
- JavaScript 提供多个内置对象：Math/Array/Number/String/Boolean...
- 对象只是带有**属性**和**方法**的特殊数据类型。
- 学习一个内置对象的使用，只要学会其常用的成员的使用（通过查文档学习）
- 可以通过MDN/W3C来查询
- 内置对象的方法很多，我们只需要知道内置对象提供的常用方法，使用的时候查询文档。
- MDN: Mozilla 开发者网络（MDN）提供有关开放网络技术（Open Web）的信息，包括 HTML、CSS 和万维网及 HTML5 应用的 API.
- 如何学习一个方法？
	1. 方法的功能
	2. 参数的意义和类型
	3. 返回值意义和类型
	4. demo进行测试

## 内置对象 - Math

- Math对象不是构造函数，它具有数学常数和函数的属性和方法，都是以静态成员的方式提供
- 常用属性：Math.PI、Math.E(自然对数的底数/欧拉常熟e)
- 常用方法：
	
	```js
	Math.random()               // 生成随机数
	Math.floor()/Math.ceil()     // 向下取整/向上取整
	Math.round()                // 取整，四舍五入
	Math.abs()                  // 绝对值
	Math.max()/Math.min()        // 求最大和最小值
	​Math.sin()/Math.cos()        // 正弦/余弦
	Math.power()/Math.sqrt()     // 求指数次幂/求平方根
	```

- 案例
	- 求10-20之间的随机数
	- 随机生成颜色RGB
	- 模拟实现max()/min()

## 内置对象 - Date

- 创建 Date 实例用来处理日期和时间。Date 对象基于1970年1月1日（世界标准时间）起的毫秒数。
	
	```js
	// 获取当前时间，UTC世界时间，距1970年1月1日（世界标准时间）起的毫秒数
	var now = new Date();
	console.log(now.valueOf()); // 获取距1970年1月1日（世界标准时间）起的毫秒数
	```
	​
	Date构造函数可以接收参数: 
	1. 毫秒数 1498099000356        new Date(1498099000356) // 毫秒数转成日期对象
	2. 日期格式字符串  '2015-5-1'   new Date('2015-5-1')
	3. 年、月、日……                new Date(2015, 4, 1)   // 月份从0开始
	4. 其他格式也可，如：2017/8/12, 2017.8.12, 2017,8,12等

- 获取日期的毫秒形式

	```js
	var now = new Date();
	console.log(date.valueOf())  // valueOf用于获取对象的原始值
	​var now = Date.now();   // HTML5中提供的方法，有兼容性问题
	​
	// 不支持HTML5的浏览器，可以用下面这种方式
	var now = + new Date();         // 调用 Date对象的valueOf() 
	```

- 日期格式化方法

	```js
	toString()      // 转换成字符串 Sun Dec 09 2018 16:20:34 GMT+0800 (China Standard Time)
	valueOf()       // 获取毫秒值 1544343834209
	// 下面格式化日期的方法，在不同浏览器可能表现不一致，一般不用
	toDateString()  //  Sun Dec 09 2018
	toLocaleDateString()  // 12/9/2018
	toTimeString()  // 16:22:06 GMT+0800 (China Standard Time)
	toLocaleTimeString()  // 4:22:06 PM
	```

- 获取日期指定部分

	```js
	getTime()     // 返回毫秒数和valueOf()结果一样，valueOf()内部调用的getTime()
	getMilliseconds() 
	getSeconds()  // 返回0-59
	getMinutes()  // 返回0-59
	getHours()    // 返回0-23
	getDay()      // 返回星期几 0-周日   6-周6
	getDate()     // 返回当前月的第几天
	getMonth()    // 返回月份，***从0开始***
	getFullYear() //返回4位的年份  如 2016
	```

- 案例
	- 写一个函数，格式化日期对象，返回yyyy-MM-dd HH:mm:ss的形式

		```js
		function formatDate(d) {
		 //如果date不是日期对象，返回
		 if (!date instanceof Date) {
		   return;
		}
		 var year = d.getFullYear(),
		     month = d.getMonth() + 1, 
		     date = d.getDate(), 
		     hour = d.getHours(), 
		     minute = d.getMinutes(), 
		     second = d.getSeconds();
		 month = month < 10 ? '0' + month : month;
		 date = date < 10 ? '0' + date : date;
		 hour = hour < 10 ? '0' + hour : hour;
		 minute = minute < 10 ? '0' + minute:minute;
		 second = second < 10 ? '0' + second:second;
		 return year + '-' + month + '-' + date + ' ' + hour + ':' + minute + ':' + second;
		}
		```

	- 计算时间差，返回相差的天/时/分/秒

		```js
		function getInterval(start, end) {
			var day, hour, minute, second, interval;
			interval = end - start;
			interval /= 1000;
			day = Math.round(interval / 60 /60 / 24);
			hour = Math.round(interval / 60 /60 % 24);
			minute = Math.round(interval / 60 % 60);
			second = Math.round(interval % 60);
			return {
				day: day,
				hour: hour,
				minute: minute,
				second: second
			}
		}
		```
	

## 内置对象 - String

- 相关说明：
	- JS中没有字符类型（ char）只有字符串（string）类型;
	- JS中的单引号/双引号都是字符串。C语言中char用单引号，string用双引号。
	- JS的字符串也可以“看作”字符组成的数组，可以用"[]"索引，可以用for， for-in遍历。
	- JS字符串具有不可变性：

		```js
		var str = 'abc';
		str = 'hello';  //  重新给字符串赋值，会重新在内存中开辟空间，这个特点就是字符串的不可变
		str[1] = a;  // 可以通过索引访问，但是不可修改！！
		```
	
	- 字符串重新赋值，会在“堆”中申请新的内存空间，“栈”中的地址只想改变而已。由于字符串的不可变，在大量拼接字符串的时候会有效率问题。

- 创建字符串对象: `var str = new String('Hello World');`
- 常用属性：`console.log(str.length);  // 获取字符串中字符的个数`
- 常用方法: 
	> 字符串所有的方法，都不会修改字符串本身(字符串是不可变的)，操作完成会返回一个新的字符串。

	```js
	1. 字符方法
	charAt()        //获取指定位置处字符,无参数默认为index=0，超出索引返回空字符串;
	charCodeAt()    //获取指定位置处字符的ASCII码
	str[0]          //HTML5，IE8+支持 和charAt()等效
	2. 字符串操作方法
	concat()        //拼接字符串，等效于+，+更常用
	slice()         //从start位置开始，截取到end位置，end取不到
	substring()     //从start位置开始，截取到end位置，end取不到
	substr()        //从start位置开始，截取length个字符
	3. 位置方法
	indexOf()       //返回指定内容在元字符串中的位置
	lastIndexOf()   //从后往前找，只找第一个匹配的
	4. 去除空白   
	trim()          //只能去除字符串前后的空白
	5. 大小写转换方法
	to(Locale)UpperCase()   //转换大写
	to(Locale)LowerCase()   //转换小写
	注：大多数情况下，toLocaleUpperCase()方法与 toUpperCase() 会产生相同的值，但是对于一些语言（locale）,例如土耳其语，因为它们的大小写映射规则与Unicode默认的映射规则不同，所以调用这两个方法将会产生不同的结果。
	From <https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase> 
	6. 其它
	search()
	replace()
	split()
	fromCharCode()
	// String.fromCharCode(83, 79, 83);   //把ASCII码转换成字符串
	```

## 内置对象 - Array

- 创建数组对象的两种方式
	- 字面量方式 var arr = [1, 2, 3];
	- 构造函数创建数组对象

		```js
		var arr = new Array(); // 创建了一个空数组
		var arr = new Array('zs', 1, 'ww');  // 创建了一个数组，
		var arr = new Array( 4); // 创建了一个长度为4的数组.
		```
	
	- `Array.from("abc") //["a", "b", "c"] `从可迭代对象生成数组。

- 获取数组中元素的个数: `console.log(arr.length);`
- 检测一个对象是否是数组: 
	- 关键字方法：xxx instanceof Array;
	- 静态方法：Array.isArray(xxx) HTML5中提供的方法，有兼容性问题;
- `toString()`/`valueOf()`
	- `toString()` 方法返回一个新的 Array Iterator 对象，该对象包含数组每个索引的值
	- `valueOf()` 返回数组对象本身
- 数组常用方法

	```js
	1. 栈操作(先进后出)
	○ push()    //在末尾追加元素，返回新数组长度
	○ pop()       //删除末尾元素，并返回该元素
	2. 队列操作(先进先出)
	○ push()
	○ shift()     //删除头部元素，并返回该元素
	○ unshift()   //在头部追加元素，返回新数组长度
	3. 排序方法
	○ reverse()   //翻转数组
	○ sort();     //排序，排序后的数组。请注意，数组已原地排序，并且不进行复制。但是sort不稳定，需要传输回调函数，参考MDN写法。
	4. 操作方法
	○ concat()    //把当前数组与N个数组拼接成新数组
	○ slice()     //从当前数组中截取一个新的数组并返回，不影响原来的数组，包括前，不包括后。
	○ splice()    //添加、删除或替换当前数组的某些项目，请参考MDN。
	5. 位置方法
	○ indexOf()、lastIndexOf()   //如果没找到返回-1
	6. 迭代方法 不会修改原数组(可选)
	○ every()  //参数为回调函数，回调函数对每个arr元素判断；回调函数可接收三个参数，分别是：元素的值ele、元素的索引index、数组本身arr；返回值为boolean。如果所有元素满足回调函数里面的条件（return ele.length>4;），返回true；
	○ filter()  //参数为回调函数，返回值为满足回调函数筛选的元素组成的新数组。回调函数的参数同every方法，arr.filter(function(el){return ele>20})
	○ forEach() //参数为回调函数，返回值为undefined。回调函数的参数同every方法，常用于遍历数组。
	○ map()  //参数为参数为回调函数，对每个元素进行加工，返回新的数组。如：arr.map(Math.sqrt);
	○ some()  //参数为
	7. 方法将数组的所有元素连接到一个字符串中。
	○ join("|") //用"|"连接各元素，返回字符串。
	```

- 清空数组

	```js
	// 方式1 推荐 
	arr = [];
	// 方式2 
	arr.length = 0;
	// 方式3
	arr.splice(0, arr.length);
	```

## 基本包装类型

- 普通变量不能直接调用属性或者方法
- 对象可以直接调用属性和方法
- 基本包装类型:本身是基本类型,但是在执行代码的过程中,如果这种类型的变量调用了属性或者是方法,那么这种类型就不再是基本类型了,而是基本包装类型,这个变量也不是普通的变量了,而是基本包装类型对象
- 常用的基本包装类型有：string number boolean。如：
![](http://ww1.sinaimg.cn/large/48356ef5ly1fzntxalphaj20dx0b5q49.jpg)


## iterable(可迭代、可遍历对象)

- 遍历`Array`可以采用下标循环，遍历`Map`和`Set`就无法使用下标。为了统一集合类型，ES6标准引入了新的`iterable`类型，`Array`、`Map`和`Set`都属于`iterable`类型。
- 具有`iterable`类型的集合可以通过新的`for ... of`循环来遍历。
- `for ... of`循环是ES6引入的新的语法，请测试你的浏览器是否支持：

```javascript
var a = [1, 2, 3];
for (var x of a) {
}
alert('你的浏览器支持for ... of');
```

- 用`for ... of`循环遍历集合，用法如下：

```javascript
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
	alert(x);
}
for (var x of s) { // 遍历Set
	alert(x);
}
for (var x of m) { // 遍历Map
	alert(x[0] + '=' + x[1]);
}
```

- 你可能会有疑问，`for ... of`循环和`for ... in`循环有何区别？

	`for ... in`循环由于历史遗留问题，它遍历的实际上是对象的属性名称。一个`Array`数组实际上也是一个对象，它的每个元素的索引被视为一个属性。

- 当我们手动给`Array`对象添加了额外的属性后，`for ... in`循环将带来意想不到的意外效果：

```javascript
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
	alert(x); // '0', '1', '2', 'name'
}
```

`for ... in`循环将把`name`包括在内，但`Array`的`length`属性却不包括在内。
`for ... of`循环则完全修复了这些问题，它只循环集合本身的元素：

```javascript
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x of a) {
	alert(x); // 'A', 'B', 'C'
}
```

这就是为什么要引入新的`for ... of`循环。

然而，更好的方式是直接使用`iterable`内置的`forEach`方法，它接收一个函数，每次迭代就自动回调该函数。以`Array`为例：

```javascript
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
	// element: 指向当前元素的值
	// index: 指向当前索引
	// array: 指向Array对象本身
	alert(element);
});
```

*注意*，`forEach()`方法是ES5.1标准引入的，你需要测试浏览器是否支持。

`Set`与`Array`类似，但`Set`没有索引，因此回调函数的前两个参数都是元素本身：

```javascript
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
	alert(element);
});
```

`Map`的回调函数参数依次为`value`、`key`和`map`本身：

```javascript
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
	alert(value);
});
```

如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，因此可以忽略它们。例如，只需要获得`Array`的`element`：

```javascript
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
	alert(element);
});
```
