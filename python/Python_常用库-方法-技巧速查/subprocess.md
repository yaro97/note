# Python subprocess模块

本文实例讲述了Python subprocess模块功能与常见用法。分享给大家供大家参考，具体如下：

## 一、subprocess概述

subprocess最早在2.4版本引入。用来生成子进程，并可以通过管道连接他们的输入/输出/错误，以及获得他们的返回值。

subprocess用来替换多个旧模块和函数：

- os.system
- os.spawn*
- os.popen*
- popen2.*
- commands.*

运行python的时候，我们都是在创建并运行一个进程，linux中一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。在python中，我们通过标准库中的subprocess包来fork一个子进程，并且运行一个外部的程序。subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所欲我们可以根据需要来从中选取一个使用。另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。

subprocess创建子进程，并能通过PIPE与子进程进行通讯。默认情况子进程直接把执行的结果通过PIPE直接发送给屏幕显示程序，显示在屏幕上。我们可以把子程序的执行结果交给管道`stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE`，认为的控制stdout/stderr/stdin的流向。可以通过`ret.stdout.read()`读出标准输出的相关内容。

subprocess实现了很多简便的方法（`run()`,`check_all()`等等），但都是包装的Popen类。相关功能的使用选择参见`第五章：总结`



```python
# subprocess实现了很多简便的方法，但都是包装的Popen类。
ret = subprocess.Popen('ls', shell=True)
# 默认subprocess子程序直接把执行结果通过PIPE直接发送到屏幕上
# 这样得到的ret是个subprocess.Popen对象，在shell中会在‘显示桌面’程序中显示‘ls’的结果
# 但是‘ls’这个程序实在subprocess中运行的，两个进程之间的通讯是通过(pipe)管道来完成的
print(ret)
print(type(ret.stdout), ret.stdout)

ret = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE)
# 把‘ls’子程序执行的结果交给管道(stdout=subprocess.PIPE)，人为控制stdout的流向
# 除了stdout,subprocess还可以把stdin,stderr也扔到管道里
print(ret.stdout.read())  # 读出管道中的stdout，而且管道的内容只能读取一次，再取为空。

# 完整的写法
ret = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
# 把stdout,stdin,stderr分别放入三个不同的管道？

```



## 二、旧有模块的使用

Python中提供了以下几个函数来帮助我们完成命令行指令的执行：

| 函数名                            | 描述                                             |
| --------------------------------- | ------------------------------------------------ |
| os.system(command)                | 返回命令执行状态码，而将命令执行结果输出到屏幕   |
| os.popen(command).read()          | 可以获取命令执行结果，但是无法获取命令执行状态码 |
| commands.getstatusoutput(command) | 返回一个元组(命令执行状态码, 命令执行结果)       |

> **说明：**
>
> 1. os.popen(command)函数得到的是一个文件对象，因此除了read()方法外还支持write()等方法，具体要根据command来定；
> 2. commands模块只存在于Python 2.7中，且不支持windows平台，因此commands模块很少被使用。另外，commands模块实际上也是通过对os.popen()的封装来完成的。

### 1. os.system()函数

```python
>>> import os
>>>
>>> retcode = os.system('dir')
 驱动器 C 中的卷没有标签。
 卷的序列号是 4C32-B292

 C:\Users\wader\PycharmProjects\LearnPython 的目录

2017/03/21  11:15    <DIR>          .
2017/03/21  11:15    <DIR>          ..
2017/07/29  18:04    <DIR>          .idea
2016/12/06  11:19    <DIR>          blog
2016/12/06  11:42    <DIR>          day01
2016/12/09  22:07    <DIR>          day02
2017/01/04  09:14    <DIR>          day03
2017/07/19  16:11    <DIR>          day04
2017/07/29  14:44    <DIR>          day05
2017/07/06  14:45    <DIR>          day06
2017/07/06  17:13    <DIR>          exam01
               0 个文件              0 字节
              11 个目录  6,659,977,216 可用字节
>>> retcode
0
```

### 2. os.popen()函数

