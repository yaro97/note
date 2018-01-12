# python_class_oop_总结及梳理.md

本文对Python的Class相关知识点做一个串联，并提出“为什么要使用这个知识点”，希望XX更好的理解Clas！

## Instance Variable and Instance Method

**问题**：没有Class的概念，如何表示各员工的相关信息呢？  
**答案**：普通`Variable（变量）`  


```python
employee_1_first_name = John
employee_1_last_name = Smith
...
employee_2_first_name = Love
employee_2_last_name = Keven
...
```

**问题**：如何更高效的实现呢？  
**答案**：Class 的 `Instance Variable（实例变量）`  

使用Class实现如下：

```python
class Employee:
    pass


emp_1 = Employee()
emp_1.first_name = 'John'
emp_1.last_name = 'Smith'
emp_1.salary = 5000
emp_1.email = 'John.Smith@email.com'
# ...
emp_2 = Employee()
emp_2.first_name = 'Keven'
emp_2.last_name = 'Love'
emp_2.salary = 6000
emp_2.email = 'Keven.Love@email.com'
# ...
```

貌似没有更高效，继续 -->

```python
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)


emp_1 = Employee('John', 'Smith', 5000)
emp_2 = Employee('Keven', 'Love', 6000)
# ...
```

> 这样貌似好了很多，尤其是员工数量多、属性多的时候！

**问题**：如何通过员工的`first_name` and `last_name` 构造出 `full_name`呢？  
**答案**：直接使用`字符串连接`或`字符串格式化`   

```python
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)


emp_1 = Employee('John', 'Smith', 5000)

print('{} {}'.format(emp_1.first_name, emp_1.last_name))
```

同样，如果有很多员工、很多要求（不只是构造`full_name`），如此就太低效了。

**问题**：如何高效实现一些特定需求(功能)呢？  
**答案**：Class的 `Instance Method（实例方法）`.  

```python
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)

    def full_name(self):  # 方法必须有self参数；
        return '{} {}'.format(self.first_name, self.last_name)


emp_1 = Employee('John', 'Smith', 5000)
emp_2 = Employee('Keven', 'Love', 6000)

# print(Employee.full_name(emp_1))  # 通过‘函数’调用也可：通过类调用需要传入Instance当做参数； 
print(emp_1.full_name())  # 通过‘方法’调用自动把Instance传入，更简洁，推荐！
# 方法本质是函数，放在Class中便改名为“方法”，需要带小括号调用
```

> Tips：
> - `__init__`为初始化方法，实例化时会执行此方法；
> - `Class`中的每个方法自动使用`Instance`作为第一个参数，即`self`表示实例本身；
> - `self`不能省略，若省略（没有参数），但是依然会自动传入`Instance`作为第一个参数，就会报错！
> - 所谓`实例方法`：其实就是Class的函数，然后自动把Instance当做参数（self）传入； 
> - 本质是`Employee.full_name(emp_1)`，但是`emp_1.full_name()`更简洁；

## Class Variable

上面说了`Instance Variable`（只能各个实例使用） ,那么什么是`Class Variable`（所有实例都可使用，类自身也可使用），为什么要有这个东东呢？？

**问题**：新的一年，给全体员工涨工资，如何实现？  
**答案**：上面已经说了，Class的 `Instance Method（实例方法）`可以解决。

```python
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * 1.04)


emp_1 = Employee('John', 'Smith', 5000)
emp_2 = Employee('Keven', 'Love', 6000)

print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)
```

**问题**：我们想知道具体的“工资涨幅”，咋整？涨1.04太少了，需要改成1.05，咋整？改源码？额...不要动不动就改源码嘛！  
**答案**：Class Variable（类变量）

```python
class Employee:
    raise_amount = 1.04
    num_of_emps = 0  # 用于统计实例数量

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)
        Employee.num_of_emps += 1  # 这里使用的是Employee调用Class变量

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        # 这里使用的是self(Instance)调用的Class变量，可以更灵活的控制各个Instance对应的raise_amount变量；
        # 试想：如果使用Employee.raise_amount调用Class变量会有何不同？？


emp_1 = Employee('John', 'Smith', 5000)
emp_2 = Employee('Keven', 'Love', 6000)

# print(emp_1.__dict__)  # emp_1实例并没有raise_amount变量
# print(Employee.__dict__)  # Employee类含有raise_amount变量
print(Employee.raise_amount)
print(emp_1.raise_amount)
Employee.raise_amount = 1.05  # 影响所有实例
# emp_1.raise_amount = 1.05  # 只影响emp_1实例
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(Employee.num_of_emps)
```

