# Python Concurrency并发编程全解析

## 1 并行/并发 异步/同步 阻塞/非阻塞区别

### 1.1 并发与并行

- 并发: 仅仅包含宏观上的意义，即多个任务同时被处理；而微观上可能仅仅是一个cpu分时间片去完成了多个任务，这个时候多个任务是被顺序处理的。
- 并行: 则更加严格，在宏观和微观上都应该具有多个任务同时被处理的含义，这个意义上多个任务被并行处理的，单cpu永远不可能并行。

- 并行和并发是站在两个不同角度上理解产生的概念。
- 并行一定是并发，并发却不一定是并行。

### 1.2 同步与异步

- 同步: 任务的执行过程是顺序的。
- 异步: 事情的执行过程不是线性的。

- 异步和同步是从任务被执行的顺序上来区分的，从这个基本概念出发，异步并不见得比同步性能高，也就是说异步模型不见得会比同步模型有优势。
- 而异步和同步这个概念却非常容易和阻塞与非阻塞混淆，因为任何一个任务理论上都不可能瞬间完成，而现实中的任务通常都需要与其他系统交互，因此可能被阻塞是不可避免的。
- 异步通常给人一个错觉，就是他比同步快。这里其实是有一个误区，因为一个任务实际被处理的时间并没有太大变化，只有在带阻塞的任务中，异步才可能比同步快，因为异步快在将同步模式下带阻塞任务执行过程中cpu的等待时间利用起来处理其他任务，借此提升了多任务系统的整体并发能力，可见，一个任务的异步不一定比同步快，同时，对于处理不阻塞的任务，异步模型也不会比同步模型快。

### 1.3 阻塞与非阻塞

- 阻塞: 任务的执行会使cpu进入等待状态。
- 非阻塞:  任务的执行不会主动让cpu进行等待。

- 阻塞不阻塞的原始语义实际上是看任务在宏观执行过程中对cpu的主动占用情况是否连续来区分的。
- 不考虑cpu时间片耗尽被重新调度或者其他干扰导致被抢占的情况下，非阻塞的任务在获得cpu后将一直执行到完成。
- 阻塞或非阻塞的任务与阻塞或非阻塞的接口是有区别的：前者隐含一个前提就是必须是任务执行从开始到结束的整个过程，而后者不用关心任务是否完整完成，仅仅关心当前这一步操作是否会阻塞。

### 1.4 开发中的现状

- 部分业务都可能阻塞(网络IO，文件IO)，常见的网络收发，数据库操作等，因此在追求海量高性能的server开发中很较少用到同步模型，这也是为什么我们潜意识里会觉得同步模型慢且容易与阻塞纠缠不清的原因 — 计算机世界的任务模型原本大多是阻塞任务。
- 开发中大多是将带阻塞的任务分解成多个不阻塞的部分（这就是异步模型中所谓的分割点），只有在这样的前提下配合异步模型才能大幅提升系统的并发能力，这就是为什么在高性能server开发中异步与非阻塞通常被混为一谈的原因 — 计算机处理海量任务只有这样才能整体最快。
- server业务，肯定提倡使用异步模型。但异步模型对开发者并不友好，因为人类的思维习惯是线性分析事务，这就是为什么大部分开发者愿意使用同步模型的原因 — 人类看待事物的习惯本就带有顺序性。

## 2 PC及操作系统基本概念

### 2.1 PC基础脑补

虽然计算机的发展很迅速，然而从整齐结构上而言其仍属于冯·诺依曼计算机的发展，冯·诺依曼计算机的特征有：

- 采用二进制数表示程序和数据；  
- 能存储程序和数据，并能自动控制程序的执行；  
- 具备运算器、控制器、存储器、输入设备和输出设备5个基本部分。  

