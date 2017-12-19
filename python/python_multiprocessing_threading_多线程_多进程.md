# Python 多线程/多进程/协程 并发技术

本文只做简单的知识点记录，系统知识请google，或参考引用。

## 先上结论

### 该选用`多线程`还是`多进程`技术？

PC的处理的任务分为`计算密集型（CPU bound jobs）`和`IO密集型（I/O bound jobs）`；  

由于CPython解释器的GIL的存在，使得不管多少个CPU，任何Python程序再能同时运行一个Thread；

Python是脚本高级语言，优势在于更高效的解决问题；`计算密集型（CPU bound jobs）`任务使用低级语言（C等）更合适；

针对于`计算密集型（CPU bound jobs）`任务，多thread的python不会提速，反而更慢，多核CPU更甚； so，只能使用多process；进一步说，计算密集型任务应该使用低级语言（C等），Python本身效率就不高。Python的 Ctypes 第三方库可以突破GIL的限制，其实也就是引用了C语言。

针对于`IO密集型（I/O bound jobs）`任务，使用多thread和多process都可以实现并发；多thread占用资源更少，但是稳定性更差，无法使用多核CPU的优势；多process资源占用较多，但是更稳定；

SO，总结：对于Python来说，无论是`计算密集型（CPU bound jobs）`还是`IO密集型（I/O bound jobs）`选择多process永远没错。多process更稳定，虽然占用较多资源，但是你多核CPU不利用岂不是浪费？资源不够的话，还可以使用分布式啊（多thread不支持）。

BTW，协程（又称微线程，纤程。英文名Coroutine）技术现对于多thread更节约资源，协程技术+异步IO（多process）或许才是终极并发大杀器；当然协程技术在python中正在发展中，很多第三方库对协程的支持还不是特别好。  

