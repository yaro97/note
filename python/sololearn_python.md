# Sololearn Python

## Basic concepts

- What is Python?: Python has several different implementations, written in various languages. The version used in this course, CPython, is the most popular by far.

- Simple Operations：加减乘除 // % **   

- String: '\n' ；  'abc{}de'.format() ；  "2" + "2"  ；  print("spam" * 3) ; str[6]  ; for i in str ;

- Output & input:  strs = input("Enter something please: ")

- Type Conversion: int("3")  float(input("Enter another number: "), 2)

- Variables: 先声明对象，然后变量指向对象； del foo ； 

- In-Place Operators： += ； 其他-, *, / and % as well.

## Control Structures

- Booleans & Comparisons： == ； != ； >= ; or ; and ; not 

- Range(1， 10， 2):生成一个range对象，迭代器； 可以用 list tuple 函数转变成序列；

- if elif else：

- Operator Precedence: 幂  正负  乘除模  加减  位移(>>)  比较  (不)相等  赋值（+=） is  (not )in  逻辑运算(and or not);

- while loop:  break  continue;

- list: [] ;  list();  list[2:] ; list1 + list2; str in list; list.append; len(list) ;list.insert(index, "is") ; list.index();  

- for loop: for i in strs ; for i in list ; for i in range(5);

## Functions & Modules

- Functions: code reuse! ; def fun(x,y): ;  return (默认是None); return 后函数终止；

- Comments & Docstrings:要记得写注释；

- Functinons as Objects : 函数可以当做参数，可以重新赋予，可以return函数；

- Modules：一些实现功能的codes的组合；import ; import xx as yy ;  random.randint; math.pi; 

- The Standard Library & Pip: 安装python自带的Modules：（string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.）； Many third-party Python modules are stored on the Python Package Index (PyPI). The best way to install these is using a program called pip. 

## Exceptions & Files

- Exceptions:When an exception occurs, the program immediately stops. eg.ImportError: IndexError:NameError: SyntaxError: TypeError:ValueError:

- Exception Handling: try: except IndexError: except: ; try except finally ; raise NameError("Invalid name!") ;  raise(捕捉异常后，可以再次唤起)

- Assertions：assert 1 + 1 == 3 ，断言正确，继续执行，断言False，唤起AssertionError异常；还可以接收参数：assert (temp >= 0), "Colder than absolute zero!"

- Opening FIles： myfile = open("filename.txt")  默认是 r ，可以指定 w r wb (binary),记得myfile.close() ；  文件对象是迭代器； file.read(16) 读取16个字符，file.read(4)再次读取，file.read()读取剩余全部；file.readlines()返回行组成的列表；

- Writing Files：file = open("newfile.txt", "w")  ； file.write("Some new text") ； 

- 正确的读写文件：try: with open("filename.txt") as f:  f.write("xxx")  except IOError:  print('Oops!')

## More Types

- None: represent the absence of a value，类似于其他语言中的 Null，函数在没有 return 语句时，返回None；

- Dictionaries： {key:value}； 根据key索引，索引没有的键时错误为：KeyError； 可以用dict.get(‘key’)方法替代，没有 key 返回 None； value 可以再赋值； 键值必须是immutalbe(不可变)，list不可以，tuple可以； 可以使用 (not) in
 判断一个key是否属于dict； 

 - Tuple：  类似于list，但是immutable（不可变）； 使用小括号，或者省略小括号，如：`my_tuple = "one", "two", "three"`； tuple is faster than list;

 - List Slices: list[2:6]，含2不含6； list[:9]，省略表示开头/结尾； list[::2],第三个参数表示 step; list[1:-1],第一个到最后一个（不含）； list[::-1] is a common and idiomatic way to reverse a list; list[4:1:-1]表示从倒数第5个到第2个（反向）； tuple也可用来切片；

 - List Comprehensions： 快速创建一个有规则的list； `cubes = [i**3 for i in range(5)]`；  `evens=[i**2 for i in range(10) if i**2 % 2 == 0]` ; `even = [2*i for i in range(10**100)]` 会在成内存占用急速升高，或者提示“MemoryError”，可以用“generators”来解决；

 - String Formatting： 连接str和non-str，可以把non-str转换成str，用`+`来连接str； 可以用str的format方法更方便的实现`"Numbers: {0} {1}".format(nums[0], nums[1])`，前面的 `0 1`可以省略，但是format里面的参数必须对应 ；  也可以指定特定变量`a = "{x}, {y}".format(x=5, y=12)`，如此参数顺序不必对应；

 - String Functions： `", ".join(["spam", "eggs"])`连接成字符串 ; `"Hello ME".replace("ME", "world")`替换 ; `"This is".startswith("This")`是否以this开头 ; `"a sentence.".endswith("sentence.")`返回TRUE ; `This is".upper()`转换为大写 ; `AN ALL".lower()`转换为小写 ; `spam, eggs, ham".split(", ")`返回列表；

- Numeric Functions： `print(min(1, 2, 3, 4, 0, 2, 1))` ； `print(max([1, 4, 9, 2, 5, 6, 8]))` ； `print(abs(-99))` ； `print(abs(42))` ； `print(sum([1, 2, 3, 4, 5]))`

- List Functions: `nums=[2,3,4,1,4]` ; `if all([i > 5 for i in nums]):pass`所有值是否都大于5 ； `any([i % 2 == 0 for i in nums]):pass`是否有一个是偶数 ； `for v in enumerate(nums):print(v)`遍历列表，并将索引和值组成tuple打印； 

## Functional Programming