![](http://upload-images.jianshu.io/upload_images/140958-d497a641f37ba2da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

计算机由硬件和软件两部分构成，只有硬件的计算机只能算裸机，硬件是筋骨，软件是灵魂。计算机的构成可以概括如下：



![](http://upload-images.jianshu.io/upload_images/140958-bb4852cbe9d21106.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

对于计算机的设计者来说，计算机系统划分成很多层，每一层都执行特定的指令集来完成特定的功能，具体如下图。

![](https://pic2.zhimg.com/80/33bb4dd4aacc777bd6e2ac06f99657a5_hd.jpg)

再说说CPU，CPU是一块超大规模的集成电路，是一台计算机的运算核心和控制核心。它的功能主要是解释计算机指令以及处理计算机软件中的数据。
中央处理器主要包括运算器和高速缓冲存储器及实现它们之间联系的数据、控制及状态的总线。它与内部存储器和输入/输出设备合称为电子计算机三大核心部件，CPU的工作原理概括如下：

 

![img](http://blog.chinaunix.net/attachment/201304/6/23069658_1365263161V4M0.jpg)

OK，总结一下，CPU的运行原理就是**：控制单元在时序脉冲的作用下，将指令计数器里所指向的指令地址(这个地址是在内存里的)送到地址总线上去，然后CPU将这个地址里的指令读到指令寄存器进行译码。对于执行指令过程中所需要用到的数据，会将数据地址也送到地址总线，然后CPU把数据读到CPU的内部存储单元(就是内部寄存器)暂存起来，最后命令运算单元对数据进行处理加工。周而复始，一直这样执行下去，天荒地老，海枯枝烂，直到停电。**       如果你对这段话还是觉得比较晕乎，那么就看我们老师是怎么讲的：
   1、**取指令：CPU的控制器从内存读取一条指令并放入指令寄存器。指令的格式一般是这个样子滴：**

 

![img](http://blog.chinaunix.net/attachment/201304/3/23069658_13649999376WN1.jpg)

​        操作码就是汇编语言里的mov,add,jmp**等符号码；操作数地址说明该指令需要的操作数所在的地方，是在内存里还是在CPU的内部寄存器里。   2、指令译码：指令寄存器中的指令经过译码，决定该指令应进行何种操作(就是指令里的操作码)、操作数在哪里(操作数的地址)。   3、 执行指令，分两个阶段“取操作数”和“进行运算”。   4、 修改指令计数器，决定下一条指令的地址。**

![img](http://blog.chinaunix.net/attachment/201304/3/23069658_1364999970ofpV.jpg)

​       关于CPU我们从宏观上把握到这个程度就OK了，后面我们会逐步进入微观阶段，依次介绍80X86寄存器及其用途，NASM汇编和AT&T的区别，以及C代码中嵌入的汇编语言的写法。之所以介绍汇编语言目的不是说用汇编去写代码，那是相当的不现实，除非你是硬件驱动工程师。稍微偏上层一点的开发人员懂点低等的东西，对自己理解整个系统的架构和原理是相当有好处的。

> **CPU的处理速度要远超过数据的读取速度，so， 如果单线程串行执行任务，CPU会过多等待，造成CPU的严重浪费！！正式因为这种效率的不对称，我们才需要并发（线程/进程/协程）来充分利用CPU**

### 2.2 为什么要有操作系统？

  现代计算机系统是由一个或者多个处理器，主存，磁盘，打印机，键盘，鼠标显示器，网络接口以及各种其他输入输出设备组成的复杂系统，每位程序员不可能掌握所有系统实现的细节，并且管理优化这些部件是一件挑战性极强的工作。所以，我们需要为计算机安装一层软件，成为操作系统，任务就是用户程序提供一个简单清晰的计算机模型，并管理以上所有设备。

   定义也就有了：操作系统是一个用来协调、管理和控制计算机硬件和软件资源的系统程序，它位于硬件和应用程序之间。

（程序是运行在系统上的具有某种功能的软件，比如说浏览器，音乐播放器等。）

> 操作系统的内核的定义：操作系统的内核是一个管理和控制程序，负责管理计算机的所有物理资源，其中包括：文件系统、内存管理、设备管理和进程管理。

### 2.3 操作系统历史

- 1 真空管与穿孔卡片（无操作系统）

```
过程：
    万能程序员们将对应于程序和数据的已穿孔的纸带（或卡片）装入输入机，然后启动输入机把程序和数据输入计算机内存，接着通过控制台开关启动程序针对数据运行；计算完毕，打印机输出计算结果；用户取走结果并卸下纸带（或卡片）后，才让下一个用户上机。

注意点：
	程序员需要在墙上的计时表上预约时间，同一时刻只有一个程序在内存中被CPU调用运行（串行的）

优缺点：
    优点：程序员在申请的时间段内独享整个资源，即时的调试自己的程序，如果有bug可以当场处理，
    缺点：这对于计算机提供商来说是一种浪费（你买一台电脑4000块，那 一年中你用365比只用1天，肯定是省成本的，物尽其用）
```

       ![img](https://images2015.cnblogs.com/blog/877318/201701/877318-20170113100848431-2086362901.png)

- 2 晶体管和批处理系统

```
一代计算机的问题：

    人机交互太多了（输入--->计算--->输出  输入--->计算--->输出 输入--->计算--->输出 ）

    解决办法：
        把一堆人的输入攒成一大波输入，然后顺序计算（这是有问题的，但是第二代计算没有解决）再把计算结果攒成一大波输出，这就是批处理系统


    操作系统前身：

    在收集了大约一个小时的批量作业之后，这些卡片被读入磁带，然后磁带被送到机房里并装到磁带上。然后磁带被送到机房里并装到磁带机上。随后，操作员装入一个特殊的程序（此乃现代操作系统的前身），它负责从磁带上读入第一个作业（job，一个或一组程序）并运行，其输出写到第二个磁带上，而且不打印。每个作业结束后，操作系统自动的从磁带上读入下一个作业并且运行。当一整批的作业全部结束后，操作员去下输入和输出磁带，讲输入磁带换成下一批作业，并且把输出磁带拿到一台1041机器上进行脱机（不与主计算机联机）打印

    优点：批处理
    缺点： 1 图的中间还有俩小人  2 仍然是顺序计算
```

 ![img](https://images2015.cnblogs.com/blog/877318/201701/877318-20170113101115900-1890806151.png)

- 3 集成电路芯片和多道程序设计

```
针对二代计算机的两个主要问题

    开发出SPOOLING技术：
    卡片被拿到机房后能够很快的将作业从卡片读入磁盘，于是任何时刻当一个作业结束时，操作系统就能将一个作业从磁带读出，装进空出啦的内存区域运行，这种技术叫做同时的外部设备联机操作：SPOOLING该技术同时用于输出。当采用了这种技术后，就不在需要IBM1401机了，也不必将磁带搬来搬去了（中间俩小人失业了），强化了操作系统的功能

    开发出多道程序设计，用于解决顺序执行的问题：

    在7094机上（程序运行的机器），若当前作业因等待磁带或等待其他IO操作而暂停，CPU就处于休闲状态直至IO操作完成，对于CPU密集的科学计算，IO操作少，浪费时间不明显，对于商业数据处理，IO等待能到达80%～90%，所以必须解决CPU浪费的现象。

    解决方案：将内存分为几个部分，每一部分存放不同的作业，如图1-5所示。当一个作业等待IO完成时，另一个作业可以使用CPU，内存中放足够的作业，则CPU的利用率能接近100%

    此时的第三代计算机适合大型科学计算和繁忙的商务数据处理，但，本质上其仍是一个批处理系统。
    虽然解决了诸如以上问题，但多个作业必须在全部运行结束后，才能得到结果，从一个作业的提交到运算结果取回往往长达数小时。
    想象一个场景：A君 B君 C君 三个程序员同时在调试程序，一旦A君写错一个逗号，那么可能需要半天的时间才能看到结果，因为B君C君的结果也同时运算出来了。时间必然要长。一言以蔽之：大家一起存作业，大家一起去数据（磁带）

    许多程序员怀念第一代独享的计算机，可以即时调试自己的程序。为了满足程序员们很快可以得到响应，出现了分时操作系统
    
    分时操作系统：多个联机终端+多道技术

    20个客户端同时加载到内存，有17在思考，3个在运行，cpu就采用多道的方式处理内存中的这3个程序，由于客户提交的一般都是简短的指令而且很少有耗时长的，索引计算机能够为许多用户提供快速的交互式服务，所有的用户都以为自己独享了计算机资源
```

- 4 个人计算机

​      随着大规模集成电路的发展，每平方厘米的硅片芯片上可以集成数千个晶体管，个人计算机的时代就此到来。

## 3 进程和线程

### 3.1 二者的区别

参考：[thread-vs-process](https://sites.google.com/site/sureshdevang/thread-vs-process)   

- 进程是**资源分配单位**，线程是**CPU调度单位**；
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

### 3.2 python的GIL

In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe. (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)

上面的核心意思就是，**无论你启多少个线程，你有多少个cpu, Python在执行的时候会淡定的在同一时刻只允许一个线程运行。GIL简单来说，就是：CPython的内存管理是线程不安全的（not thread-safe），所以通过GIL将线程序列化，阻止原生多线程执行Python字节码，顺便也干死了Python的多线程！！**



### 3.3 python多线程毫无意义？

非也！！ 

- 计算机内部的任务无非是 I/O（IO bound jobs） 或者 计算（CPU bound jobs ），**多线程在I/O密集型的jobs上还是有很大效果的**。I/O密集型的jobs执行时序图如下：

![](https://i.loli.net/2017/12/16/5a349164946cc.png)

> 解释如下：当Thread1执行时遇到I/O时，GIL会释放，此时的Thread1等待I/O（速度相对于CPU处理速度慢很多），Thread2会执行获得GIL，以此类推。。。其实就是：下一个线程有效的利用了上一个线程的I/O的时间。如此**线程伪并发**相对与单线程效率还是高很多！！

- 在CPU密集型任务（CPU bound jobs），Python的多线程相对于单线程不仅不会提升效率，还会失效率下降（线程的创建、转换、结束浪费效率）！
- 退一步讲，Python这种高级脚本语言本身的运行效率就很低，CPU bound jobs 使用计算机低级语言（C语言等）效果会更好。



### 3.3 多线程/进程的选择

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

### 3.4 Python如何处理CPU密集型的任务呢？

> 首先建议使用其他低级语言（c）来处理cpu密集型任务；工程师大部分工作中遇到的都是I/O密集型任务；科学家遇到的CPU密集型任务较多。

方法1：使用 Ctypes 第三方库，Ctypes可以绕过GIL的限制，提升多线程的执行效率；但是并不是所有人都精通C语言，尤其C语言还是不太安全的语言；不会C语言，咋整？    
方法2：不使用CPython解释器，换其他的Python解释器；  
方法3：Python自带了 multiprocessing 库（多进程）；    

multiprocessing库实现多进程代码如下：

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

## 4 Python并发相关库

Python标准库为我们提供了threading和multiprocessing模块编写相应的多线程/多进程代码，但是当项目达到一定的规模，频繁创建/销毁进程或者线程是非常消耗资源的，这个时候我们就要编写自己的线程池/进程池，以空间换时间。

Python提供的并发编程库如下：

- **threading库**： 多线程库，是 _thread 库的进一步封装  
- **multiprocessing库**： 多线程库  
- **multiprocessing.Pool**： 多进程库Pool  
- multiprocessing.pool.ThreadPool： 多线程库Pool（和multiprocessing.Pool具有相同的API），  
- multiprocessing.dummy.Pool：等同于 multiprocessing.pool.ThreadPool（别名而已）  
- **concurrent.futures库**： Python3.2+支持，实现了对threading和multiprocessing的进一步抽象  

> 使用map方法时，future库是逐个迭代提交，multiprocessing.Pool是批量提交jobs，因此对于大批量jobs的处理，multiprocessing.Pool效率会更高一些。对于需要长时间运行的作业，用future更佳，future提供了更多的功能（callback, check status, cancel）。

频繁创建/销毁process或者thread是非常消耗资源的，所以，**使用并发技术时，尽量选择线程池/进程池(pool)**。

Python早期有`threading`（`_thread`模块的包装）支持多线程,`multiprocessing`支持多进程；然后是`multiprocessing.dummy.Pool`（等同于`multiprocessing.pool.ThreadPool`）进一步包装`threading`，`multiprocessing`同时支持多线程和多进程，而且API相同；Python3.2+，又引入`concurrent.futures`库，对threading和multiprocessing的进一步抽象（包装）。

每一次抽象（包装）之后，提供的接口更加统一、简单、易用，当然灵活性会有一定的损失；比如，`concurrent.futures`库中的参数就一个max_workers，`ThreadPool/Pool`的API中有`processes, initializer，initargs，maxtasksperchild，context`等参数。

应该选择哪个？**这里推荐首选`concurrent.futures`，候选`multiprocessing.(dummy.)Pool`，二者多线程、多进程的API是一样的**； 选择的原因：越简单，出错概率越小！坚持使用API更简单的`concurrent.futures`是的项目更容易维护，性能基本上没有损失！！

参考：  
[concurrent.futures官网](https://docs.python.org/3.6/library/concurrent.futures.html)  
[python各线程/进程Pools性能测试](https://github.com/JohnStarich/python-pool-performance)  
[使用Python进行并发编程-PoolExecutor篇](http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-PoolExecutor%E7%AF%87/)  
[python-concurrency-Cheatsheet](https://www.pythonsheets.com/notes/python-concurrency.html)  
[futures-vs-multiprocessing](https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3)  
[fluent_Python-使用futures处理并发](http://forrestchang.com/wiki/15058857487655.html)  
[concurrent_futures介绍](http://nulls.cc/2017/09/01/python_concurrent_futures/)  



## 5 threading线程模块

### 5.1 线程的两种调用方式

​      threading 模块建立在thread 模块之上。thread模块以低级、原始的方式来处理和控制线程，而threading 模块通过对thread进行二次封装，

提供了更方便的api来处理线程。

**直接调用：**

```python
import threading
import time
 
def sayhi(num): #定义每个线程要运行的函数
 
    print("running on number:%s" %num)
 
    time.sleep(3)
 
if __name__ == '__main__':
 
    t1 = threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例
    t2 = threading.Thread(target=sayhi,args=(2,)) #生成另一个线程实例
 
    t1.start() #启动线程
    t2.start() #启动另一个线程
 
    print(t1.getName()) #获取线程名
    print(t2.getName())
```

**继承式调用：**

```python
import threading
import time


class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):#定义每个线程要运行的函数

        print("running on number:%s" %self.num)

        time.sleep(3)

if __name__ == '__main__':

    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    
    print("ending......")
```

### 5.2 threading.thread的实例方法

#### 5.2.1 join&Daemon方法

```python
import threading
from time import ctime,sleep
import time

def ListenMusic(name):

        print ("Begin listening to %s. %s" %(name,ctime()))
        sleep(3)
        print("end listening %s"%ctime())

def RecordBlog(title):

        print ("Begin recording the %s! %s" %(title,ctime()))
        sleep(5)
        print('end recording %s'%ctime())


threads = []


t1 = threading.Thread(target=ListenMusic,args=('水手',))
t2 = threading.Thread(target=RecordBlog,args=('python线程',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        #t.setDaemon(True) #注意:一定在start之前设置
        t.start()
        # t.join()
    # t1.join()
    t1.setDaemon(True)

    #t2.join()########考虑这三种join位置下的结果？
    print ("all over %s" %ctime())
```

join()：在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

setDaemon(True)：

​         将线程声明为守护线程，必须在start() 方法调用之前设置， 如果不设置为守护线程程序会被无限挂起。这个方法基本和join是相反的。

​         当我们 在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程 就分兵两路，分别运行，那么当主线程完成

​         想退出时，会检验子线程是否完成。如 果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是 只要主线程

​         完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法啦

#### 5.2.2 其它方法

```python
# run():  线程被cpu调度后自动执行线程对象的run方法
# start():启动线程活动。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

threading模块提供的一些方法：
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
```

### 5.3 同步锁(Lock)

```python
import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    #num-=1

    temp=num
    #print('--get num:',num )
    time.sleep(0.1)
    num =temp-1 #对此公共变量进行-1操作

num = 100  #设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )
```

![img](https://images2015.cnblogs.com/blog/877318/201701/877318-20170113104541525-1204673742.png)

 

**观察：time.sleep(0.1)  /0.001/0.0000001 结果分别是多少？**

多个线程都在同时操作同一个共享资源，所以造成了资源破坏，怎么办呢？(join会造成串行，失去所线程的意义)

我们可以通过同步锁来解决这种问题

```python
R=threading.Lock()
 
####
def sub():
    global num
    R.acquire()
    temp=num-1
    time.sleep(0.1)
    num=temp
    R.release()
```

### 5.4 线程死锁和递归锁

在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁，因为系统判断这部分资源都正在使用，所有这两个线程在无外力作用下将一直等待下去。下面是一个死锁的例子：

```python
import threading,time

class myThread(threading.Thread):
    def doA(self):
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        lockA.release()
        lockB.release()

    def run(self):
        self.doA()
        self.doB()
if __name__=="__main__":

    lockA=threading.Lock()
    lockB=threading.Lock()
    threads=[]
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()#等待线程结束，后面再讲。
```

解决办法：使用递归锁，将

```python
lockA=threading.Lock()
lockB=threading.Lock()<br>#--------------<br>lock=threading.RLock()
```

为了支持在同一线程中多次请求同一资源，python提供了“可重入锁”：threading.RLock。RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次acquire。直到一个线程所有的acquire都被release，其他的线程才能获得资源。

**应用**

```python
import time

import threading

class Account:
    def __init__(self, _id, balance):
        self.id = _id
        self.balance = balance
        self.lock = threading.RLock()

    def withdraw(self, amount):

        with self.lock:
            self.balance -= amount

    def deposit(self, amount):
        with self.lock:
            self.balance += amount


    def drawcash(self, amount):#lock.acquire中嵌套lock.acquire的场景

        with self.lock:
            interest=0.05
            count=amount+amount*interest

            self.withdraw(count)


def transfer(_from, to, amount):

    #锁不可以加在这里 因为其他的其它线程执行的其它方法在不加锁的情况下数据同样是不安全的
     _from.withdraw(amount)

     to.deposit(amount)


alex = Account('alex',1000)
yuan = Account('yuan',1000)

t1=threading.Thread(target = transfer, args = (alex,yuan, 100))
t1.start()

t2=threading.Thread(target = transfer, args = (yuan,alex, 200))
t2.start()

t1.join()
t2.join()

print('>>>',alex.balance)
print('>>>',yuan.balance)
```

### 5.5 同步条件(Event)

An event is a simple synchronization object;the event represents an internal flag,

and threads can wait for the flag to be set, or set or clear the flag themselves.

event = threading.Event()
\# a client thread can wait for the flag to be set
event.wait()
\# a server thread can set or reset it
event.set()
event.clear()

If the flag is set, the wait method doesn’t do anything.
If the flag is cleared, wait will block until it becomes set again.
Any number of threads may wait for the same event.

```python
import threading,time
class Boss(threading.Thread):
    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        print(event.isSet())
        event.set()
        time.sleep(5)
        print("BOSS：<22:00>可以下班了。")
        print(event.isSet())
        event.set()
class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker：哎……命苦啊！")
        time.sleep(1)
        event.clear()
        event.wait()
        print("Worker：OhYeah!")
if __name__=="__main__":
    event=threading.Event()
    threads=[]
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
```

### 5.6 信号量(Semaphore)

​      信号量用来控制线程并发数的，BoundedSemaphore或Semaphore管理一个内置的计数 器，每当调用acquire()时-1，调用release()时+1。

​      计数器不能小于0，当计数器为 0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。(类似于停车位的概念)

​      BoundedSemaphore与Semaphore的唯一区别在于前者将在调用release()时检查计数 器的值是否超过了计数器的初始值，如果超过了将抛出一个异常。

```python
import threading,time
class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()
if __name__=="__main__":
    semaphore=threading.Semaphore(5)
    thrs=[]
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()
```

### 5.7 多线程利器－队列(queue)

#### 5.7.1 列表是不安全的数据结构

```python
import threading,time

li=[1,2,3,4,5]

def pri():
    while li:
        a=li[-1]
        print(a)
        time.sleep(1)
        try:
            li.remove(a)
        except Exception as e:
            print('----',a,e)

t1=threading.Thread(target=pri,args=())
t1.start()
t2=threading.Thread(target=pri,args=())
t2.start()
```

**思考：如何通过对列来完成上述功能？**

queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.

#### 5.7.2 queue列队类的方法

```python
创建一个“队列”对象
import Queue
q = Queue.Queue(maxsize = 10)
Queue.Queue类即是一个队列的同步实现。队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。

将一个值放入队列中
q.put(10)
调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为
1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。

将一个值从队列中取出
q.get()
调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，
get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。

Python Queue模块有三种队列及构造函数:
1、Python Queue模块的FIFO队列先进先出。   class queue.Queue(maxsize)
2、LIFO类似于堆，即先进后出。               class queue.LifoQueue(maxsize)
3、还有一种是优先级队列级别越低越先出来。        class queue.PriorityQueue(maxsize)

此包中的常用方法(q = Queue.Queue()):
q.qsize() 返回队列的大小
q.empty() 如果队列为空，返回True,反之False
q.full() 如果队列满了，返回True,反之False
q.full 与 maxsize 大小对应
q.get([block[, timeout]]) 获取队列，timeout等待时间
q.get_nowait() 相当q.get(False)
非阻塞 q.put(item) 写入队列，timeout等待时间
q.put_nowait(item) 相当q.put(item, False)
q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空，再执行别的操作
```

**other mode:**

```python
import queue

#先进后出

q=queue.LifoQueue()

q.put(34)
q.put(56)
q.put(12)

#优先级
# q=queue.PriorityQueue()
# q.put([5,100])
# q.put([7,200])
# q.put([3,"hello"])
# q.put([4,{"name":"alex"}])

while 1:

  data=q.get()
  print(data)
```

## 6 生产者消费者模型

### 6.1 为什么要使用生产者和消费者模式

在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

### 6.2 什么是生产者消费者模式

在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

随着软件业的发展，互联网用户的日渐增多，并发这门艺术的兴起似乎是那么合情合理。每日PV十多亿的淘宝，处理并发的手段可谓是业界一流。用户访问淘宝首页的平均等待时间只有区区几秒，但是服务器所处理的流程十分复杂。首先负责首页的服务器就有好几千台，通过计算把与用户路由最近的服务器处理首页的返回。其次是网页上的资源，就JS和CSS文件就有上百个，还有图片资源等。它能在几秒内加载出来。

而在大型电商网站中，**他们的服务或者应用解耦之后，是通过消息队列在彼此间通信的。消息队列和应用之间的架构关系就是生产者消费者模型。**

**生产者：负责产生数据的模块（此处的模块是广义的，可以是类、函数、线程、进程等）。**

**消费者：处理数据的模块。**

在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

**生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。**在这个模型中，最关键就是内存缓冲区为空的时候消费者必须等待，而内存缓冲区满的时候，生产者必须等待。其他时候可以是个动态平衡。

![img](https://images2017.cnblogs.com/blog/999584/201710/999584-20171030153259152-1414686247.png)

### 6.3 生产者消费者模式的优点

a）解耦

假设生产者和消费者分别是两个类。如果让生产者直接调用消费者的某个方法，那 么生产者对于消费者就会产生依赖（也就是耦合）。将来如果消费者的代码发生变化， 可能会影响到生产者。而如果两者都依赖于某个缓冲区，两者之间不直接依赖，耦合也 就相应降低了。

举个例子，我们去邮局投递信件，如果不使用邮筒（也就是缓冲区），你必须得把 信直接交给邮递员。有同学会说，直接给邮递员不是挺简单的嘛？其实不简单，你必须 得认识谁是邮递员，才能把信给他（光凭身上穿的制服，万一有人假冒，就惨了）。这 就产生和你和邮递员之间的依赖（相当于生产者和消费者的强耦合）。万一哪天邮递员 换人了，你还要重新认识一下（相当于消费者变化导致修改生产者代码）。而邮筒相对 来说比较固定，你依赖它的成本就比较低（相当于和缓冲区之间的弱耦合）。

b）支持并发

由于生产者与消费者是两个独立的并发体，他们之间是用缓冲区作为桥梁连接，生产者只需要往缓冲区里丢数据，就可以继续生产下一个数据，而消费者只需要从缓冲区了拿数据即可，这样就不会因为彼此的处理速度而发生阻塞。

接上面的例子，如果我们不使用邮筒，我们就得在邮局等邮递员，直到他回来，我们把信件交给他，这期间我们啥事儿都不能干（也就是生产者阻塞），或者邮递员得挨家挨户问，谁要寄信（相当于消费者轮询）。

c）支持忙闲不均

缓冲区还有另一个好处。如果制造数据的速度时快时慢，缓冲区的好处就体现出来 了。当数据制造快的时候，消费者来不及处理，未处理的数据可以暂时存在缓冲区中。 等生产者的制造速度慢下来，消费者再慢慢处理掉。

为了充分复用，我们再拿寄信的例子来说事。假设邮递员一次只能带走1000封信。 万一某次碰上情人节（也可能是圣诞节）送贺卡，需要寄出去的信超过1000封，这时 候邮筒这个缓冲区就派上用场了。邮递员把来不及带走的信暂存在邮筒中，等下次过来 时再拿走。

实际应用：

在版本升级项目中，信息服务器要接收大批量的客户端请求，原来那种串行化的 处理，根本无法及时处理客户端请求，造成信息服务器大量请求堆积，导致丢包异 常严重。之后就采用了生产者消费者模式，在业务请求与业务处理间，建立了一个List 类型的缓冲区，服务端接收到业务请求，就往里扔，然后再去接收下一个业务请求，而 多个业务处理线程，就会去缓冲区里取业务请求处理。这样就大大提高了服务器的相 应速度。

Python中应用：

```python
from threading import Thread, RLock
from queue import Queue
import time

q = Queue(10)
count = 0
l = RLock()

#创建生产者
class Producer(Thread):
    def __init__(self, name, que):
        super(Producer, self).__init__()
        self.__name = name
        self.__que = que

    def run(self):
        while True:
            global count
            l.acquire()
            count += 1
            l.release()
            self.__que.put(count)
            print('%s produce baozi %s' % (self.__name, count))
            time.sleep(0.5)
            self.__que.join()

#创建消费者
class Consumer(Thread):
    def __init__(self, name, que):
        super(Consumer, self).__init__()
        self.__name = name
        self.__que = que

    def run(self):
        while True:
            data = self.__que.get()
            print('%s eat baozi %s' % (self.__name, data))
            time.sleep(1)
            self.__que.task_done()

def main():
    #创建1个生产者，3个消费者
    p1 = Producer('winter', q)
    c1 = Consumer('elly', q)
    c2 = Consumer('jack', q)
    c3 = Consumer('frank', q)
    p1.start()
    c1.start()
    c2.start()
    c3.start()

if __name__ == '__main__':
    main()
```

生产者消费者模型设计要合理，如果生产者慢了，可以增加生产者，消费者慢了，增加消费者；

**实际应用中，生产者，消费者可能是两套不同的系统，不会存在于一个进程里，甚至不在同一台设备上；而queue.Queue只能用于线程间通讯，那么该怎么办呢？**

**采用消息队列，比如rabbitMQ；**

## 7 multiprocessing进程模块

### 7.1 概述

`进程`是程序的一次动态执行过程，它对应了从代码加载、执行到执行完毕的一个完整过程。

程序是一段代码-静态的，进程是有生命周期的-动态的。

进程是系统进行资源分配和调度的一个独立单位。进程是由代码（堆栈段）、数据（数据段）、内核状态和一组寄存器组成。 

在多任务操作系统中，通过运行多个进程来并发地执行多个任务。由于每个线程都是一个能独立执行自身指令的不同控制流，因此一个包含多个线程的进程也能够实现进程内多任务的并发执行。 

进程是一个内核级的实体，进程结构的所有成分都在`内核空间`中，一个用户程序不能直接访问这些数据。 

> 进程是在内存中的，计算机和硬件打交道的是操作系统的内核，在内存中占有独立的空间-`内核空间；`
>
> 用户使用的程序，都是建立在操作系统之上，通过操作系统和硬件通讯，在内存中占有独立的空间-`用户空间`

进程的状态： 创建、准备、运行、阻塞、结束。

进程间的通信方式可以有：

- 文件
- 管道
- socket
- 信号
- 信号量
- 共享内存

### 7.2 fork

要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。

Unix/Linux操作系统提供了一个`fork()`系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是`fork()`调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回`0`，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。

Python的`os`模块封装了常见的系统调用，其中就包括`fork`，可以在Python程序中轻松创建子进程：

```python
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```

运行结果如下：

```python
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
```

由于Windows没有`fork`调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！

有了`fork`调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

> fork 创建的子进程和父进程是独立的，父进程不会等待子进程，父进程运行完毕会自己先结束。
>
> 但是multiprocess模块创建的子进程附属于父进程，父进程会等待子进程结束后再结束。

### 7.3 fork/multiprocessing/pool对比

fork：只有linux才有，底层实现依赖它，但是太底层，使用的便捷性太低，不推荐。

multiprocessing：python为了在linux、windows下提供的同意API；父进程、子进程都做事，平时可以选择。

进程池Pool(n)：一般是父进程等待，子进程做事，推荐！至于子进程的数量n，需要服务器性能、压力测试...后才能确定。就像很多游客区公园划船，老板需要多少船才好呢？太多浪费，太少不够用。

### 7.4 multiprocessing

如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有`fork`调用，难道在Windows上无法用Python编写多进程的程序？

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。`multiprocessing`模块就是跨平台版本的多进程模块。`multiprocessing`模块提供了一个`Process`类来代表一个进程对象。

#### 7.4.1 进程的调用

- A 调用方式1

```python
from multiprocessing import Process
import time
def f(name):
    time.sleep(1)
    print('hello', name,time.ctime())

if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p = Process(target=f, args=('alvin',))
        p_list.append(p)
        p.start()
    for i in p_list:
        p.join()
    print('end')
```

- B 调用方式2

```python
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        #self.name = name

    def run(self):
        time.sleep(1)
        print ('hello', self.name,time.ctime())


if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p = MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('end')
```

To show the individual process IDs involved, here is an expanded example: 

```python
from multiprocessing import Process
import os
import time
def info(title):
  
    print("title:",title)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main process line')
    time.sleep(1)
    print("------------------")
    p = Process(target=info, args=('yuan',))
    p.start()
    p.join()
```

`join()`方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

> fork 创建的子进程和父进程是独立的，父进程不会等待子进程，父进程运行完毕会自己先结束。
>
> 但是multiprocess模块创建的子进程附属于父进程，父进程会等待子进程结束后再结束。

#### 7.4.2 Process类

**构造方法：**

Process([group [, target [, name [, args [, kwargs]]]]])

　　group: 线程组，目前还没有实现，库引用中提示必须是None； 
　　target: 要执行的方法； 
　　name: 进程名； 
　　args/kwargs: 要传入方法的参数。

**实例方法：**

　　is_alive()：返回进程是否在运行。

　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。

　　start()：进程准备就绪，等待CPU调度

　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。

　　terminate()：不管任务是否完成，立即停止工作进程

**属性：**

　　daemon：和线程的setDeamon功能一样

　　name：进程名字。

　　pid：进程号。

```python
import time
from  multiprocessing import Process

def foo(i):
    time.sleep(1)
    print (p.is_alive(),i,p.pid)
    time.sleep(1)

if __name__ == '__main__':
    p_list=[]
    for i in range(10):
        p = Process(target=foo, args=(i,))
        #p.daemon=True
        p_list.append(p)

    for p in p_list:
        p.start()
    # for p in p_list:
    #     p.join()

    print('main process end')
```

### 7.5 Pool进程池

进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中有两个方法：

- apply (一个一个的运行，没意义)
- apply_async

如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

```python
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  # 不允许在向pool里面添加任务
    p.join()  # 主进程需等待pool里面的自己进程完成才结束，要是没有这句话，会不执行pool里面的子进程。
    print('All subprocesses done.')
```

执行结果如下：

```python
Parent process 669.
Waiting for all subprocesses done...
Run task 0 (671)...
Run task 1 (672)...
Run task 2 (673)...
Run task 3 (674)...
Task 2 runs 0.14 seconds.
Run task 4 (673)...
Task 1 runs 0.27 seconds.
Task 3 runs 0.86 seconds.
Task 0 runs 1.41 seconds.
Task 4 runs 1.91 seconds.
All subprocesses done.
```

代码解读：

对`Pool`对象调用`join()`方法会等待所有子进程执行完毕，调用`join()`之前必须先调用`close()`，调用`close()`之后就不能继续添加新的`Process`了。

请注意输出的结果，task `0`，`1`，`2`，`3`是立刻执行的，而task `4`要等待前面某个task完成后才执行，这是因为`Pool`的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是`Pool`有意设计的限制，并不是操作系统的限制。如果改成：

```python
p = Pool(5)
```

就可以同时跑5个进程。

由于`Pool`的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

### 7.6 进程之间的通讯

`Process`之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的`multiprocessing`模块包装了底层的机制，提供了`Queue`、`Pipes`等多种方式来交换数据。

multiprocessing 创建的进程之间通过 `multiprocessing.queue`（进程queue）通讯。

```python
from multiprocessing import Queue
q = Queue()
```

Pool创建的进程之间通过`multiprocessing.manager().Queue()`进行通讯。

```python
from multiprocessing import Manager
q = Manager().Queue()
```

> threading创建的线程通过`import queue` （线程queue）通讯。
>
> ```python
> import queue
> q = queue()
> ```

#### 7.6.1 进程对列Queue

```python
from multiprocessing import Process, Queue
import queue

def f(q,n):
    #q.put([123, 456, 'hello'])
    q.put(n*n+1)
    print("son process",id(q))

if __name__ == '__main__':
    q = Queue()  #try: q=queue.Queue()
    print("main process",id(q))

    for i in range(3):
        p = Process(target=f, args=(q,i))
        p.start()

    print(q.get())
    print(q.get())
    print(q.get())
```

#### 7.6.2 管道

The` Pipe()` function returns a pair of connection objects connected by a pipe which by default is duplex (two-way). For example:

```python
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([12, {"name":"yuan"}, 'hello'])
    response=conn.recv()
    print("response",response)
    conn.close()
    print("q_ID2:",id(child_conn))

if __name__ == '__main__':

    parent_conn, child_conn = Pipe()
    print("q_ID1:",id(child_conn))
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    parent_conn.send("儿子你好!")
    p.join()
```

The two connection objects returned by [`Pipe()`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Pipe) represent the two ends of the pipe. Each connection object has [`send()`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Connection.send) and [`recv()`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Connection.recv) methods (among others). Note that data in a pipe may become corrupted if two processes (or threads) try to read from or write to the *same* end of the pipe at the same time. Of course there is no risk of corruption from processes using different ends of the pipe at the same time.

#### 7.6.3 Managers

**Queue和pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。**

A manager object returned by `Manager()` controls a server process which holds Python objects and allows other processes to manipulate them using proxies.

A manager returned by `Manager()` will support types [`list`](https://docs.python.org/3.5/library/stdtypes.html#list), [`dict`](https://docs.python.org/3.5/library/stdtypes.html#dict), [`Namespace`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.managers.Namespace), [`Lock`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Lock), [`RLock`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.RLock), [`Semaphore`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Semaphore), [`BoundedSemaphore`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.BoundedSemaphore), [`Condition`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Condition), [`Event`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Event), [`Barrier`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Barrier), [`Queue`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Queue), [`Value`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Value) and [`Array`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.Array). For example：

```python
from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    #print(l)

    print("son process:",id(d),id(l))

if __name__ == '__main__':

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))

        print("main process:",id(d),id(l))

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d,l,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)
```

### 7.7 进程同步

Without using the lock output from the different processes is liable to get all mixed up.

```python
from multiprocessing import Process, Lock

def f(l, i):
  
    with l.acquire():
        print('hello world %s'%i)

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start() 
```

## 8 协程

协程，又称微线程，纤程。英文名Coroutine。

优点1: 协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

优点2: 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

### 8.1 yield的简单实现

```python
import time
import queue

def consumer(name):
    print("--->ready to eat baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name,new_baozi))
        #time.sleep(1)

def producer():

    r = con.__next__()
    r = con2.__next__()
    n = 0
    while 1:
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi %s and %s" %(n,n+1) )
        con.send(n)
        con2.send(n+1)

        n +=2

if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()
```

### 8.2 Greenlet

greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator

```python
from greenlet import greenlet
 
 
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
 
 
def test2():
    print(56)
    gr1.switch()
    print(78)
 
 
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
```

### 8.3 Gevent

```python
import gevent

import requests,time


start=time.time()

def f(url):
    print('GET: %s' % url)
    resp =requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([

        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.sina.com.cn/'),

])

# f('https://www.python.org/')
#
# f('https://www.yahoo.com/')
#
# f('https://baidu.com/')
#
# f('https://www.sina.com.cn/')

print("cost time:",time.time()-start)
```

### 8.4 协程展望

进程的好费资源严重；

线程的耗费少许资源（硬件、OS）、无法利用多核cpu；协程不占用硬件资源。

多进程+协程可以很好的解决I/O密集型任务，但是计算密集型任务python这门语言就不合适，建议使用c语言。

协程还在不断的发展中，3.4版本引入了asyncio模块，性能得到提升....

一直在发展，值得好好研究。