> Tips：
> - Class变量可以使用Instance(self)调用，也可以使用Class(Employee)调用（更灵活）；
> - `emp_1.raise_amount`会首先查找`emp_1.__dict__`有无`raise_amount`，没有的话，进一步查看`Employee.__dict__`,再进一步查看`Employee`的父类；
> - 通过类调用Class变量`Employee.num_of_emps`可以不受Instance的干扰；

上面讨论了`Instance Variable（实例变量）` and `Instance Method（实例方法）` 以及`Class Variable(类变量)`，那么，有没有`类方法`呢？

答案是肯定的，不光有，还有两个`“类方法”`,`Class Method`和`Static Method`。

 ## 类方法（`Class Method`和`Static Method`）

 先说说`Class Method`。。

 之前我们讨论过，`Instance Method`把自动把实例本身当做第一个参数（`self`）传入；类似的，`Class Method`则自动把`Class`当做第一个参数（`cls`）传入，同时增加`@classmethod`装饰器；

 > `class`已经被用来作为定义`类`的关键字，所以这里只能使用`cls`关键字了。

问题引入：上一章，我们通过`Employee.raise_amount = 1.05`来改变`Class Variable`；如果我们针对于`Class Variable`做更复杂的事情，难道也一行一行的实现？  

**问题**：如何更高效、简洁、优雅的对`类`的相关属性进行更复杂的操作？  
**答案**：Class Method

```python
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        """通过类方法修改工资涨幅"""
        cls.raise_amount = amount


emp_1 = Employee('John', 'Smith', 5000)
emp_2 = Employee('Keven', 'Love', 6000)

Employee.set_raise_amt(1.05)  # 同样，自动传入当前类名称给cls，只需传入amount一个参数；

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
```

貌似，为了所谓的“优雅”，只是改变个`raise_amount`，写了这么多东东，有点不值得！！

**更进一步**：那么让我们看新的应用场景：每次创建新的`Instance`都要传入`Employee('John', 'Smith', 5000)`三个参数，加入我们现在有一些字符串数据（`John-Smith-5000`），如何批量的生成`Instance`呢？

> 前一种情况称作`Using the normal constructor`，后一种情况叫做`Using the alternative constructor`。

```python
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def from_str(cls, emp_str):
        """接收字符串构造实例对象"""
        first_name, last_name, salary = emp_str.split('-')
        return cls(first_name, last_name, salary)


emp_str_1 = 'John-Smith-5000'
emp_str_2 = 'Keven-Love-6000'

emp_1 = Employee.from_str(emp_str_1)
emp_2 = Employee.from_str(emp_str_2)
print(emp_1.email)
print(emp_2.full_name())
```

> Tips：
> - 实例（`self`）可以调用类变量，同样，实例也可以调用`Class Method`（`emp_1.set_raise_amt(1.05)`）,只是我们很少这么用；
> - `datetime`模块的`fromtimestamp()`方法（传入时间戳作为参数而不是`datetime.date(2017,1,22)`创建datetime.date对象）便是通过`alternative constructor`实现的；

**引出`Static Method``**：  

- `Instance Method`自动传入Instance为第一个参数`self`；  
- `Class Method`自动传入Class为第一个参数`cls`；   
- `Static Method`并不会自动传入Instance或者Class，形式上和普通的函数类似；需要添加`@staticmethod`，使用类名称调用(如：`Employee.static_func()`)；
- `Static Method`使用场景：方法内部不需要`self` or `cls`。

```python
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @staticmethod
    def is_workday(day):
        """判断是否是工作日"""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime

my_date = datetime.datetime(2016, 9, 15)
print(Employee.is_workday(my_date))
```

## Inheritance（继承） - Subclass(子类)

引出问题：现在我们已经创建了Employee类了，但是现在我们需要 Developer、Manager类，难道我们重新定义`first_name, last_name, salary`这些属性？

> 注: 开发人员、管理人员，属于员工；

**问题**：定义子类时，如何避免重复代码？  
**答案**：Inheritance（继承）

```python
class Employee:
    raise_amt = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)
        self.salary = salary

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