- higher-order functions：可以把其他函数当做参数，函数本身也是object；

- Pure Functions：Pure functions have no side effects, and return a value that depends only on their arguments.自己功能单一，不和其他对象交互，没有副作用；

-  Pure Functions are easier to reason about and test，more efficient，easier to run in parallel，但是也有缺点（they majorly complicate the otherwise simple task of I/O, since this appears to inherently require side effects. ）。

- Lambdas：匿名函数； 没有def函数功能强大； 

```python
lambda x: 2*x*x
(lambda x: x**2 + 5*x + 4) (-4)  # 但是这样就不如def函数了，很少这样用，

double = lambda x: x * 2  # 也可以复制给变量
print(double(7))
```

- map & filter： 操作序列的built-in高阶函数；返回的是map/filter对象；

```python
def add_five(x):return x+5
m = map(add_five, [1,2,3]])   # 返回的是map对象；
m = map(lambda x: x+5, [1,2,3]])  # 也可以使用lambda表达式；
list(map(lambda x: x+5, [1,2,3]]))  
filter(lambda x: x%2==0, nums)  # 返回的是filter表达式；
``

- Generators：Generators are a type of iterable（可迭代类型）, like lists or tuples. 但是，不能索引，可以用循环迭代； 一次yield一个，内存占用很少；

```python
def countdown():
  i=5
  while i > 0:  # 我们可以while Ture 一直返回每个值，也不会内存过大；
    yield i
    i -= 1
list(countdown())  # 可以转换为list；
for i in countdown():
  print(i)
```

- Decorators：在不修改函数A的情况下，用另一个函数B来修改函数A; 把需要修改的函数当做一个参数（Object）传给另一个修饰函数；

```python
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

print_text = decor(print_text)  

@decor            # 上面两行的缩写
def print_text():
  print("Hello world!")
```

- Recursion：self-reference（自引用） - functions calling themselves. 

```python
def factorial(x):  # 求阶乘
  if x == 1:   # 加入没有 base case 的话，会一直递归下去，只到out of memory and crashes；
    return 1
  else: 
    return x * factorial(x-1)
    
# 当然也可以两个函数之间递归
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)

print(is_odd(17))
print(is_even(23))
```

- Sets： `{1, 2, 3, 4, 5}` ； 无序、不重复（`in`判断比list更快）； 空集合只能使用` set()` ； 

```python
num_set = {1, 2, 3, 4, 5}
print(3 in num_set)
nums.add(-7)  # 没有append
nums.remove(3)
first_set | second_set  # 交& 叉- 并| 补^
```
- itertools

```python
## One type of function it produces is infinite iterators. 
#The function count counts up infinitely from a value. 
#The function cycle infinitely iterates through an iterable (for instance a list or string). 
#The function repeat repeats an object, either infinitely or a specific number of times.
from itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break

##There are many functions in itertools that operate on iterables, in a similar way to map and filter. 
#Some examples:
#takewhile - takes items from an iterable while a predicate（断言、判定） function remains true;
#chain - combines several iterables into one long one; 
#accumulate累加 - returns a running total of values in an iterable.
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))  #[0, 1, 3, 6, 10, 15, 21, 28]
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))  #[0, 1, 3, 6]

#There are also several combinatoric组合 functions in itertool, such as product and permutation排列.
#These are used when you want to accomplish a task with all possible combinations of some items.
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 
```

## Object-Oriented Programming

- `Object-oriented programming` (OOP)面向对象编程 is a very popular paradigm of programming；之前已经讨论过 `imperative命令式编程` (using statements, loops, and functions as subroutines), and `functional函数式编程` (using pure functions, higher-order functions, and recursion)..

- Classes： Objects are created using `classes`,  类包含`attributes`、`method`等； 类的方法和属性通过`dot（.）` syntax 访问。

```python
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
```

- __init__ ： The `__init__` method is the most important method in a class. 
This is called when an instance (object) of the class is created, using the class name as a function.

- 所有的方法必须把`self`当做第一个parameter，当该方法被调用时，`self`代表实例本身。

- 尝试access为定义的属性 or 方法，会报错`AttributeError`； 

- Inheritance： `subclass` `superclass`； 也可以间接继承（A集成于B，B继承于C）

```python
class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
```

- super函数可以调用父类（superclass）的方法；

```python
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)  # 2
    super().spam()  # 1
            
B().spam()  # 相当于：b=B(); b.spam()
```

- Magic Methods： 两边都有` double underscores`的方法； 可以用于操作符重载（`operator overloading`）

```python
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):   # The expression x + y is translated into x.__add__(y). 
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)  # 8
print(result.y)  # 16
```

- 其他Magic Methods

```python
More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
```

- The expression `x + y` is translated into `x.__add__(y)`. However, if x hasn't implemented `__add__`, and x and y are of different types, then `y.__radd__(x)` is called. There are equivalent r methods for all magic methods just mentioned.

```python
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

>>>结果
spam
============
Hello world!
>>>
# In the example above, we defined the division operation for our class SpecialString.
```

- Magic Methods for comparisons.

```python
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
=================
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

>>>结果
>spam>eggs
e>spam>ggs
eg>spam>gs
egg>spam>s
eggs>spam>
>>>
```

- There are several magic methods for making classes act like containers.

```python
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
```


暂时先写这么多，具体参考SoloLearn APP；
暂时先写这么多，具体参考SoloLearn APP；
暂时先写这么多，具体参考SoloLearn APP；
暂时先写这么多，具体参考SoloLearn APP；

## Regular Expressions

## Pythonicness & Packaging