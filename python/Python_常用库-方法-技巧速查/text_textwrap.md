# textwrap模块

该模块主要用于控制段落的缩进、换行等格式的。

参考：

https://pymotw.com/3/textwrap/index.html

https://docs.python.org/3/library/textwrap.html

textwrap模块首先提供了三个便捷的方法：wrap，fill和decent，也提供了TextWrapper类。其中TextWrapper提供了全套的方法，前三个方法只是便捷的使用，因为在内部的运行中也是建立了一个TextWrapper对象。如果程序中需要大量运用这几个方法，最好还是创建TextWrapper比较快一些。

## textwrap.wrap(text,[width[,…]])

这个方法是将一个字符串按照width的宽度进行切割，切割后返回list

```python
#-*-coding:utf-8-*-
import textwrap
sample_text = '''aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk'''
sample_text2 = '''aaa bbb ccc ddd eeee ddddd fffff ggggg hhhhhh kkkkkkk'''

print sample_text
print textwrap.wrap(sample_text,width=5)
print textwrap.wrap(sample_text2,width=5)12345678
```

下面是执行结果

```
aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk
['aaabb', 'bcccd', 'ddeee', 'edddd', 'dffff', 'fgggg', 'ghhhh', 'hhkkk', 'kkkk']
['aaa', 'bbb', 'ccc', 'ddd', 'eeee', 'ddddd', 'fffff', 'ggggg', 'hhhhh', 'h kkk', 'kkkk']
1234
```

看第三个打印的结果，并不是保证了每个list元素都是按照width的，因为不但要考虑到width，也要考虑到空格，也就是一个单词。

## textwrap.fill(text[, width[, …]])

这个和上面wrap方法类似，不过返回结果是不一样的。

```python
#-*-coding:utf-8-*-
import textwrap
sample_text = '''aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk'''
sample_text2 = '''aaa bbb ccc ddd eeee ddddd fffff ggggg hhhhhh kkkkkkk'''

print sample_text
print textwrap.fill(sample_text,width=5)
print textwrap.fill(sample_text2,width=5)12345678
```

这是返回结果

```
aaabbbcccdddeeeedddddfffffggggghhhhhhkkkkkkk
aaabb
bcccd
ddeee
edddd
dffff
fgggg
ghhhh
hhkkk
kkkk
aaa
bbb
ccc
ddd
eeee
ddddd
fffff
ggggg
hhhhh
h kkk
kkkk123456789101112131415161718192021
```

## textwrap.dedent(text)

这个方法是用来移除不被期望的空白符。

```python
#-*-coding:utf-8-*-
import textwrap
sample_text = '''
    aaabbb
                cccdddee    eedddddfffffggggghhhhhhkkkkkkk'''
print sample_text
print textwrap.dedent(sample_text)1234567
```

下面是执行结果

```
    aaabbb
                cccdddee    eedddddfffffggggghhhhhhkkkkkkk

aaabbb
            cccdddee    eedddddfffffggggghhhhhhkkkkkkk12345
```

## textwrap.shorten(*text*, *width*, **kwargs)

## textwrap.indent(*text*, *prefix*, predicate=None)

下面是包中的一个类TextWrapper 

## class textwrap.TextWrapper(…)

这个类的构造函数接受一系列的关键字参数来初始化自己的属性信息，例如用如下代码初始化：

```python
wrapper = TextWrapper(initial_indent="* ")1
```

相当于是用了如下代码

```python
wrapper = TextWrapper()
wrapper.initial_indent = "* "12
```

你可以多次复用自己创建的实例，而且在用的过程中可以随意改变实例属性值。 
下面是该类的一些属性： 
width：宽度最大值，默认是70，这和上面wrap的参数一样。 
expand_tabs：默认为true，如果设置为true，那么字符串里的所有制表符都会被变成空格，相当于用了字符串方法的expandtabs()。

```python
import textwrap
sample_text = '''   aaa'''
textWrap = textwrap.TextWrapper()
textWrap.expand_tabs = True
print textWrap.wrap(sample_text)12345
```

replace_whitespace：如果设置为true，那么就会把字符串中的空白符转化为空格。 
drop_whitespace：默认true，如果设置为true，则每行开头和结尾的空白符都会被去掉，如果要去掉的空白符占据了整行，那么就会把整行去掉。 
initial_indent:进行初始化，如下代码：

```python
#-*-coding:utf-8-*-
import textwrap
sample_text = '''aaa'''
textWrap = textwrap.TextWrapper()
textWrap.initial_indent = 'bbb'
print textWrap.wrap(sample_text)
---------------------------------------
执行结果
['bbbaaa']123456789
```

subsequent_indent:初始化除了第一行的所有行：

```python
#-*-coding:utf-8-*-
import textwrap
sample_text = '''aaa
kkk
jjj'''
textWrap = textwrap.TextWrapper(width = 2)
textWrap.initial_indent = 'bbb'
textWrap.subsequent_indent = 'ccc'
print textWrap.wrap(sample_text)
---------------------------------------
下面是执行结果
['bbba', 'ccca', 'ccca', 'ccck', 'ccck', 'ccck', 'cccj', 'cccj', 'cccj']123456789101112
```

fix_sentence_endings：默认为false，如果为true，那么就会试图检查每个句子的结尾是两个空格分割，这个只在等宽字体里被需要。但是这个检查的算法是有缺陷的，它假设了句子是以.!?等这些字符为结尾。 
break_long_words：默认为true，切断长句子来让每行的数据宽度都小于width。 
break_on_hyphens：连字符相关，默认true 
wrap(text) 
fill(text)上面两个方法和最上面的类似，不细说。

