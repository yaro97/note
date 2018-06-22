# json_pickle_shelve模块

> - 序列化（serialize）：[computing] To convert an object into a sequence of bytes that can later be converted back into an object with equivalent properties.不同的语言不同的叫法，比如：serialization，marshalling，flattening等等；
>   **序列化的目的**：把python的对象转变为**byte或str类型**，方便我们**存储、网络传输**等
> - pickle（腌、腌制），假如我们想把python的对象存起来，就想把各种蔬菜放进坛子（jar）腌制一样，方便我们重新利用；优点：支持所有python对象（**序列化为bytes类型-不可读**）；缺点：不能与其他语言交互。
> - shelve（搁置、放在架子上），比喻暂时不做处理；shelve模块是pickle的进一步包装（把腌制用的坛子jar放置于架子），提供一个类似于python的dict对象的API；优缺点：同pickle。
> - json（JavaScript Object Notation）：不像pickle只能用于python自己的序列化与反序列化，json是很多语言都支持的数据类型，这样就方便我们与其他语言进行交互(传统的XML也有类似的功能，很多银行业还在使用)；**序列化为字符串-可读**；缺点：有些python对象不支持，如：class、function、tuple等，不过这些序列化的意义不大。
>
> 

## 0. 引言（eval->json）

在没有json模式的时候，我们遇到字符串转为字典的时候可以使用`eval`，如下：

```python
>>> import json  
>>> s = '{"one":1,"two":2}'  
>>> json.loads(s)  
{u'two': 2, u'one': 1}  
>>> eval(s)  
{'two': 2, 'one': 1}
```

但是：null、true、false等特殊类型eval就不能处理了。

```python
>>> x="[null,true,false,1]"  
>>> json.loads(x)  
[None, True, False, 1]  
>>> eval(x)  
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
  File "<string>", line 1, in <module>  
NameError: name 'null' is not define
```

eval通常用来执行一个字符串表达式，并返回表达式的值。比如：

```python
>>> eval('1+1')  
>>> json.loads('1+1')  # 报错ValueError...
```

**终上所述，json与eval区别有：**

1、json.loads与eval都能将s转成python中的对象，json.loads将json中的字符串转成unicode(types.UnicodeType)，eval转成了str(types.StringType)。

2、json中只能用双引号`""`，不能使用单引号`''`。

3、eval可能会引起安全问题，建议不要乱用。

## A. json模块

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

- json字符串转python对象的数据类型转换表

| JSON          | Python    |
| ------------- | --------- |
| object        | dict      |
| array         | list      |
| string        | unicode   |
| number (int)  | int, long |
| number (real) | float     |
| true          | True      |
| false         | False     |
| null          | None      |

- python对象转json字符串类型转换表

| Python           | JSON   |
| ---------------- | ------ |
| dict             | object |
| list, tuple      | array  |
| str, unicode     | string |
| int, long, float | number |
| True             | true   |
| False            | false  |
| None             | null   |

```python
import json
 
dic={'name':'alvin','age':23,'sex':'male'}  #<class 'dict'>

# 序列化方法1：
with open('序列化对象','w') as f:
	f.write(json.dumps(dic))  # 需要先json.dumps(dic)为字符串，再f.write()写入文件

# 序列化方法2（进一步包装）：
with open('序列化对象', 'w') as f:
    json.dump(dic, f)  # 直接把dic对象以字符串的方式dump到文件对象f中

# 反序列化方法1：
with open('可序列化对象', 'r') as f:
	data=json.loads(f.read())  # 需要先f.read()为字符串，然后json.loads()为python对象
# 反序列化方法2（进一步包装）：
with open('可序列化对象', 'r') as f:
    data = json.load(f)  # 直接把文件内容读取别转化为python对象。

# 只要是符合json规范格式的字符串，皆可以被load(s)，不一定要dump(s)。
```



## B. pickle模块

pickle的使用（API）和json完全一样，只不过，pickle是把python对象序列化为bytes（字节）类型。如下：

```python
import pickle

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}  # <class 'dict'>

# 序列化方法1：
with open('序列化对象', 'wb') as f:  # 注意是’wb‘，不是’w‘
    f.write(pickle.dumps(dic))  # 注意是w是写入str,wb是写入bytes,j是'bytes'

# 序列化方法2（进一步包装）：
with open('序列化对象', 'wb') as f:
    pickle.dump(dic, f)  # 直接把dic对象以字符串的方式dump到文件对象f中

# 反序列化方法1：
with open('可序列化对象', 'rb') as f:
    data = pickle.loads(f.read())  
# 反序列化方法2（进一步包装）：
with open('可序列化对象', 'rb') as f:
    data = pickle.load(f)  

# pickle序列化的文件是供内存调用的，不是供human查看的（乱码）。
```

## C. shelve模块

shelve是pickle的进一步包装，像使用python的dict类一样的API。shelve模块只有一个open函数，返回"类似字典的对象"，可读可写。key必须为字符串，而值可以是python所支持的数据类型

```python
import shelve
 
f = shelve.open(r'shelve.txt')
 
# f['stu1_info']={'name':'alex','age':'18'}
# f['stu2_info']={'name':'alvin','age':'20'}
# f['school_info']={'website':'oldboyedu.com','city':'beijing'}
# f.close()

print(f.get('stu_info')['age'])

# shelve会生成三个文件，也是供计算机内存调用的（乱码）
```