class Developer(Employee):
    """定义继承与Employee类的Developer空类"""
    pass


dev_1 = Developer('John', 'Smith', 5000)
dev_2 = Developer('Keven', 'Love', 6000)

print(help(Developer))  # 可以查看继承关系
print(dev_1.salary)
dev_1.apply_raise()
print(dev_1.salary)
```

如上可知：Developer类虽然没有定义任何东西，由于其继承Employee类，可以使用Employee类定义的所有属性、方法；

引出问题：普通员工工作涨幅为1.04，开发、管理人员的工作涨幅应该高点吧！！？？

**问题**：除了继承父类的属性、方法外，子类如何实现覆盖父类特性、添加新特性？  
**答案**：polymorphism（多态）

```python
class Employee:
    raise_amt = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)
        self.salary = salary

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10  # 覆盖父类的工资涨幅

    def __init__(self, first_name, last_name, salary, program_lang):
        super(Developer, self).__init__(first_name, last_name, salary)  # 推荐这种写法
        # super().__init__(first_name, last_name, salary)  # 此法也可以
        # Employee.__init__(self, first_name, last_name, salary) # 不推荐这种写法
        self.program_lang = program_lang


class Manager(Employee):
    """定义管理员类，并添加一些特有方法"""
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.full_name())


dev_1 = Developer('John', 'Smith', 8000, 'Python')
dev_2 = Developer('Keven', 'Love', 9000, 'Java')

mgr_1 = Manager('Jacki', 'Alan', 1200, employees=[dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
```

> Tips：
> - 可以使用内置的函数`issubclass(Developer, Employee)`来判断类的继承关系；
> - Python中，所有类都是`object`类的子类，So，一切皆对象！！；
> - 可以使用内置函数`isinstance(mgr_1, Employee)`来判断实例和类的关系；
> - 类的继承特性在`Exception`模块体现的尤为突出，

## Special(Magic/Dunder) Method

> Dunder  = **D**ouble **under**line surround，即，所谓的魔术/特殊/Dunder方法其实就是`名称两边带双划线的方法`;比如上面常用的`__init__()`方法；

引出问题：

方法名称两边为啥加上双划线呢？书写时岂不是更复杂？因为这些方法我们`经常用` or `很少用`！！有没有更晕？哈哈！！

`很少用`可以理解，比如`__doc__, __dict__等`; `经常用`咋说呢？比如`__add__, __str__等`，不认识这些方法！？那`加号(+), print`你是不是经常用呢？`加号(+), print`本质上就是`__add__, __str__`，其他的`加减乘除..大于等于..len()/iter()/in/`都属于这一类。

> 类似上面的这种(把`int.__add__(1, 2)`简写为`1 + 2`)，让程序更加简洁，有更高的可读性的做法，有个学名：`语法糖（Syntactic sugar）`；装饰器也是`语法糖`哒！。

当你执行`a = 123`,内部其实执行`a = int(123)`,`int`是系统内置的`Class`，和我们上面自定义的`Employee`类似；即，`a`是`int`类的一个实例；

再者，执行`print(a)`命令，会打印`123`，其实内部执行的是`a.__str__()`（或者`str(a)`）,即，`int`类的`__str__()`方法；

系统的`int/str`类含有`__add__（+）`等方法，`str/list/tuple/dict`类含有`__len__(len()), __contains__(in), __iter__(iter) `等方法，这些方法允许我们执行`+, len(), print(), iter() in`等操作。

那么我们自定义的类`Employee`如何执行这些操作呢？

**问题**：如何让我们自定义的类可以执行`+, len(), print(), iter() in`等操作？  
**答案**：设置相应的`Magic Method`。

```python
class Employee:
    raise_amt = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)
        self.salary = salary

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.first_name, self.last_name, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('John', 'Smith', 8000)
emp_2 = Employee('Keven', 'Love', 9000)

print(emp_1)  # 不定义__str__, __repr__方法的话，打印结果是对象
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1 + emp_2)
print(len(emp_1))
```
> Tips:
> - `repr()` use for debugging和logging;  
> - `str()` display to end-user;  
> - print默认首先尝试调用`__str__`，没有定义的话调用`__repr__`;  

## Property Decorators - (Getters, Setters, and Deleters)

`@property`为内置装饰器，和普通的装饰器原理是一样的，只不过返回的不是函数，而是类对象。

在了解这个装饰器前，你需要知道在不使用装饰器怎么写一个属性:

```python
def getx(self):
    return self._x

