#  黑魔法-上下文管理器contextor

## 1 所谓上下文

计算机上下文（Context）对于我而言，一直是一个很抽象的名词。就像`形而上`一样，经常听见有人说，但是无法和现实认知世界相结合。

最直观的上下文，莫过于小学的语文课，经常会问`联系上下文，推测...，回答...，表明作者...`。文章里的上下文比较好懂，无非就是`前`与`后`。

直到了解了计算机的执行状态，程式的运行，才稍微对计算机的上下文(context)有了一定的认识，多半还是只可意会，不可言传。本文所讨论的上下文，简而言之，就是程式所执行的环境状态，或者说程式运行的情景。

关于上下文的定义，我就不在多言，具体通过程式来理解。既然提及上下文，就不可避免的涉及Python中关于上下文的魔法，即上下文管理器（contextor）。

## 2 资源的创建和释放场景

上下文管理器的常用于一些资源的操作，需要在资源的获取与释放相关的操作，一个典型的例子就是数据库的连接，查询，关闭处理。先看如下一个例子：

```python
class Database(object):

    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def close(self):
        self.connected = False

    def query(self):
        if self.connected:
            return 'query data'
        else:
            raise ValueError('DB not connected ')
            
def handle_query():
    db = Database()
    db.connect()
    print 'handle --- ', db.query()
    db.close()

def main():
    handle_query()

if __name__ == '__main__':
    main()
```

上述的代码很简单，针对`Database`这个数据库类，提供了`connect` `query` 和`close` 三种常见的db交互接口。客户端的代码中，需要查询数据库并处理查询结果。当然这个操作之前，需要连接数据库（db.connect()）和操作之后关闭数据库连接（ db.close()）。上述的代码可以work，可是如果很多地方有类似handle_query的逻辑，连接和关闭这样的代码就得copy很多遍，显然不是一个优雅的设计。