```python
>>> import os
>>>
>>> ret = os.popen('dir').read()
>>> print(ret)
 驱动器 C 中的卷没有标签。
 卷的序列号是 4C32-B292

 C:\Users\wader\PycharmProjects\LearnPython 的目录

2017/03/21  11:15    <DIR>          .
2017/03/21  11:15    <DIR>          ..
2017/07/29  18:04    <DIR>          .idea
2016/12/06  11:19    <DIR>          blog
2016/12/06  11:42    <DIR>          day01
2016/12/09  22:07    <DIR>          day02
2017/01/04  09:14    <DIR>          day03
2017/07/19  16:11    <DIR>          day04
2017/07/29  14:44    <DIR>          day05
2017/07/06  14:45    <DIR>          day06
2017/07/06  17:13    <DIR>          exam01
               0 个文件              0 字节
              11 个目录  6,664,052,736 可用字节
```

### 3. commands.getstatusoutput()函

> 需要注意的是commands模块不支持windows平台，因此该实例是在Linux平台下执行的

```python
>>> import os
>>> os.system('ls')
cmdline-jmxclient-0.10.3.jar  dhparam.pem  FtpMan.class  gitlab.crt  gitlab.csr  gitlab.key  resolv.txt  test.json  test.php  test.sh  test.text  test.txt
0
>>> import commands
>>> retcode, ret = commands.getstatusoutput('ls -l')
>>> retcode
0
>>> print(ret)
total 68
-rw-r--r-- 1 root root 20124 Jul 11  2016 cmdline-jmxclient-0.10.3.jar
-rw-r--r-- 1 root root   424 Aug 22  2016 dhparam.pem
-rw-r--r-- 1 root root  2576 Jul 13  2016 FtpMan.class
-rw-r--r-- 1 root root  1302 Aug 22  2016 gitlab.crt
-rw-r--r-- 1 root root  1054 Aug 22  2016 gitlab.csr
-rw-r--r-- 1 root root  1675 Aug 22  2016 gitlab.key
-rw-r--r-- 1 root root  9329 Jun 24  2016 resolv.txt
-rw-r--r-- 1 root root   594 Mar  7 08:14 test.json
-rw-r--r-- 1 root root   162 Jun 28 10:39 test.php
-rw-r--r-- 1 root root   760 Jun 24  2016 test.sh
-r-x------ 1 root root     0 Feb  6 08:21 test.text
drwxr-xr-x 2 root root  4096 Feb  7 16:43 test.txt
```

通过查看commands模块提供的属性可知，它也提供了单独获取命令执行状态码和执行结果的函数，如下所示：

```python
>>> dir(commands)
['__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'getoutput', 'getstatus', 'getstatusoutput', 'mk2arg', 'mkarg']
```

## 三、subprocess模块

subprocess是Python 2.4中新增的一个模块，它允许你生成新的进程，连接到它们的 input/output/error 管道，并获取它们的返回（状态）码。这个模块的目的在于替换几个旧的模块和方法，如：

- os.system
- os.spawn*

### 1. 常用函数

| 函数                            | 描述                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| subprocess.run()                | Python 3.5中新增的函数。执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。 |
| subprocess.call()               | 执行指定的命令，返回命令执行状态，其功能类似于os.system(cmd)。 |
| subprocess.check_call()         | Python 2.5中新增的函数。 执行指定的命令，如果执行成功则返回状态码，否则抛出异常。其功能等价于subprocess.run(..., check=True)。 |
| subprocess.check_output()       | Python 2.7中新增的的函数。执行指定的命令，如果执行状态码为0则返回命令执行结果，否则抛出异常。 |
| subprocess.getoutput(cmd)       | 接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)。 |
| subprocess.getstatusoutput(cmd) | 执行cmd命令，返回一个元组(命令执行状态, 命令执行结果输出)，其功能类似于commands.getstatusoutput()。 |

> **说明：**
>
> 1. 在Python 3.5之后的版本中，官方文档中提倡通过subprocess.run()函数替代其他函数来使用subproccess模块的功能；
> 2. 在Python 3.5之前的版本中，我们可以通过subprocess.call()，subprocess.getoutput()等上面列出的其他函数来使用subprocess模块的功能；
> 3. subprocess.run()、subprocess.call()、subprocess.check_call()和subprocess.check_output()都是通过对subprocess.Popen的封装来实现的高级函数，因此如果我们需要更复杂功能时，可以通过subprocess.Popen来完成。
> 4. subprocess.getoutput()和subprocess.getstatusoutput()函数是来自Python 2.x的commands模块的两个遗留函数。它们隐式的调用系统shell，并且不保证其他函数所具有的安全性和异常处理的一致性。另外，它们从Python 3.3.4开始才支持Windows平台。

