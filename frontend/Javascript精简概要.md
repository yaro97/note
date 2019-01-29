## 语法

JS = ECMA +DOM +BOM

var foo = '1111';

ECMAScript数据类型：
1.简单数据类型：undefined null booleam number string
2.复杂数据类型：Object

可以使用 typeof 检测
undefined == null  返回True

NaN 是特殊的number,有数字的非法运算会得到NaN，任何有NaN运算都是NaN，和任何值不想等包括自己；
isNaN()  会尝试转换为数字，再检测；

parseInt() 函数（采集最左边的有效数）
parseFloat()  函数
Number()  函数

toString() 方法
String() 函数

Boolean() 函数

&& || !

## 流程控制

分支 if语句

```js
if(condition){
    statement;
    // alert('Fuck')  //浏览器弹窗
}
```

```js
if(condition){
    statement;
    // alert('Fuck')  //浏览器弹出警告窗
}else{
    statement
    // prompt('') //弹出提示框，返回用户输入值，‘取消’返回null
}
```

```js
if(condition){
    statement;
    // alert('Fuck')  //浏览器弹出警告窗
}else if{
    statement
    // prompt('') //弹出提示框，返回用户输入值，‘取消’返回null
}else{
    statement
    // 'aaa'.length  //length属性获取str长度。
}
```


switch语句

```js
var d=new Date().getDay(); 
switch (d) 
{ 
  case 0:
  x="今天是星期日"; 
  break; 
  case 1:
  x="今天是星期一"; 
  break; 
  case 2:
  x="今天是星期二"; 
  break; 
  case 3:
  x="今天是星期三"; 
  break; 
  case 4:
  x="今天是星期四"; 
  break; 
  case 5:
  x="今天是星期五"; 
  break; 
  case 6:
  x="今天是星期六"; 
  break; 
}
document.write('今天是星期' + 'x')
```

循环 

for - 循环代码块一定的次数
for/in - 循环遍历对象的属性
while - 当指定的条件为 true 时循环指定的代码块
do/while - 同样当指定的条件为 true 时循环指定的代码块

```js
for (var i=0; i<5; i++)
{
      x=x + "该数字为 " + i + "<br>";
}

// 或者
var i=2,len=cars.length;
for (; i<len; i++)
{ 
    document.write(cars[i] + "<br>");
}
// 或者
var i=0,len=cars.length;
for (; i<len; )
{ 
    document.write(cars[i] + "<br>");
    i++;
}
```

```js
var person={fname:"John",lname:"Doe",age:25}; 
for (x in person)  // x 为属性名
{
    txt=txt + person[x];
}
```

```js
while (i<5)
{
    x=x + "The number is " + i + "<br>";
    i++;
}
```

```js
do
{
    x=x + "The number is " + i + "<br>";
    i++;
}
while (i<5);
```

break/continue  退出循环/跳过本次循环

## JavaScript函数

函数的声明/调用

```js
function foo(){
    // xxxx
}

foo()

// 可以传递参数，
// 记得return的用法
// 函数中调用arguments.length 可调用参数的个数
// arguments[0] 可以调用第一个参数，也可以赋值
```

可以类似于python中的不定参数`*args`，js中为空即可：

```js
function getAvg(){
    var sum=0,len=arguments.length,i;
    for (i=0,i<len,i++){
        sum+=arguments[i];
    }
}

// 调用

var avg=getAvg(5,55,66,8,99,4,77);
console.log(avg);
```

## JS中的内置对象

js是面向对象的：字符串、函数、数组都是对象

内置对象：浏览器默认封装的对象，我们可以直接调用

### Array

- 创建数组

1、new Array()

```js
var colors=new Array();
var colors=new Array(3);  //指定元素的数量
var colors=new Array(1,3,6,9); //预存4个元素
console.log(colors);
```

2、使用数组字面量表示法创建

```js
var colors=['red','green','yellow',1,2,{'name‘：'yaro'‘}];
console.log(colors)
```

- 读取数组

```js
console.log(colors[0]);
```

### String

### Math

### Date

