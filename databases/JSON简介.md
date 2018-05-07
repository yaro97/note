## JSON简介

参考文件：https://www.json.org/json-zh.html

JSON（JavaScript Object Notation） 是一种轻量级的数据交换格式；

```json
{"name":"eric","age":"24"}
{"first":{"name":"eric","age":"24"},"second":{"name":"yaro","age":"33"}}
```

## JSON优/缺点

优点：

1、数据格式比较简单，易于读写，格式都是压缩的，占用宽带小；
2、支持多种语言，包括Python、JAVA、Ruby、JS、Perl、PHP、C、C#等服务器端语言，便于服务器端解析；

缺点：

1、字符集必须是Unicode，受约束性强；
2、语法过于严谨，必须遵循JSON语法的四个原则；


## JSON的起源

常用语言的数据类型：

1、标量（Scalar）：单独的字符串/数字，如：“北京”；
2、序列（Sequence）：若干个相关数据按照一定的顺序放在一起，又叫数组（Array）or列表（List），如：“北京，上海”;
3、映射（Mapping）：键值对（key-value）,数据有一个名称，还有一个对应的值。又称为散列（Hash）or字典（Dict），如：“首都：北京”；

## JSON的基本语法

JSON基本类型：string number true false null
JSON数据结构：Object(key必须为string类型：value可以为任何基本类型or数据结构) Array（value可以是任何基本类型or数据结构）

基本规则：

1、并列的数据之间用逗号（“,”）分隔
2、映射用冒号（":"）表示
3、并列的数据集合（数组）用方括号（"[]"）表示
4、映射的集合（对象）用大括号（"{}"）表示

举例：`“北京的面积为16800平方公里，常住人口1600万人。上海的面积为6400平方公里，常住人口为1800万人。”`
转换为JSON格式后：

```json
[
    {"城市":"北京","面积":"16800","人口":"1600"},
    {"城市":"上海","面积":"6400","人口":"1800"}
]
```

## 相提并论

![Snipaste_2018-05-06_08-09-51.png](https://i.loli.net/2018/05/06/5aee47df90ae0.png)