### 2. 各函数参数说明

函数参数列表：

```python
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, universal_newlines=False)

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False, timeout=None)

subprocess.getstatusoutput(cmd)

subprocess.getoutput(cmd)
```

参数说明：

- **args：** 要执行的shell命令，默认应该是一个字符串序列，如['df', '-Th']或('df', '-Th')，也可以是一个字符串，如'df -Th'，但是此时需要把shell参数的值置为True。
- **shell：** 如果shell为True，那么指定的命令将通过shell执行。如果我们需要访问某些shell的特性，如管道、文件名通配符、环境变量扩展功能，这将是非常有用的。当然，python本身也提供了许多类似shell的特性的实现，如glob、fnmatch、os.walk()、os.path.expandvars()、os.expanduser()和shutil等。
- **check：** 如果check参数的值是True，且执行命令的进程以非0状态码退出，则会抛出一个CalledProcessError的异常，且该异常对象会包含 参数、退出状态码、以及stdout和stderr(如果它们有被捕获的话)。
- **stdout, stderr：**
- run()函数默认不会捕获命令执行结果的正常输出和错误输出，如果我们向获取这些内容需要传递subprocess.PIPE，然后可以通过返回的CompletedProcess类实例的stdout和stderr属性或捕获相应的内容；
- call()和check_call()函数返回的是命令执行的状态码，而不是CompletedProcess类实例，所以对于它们而言，stdout和stderr不适合赋值为subprocess.PIPE；
- check_output()函数默认就会返回命令执行结果，所以不用设置stdout的值，如果我们希望在结果中捕获错误信息，可以执行stderr=subprocess.STDOUT。
- **input：** 该参数是传递给Popen.communicate()，通常该参数的值必须是一个字节序列，如果universal_newlines=True，则其值应该是一个字符串。
- **universal_newlines：** 该参数影响的是输入与输出的数据格式，比如它的值默认为False，此时stdout和stderr的输出是字节序列；当该参数的值设置为True时，stdout和stderr的输出是字符串。

### 3. subprocess.CompletedProcess类介绍

需要说明的是，subprocess.run()函数是Python3.5中新增的一个高级函数，其返回值是一个subprocess.CompletedPorcess类的实例，因此，subprocess.completedPorcess类也是Python 3.5中才存在的。它表示的是一个已结束进程的状态信息，它所包含的属性如下：

- **args：** 用于加载该进程的参数，这可能是一个列表或一个字符串
- **returncode：** 子进程的退出状态码。通常情况下，退出状态码为0则表示进程成功运行了；一个负值-N表示这个子进程被信号N终止了
- **stdout：** 从子进程捕获的stdout。这通常是一个字节序列，如果run()函数被调用时指定universal_newlines=True，则该属性值是一个字符串。如果run()函数被调用时指定stderr=subprocess.STDOUT，那么stdout和stderr将会被整合到这一个属性中，且stderr将会为None
- **stderr：** 从子进程捕获的stderr。它的值与stdout一样，是一个字节序列或一个字符串。如果stderr灭有被捕获的话，它的值就为None
- **check_returncode()：** 如果returncode是一个非0值，则该方法会抛出一个CalledProcessError异常。

### 4. 实例

- subprocess.run()

```python
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')
```

- subprocess.call()

```python
>>> subprocess.call(['ls',  '-l'])
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.call('ls -l', shell=True)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.call(['ls',  '-l'], stdout=subprocess.DEVNULL)
0
>>> subprocess.call(['ls',  '-l', '/test'])
ls: 无法访问/test: 没有那个文件或目录
2
```

- suprocess.check_call()

```python
>>> subprocess.check_call(['ls',  '-l'])
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.check_call('ls -l', shell=True)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.check_call('ls -l /test', shell=True)
ls: 无法访问/test: 没有那个文件或目录
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.4/subprocess.py", line 557, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'ls -l /test' returned non-zero exit status 2
```

