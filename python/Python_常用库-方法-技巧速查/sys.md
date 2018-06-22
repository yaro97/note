# sys模块

sys模块包括了一组非常实用的服务，内含很多[函数](http://www.iplaypython.com/jichu/function.html)方法和[变量](http://www.iplaypython.com/jichu/var.html)，用来处理Python运行时配置以及资源，从而可以与前当程序之外的系统环境交互，如：[Python解释器](http://www.iplaypython.com/jichu/interpreter.html)。

```python
import sys
dir(sys)  # 查看可以的属性
```

实例：进度条实现

```python
import sys,time
for i in range(10):
    sys.stdout.write('#')
    time.sleep(1)
    sys.stdout.flush() # 清理缓存区，否则python会将“#”放到缓存区，然后一次性显示。
```

