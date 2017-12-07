# Python 代码调试技巧

Tags: debug, pdb, pycharm, pydev, python调试

pyhton调试工具多多，pdb ipdb pycharm ripdb pudb Pydbgr wdb pyringe，额..哪个合适、顺手你就用哪个呗。

参考：  
[pyd官网](https://docs.python.org/3/library/pdb.html)  
[logging官网](https://docs.python.org/3/library/logging.html)  
[pdb简单教程](https://github.com/spiside/pdb-tutorial)  
[调试工具比较](http://python.jobbole.com/52171/)  
[python调试技巧](https://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/index.html)  
[廖雪峰python调试](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138683229901532c40b749184441dbd428d2e0f8aa50e000)

## pdd/ipdb

### pdb

pdb 是 python 自带的一个包，为 python 程序提供了一种交互的源代码调试功能，主要特性包括设置断点、单步调试、进入函数调试、查看当前代码、查看栈片段、动态改变变量的值等。

- 方法1

`python -m pdb you.py`

- 方法2

需要断点的地方插入如下代码：

`import pdb； pdb.set_trace()`

- 使用说明

```sh
h(elp)	#可以看到所有的命令；
h h 
# 不知道具体某个命令什么意思？
h c   # 可以查看 c 命令的帮助，Got it？

l(ist) - Displays 11 lines around the current line or continue the previous listing.
l
l 22
l 2,16  # 2~16
l 3,2  # 3~(3+2)
ll  # 推荐代替l，具体请h；

n(ext) #- 根据逻辑一行一行的执行，但是加入是for循环1000次呢？那就，设置断点，用c命令
s(tep) #- 可以跟踪到call的函数（方法）中,n命令不会进入引用的函数内部；
c(ontinue) #- 执行到下一个断点；
b(reak) #- 0参数=查看断点，1参数=设置断点（file_name:20 设置某个文件的20行为断点），也可以接收2个参数；
cl #- 清除断点，0参数=清除所有（需要确认），可以指定清除哪个断点，其他参考（b）设置断点；

r(eturn) #- 当s进入函数时，可以通过设置断点，执行c命令退出函数，r命令则更简单；
j(ump) #- 可以jump back to execute code again,or jump forward to skip code;

exit() OR CTRL+D #- 退出
q(uit) #- Quit from the debugger. The program being executed is aborted.

！ #- 执行额外python（而不是pdb）命令，重新赋值等等，比如查看一个c变量的值，可以`!c`，（Execute the (one-line) statement in the context of the current stack frame.）

p/pp #- 打印变量，等同于`print(var_a)`(可以打印回车 \n 的哦),也可以直接pdb界面，输入变量等，查看var_a、var.value、die.show()等值；

变量和命令重名时，命令优先，所以，变量名最好有意义，不要设置为l、a、b；
```

就这么多，不知道用`h`命令，再参考python官网的解释，基本都能搞定了。

### ipdb

IPDB是什么？IPDB（Ipython Debugger），亲你听过ipython么？ 类似的，ipdb就是pdb的升级版，需要单独安装。

`pip install ipdb`

用法参考pdb，此处略；不懂就 help ！

## Pycharm调试

PyCharm 是由 JetBrains 打造的一款 Python IDE，提供了较为完善的调试功能，支持多线程，远程调试等，可以支持断点设置，单步模式，表达式求值，变量查看等一系列功能。

在调试之前通常需要设置断点，断点可以设置在循环或者条件判断的表达式处或者程序的关键点。


- Evaluate Expression 可以在debug过程中evaluate某个表达式（变量）的值；  
- Variables 可以查看变量的值；  
- Watches 可以检测变量的值；  

对于多线程程序来说，通常会有多个线程，当需要 debug 的断点分别设置在不同线程对应的线程体中的时候，通常需要 IDE 有良好的多线程调试功能的支持。 Pycharm 中在主线程启动子线程的时候会自动产生一个 Dummy 开头的名字的虚拟线程，每一个 frame 对应各自的调试帧


其他貌似没什么好说的，设置断点之、debug、查看变量、动态观察变量(watches)，GUI感觉还是方便的多，其他的内容参考[官网帮助](https://www.jetbrains.com/help/pycharm/debugging.html)

## 使用日志功能调试

日志信息是软件开发过程中进行调试的一种非常有用的方式，特别是在大型软件开发过程需要很多相关人员进行协作的情况下。开发人员通过在代码中加入一些特定的能够记录软件运行过程中的各种事件信息能够有利于甄别代码中存在的问题。这些信息可能包括时间，描述信息以及错误或者异常发生时候的特定上下文信息。

最原始的 debug 方法是通过在代码中嵌入 print 语句，通过输出一些相关的信息来定位程序的问题。但这种方法有一定的缺陷，正常的程序输出和 debug 信息混合在一起，给分析带来一定困难，当程序调试结束不再需要 debug 输出的时候，通常没有很简单的方法将 print 的信息屏蔽掉或者定位到文件。

python 中自带的 logging 模块可以比较方便的解决这些问题，它提供日志功能，将 logger 的 level 分为五个级别，可以通过 Logger.setLevel(lvl) 来设置。默认的级别为 warning。

- DEBUG	详细的信息，在追踪问题的时候使用
- INFO	正常的信息
- WARNING	一些不可预见的问题发生，或者将要发生，如磁盘空间低等，但不影响程序的运行
- ERROR	由于某些严重的问题，程序中的一些功能受到影响
- CRITICAL	严重的错误，或者程序本身不能够继续运行

其他请参考[logging官网](https://docs.python.org/3/library/logging.html)