- sbuprocess.check_output()

```python
>>> ret = subprocess.check_output(['ls',  '-l'])
>>> print(ret)
b' \xe5\x85\xac\xe5\x85\xb1\xe7\x9a\x84\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe6\xa8\xa1\xe6\x9d\xbf\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe8\xa7\x86\xe9\xa2\x91\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe5\x9b\xbe\xe7\x89\x87\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe6\x96\x87\xe6\xa1\xa3\ndrwxr-xr-x  2 wader wader   4096  4\xe6\x9c\x88 13  2016 \xe4\xb8\x8b\xe8\xbd\xbd\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe9\x9f\xb3\xe4\xb9\x90\ndrwxr-xr-x  7 wader wader   4096  5\xe6\x9c\x88 26  2016 \xe6\xa1\x8c\xe9\x9d\xa2\n'
>>> ret = subprocess.check_output(['ls',  '-l'], universal_newlines=True)
>>> print(ret)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
```

- subprocess.getoutput()与subprocess.getstatusoutput()

```python
>>> ret = subprocess.getoutput('ls -l')
>>> print(ret)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
>>> retcode, output = subprocess.getstatusoutput('ls -l')
>>> print(retcode)
0
>>> print(output)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
>>> retcode, output = subprocess.getstatusoutput('ls -l /test')
>>> print(retcode)
2
>>> print(output)
ls: 无法访问/test: 没有那个文件或目录
```

## 四、subprocess.Popen介绍

该类用于在一个新的进程中执行一个子程序。前面我们提到过，上面介绍的这些函数都是基于subprocess.Popen类实现的，通过使用这些被封装后的高级函数可以很方面的完成一些常见的需求。由于subprocess模块底层的进程创建和管理是由Popen类来处理的，因此，当我们无法通过上面哪些高级函数来实现一些不太常见的功能时就可以通过subprocess.Popen类提供的灵活的api来完成。

### 1.subprocess.Popen的构造函数

```python
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
    preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False,
    startup_info=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=())
```

参数说明：

- **args：** 要执行的shell命令，可以是字符串，也可以是命令各个参数组成的序列。当该参数的值是一个字符串时，该命令的解释过程是与平台相关的，因此通常建议将args参数作为一个序列传递。
- **bufsize：** 指定缓存策略，0表示不缓冲，1表示行缓冲，其他大于1的数字表示缓冲区大小，负数 表示使用系统默认缓冲策略。
- **stdin, stdout, stderr：** 分别表示程序标准输入、输出、错误句柄。
- **preexec_fn：** 用于指定一个将在子进程运行之前被调用的可执行对象，只在Unix平台下有效。
- **close_fds：** 如果该参数的值为True，则除了0,1和2之外的所有文件描述符都将会在子进程执行之前被关闭。
- **shell：** 该参数用于标识是否使用shell作为要执行的程序，如果shell值为True，则建议将args参数作为一个字符串传递而不要作为一个序列传递。
- **cwd：** 如果该参数值不是None，则该函数将会在执行这个子进程之前改变当前工作目录。
- **env：** 用于指定子进程的环境变量，如果env=None，那么子进程的环境变量将从父进程中继承。如果env!=None，它的值必须是一个映射对象。
- **universal_newlines：** 如果该参数值为True，则该文件对象的stdin，stdout和stderr将会作为文本流被打开，否则他们将会被作为二进制流被打开。
- **startupinfo和creationflags：** 这两个参数只在Windows下有效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如主窗口的外观，进程优先级等。

### 2. subprocess.Popen类的实例可调用方法

| 方法                                        | 描述                                                         |
| ------------------------------------------- | ------------------------------------------------------------ |
| Popen.poll()                                | 用于检查子进程（命令）是否已经执行结束，没结束返回None，结束后返回状态码。 |
| Popen.wait(timeout=None)                    | 等待子进程结束，并返回状态码；如果在timeout指定的秒数之后进程还没有结束，将会抛出一个TimeoutExpired异常。 |
| Popen.communicate(input=None, timeout=None) | 该方法可用来与进程进行交互，比如发送数据到stdin，从stdout和stderr读取数据，直到到达文件末尾。 |
| Popen.send_signal(signal)                   | 发送指定的信号给这个子进程。                                 |
| Popen.terminate()                           | 停止该子进程。                                               |
| Popen.kill()                                | 杀死该子进程。                                               |

