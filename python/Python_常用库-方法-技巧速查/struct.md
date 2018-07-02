# struct模块

## 1 概述

>  struct模块的作用，把`python内置对象`转变为`字节类型`方便网络socket传输等等。

Python是一门非常简洁的语言，对于数据类型的表示，不像其他语言预定义了许多类型（如：在C#中，光整型就定义了8种），它只定义了六种基本类型：字符串，整数，浮点数，元组，列表，字典。通过这六种数据类型，我们可以完成大部分工作。但当Python需要与其他的平台(其他的编程语言)进行交互的时候，必须考虑到将这些数据类型与其他平台或语言之间的类型进行互相转换问题。打个比方：C++写的客户端发送一个int型(4字节)变量的数据到Python写的服务器，Python接收到表示这个整数的4个字节数据，怎么解析成Python认识的整数呢？ Python的标准模块struct就用来解决这个问题。

了解c语言的人，一定会知道struct结构体在c语言中的作用，它定义了一种结构，里面包含不同类型的数据(int,char,bool等等)，方便对某一结构对象进行处理。而在网络通信当中，大多传递的数据是以二进制流（binary data）存在的。当传递字符串时，不必担心太多的问题，而当传递诸如int、char之类的基本数据的时候，就需要有一种机制将某些特定的结构体类型打包成二进制流的字符串然后再网络传输，而接收端也应该可以通过某种机制进行解包还原出原始的结构体数据。python中的struct模块就提供了这样的机制，该模块的主要作用就是对python基本类型值与用python字符串格式表示的C struct类型间的转化（This module performs conversions between Python values and C structs represented as Python strings.）。

struct模块的内容不多，也不是太难，下面对其中最常用的方法进行介绍，struct模块中最重要的三个函数是pack(), unpack(), calcsize()

- `pack(fmt, v1, v2, ...)`     按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流)
- `unpack(fmt, string)`       按照给定的格式(fmt)解析字节流string，返回解析出来的tuple
- `calcsize(fmt) `                计算给定的格式(fmt)占用多少字节的内存

## 2 struct.pack

struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）。其函数原型为：struct.pack(fmt, v1, v2, …)，参数fmt是格式字符串，关于格式字符串的相关信息在下面有所介绍。v1, v2, …表示要转换的python值。下面的例子将两个整数转换为字符串（字节流）:

```python
import struct
 
a = 20
b = 400
 
s = struct.pack("ii", a, b)  #转换后的str虽然是字符串类型，但相当于其他语言中的字节流（字节数组），可以在网络上传输
print（type(s）, len(s), s)
```

格式符”i”表示转换为int，’ii’表示有两个int变量。进行转换后的结果长度为8个字节（int类型占用4个字节，两个int为8个字节），可以看到输出的结果是乱码，因为结果是二进制数据，所以显示为乱码。可以使用python的内置函数repr来获取可识别的字符串，其中十六进制的0x00000014, 0x00001009分别表示20和400。

struct模块定义的数据类型表：

## 3 struct.unpack

struct.unpack做的工作刚好与struct.pack相反，用于将字节流转换成python数据类型。它的函数原型为：struct.unpack(fmt, string)，该函数返回一个元组。 下面是一个简单的例子：

```python
str = struct.pack("ii", 20, 400)
a1, a2 = struct.unpack("ii", str)
print('a1:', a1)
print('a2:', a2)
```

## 4 struct.calcsize

struct.calcsize用于计算格式字符串所对应的结果的长度，如：struct.calcsize(‘ii’)，返回8。因为两个int类型所占用的长度是8个字节。

## 一个例子

```python
# -*- coding: utf-8 -*-
 
import struct
 
# 定义数据
a = "hello"
b = "world!"
c = 20
d = 42.56
 
# 打包
binStr = struct.pack("5s6sif", a, b, c, d)
print(len(binStr))
binStr2 = struct.pack("i", c)
 
# 解包
e, f, g, h = struct.unpack("5s6sif", binStr)
print(e, f, g, h)
 
i, = struct.unpack("i", binStr2)
print(i)
 
# 计算转换字节长度
print(struct.calcsize("5s6sif"))
```

输出结果：

```
20
hello world! 20 42.5600013733
20
20
```







