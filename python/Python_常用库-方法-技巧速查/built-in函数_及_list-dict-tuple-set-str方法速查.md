# 内置函数和常用方法作弊单

参考：

内置函数及内置类型方法清单： https://www.programiz.com/python-programming/methods/built-in

Cheat sheet： http://overapi.com/python

内置函数：https://docs.python.org/3/library/functions.html

内置类型：https://docs.python.org/3/library/stdtypes.html

Python菜鸟教程：http://www.runoob.com/python3/python3-tutorial.html

## 内置函数Built-in Fn

The Python interpreter has a number of functions that are always available for use. These functions are called built-in functions. For example, `print()` function prints the given object to the standard output device (screen) or to the text stream file.

In Python 3.6 (latest version), there are 68 built-in functions. They are listed below alphabetically along with brief description.

| Method                                                       | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Python abs()](https://www.programiz.com/python-programming/methods/built-in/abs) | returns absolute value of a number返回绝对值                 |
| [Python all()](https://www.programiz.com/python-programming/methods/built-in/all) | returns true when all elements in iterable is true           |
| [Python any()](https://www.programiz.com/python-programming/methods/built-in/any) | Checks if any Element of an Iterable is True                 |
| [Python ascii()](https://www.programiz.com/python-programming/methods/built-in/ascii) | Returns String Containing Printable Representation           |
| [Python bin()](https://www.programiz.com/python-programming/methods/built-in/bin) | converts integer to binary string转化为二进制                |
| [Python bool()](https://www.programiz.com/python-programming/methods/built-in/bool) | Coverts a Value to Boolean                                   |
| [Python bytearray()](https://www.programiz.com/python-programming/methods/built-in/bytearray) | returns array of given byte size可变的byte类型               |
| [Python bytes()](https://www.programiz.com/python-programming/methods/built-in/bytes) | returns immutable bytes object不可变byte类型                 |
| [Python callable()](https://www.programiz.com/python-programming/methods/built-in/callable) | Checks if the Object is Callable                             |
| [Python chr()](https://www.programiz.com/python-programming/methods/built-in/chr) | Returns a Character (a string) from an Integer与ord('a')相反 |
| [Python classmethod()](https://www.programiz.com/python-programming/methods/built-in/classmethod) | returns class method for given function使用@classmethod替换  |
| [Python compile()](https://www.programiz.com/python-programming/methods/built-in/compile) | Returns a Python code object返回编译过的代码                 |
| [Python complex()](https://www.programiz.com/python-programming/methods/built-in/complex) | Creates a Complex Number创建复数（使用j而不是i）             |
| [Python delattr()](https://www.programiz.com/python-programming/methods/built-in/delattr) | Deletes Attribute From the Object删除属性                    |
| [Python dict()](https://www.programiz.com/python-programming/methods/built-in/dict) | Creates a Dictionary三种参数创建词典：关键词参数a=1； 映射'a':1；可迭代对象[('a',1)] |
| [Python dir()](https://www.programiz.com/python-programming/methods/built-in/dir) | Tries to Return Attributes of Object尝试调用`__dir__()`先，后调用`__dict__`属性（参考`vars()`函数） |
| [Python divmod()](https://www.programiz.com/python-programming/methods/built-in/divmod) | Returns a Tuple of Quotient and Remainder返回商和余数        |
| [Python enumerate()](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Returns an Enumerate Object返回枚举对象                      |
| [Python eval()](https://www.programiz.com/python-programming/methods/built-in/eval) | Runs Python Code Within Program运行/计算字符串格式的python代码 |
| [Python exec()](https://www.programiz.com/python-programming/methods/built-in/exec) | Executes Dynamically Created Program执行编译过的python代码（compile()的结果） |
| [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter) | constructs iterator from elements which are true建议使用`生成器表达式`替换 |
| [Python float()](https://www.programiz.com/python-programming/methods/built-in/float) | returns floating point number from number, string            |
| [Python format()](https://www.programiz.com/python-programming/methods/built-in/format) | returns formatted representation of a value建议使用str的format方法替换 |
| [Python frozenset()](https://www.programiz.com/python-programming/methods/built-in/frozenset) | returns immutable frozenset object创建冻结的set(集合)        |
| [Python getattr()](https://www.programiz.com/python-programming/methods/built-in/getattr) | returns value of named attribute of an object建议使用`.`的方式访问属性，等效 |
| [Python globals()](https://www.programiz.com/python-programming/methods/built-in/globals) | returns dictionary of current global symbol table返回当前环境全局变量？ |
| [Python hasattr()](https://www.programiz.com/python-programming/methods/built-in/hasattr) | returns whether object has named attribute                   |
| [Python hash()](https://www.programiz.com/python-programming/methods/built-in/hash) | returns hash value of an object                              |
| [Python help()](https://www.programiz.com/python-programming/methods/built-in/help) | Invokes the built-in Help System帮助函数                     |
| [Python hex()](https://www.programiz.com/python-programming/methods/built-in/hex) | Converts to Integer to Hexadecimal转换为16进制               |
| [Python id()](https://www.programiz.com/python-programming/methods/built-in/id) | Returns Identify of an Object返回对象的内存地址              |
| [Python input()](https://www.programiz.com/python-programming/methods/built-in/input) | reads and returns a line of string                           |
| [Python int()](https://www.programiz.com/python-programming/methods/built-in/int) | returns integer from a number or string                      |
| [Python isinstance()](https://www.programiz.com/python-programming/methods/built-in/isinstance) | Checks if a Object is an Instance of Class是否是class的实例（对象） |
| [Python issubclass()](https://www.programiz.com/python-programming/methods/built-in/issubclass) | Checks if a Object is Subclass of a Class是否是子类          |
| [Python iter()](https://www.programiz.com/python-programming/methods/built-in/iter) | returns iterator for an object根据list、dict、set等创建迭代器 |
| [Python len()](https://www.programiz.com/python-programming/methods/built-in/len) | Returns Length of an Object                                  |
| [Python list()](https://www.programiz.com/python-programming/methods/built-in/list) | creates list in Python                                       |
| [Python locals()](https://www.programiz.com/python-programming/methods/built-in/locals) | returns dictionary of current local symbol table返回当前环境局部变量？ |
| [Python map()](https://www.programiz.com/python-programming/methods/built-in/map) | Applies Function and Returns a List使用：map(func, *iterables)，返回map对象 |
| [Python max()](https://www.programiz.com/python-programming/methods/built-in/max) | returns largest element参数：1、iterable; 2、*args。注意：可以指定key和reverse |
| [Python memoryview()](https://www.programiz.com/python-programming/methods/built-in/memoryview) | returns memory view of an argument和byte对象有关             |
| [Python min()](https://www.programiz.com/python-programming/methods/built-in/min) | returns smallest element参数：1、iterable; 2、*args。注意：可以指定key和reverse |
| [Python next()](https://www.programiz.com/python-programming/methods/built-in/next) | Retrieves Next Element from Iterator                         |
| [Python object()](https://www.programiz.com/python-programming/methods/built-in/object) | Creates a Featureless Object没用！？                         |
| [Python oct()](https://www.programiz.com/python-programming/methods/built-in/oct) | converts integer to octal转换为8进制                         |
| [Python open()](https://www.programiz.com/python-programming/methods/built-in/open) | Returns a File object文件                                    |
| [Python ord()](https://www.programiz.com/python-programming/methods/built-in/ord) | returns Unicode code point for Unicode character与chr(97)相反 |
| [Python pow()](https://www.programiz.com/python-programming/methods/built-in/pow) | returns x to the power of y幂计算                            |
| [Python print()](https://www.programiz.com/python-programming/methods/built-in/print) | Prints the Given Object                                      |
| [Python property()](https://www.programiz.com/python-programming/methods/built-in/property) | returns a property attribute使用@property装饰器替换          |
| [Python range()](https://www.programiz.com/python-programming/methods/built-in/range) | return sequence of integers between start and stop返回range对象 |
| [Python repr()](https://www.programiz.com/python-programming/methods/built-in/repr) | returns printable representation of an object实际调用`__repr__()`方法，表达是字符串 |
| [Python reversed()](https://www.programiz.com/python-programming/methods/built-in/reversed) | returns reversed iterator of a sequence参数： sequence，返回：iterator |
| [Python round()](https://www.programiz.com/python-programming/methods/built-in/round) | rounds a floating point number to ndigits places.四舍五入，可以指定小数点位数 |
| [Python set()](https://www.programiz.com/python-programming/methods/built-in/set) | returns a Python set集合                                     |
| [Python setattr()](https://www.programiz.com/python-programming/methods/built-in/setattr) | sets value of an attribute of object结合property装饰器使用   |
| [Python slice()](https://www.programiz.com/python-programming/methods/built-in/slice) | creates a slice object specified by range()列表：list[slice对象] |
| [Python sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted) | returns sorted list from a given iterable列表的sort方法改变原list，sorted()函数返回新对象；注意：可以指定key和reverse |
| [Python staticmethod()](https://www.programiz.com/python-programming/methods/built-in/staticmethod) | creates static method from a function使用@staticmethod装饰器替换 |
| [Python str()](https://www.programiz.com/python-programming/methods/built-in/str) | returns informal representation of an object字符串           |
| [Python sum()](https://www.programiz.com/python-programming/methods/built-in/sum) | Add items of an Iterable求和                                 |
| [Python super()](https://www.programiz.com/python-programming/methods/built-in/super) | Allow you to Refer Parent Class by super父类/基类/超类       |
| [Python tuple()](https://www.programiz.com/python-programming/methods/built-in/tuple) | Creates a Tuple                                              |
| [Python type()](https://www.programiz.com/python-programming/methods/built-in/type) | Returns Type of an Object返回类型                            |
| [Python vars()](https://www.programiz.com/python-programming/methods/built-in/vars) | Returns `__dict__` attribute of a class注意和`dir()`的关系   |
| [Python zip()](https://www.programiz.com/python-programming/methods/built-in/zip) | Returns an Iterator of Tuples可以方便的转置dict的keys和values |
| [Python `__import__()`](https://www.programiz.com/python-programming/methods/built-in/__import__) | Advanced Function Called by import使用`import`语句替换       |

## 字符串str

### 字符串运算、索引、截取

| 操作符        | 描述                                                         | 实例                                 |
| :------------ | ------------------------------------------------------------ | ------------------------------------ |
| +             | 字符串连接                                                   | >>>a + b 'HelloPython'               |
| *             | 重复输出字符串                                               | >>>a * 2 'HelloHello'                |
| []            | 通过索引获取字符串中字符                                     | >>>a[1] 'e'                          |
| [ : ]         | 截取字符串中的一部分                                         | >>>a[1:4] 'ell'                      |
| in            | 成员运算符 - 如果字符串中包含给定的字符返回 True             | >>>"H" in a True                     |
| not in        | 成员运算符 - 如果字符串中不包含给定的字符返回 True           | >>>"M" not in a True                 |
| r/R           | 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 | >>>print r'\n' \n >>> print R'\n' \n |
| %或format方法 | 格式字符串                                                   | 请看下一章节                         |

### 转义字符

| 转义字符    | 描述                                         |
| ----------- | -------------------------------------------- |
| \(在行尾时) | 续行符                                       |
| \\          | 反斜杠符号                                   |
| \'          | 单引号                                       |
| \"          | 双引号                                       |
| \a          | 响铃                                         |
| \b          | 退格(Backspace)                              |
| \e          | 转义                                         |
| \000        | 空                                           |
| \n          | 换行                                         |
| \v          | 纵向制表符                                   |
| \t          | 横向制表符                                   |
| \r          | 回车                                         |
| \f          | 换页                                         |
| \oyy        | 八进制数，yy代表的字符，例如：\o12代表换行   |
| \xyy        | 十六进制数，yy代表的字符，例如：\x0a代表换行 |
| \other      | 其它的字符以普通格式输出                     |

### 字符串格式化

参考：“Python_format常用格式化示例.md”

或者参考：https://pyformat.info/

### str内置方法

| [string.capitalize()](http://www.runoob.com/python/att-string-capitalize.html) | 把字符串的第一个字符大写                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [string.center(width)](http://www.runoob.com/python/att-string-center.html) | 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串   |
| **string.count(str, beg=0, end=len(string))**                | 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数 |
| [string.decode(encoding='UTF-8', errors='strict')](http://www.runoob.com/python/att-string-decode.html) | 以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace' |
| [string.encode(encoding='UTF-8', errors='strict')](http://www.runoob.com/python/att-string-encode.html) | 以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace' |
| **string.endswith(obj, beg=0, end=len(string))**             | 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False. |
| [string.expandtabs(tabsize=8)](http://www.runoob.com/python/att-string-expandtabs.html) | 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。 |
| **string.find(str, beg=0, end=len(string))**                 | 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1 |
| **string.format()**                                          | 格式化字符串                                                 |
| **string.index(str, beg=0, end=len(string))**                | 跟find()方法一样，只不过如果str不在 string中会报一个异常.    |
| [string.isalnum()](http://www.runoob.com/python/att-string-isalnum.html) | 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False |
| [string.isalpha()](http://www.runoob.com/python/att-string-isalpha.html) | 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False |
| [string.isdecimal()](http://www.runoob.com/python/att-string-isdecimal.html) | 如果 string 只包含十进制数字则返回 True 否则返回 False.      |
| [string.isdigit()](http://www.runoob.com/python/att-string-isdigit.html) | 如果 string 只包含数字则返回 True 否则返回 False.            |
| [string.islower()](http://www.runoob.com/python/att-string-islower.html) | 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False |
| [string.isnumeric()](http://www.runoob.com/python/att-string-isnumeric.html) | 如果 string 中只包含数字字符，则返回 True，否则返回 False    |
| [string.isspace()](http://www.runoob.com/python/att-string-isspace.html) | 如果 string 中只包含空格，则返回 True，否则返回 False.       |
| [string.istitle()](http://www.runoob.com/python/att-string-istitle.html) | 如果 string 是标题化的(见 title())则返回 True，否则返回 False |
| [string.isupper()](http://www.runoob.com/python/att-string-isupper.html) | 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False |
| **string.join(seq)**                                         | 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
| [string.ljust(width)](http://www.runoob.com/python/att-string-ljust.html) | 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串 |
| [string.lower()](http://www.runoob.com/python/att-string-lower.html) | 转换 string 中所有大写字符为小写.                            |
| [string.lstrip()](http://www.runoob.com/python/att-string-lstrip.html) | 截掉 string 左边的空格                                       |
| [string.maketrans(intab, outtab\])](http://www.runoob.com/python/att-string-maketrans.html) | maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 |
| [max(str)](http://www.runoob.com/python/att-string-max.html) | 返回字符串 *str* 中最大的字母。                              |
| [min(str)](http://www.runoob.com/python/att-string-min.html) | 返回字符串 *str* 中最小的字母。                              |
| **string.partition(str)**                                    | 有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string. |
| **string.replace(str1, str2,  num=string.count(str1))**      | 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次. |
| [string.rfind(str, beg=0,end=len(string) )](http://www.runoob.com/python/att-string-rfind.html) | 类似于 find()函数，不过是从右边开始查找.                     |
| [string.rindex( str, beg=0,end=len(string))](http://www.runoob.com/python/att-string-rindex.html) | 类似于 index()，不过是从右边开始.                            |
| [string.rjust(width)](http://www.runoob.com/python/att-string-rjust.html) | 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串 |
| [string.rpartition(str)](http://www.runoob.com/python/att-string-rpartition.html) | 类似于 partition()函数,不过是从右边开始查找                  |
| [string.rstrip()](http://www.runoob.com/python/att-string-rstrip.html) | 删除 string 字符串末尾的空格.                                |
| **string.split(str="", num=string.count(str))**              | 以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串 |
| [string.splitlines([keepends\])](http://www.runoob.com/python/att-string-splitlines.html) | 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
| [string.startswith(obj, beg=0,end=len(string))](http://www.runoob.com/python/att-string-startswith.html) | 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查. |
| **string.strip([obj])**                                      | 在 string 上执行 lstrip()和 rstrip()                         |
| [string.swapcase()](http://www.runoob.com/python/att-string-swapcase.html) | 翻转 string 中的大小写                                       |
| [string.title()](http://www.runoob.com/python/att-string-title.html) | 返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) |
| **string.translate(str, del="")**                            | 根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中 |
| [string.upper()](http://www.runoob.com/python/att-string-upper.html) | 转换 string 中的小写字母为大写                               |
| [string.zfill(width)](http://www.runoob.com/python/att-string-zfill.html) | 返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0 |

## 列表list

### 列表运算、索引、截取

| Python 表达式                | 结果                         | 描述                     |
| ---------------------------- | ---------------------------- | ------------------------ |
| len([1, 2, 3])               | 3                            | 长度                     |
| [1, 2, 3] + [4, 5, 6]        | [1, 2, 3, 4, 5, 6]           | 组合                     |
| ['Hi!'] * 4                  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复                     |
| 3 in [1, 2, 3]               | True                         | 元素是否存在于列表中     |
| for x in [1, 2, 3]: print x, | 1 2 3                        | 迭代                     |
| L[2]                         | 'Taobao'                     | 读取列表中第三个元素     |
| L[-2]                        | 'Runoob'                     | 读取列表中倒数第二个元素 |
| L[1:]                        | ['Runoob', 'Taobao']         | 从第二个元素开始截取列表 |

### list内置方法

| 序号 | 方法                                                         |
| ---- | ------------------------------------------------------------ |
| 1    | [list.append(obj)](http://www.runoob.com/python/att-list-append.html) 在列表末尾添加新的对象 |
| 2    | [list.count(obj)](http://www.runoob.com/python/att-list-count.html) 统计某个元素在列表中出现的次数 |
| 3    | [list.extend(seq)](http://www.runoob.com/python/att-list-extend.html) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）`+`云算法 |
| 4    | [list.index(obj)](http://www.runoob.com/python/att-list-index.html) 从列表中找出某个值第一个匹配项的索引位置 |
| 5    | [list.insert(index, obj)](http://www.runoob.com/python/att-list-insert.html) 将对象插入列表 |
| 6    | list.pop([index=-1\])](http://www.runoob.com/python/att-list-pop.html) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| 7    | [list.remove(obj)](http://www.runoob.com/python/att-list-remove.html) 移除列表中某个值的第一个匹配项 |
| 8    | [list.reverse()](http://www.runoob.com/python/att-list-reverse.html) 反向列表中元素 |
| 9    | [list.sort(cmp=None, key=None, reverse=False)](http://www.runoob.com/python/att-list-sort.html) 对原列表进行排序 |
| 10   | list.copy()  Returns Shallow Copy of a List 等同于: `list[:]` |
| 11   | list.clear()  Removes all Items from the List                |

### 可以接受list为参数的内置函数

| Method                                                       | Description                                        |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [Python any()](https://www.programiz.com/python-programming/methods/built-in/any) | Checks if any Element of an Iterable is True       |
| [Python all()](https://www.programiz.com/python-programming/methods/built-in/all) | returns true when all elements in iterable is true |
| [Python ascii()](https://www.programiz.com/python-programming/methods/built-in/ascii) | Returns String Containing Printable Representation |
| [Python bool()](https://www.programiz.com/python-programming/methods/built-in/bool) | Coverts a Value to Boolean                         |
| [Python enumerate()](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Returns an Enumerate Object                        |
| [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter) | constructs iterator from elements which are true   |
| [Python iter()](https://www.programiz.com/python-programming/methods/built-in/iter) | returns iterator for an object                     |
| [Python list() Function](https://www.programiz.com/python-programming/methods/built-in/list) | creates list in Python                             |
| [Python len()](https://www.programiz.com/python-programming/methods/built-in/len) | Returns Length of an Object                        |
| [Python max()](https://www.programiz.com/python-programming/methods/built-in/max) | returns largest element                            |
| [Python min()](https://www.programiz.com/python-programming/methods/built-in/min) | returns smallest element                           |
| [Python map()](https://www.programiz.com/python-programming/methods/built-in/map) | Applies Function and Returns a List                |
| [Python reversed()](https://www.programiz.com/python-programming/methods/built-in/reversed) | returns reversed iterator of a sequence            |
| [Python slice()](https://www.programiz.com/python-programming/methods/built-in/slice) | creates a slice object specified by range()        |
| [Python sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted) | returns sorted list from a given iterable          |
| [Python sum()](https://www.programiz.com/python-programming/methods/built-in/sum) | Add items of an Iterable                           |
| [Python zip()](https://www.programiz.com/python-programming/methods/built-in/zip) | Returns an Iterator of Tuples                      |

## 元组tuple

tuple is **immutable**. You cannot change elements of a tuple once it is assigned.

> 元组定义： `a = 1,`,  `a = 1, 2`, `a = ('some',)` ...

### 元组运算、索引、截取

| Python 表达式                | 结果                         | 描述                         |
| ---------------------------- | ---------------------------- | ---------------------------- |
| len((1, 2, 3))               | 3                            | 计算元素个数                 |
| (1, 2, 3) + (4, 5, 6)        | (1, 2, 3, 4, 5, 6)           | 连接                         |
| ('Hi!',) * 4                 | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制                         |
| 3 in (1, 2, 3)               | True                         | 元素是否存在                 |
| for x in (1, 2, 3): print x, | 1 2 3                        | 迭代                         |
| L[2]                         | 'SPAM!'                      | 读取第三个元素               |
| L[-2]                        | 'Spam'                       | 反向读取；读取倒数第二个元素 |
| L[1:]                        | ('Spam', 'SPAM!')            | 截取元素                     |

### tuple内置方法

There are only 2 tuple methods that tuple objects can call: `count` and `index`.

| Method                                                       | Description                                |
| ------------------------------------------------------------ | ------------------------------------------ |
| [Python Tuple count()](https://www.programiz.com/python-programming/methods/tuple/count) | returns occurrences of element in a tuple  |
| [Python Tuple index()](https://www.programiz.com/python-programming/methods/tuple/index) | returns smallest index of element in tuple |

### 可以接受tuple为参数的内置函数

| Method                                                       | Description                                        |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [Python any()](https://www.programiz.com/python-programming/methods/built-in/any) | Checks if any Element of an Iterable is True       |
| [Python all()](https://www.programiz.com/python-programming/methods/built-in/all) | returns true when all elements in iterable is true |
| [Python ascii()](https://www.programiz.com/python-programming/methods/built-in/ascii) | Returns String Containing Printable Representation |
| [Python bool()](https://www.programiz.com/python-programming/methods/built-in/bool) | Coverts a Value to Boolean                         |
| [Python enumerate()](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Returns an Enumerate Object                        |
| [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter) | constructs iterator from elements which are true   |
| [Python iter()](https://www.programiz.com/python-programming/methods/built-in/iter) | returns iterator for an object                     |
| [Python len()](https://www.programiz.com/python-programming/methods/built-in/len) | Returns Length of an Object                        |
| [Python max()](https://www.programiz.com/python-programming/methods/built-in/max) | returns largest element                            |
| [Python min()](https://www.programiz.com/python-programming/methods/built-in/min) | returns smallest element                           |
| [Python map()](https://www.programiz.com/python-programming/methods/built-in/map) | Applies Function and Returns a List                |
| [Python reversed()](https://www.programiz.com/python-programming/methods/built-in/reversed) | returns reversed iterator of a sequence            |
| [Python slice()](https://www.programiz.com/python-programming/methods/built-in/slice) | creates a slice object specified by range()        |
| [Python sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted) | returns sorted list from a given iterable          |
| [Python sum()](https://www.programiz.com/python-programming/methods/built-in/sum) | Add items of an Iterable                           |
| [Python tuple() Function](https://www.programiz.com/python-programming/methods/built-in/tuple) | Creates a Tuple                                    |
| [Python zip()](https://www.programiz.com/python-programming/methods/built-in/zip) | Returns an Iterator of Tuples                      |

## 集合set

### 集合运算

| 名称 | 含义                    |
| ---- | ----------------------- |
| &    | 交 intersection         |
| -    | 差 difference           |
| \|   | 并 union                |
| ^    | 补 symmetric_difference |

### set内置方法

| Method                                                       | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Python Set remove()](https://www.programiz.com/python-programming/methods/set/remove) | Removes Element from the Set移除元素，没有此元素会报错       |
| [Python Set add()](https://www.programiz.com/python-programming/methods/set/add) | adds element to a set添加元素                                |
| [Python Set copy()](https://www.programiz.com/python-programming/methods/set/copy) | Returns Shallow Copy of a Set浅复制返回新set                 |
| [Python Set clear()](https://www.programiz.com/python-programming/methods/set/clear) | remove all elements from a set清空元素                       |
| [Python Set difference()](https://www.programiz.com/python-programming/methods/set/difference) | Returns Difference of Two Sets差运算，返回新set              |
| [Python Set difference_update()](https://www.programiz.com/python-programming/methods/set/difference_update) | Updates Calling Set With Intersection of Sets拆运算，更新当前set |
| [Python Set discard()](https://www.programiz.com/python-programming/methods/set/discard) | Removes an Element from The Set移除元素，但是没有此元素不会报错，返回None |
| [Python Set intersection()](https://www.programiz.com/python-programming/methods/set/intersection) | Returns Intersection of Two or More Sets交运算，返回新set    |
| [Python Set intersection_update()](https://www.programiz.com/python-programming/methods/set/intersection_update) | Updates Calling Set With Intersection of Sets交运算，并更新当前set |
| [Python Set isdisjoint()](https://www.programiz.com/python-programming/methods/set/isdisjoint) | Checks Disjoint Sets两个set是否是“互斥关系”（没有重复的元素） |
| [Python Set issubset()](https://www.programiz.com/python-programming/methods/set/issubset) | Checks if a Set is Subset of Another Set是否是子集           |
| Python Set issuperset()                                      | 是否是父集                                                   |
| [Python Set pop()](https://www.programiz.com/python-programming/methods/set/pop) | Removes an Arbitrary Element随机pop一个元素                  |
| [Python Set symmetric_difference()](https://www.programiz.com/python-programming/methods/set/symmetric_difference) | Returns Symmetric Difference补运算，返回新set                |
| [Python Set symmetric_difference_update()](https://www.programiz.com/python-programming/methods/set/symmetric_difference_update) | Updates Set With Symmetric Difference补运算，更新当前set     |
| [Python Set union()](https://www.programiz.com/python-programming/methods/set/union) | Returns Union of Sets并运算                                  |
| [Python Set update(queue)](https://www.programiz.com/python-programming/methods/set/update) | Add Elements to The Set.接受一个序列，批量添加元素           |

### 可以接受set为参数的内置函数

| Method                                                       | Description                                        |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [Python any()](https://www.programiz.com/python-programming/methods/built-in/any) | Checks if any Element of an Iterable is True       |
| [Python all()](https://www.programiz.com/python-programming/methods/built-in/all) | returns true when all elements in iterable is true |
| [Python ascii()](https://www.programiz.com/python-programming/methods/built-in/ascii) | Returns String Containing Printable Representation |
| [Python bool()](https://www.programiz.com/python-programming/methods/built-in/bool) | Coverts a Value to Boolean                         |
| [Python enumerate()](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Returns an Enumerate Object                        |
| [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter) | constructs iterator from elements which are true   |
| [Python frozenset()](https://www.programiz.com/python-programming/methods/built-in/frozenset) | returns immutable frozenset object                 |
| [Python iter()](https://www.programiz.com/python-programming/methods/built-in/iter) | returns iterator for an object                     |
| [Python len()](https://www.programiz.com/python-programming/methods/built-in/len) | Returns Length of an Object                        |
| [Python max()](https://www.programiz.com/python-programming/methods/built-in/max) | returns largest element                            |
| [Python min()](https://www.programiz.com/python-programming/methods/built-in/min) | returns smallest element                           |
| [Python map()](https://www.programiz.com/python-programming/methods/built-in/map) | Applies Function and Returns a List                |
| [Python set()](https://www.programiz.com/python-programming/methods/built-in/set) | returns a Python set                               |
| [Python sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted) | returns sorted list from a given iterable          |
| [Python sum()](https://www.programiz.com/python-programming/methods/built-in/sum) | Add items of an Iterable                           |
| [Python zip()](https://www.programiz.com/python-programming/methods/built-in/zip) | Returns an Iterator of Tuples                      |

## 字典dict

### dict内置方法

| 序号 | 函数及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | [dict.clear()](http://www.runoob.com/python/att-dictionary-clear.html) 删除字典内所有元素 |
| 2    | [dict.copy()](http://www.runoob.com/python/att-dictionary-copy.html) 返回一个字典的浅复制 |
| 3    | [dict.fromkeys(seq[, val\])](http://www.runoob.com/python/att-dictionary-fromkeys.html) 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值 |
| 4    | [dict.get(key, default=None)](http://www.runoob.com/python/att-dictionary-get.html) 返回指定键的值，如果值不在字典中返回default值 |
| 5    | [dict.has_key(key)](http://www.runoob.com/python/att-dictionary-has_key.html) 如果键在字典dict里返回true，否则返回false |
| 6    | [dict.items()](http://www.runoob.com/python/att-dictionary-items.html) 以列表返回可遍历的(键, 值) 元组数组 |
| 7    | [dict.keys()](http://www.runoob.com/python/att-dictionary-keys.html) 以列表返回一个字典所有的键 |
| 8    | [dict.setdefault(key, default=None)](http://www.runoob.com/python/att-dictionary-setdefault.html) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| 9    | [dict.update(dict2)](http://www.runoob.com/python/att-dictionary-update.html) 把字典dict2的键/值对更新到dict里 |
| 10   | [dict.values()](http://www.runoob.com/python/att-dictionary-values.html) 以列表返回字典中的所有值 |
| 11   | [pop(key[,default\])](http://www.runoob.com/python/python-att-dictionary-pop.html) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| 12   | [popitem()](http://www.runoob.com/python/python-att-dictionary-popitem.html) 随机返回并删除字典中的一对键和值。 |

> 删除字典的某个条目：`del dict['key_name']`

### 可以接受dict为参数的内置函数

| Title                                                        | Description                                        |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [Python any()](https://www.programiz.com/python-programming/methods/built-in/any) | Checks if any Element of an Iterable is True       |
| [Python all()](https://www.programiz.com/python-programming/methods/built-in/all) | returns true when all elements in iterable is true |
| [Python ascii()](https://www.programiz.com/python-programming/methods/built-in/ascii) | Returns String Containing Printable Representation |
| [Python bool()](https://www.programiz.com/python-programming/methods/built-in/bool) | Coverts a Value to Boolean                         |
| [Python dict()](https://www.programiz.com/python-programming/methods/built-in/dict) | Creates a Dictionary                               |
| [Python enumerate()](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Returns an Enumerate Object                        |
| [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter) | constructs iterator from elements which are true   |
| [Python iter()](https://www.programiz.com/python-programming/methods/built-in/iter) | returns iterator for an object                     |
| [Python len()](https://www.programiz.com/python-programming/methods/built-in/len) | Returns Length of an Object                        |
| [Python max()](https://www.programiz.com/python-programming/methods/built-in/max) | returns largest element                            |
| [Python min()](https://www.programiz.com/python-programming/methods/built-in/min) | returns smallest element                           |
| [Python map()](https://www.programiz.com/python-programming/methods/built-in/map) | Applies Function and Returns a List                |
| [Python sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted) | returns sorted list from a given iterable          |
| [Python sum()](https://www.programiz.com/python-programming/methods/built-in/sum) | Add items of an Iterable                           |
| [Python zip()](https://www.programiz.com/python-programming/methods/built-in/zip) | Returns an Iterator of Tuples                      |