**关于communicate()方法的说明：**

- 该方法中的可选参数 input 应该是将被发送给子进程的数据，或者如没有数据发送给子进程，该参数应该是None。input参数的数据类型必须是字节串，如果universal_newlines参数值为True，则input参数的数据类型必须是字符串。
- 该方法返回一个元组(stdout_data, stderr_data)，这些数据将会是字节穿或字符串（如果universal_newlines的值为True）。
- 如果在timeout指定的秒数后该进程还没有结束，将会抛出一个TimeoutExpired异常。捕获这个异常，然后重新尝试通信不会丢失任何输出的数据。但是超时之后子进程并没有被杀死，为了合理的清除相应的内容，一个好的应用应该手动杀死这个子进程来结束通信。
- 需要注意的是，这里读取的数据是缓冲在内存中的，所以，如果数据大小非常大或者是无限的，就不应该使用这个方法。

### 3. subprocess.Popen使用实例

- 实例1：

```python
>>> import subprocess
>>>
>>> p = subprocess.Popen('df -Th', stdout=subprocess.PIPE, shell=True)
>>> print(p.stdout.read())
Filesystem     Type      Size  Used Avail Use% Mounted on
/dev/vda1      ext4       40G   12G   26G  31% /
devtmpfs       devtmpfs  3.9G     0  3.9G   0% /dev
tmpfs          tmpfs     3.9G     0  3.9G   0% /dev/shm
tmpfs          tmpfs     3.9G  386M  3.5G  10% /run
tmpfs          tmpfs     3.9G     0  3.9G   0% /sys/fs/cgroup
tmpfs          tmpfs     783M     0  783M   0% /run/user/0
tmpfs          tmpfs     783M     0  783M   0% /run/user/1000
```

- 实例2：

```python
>>> obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> obj.stdin.write('print(1) \n')
>>> obj.stdin.write('print(2) \n')
>>> obj.stdin.write('print(3) \n')
>>> out,err = obj.communicate()
>>> print(out)
1
2
3

>>> print(err)
```

- 实例3：

```python
>>> obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> out,err = obj.communicate(input='print(1) \n')
>>> print(out)
1

>>> print(err)
```

- 实例4：

实现类似`df -Th | grep data`命令的功能，实际上就是实现shell中管道的共功能。

```python
>>> 
>>> p1 = subprocess.Popen(['df', '-Th'], stdout=subprocess.PIPE)
>>> p2 = subprocess.Popen(['grep', 'data'], stdin=p1.stdout, stdout=subprocess.PIPE)
>>> out,err = p2.communicate()
>>> print(out)
/dev/vdb1      ext4      493G  4.8G  463G   2% /data
/dev/vdd1      ext4     1008G  420G  537G  44% /data1
/dev/vde1      ext4      985G  503G  432G  54% /data2

>>> print(err)
None
```

## 五、总结

那么我们到底该用哪个模块、哪个函数来执行命令与系统及系统进行交互呢？下面我们来做个总结：

- 首先应该知道的是，Python2.4版本引入了subprocess模块用来替换os.system()、os.popen()、os.spawn*()等函数以及commands模块；也就是说如果你使用的是Python 2.4及以上的版本就应该使用subprocess模块了。
- 如果你的应用使用的Python 2.4以上，但是是Python 3.5以下的版本，Python官方给出的建议是使用subprocess.call()函数。Python 2.5中新增了一个subprocess.check_call()函数，Python 2.7中新增了一个subprocess.check_output()函数，这两个函数也可以按照需求进行使用。
- 如果你的应用使用的是Python 3.5及以上的版本（目前应该还很少），Python官方给出的建议是尽量使用subprocess.run()函数。
- 当subprocess.call()、subprocess.check_call()、subprocess.check_output()和subprocess.run()这些高级函数无法满足需求时，我们可以使用subprocess.Popen类来实现我们需要的复杂功能。 