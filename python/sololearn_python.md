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

## Functional Programming

## Object-Oriented Programming

## Regular Expressions

## Pythonicness & Packaging