def setx(self, value):
    self._x = value
    
def delx(self):
   del self._x

# create a property
x = property(getx, setx, delx, "I am doc for x property")
```
以上就是一个Python属性的标准写法，其实和Java挺像的，但是太罗嗦。有了@语法糖，能达到一样的效果但看起来更简单。

```python
@property
def x(self): ...

# 等同于

def x(self): ...
x = property(x)
```

属性有三个装饰器：`setter`, `getter`, `deleter` ，都是在`property()`的基础上做了一些封装，因为`setter`和`deleter`是`property()`的第二和第三个参数，不能直接套用@语法。`getter`装饰器和不带`getter`的属性装饰器效果是一样的，估计只是为了凑数，本身没有任何存在的意义。经过`@property`装饰过的函数返回的不再是一个函数，而是一个`property`对象。

```
>>> property()
<property object at 0x10ff07940>
```


我们首先看一段代码：

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}.{}@email.com'.format(self.first_name, self.last_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp_1 = Employee('John', 'Smith')
emp_1.first_name = 'Keener'  # 改变first_name为Keener

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.full_name())  # 注意是函数的调用
# 会打印出如下结果：
# ...Keener
# ...John.Smith@email.com
# ...Keener Smith
```

引出问题：上述代码中，当改变`Instance`的某个`Attribute`时，其他依托于此`Attribute`的属性会出现不同的变化。1、通过直接赋值（`self.email = ...`）得到的属性保持原值(`John.Smith@email.com`)；2、通过方法（`def full_name(self): ...`）得到的属性会自动变化(`Keener Smith`)。

实际应用中我们更希望第2种情况（自动改变），So，我们`self.email`也定义为`Method`岂不是就搞定了？ But，`email`属性的原来的调用是`emp_1.email`，修改为`def email: ...`之后的调用应该是`emp_1.email()`。

调用的API改变了，原来使用该属性的其他人都有做相应的改变，貌似不太好吧！！

> 程序设计原则：封闭 & 开放；所谓封闭=设计好的程序最好不要再去改动；所谓开放=在保证封闭原则的情况下，对程序功能进行扩展；`装饰器（Decorator）`便是一个极好的例子。

**问题**：如何在保证原有API不变的情况下，实现上述`Attribute`之间的联动？or，如何像调用属性一样调用方法？   
**答案**：`@property`（属性装饰器）

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp_1 = Employee('John', 'Smith')
emp_1.first_name = 'Keener'

print(emp_1.first_name)
print(emp_1.email)  # 像属性一样调用方法！！
print(emp_1.full_name)
# 会打印出如下结果：
# ...Keener
# ...Keener.Smith@email.com
# ...Keener Smith
```

> `@property`本质是装饰器，这里实现的原理为`email = email()`, `full_name = full_name()`。

如此，我们便可以像获取属性一样（`emp_1.email`），调用方法（`emp_1.email()`）了！

但是我们还不满足，上面我们改变`first_name`使用`emp_1.first_name = 'Keener'`,那么改变`last_name`也是类似，要想改变`full_name`需要分别改变`first_name` and `last_name`，能不能直接赋值改变呢？

注意，`emp_1.full_name`现在是方法哦！直接赋值的话，会报错：`AttributeError: can't set attribute`。

**问题**：如何直接对`间接属性(full_name)`进行赋值？   
**答案**：`@property`的基础上使用`@setter装饰器`

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name_str):
        first_name, last_name = full_name_str.split(' ')
        self.first_name = first_name
        self.last_name = last_name


emp_1 = Employee('John', 'Smith')
emp_1.full_name = 'Karl Derron'
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.full_name)
```

同样，我们可以定义`@full_name.deleter`装饰器，并使用`del`调用，如下：

```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name_str):
        first_name, last_name = full_name_str.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print('Del name!')
        self.first_name = None
        self.last_name = None


emp_1 = Employee('John', 'Smith')
emp_1.full_name = 'Karl Derron'
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.full_name)
del emp_1.full_name
print(emp_1.full_name)
```

哎╮(╯▽╰)╭，先到这里，有点困了，睡觉去！！ (～﹃～)~zZ