参考：   
[**Python协程**](https://thief.one/2017/02/20/Python%E5%8D%8F%E7%A8%8B/)   
[**基于协程、异步IO的python爬虫**](https://ayonel.me/index.php/2017/05/17/coroutine_spider/)

### 并发技术的实现（Python库）

频繁创建/销毁process或者thread是非常消耗资源的，所以，**使用并发技术时，尽量选择线程池/进程池(pool)**。

Python早期有`threading`（`_thread`模块的包装）支持多线程；然后是`multiprocessing.dummy.Pool`（等同于`multiprocessing.pool.ThreadPool`）进一步包装`threading`；Python3.2+，又引入`concurrent.futures`库，对threading和multiprocessing的进一步抽象（包装）。

每一次抽象（包装）之后，提供的接口更加统一、简单、易用，当然灵活性会有一定的损失；比如，`concurrent.futures`库中的参数就一个max_workers，`ThreadPool/Pool`的API中有`processes, initializer，initargs，maxtasksperchild，context`等参数。

应该选择哪个？**这里推荐首选`concurrent.futures`，候选`multiprocessing.(dummy.)Pool`，二者多线程、多进程的API是一样的**，原因：越简单，出错概率越小！坚持使用API更简单的`concurrent.futures`是的项目更容易维护，性能基本上没有损失！！

参考：  
[concurrent.futures官网](https://docs.python.org/3.6/library/concurrent.futures.html)  
[python各线程/进程Pools性能测试](https://github.com/JohnStarich/python-pool-performance)  
[使用Python进行并发编程-PoolExecutor篇](http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-PoolExecutor%E7%AF%87/)  
[python-concurrency-Cheatsheet](https://www.pythonsheets.com/notes/python-concurrency.html)  
[futures-vs-multiprocessing](https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3)  
[fluent_Python-使用futures处理并发](http://forrestchang.com/wiki/15058857487655.html)  
[concurrent_futures介绍](http://nulls.cc/2017/09/01/python_concurrent_futures/)  

### concurrent.futures代码实例

以下演示多进程，多线程的API完全一样。

```python
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    """判断是否是质数"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:  # with语句保证及时关闭进程
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('{:d} is prime: {}'.format(number, prime))

if __name__ == '__main__':
    main()
```

> executor.map函数说明：如果函数调用引发了异常，那么那个异常也会从返回的迭代器抛出。对于非常长的迭代任务来说，比较大的chunksize值能加快速度(仅仅是使用ProcessPoolExecutor模块的情况，使用ThreadPoolExecutor的情况，chunksize没有任何用处)。
> 原文：When using ProcessPoolExecutor, this method chops iterables into a number of chunks which it submits to the pool as separate tasks. The (approximate) size of these chunks can be specified by setting chunksize to a positive integer. For very long iterables, using a large value for chunksize can significantly improve performance compared to the default size of 1. With ThreadPoolExecutor, chunksize has no effect.

### concurrent.futures和multiprocessing结构对比

```python
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor


def pool_main(primes, nprocs):
    # Let the executor divide the work among processes by using 'map'.
    with ProcessPoolExecutor(max_workers=nprocs) as executor:
        return {num: factors for num, factors in
                zip(primes,
                    executor.map(is_prime, primes))}


def mp_main(primes, nprocs):
    with mp.Pool(nprocs) as pool:
        return {num: factors for num, factors in
                zip(primes,
                    pool.map(is_prime, primes))}
```

## 为嘛使用多线程、多进程

答：提高效率，节约时间

## 先说说计算机组成

虽然计算机的发展很迅速，然而从整齐结构上而言其仍属于冯·诺依曼计算机的发展，冯·诺依曼计算机的特征有：

- 采用二进制数表示程序和数据；  
- 能存储程序和数据，并能自动控制程序的执行；  
- 具备运算器、控制器、存储器、输入设备和输出设备5个基本部分。  

![](http://upload-images.jianshu.io/upload_images/140958-d497a641f37ba2da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

计算机由硬件和软件两部分构成，只有硬件的计算机只能算裸机，硬件是筋骨，软件是灵魂。计算机的构成可以概括如下：

![](http://upload-images.jianshu.io/upload_images/140958-bb4852cbe9d21106.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

再说说CPU，CPU是一块超大规模的集成电路，是一台计算机的运算核心和控制核心。它的功能主要是解释计算机指令以及处理计算机软件中的数据。
中央处理器主要包括运算器和高速缓冲存储器及实现它们之间联系的数据、控制及状态的总线。它与内部存储器和输入/输出设备合称为电子计算机三大核心部件。

![](http://upload-images.jianshu.io/upload_images/140958-fc585abc592db325.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

**CPU的处理速度要远超过数据的读取速度，so， 如果单线程串行执行任务，CPU会过多等待，造成CPU的严重浪费！！正式因为这种效率的不对称，我们才需要并发（多线程、多进程）来充分利用CPU**

## 什么是线程、进程？

参考：https://sites.google.com/site/sureshdevang/thread-vs-process

- 进程是资源分配单位，线程是CPU调度单位；
- 进程 = 线程 + 共享资源；
- 进程拥有完整的资源平台，线程只独享必不可少的资源（寄存器、栈）；
- 进程和线程都具有：就绪、阻塞和执行三种基本状态，状态之间可以转换；
- 线程之间共享内存、文件等资源，线程创建、状态转换、终止消耗时间更短；
- 线程之间通讯可以不经过内核；
- 线程优点：线程创建、状态转换、终止时间更短，消耗资源更少；
- 线程缺点：一个线程崩溃，会导致所属进程的所有线程都崩溃；
- 进程优点：稳定，进程是一个完整的平台，进程之间相互隔离；
- 进程缺点：消耗时间、资源更多；

单线程和多线程对比图

![单线程和多线程对比图](https://applied-programming.github.io/Operating-Systems-Notes/images/processvthread.png)

![单线程和多线程对比图](http://www.pling.org.uk/cs/opsimg/threadmodel.png)

## python使用多线程还是多进程呢？

上面已经说过，多线程的开销比多进程开销更少，而且多进程之间的通讯也比较麻烦；

那么我们就选择多线程？ 非也！！ 请了解下python(其实是实现CPython解释器引入)的 [GIL](https://wiki.python.org/moin/GlobalInterpreterLock)（Global Interpreter Lock）；

GIL简单来说，就是：CPython的内存管理是线程不安全的（not thread-safe），所以通过GIL将线程序列化，阻止原生多线程执行Python字节码，顺便也干死了Python的多线程！！

```python
from threading import Thread

def test():  # 创建死循环函数
    i = 0
    while True:
        i += 1

for _ in range(8):  # 创建了8个线程，电脑是8核的
    t = Thread(target=test)
    t.start()
```

上面代码开启了8个线程，运行之后，理论上CPU使用率应该在800%，你会发现CPU使用率也只是100%左右。如下图：

![](https://i.loli.net/2017/12/16/5a348c26b29f3.png)

## 协程

参考：[基于协程、异步IO的python爬虫](https://ayonel.me/index.php/2017/05/17/coroutine_spider/)
参考：https://thief.one/2017/02/20/Python%E5%8D%8F%E7%A8%8B/

## GIL既然阻止多线程，难道Python多线程无用？

非也！！ 

- 计算机内部的任务无非是 I/O（IO bound jobs） 或者 计算（CPU bound jobs ），**多线程在I/O密集型的jobs上还是有很大效果的**。I/O密集型的jobs执行时序图如下：

![](https://i.loli.net/2017/12/16/5a349164946cc.png)

> 解释如下：当Thread1执行时遇到I/O时，GIL会释放，此时的Thread1等待I/O（速度相对于CPU处理速度慢很多），Thread2会执行获得GIL，以此类推。。。其实就是：下一个线程有效的利用了上一个线程的I/O的时间。如此**线程伪并发**相对与单线程效率还是高很多！！

- 在CPU密集型任务（CPU bound jobs），Python的多线程相对于单线程不仅不会提升效率，还会失效率下降（线程的创建、转换、结束浪费效率）！

- 退一步讲，Python这种高级脚本语言本身的运行效率就很低，CPU bound jobs 使用计算机低级语言（C语言等）效果会更好。

## 在Python中如何处理CPU密集型的任务呢

方法1： 使用 Ctypes 第三方库，Ctypes可以绕过GIL的限制，提升多线程的执行效率；但是并不是所有人都精通C语言，尤其C语言还是不太安全的语言；不会C语言，咋整？
方法2：Python自带了 multiprocessing 库（多进程）

代码如下：

```python
from multiprocessing import Process


def test():
    i = 0
    while True:
        i += 1


for _ in range(8):  # 开启8个进程
    p = Process(target=test)
    p.start()
```

运行如上多进程代码后CPU使用率为800%，截图如下：

![](https://i.loli.net/2017/12/16/5a3498ba37a03.png)

## python中多进程、多线程相关的库

Python标准库为我们提供了threading和multiprocessing模块编写相应的多线程/多进程代码，但是当项目达到一定的规模，频繁创建/销毁进程或者线程是非常消耗资源的，这个时候我们就要编写自己的线程池/进程池，以空间换时间。

Python提供的并发编程库如下：

- threading库： 多线程库，是 _thread 库的进一步封装  
- multiprocessing库： 多线程库  
- multiprocessing.Pool： 多进程库Pool  
- multiprocessing.pool.ThreadPool： 多线程库Pool（和multiprocessing.Pool具有相同的API），  
- multiprocessing.dummy.Pool：等同于 multiprocessing.pool.ThreadPool（别名而已）  
- concurrent.futures库： Python3.2+支持，实现了对threading和multiprocessing的进一步抽象  
- 使用map时，future是逐个迭代提交，multiprocessing.Pool是批量提交jobs，因此对于大批量jobs的处理，multiprocessing.Pool效率会更高一些。对于需要长时间运行的作业，用future更佳，future提供了更多的功能（callback, check status, cancel）。

## 并发-多线程

参考：https://juejin.im/post/5845134da22b9d006c2959c3  
参考：https://tracholar.github.io/wiki/python/python-multiprocessing-tutorial.html

## 并发-多进程

参考：https://juejin.im/post/5847853661ff4b006c431c64

## concurrent.futures库

参考：https://www.ziwenxie.site/2016/12/24/python-concurrent-futures/  
参考：https://www.ziwenxie.site/2016/12/19/python-asyncio/  
参考：http://www.cnblogs.com/dylan-wu/p/7163823.html
参考：http://lovesoo.org/analysis-of-asynchronous-concurrent-python-module-concurrent-futures.html


- Executor和Future

concurrent.futures模块的基础是Exectuor，Executor是一个抽象类，它不能被直接使用。但是它提供的两个子类ThreadPoolExecutor和ProcessPoolExecutor却是非常有用，顾名思义两者分别被用来创建线程池和进程池的代码。我们可以将相应的tasks直接放入线程池/进程池，不需要维护Queue来操心死锁的问题，线程池/进程池会自动帮我们调度。



## 具体项目使用多线程 or 多进程？

- IO bound jobs -> multiprocessing.pool.ThreadPool（等同于 multiprocessing.dummy.Pool）  
- CPU bound jobs -> multiprocessing.Pool  
- Hybrid jobs -> depends on the workload, I usually prefer the multiprocessing.Pool due to the advantage process isolation brings


## 踩过的坑

- join()的正确使用

```python
# 正确用法：
threads = []
for i in range(8):
    down = Downloader(queue)
    threads.append(down)
    down.start()
for t in threads:
    t.join()

# 错误用法：
# 主线程会被阻塞，按照单线程在运行
for x in range(8):
    down = Downloader(queue)
    down.start()
    down.join()
```

- File discripter

在Linux内，对所有设备or文件的操作都是通过文件描述符进行的；  
使用多进程时，python在linux平台上，通过主进程 fork() 出各个子进程（Windows压根没有fork，所有没有这个问题）；这些子进程会继承父进程的文件描述符（文件位置、文件偏移量、设备状态等）；当子进程执行操作（比如：访问日志文件），会父进程的文件偏移量上继续操作，这显然是不合理的。

```python
# 错误用法：
from mutiprocessing import Pool
pool = Pool()
pool.map(do_monitor, inst_list)

# 正确用法：
# 当生成一个进程（池）的时候，立刻对其初始化；该重新连接数据库，就重新连接；该重新打开日志文件，就重新打开；
# 可以避免一些莫名其妙的错误
from mutiprocessing import Pool

def pool_initialize(*args):
    from django_cassandra_engine.models import cassandra_connection
    from services.base import write_pid_file

    write_pid_file('alert_service')
    if cassandra_connection is not None:
        cassandra_connection.reconnct()

pool = Pool(None, pool_initialize)
pool.map(do_monitor, inst_list)

```