对于这样的场景，在[python黑魔法---装饰器](https://www.jianshu.com/p/7e5466661744)中有讨论如何优雅的处理。下面使用装饰器进行改写如下：

```python
class Database(object):
    ...
    
def dbconn(fn):
    def wrapper(*args, **kwargs):
        db = Database()
        db.connect()
        ret = fn(db, *args, **kwargs)
        db.close()
        return ret
    return wrapper

@dbconn
def handle_query(db=None):
    print 'handle --- ', db.query()
    
def main():
    ...
```

编写一个dbconn的装饰器，然后在针对handle_query进行装饰即可。使用装饰器，复用了很多数据库连接和释放的代码逻辑，看起来不错。

装饰器解放了生产力。可是，每个装饰器都需要事先定义一下db的资源句柄，看起来略丑，不够优雅。

## 3 优雅的With as语句

Python提供了With语句语法，来构建对资源创建与释放的语法糖。给Database添加两个魔法方法：

```python
class Database(object):

    ...
    
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```

然后修改handle_query函数如下：

```python
def handle_query():
    with Database() as db:
        print 'handle ---', db.query()
```

在Database类实例的时候，使用with语句。一切正常work。比起装饰器的版本，虽然多写了一些字符，但是代码可读性变强了。

## 4 上下文管理协议

前面初略的提及了上下文，那什么又是上下文管理器呢？与[python黑魔法---迭代器](https://www.jianshu.com/p/dcf83643deeb)类似，实现了迭代协议的函数/对象即为迭代器。实现了上下文协议的函数/对象即为上下文管理器。

迭代器协议是实现了`__iter__`方法。上下文管理协议则是`__enter__`和`__exit__`。对于如下代码结构：

```python
class Contextor:
    def __enter__(self):
        pass
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

contextor = Contextor()

with contextor [as var]:
    with_body
```

`Contextor` 实现了`__enter__`和`__exit__`这两个上下文管理器协议，当Contextor调用/实例化的时候，则创建了上下文管理器`contextor`。类似于实现迭代器协议类调用生成迭代器一样。

配合with语句使用的时候，上下文管理器会自动调用`__enter__`方法，然后进入运行时上下文环境，如果有as 从句，返回自身或另一个与运行时上下文相关的对象，值赋值给var。当with_body执行完毕退出with语句块或者with_body代码块出现异常，则会自动执行`__exit__`方法，并且会把对于的异常参数传递进来。如果`__exit__`函数返回`True`。则with语句代码块不会显示的抛出异常，终止程序，如果返回None或者False，异常会被主动raise，并终止程序。

大致对with语句的执行原理总结[Python上下文管理器与with语句](https://link.jianshu.com?t=http://kuanghy.github.io/2015/08/08/python-with):

> 1. 执行 contextor 以获取上下文管理器
> 2. 加载上下文管理器的 **exit**() 方法以备稍后调用
> 3. 调用上下文管理器的 **enter**() 方法
> 4. 如果有 as var 从句，则将 **enter**() 方法的返回值赋给 var
> 5. 执行子代码块 with_body
> 6. 调用上下文管理器的 **exit**() 方法，如果 with_body 的退出是由异常引发的，那么该异常的 type、value 和 traceback 会作为参数传给 **exit**()，否则传三个 None
> 7. 如果 with_body 的退出由异常引发，并且 **exit**() 的返回值等于 False，那么这个异常将被重新引发一次；如果 **exit**() 的返回值等于 True，那么这个异常就被无视掉，继续执行后面的代码

了解了with语句和上下文管理协议，或许对上下文有了一个更清晰的认识。即代码或函数执行的时候，调用函数时候有一个环境，在不同的环境调用，有时候效果就不一样，这些不同的环境就是上下文。例如数据库连接之后创建了一个数据库交互的上下文，进入这个上下文，就能使用连接进行查询，执行完毕关闭连接退出交互环境。创建连接和释放连接都需要有一个共同的调用环境。不同的上下文，通常见于异步的代码中。

## 5 上下文管理器工具

通过实现上下文协议定义创建上下文管理器很方便，Python为了更优雅，还专门提供了一个模块用于实现更函数式的上下文管理器用法。

```python
import contextlib

@contextlib.contextmanager
def database():
    db = Database()
    try:
        if not db.connected:
            db.connect()
        yield db
    except Exception as e:
        db.close()

def handle_query():
    with database() as db:
        print 'handle ---', db.query()
```

使用contextlib 定义一个上下文管理器函数，通过with语句，database调用生成一个上下文管理器，然后调用函数隐式的`__enter__`方法，并将结果通yield返回。最后退出上下文环境的时候，在excepit代码块中执行了`__exit__`方法。当然我们可以手动模拟上述代码的执行的细节。

```python
In [1]: context = database()    # 创建上下文管理器

In [2]: context
<contextlib.GeneratorContextManager object at 0x107188f10>

In [3]: db = context.__enter__() # 进入with语句

In [4]: db                          # as语句，返回 Database实例
Out[4]: <__main__.Database at 0x107188a10>

In [5]: db.query()       
Out[5]: 'query data'

In [6]: db.connected
Out[6]: True

In [7]: db.__exit__(None, None, None)    # 退出with语句

In [8]: db
Out[8]: <__main__.Database at 0x107188a10>

In [9]: db.connected
Out[9]: False
```

## 6 上下文管理器的用法

既然了解了上下文协议和管理器，当然是运用到实践啦。通常需要切换上下文环境，往往是在多线程/进程这种编程模型。当然，单线程异步或者协程的当时，也容易出现函数的上下文环境经常变动。

异步式的代码经常在定义和运行时存在不同的上下文环境。此时就需要针对异步代码做上下文包裹的hack。看下面一个例子：

```python
import tornado.ioloop

ioloop = tornado.ioloop.IOLoop.instance()


def callback():
    print 'run callback'
    raise ValueError('except in callback')

def async_task():
    print 'run async task'
    ioloop.add_callback(callback=callback)

def main():

    try:
        async_task()
    except Exception as e:
        print 'exception {}'.format(e)
    print 'end'

main()
ioloop.start()

运行上述代码得到如下结果

run async task
end
run callback
ERROR:root:Exception in callback <tornado.stack_context._StackContextWrapper object at 0x1098cb7e0>
Traceback (most recent call last):
  ...
    raise ValueError('except in callback')
ValueError: except in callback
```

主函数中main中，定义了异步任务函数async_task的调用。async_task中异常，在except中很容易catch，可是callback中出现的异常，则无法捕捉。原因就是定义的时候上下文为当前的线程执行环境，而使用了tornado的ioloop.add_callback方法，注册了一个异步的调用。当callback异步执行的时候，他的上下文已经和async_task的上下文不一样了。因此在main的上下文，无法catch异步中callback的异常。

下面使用上下文管理器包装如下：

```python
class Contextor(object):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if all([exc_type, exc_val, exc_tb]):
            print 'handler except'
            print 'exception {}'.format(exc_val)
        return True

def main():
    with tornado.stack_context.StackContext(Contextor):
        async_task()
        
运行main之后的结果如下：

run async task
handler except
run callback
handler except
exception except in callback
```

可见，callback的函数的异常，在上下文管理器Contextor中被处理了，也就是说callback调用的时候，把之前main的上下文保存并传递给了callback。当然，上述的代码也可以改写如下：

```
@contextlib.contextmanager
def contextor():
    try:
        yield
    except Exception as e:
        print 'handler except'
        print 'exception {}'.format(e)
    finally:    
        print 'release'

def main():
    with tornado.stack_context.StackContext(contextor):
        async_task()
        
```

效果类似。当然，也许有人会对StackContext这个tornado的模块感到迷惑。其实他恰恰应用上下文管理器的魔法的典范。查看StackContext的源码，实现非常精秒，非常佩服tornado作者的编码设计能力。至于StackContext究竟如何神秘，已经超出了本篇的范围，将会在介绍[tonrado异步上下文管理器](https://www.jianshu.com/p/3e58f977b908)中介绍

 

 

 

 

 