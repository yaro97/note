# Python snippets

This is a basket of Python snippets. Some of them are from Stack Overflow, others are written by me or taken from various web resources.

Refer to : https://snippets.readthedocs.io

[TOC]

## Basic

Snippets on basic things.

### not None test

```python
if value is not None:
    pass
```

### dump variable

```python
import pprint

pprint.pprint(globals())
```

### ternary conditional operator

```python
>>> 'true' if True else 'false'
'true'
>>> 'true' if False else 'false'
'false'
```

### accessing the index in for loops

```python
for idx, val in enumerate(ints):
    print idx, val
```

### how do I check if a variable exists

To check the existence of a local variable:

```python
if 'myVar' in locals():
    # myVar exists.
```

To check the existence of a global variable:

```python
if 'myVar' in globals():
    # myVar exists.
```

To check if an object has an attribute:

```python
if hasattr(obj, 'attr_name'):
    # obj.attr_name exists.
```

## String

Snippets on string manipulation.

### check if a string is a number

```python
>>> a = "123"
>>> a.isdigit()
True
>>> b = "123abc"
>>> b.isdigit()
False
```

### reverse a string

```python
>>> 'hello world'[::-1]
'dlrow olleh'

```

### write long string

If you follow PEP8, there is a maximum of 79 characters limit, BTW, you should follow PEP8, :)

```python
string = ("this is a "
          "really long long "
          "string")

```

### number with leading zeros

```python
>>> "%02d" % 1
'01'
>>> "%02d" % 100
'100'
>>> str(1).zfill(2)
'01'
```

## List

Snippets on list manipulation.

### [check if a list is empty](http://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty)

```python
if not a:
    print "List is empty"
```

### empty a list

```python
del l[:]
```

### shuffle a list

```python
from random import shuffle
# works in place
l = range(10)
shuffle(l)
```

### [append vs extend](http://stackoverflow.com/questions/252703/python-append-vs-extend)

append:

```python
x = [1, 2, 3]
x.append([4, 5])
# [1, 2, 3, [4, 5]]
```

extend:

```python
x = [1, 2, 3]
x.extend([4, 5])
# [1, 2, 3, 4, 5]
```

### [split a list into evenly sized chunks](http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python)

Here’s a generator that yields the chunks you want:

```python
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
```

### [finding the index of an item](http://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python)

```python
>>> ["foo","bar","baz"].index('bar')
1
```

### [sort a list of dictionaries by values of the dictionary](http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python)[¶](https://snippets.readthedocs.io/en/latest/list.html#sort-a-list-of-dictionaries-by-values-of-the-dictionary)

```python
newlist = sorted(list_to_be_sorted, key=lambda k: k['name'])
```

### [randomly select an item from a list](http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python)

```python
import random

foo = ['a', 'b', 'c', 'd', 'e']
random.choice(foo)
```

### list comprehension

```python
new_list = [i * 2 for i in [1, 2, 3]]
```

## Dictionary

Snippets on dict manipulation.

### [merge (union) two Python dictionaries](http://stackoverflow.com/questions/38987/how-can-i-merge-union-two-python-dictionaries-in-a-single-expression)

```python
>>> x = {'a':1, 'b': 2}
>>> y = {'b':10, 'c': 11}
>>> z = x.copy()
>>> z.update(y)
{'a': 1, 'c': 11, 'b': 10}

```

### [create a dictionary with list comprehension](http://stackoverflow.com/questions/1747817/python-create-a-dictionary-with-list-comprehension)

In Python 2.6 (or earlier), use the dict constructor:

```python
d = dict((key, value) for (key, value) in sequence)

```

In Python 2.7+ or 3, you can just use the dict comprehension syntax directly:

```python
d = {key: value for (key, value) in sequence}
```

## Class

Snippets on classes.

### New-style and classic classes

Classes and instances come in two flavors: old-style and new-style. For more details, check out [New-style and classic classes](https://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes)

### print a object

```python
Class User(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return self.name
```

## Decorator

Snippets about decorators.

### decorators 101

Let’s begin with syntactic sugar:

```python
@EXPR
def add(a, b):
    return a + b

# The same thing as

def add(a, b):
    return a + b
add = EXPR(add)

@EXPR(ARG)
def add(a, b):
    return a + b

# The same thing as

def add(a, b):
    return a + b
add = EXPR(ARG)(add)

```

### good decorator

We want to run a function for certain times, if you do not know what does`functools.wraps` do, check out [What does functools.wraps do](http://stackoverflow.com/questions/308999/what-does-functools-wraps-do):

```python
from functools import wraps

def spam(repeats):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(repeats):
                func(*args, **kwargs)
        return wrapper
    return decorator

@spam(11)
def talk(word):
    """talk docstring"""
    print word

```

### method decorator

We need one decorator that makes function to method decorators:

```python
from functools import update_wrapper

class MethodDecoratorDescriptor(object):

    def __init__(self, func, decorator):
        self.func = func
        self.decorator = decorator

    def __get__(self, obj, type=None):
        return self.decorator(self.func.__get__(obj, type))

def method_decorator(decorator):
    def decorate(f):
        return MethodDecoratorDescriptor(f, decorator)
    return decorate

# usage
def spam(f):
    def wrapper(value):
        return f(value) + ":spamed"
    return update_wrapper(wrapper, f)

class MyClass(object):

    @method_decorator(spam)
    def my(self, value):
        return value

foo = MyClass()
print foo.my('hello')
```

## Iterator And Generator

Snippets about iterators and generators.

### [iterator - the Python yield keyword explained](http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained)

Iterables:

```python
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
```

Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly:

```python
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
```

Yield is a keyword that is used like return, except the function will return a generator:

```python
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

### [how do I determine if an object is iterable](http://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable)

Duck typing:

```python
try:
    iterator = iter(theElement)
except TypeError:
    # not iterable
else:
    # iterable
```

Type checking, need at least Python 2.6 and work only for new-style classes:

```python
import collections

if isinstance(theElement, collections.Iterable):
    # iterable
else:
    # not iterable
```

## Descriptor

Snippets about descriptors.

### descriptors 101

What is descriptor:

- __get__
- __set__
- __delete__
- Common descriptors: function, property

Demo:

```python
>>> class Demo(object):
...     def hello(self):
...         pass
...
>>> Demo.hello
<unbound method Demo.hello>
>>> Demo.__dict__['hello']
<function hello at 0x102b17668>
>>> Demo.__dict__['hello'].__get__(None, Demo)
<unbound method Demo.hello>
>>>
>>> Demo().hello
<bound method Demo.hello of <__main__.Demo object at 0x102b28550>>
>>> Demo.__dict__['hello'].__get__(Demo(), Demo)
<bound method Demo.hello of <__main__.Demo object at 0x102b285d0>>

```

### data and non-data descriptors

If an object defines both `__get__` and `__set__`, it is considered a data descriptor. Descriptors that only define `__get__` are called non-data descriptors.

Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance’s dictionary. If an instance’s dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence. If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.

Demo:

```python
class Demo(object):

    def __init__(self):
        self.val = 'demo'

    def __get__(self, obj, objtype):
        return self.val


class Foo(object):

    o = Demo()
```

```python
>>> f = Foo()
>>> f.o
'demo'
>>> f.__dict__['o'] = 'demo2'
>>> f.o
'demo2'
```

Now we add `__set__`:

```python
class Demo(object):

    def __init__(self):
        self.val = 'demo'

    def __get__(self, obj, objtype):
        return self.val

    def __set__(self, obj, val):
        self.val = val
```

```python
>>> f = Foo()
>>> f.o
'demo'
>>> f.__dict__['o'] = 'demo2'
>>> f.o
'demo'
>>> f.o = 'demo3'
>>> f.o
'demo3'
```

### better way to write property

Let’s just see the code:

```python
class Foo(object):

    def _get_thing(self):
        """Docstring"""
        return self._thing

    def _set_thing(self, value):
        self._thing = value

    thing = property(_get_thing, _set_thing)
    del _get_thing, _set_thing
```

### cached property

Just grab it from django source:

```python
class cached_property(object):
    """
    Decorator that creates converts a method with a single
    self argument into a property cached on the instance.
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, type):
        res = instance.__dict__[self.func.__name__] = self.func(instance)
        return res
```

## Context Manager

Snippets about with blocks.

### open and close files

```python
with open('data.txt') as f:
    data = f.read()
```

### threading locks

```python
lock = threading.Lock()

with lock:
    print 'do something'
```

### ignore exceptions

```python
from contextlib import contextmanager

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

with ignored(ValueError):
    int('string')
```

### assert raises

This one is taken from Flask source:

```python
from unittest import TestCase

class MyTestCase(TestCase):
    def assert_raises(self, exc_type):
        return _ExceptionCatcher(self, exc_type)

class _ExceptionCatcher(object):

    def __init__(self, test_case, exc_type):
        self.test_case = test_case
        self.exc_type = exc_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        exception_name = self.exc_type.__name__
        if exc_type is None:
            self.test_case.fail('Expected exception of type %r' %
                                exception_name)
        elif not issubclass(exc_type, self.exc_type):
            reraise(exc_type, exc_value, tb)
        return True

class DictTestCase(MyTestCase):

    def test_empty_dict_access(self):
        d = {}
        with self.assert_raises(KeyError):
            d[42]
```

## Method

Snippets about method.

### method 101

Instancemethods take `self` argument, classmethods take `cls` argument, staticmethods take no magic argument(not very useful).

```python
class FancyDict(dict):
    @classmethod
    def fromkeys(cls, keys, value=None):
        data = [(key, value) for key in keys]
        return cls(data)
```

```python
>>> FancyDict(key1='value1', key2='value2', key3='value3')
{'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
>>> FancyDict.fromkeys(['key1', 'key2'], 'value')
{'key2': 'value', 'key1': 'value'}
```

We are gonna talk a little more about classes, `__slots__`, you can use it to omit dict of python instances and reduce memory use in the end:

```python
class Tiny(object):
    __slots__ = ['value']
    def __init__(self, value):
        self.value = value
t = Tiny(1)
```

```python
>>> t.value
1
>>> t.value2 = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Tiny' object has no attribute 'value2'
```

Then talk a little about `__new__`, this is the actual constructor method of one instance, and it is one static method:

```python
class WrappingInt(int):
    __slots__ = []
    def __new__(cls, value):
        value = value % 255
        self = int.__new__(cls, value)
        return self

wrapping_int = WrappingInt(256)

>>> wrapping_int
1
```

## Metaclass

Snippets about metaclasses.

### metaclasses 101

In Python, everything is one object. Take CPython for example, we have PyObject, everything else is inherited from it, and each PyObject has one type attribute, PyTypeObject, actually PyTypeObject is one PyObject by itself too, so PyTypeObject has one type attribute, PyTypeType, PyTypeType has type attribute too, which is PyTypeType itself. So come back to Python, we have object, each object has one type, and the type of `type` is `type`.

You can also have a look on this stack overflow question [What is a metaclass in Python](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python).

Ok, in Python, everything is simple, so you can just treat metaclass as the class that creates a class. This is useful for post-processing classes, and is capable of much more magic(Dangerous though):

```python
class ManglingType(type):
    def __new__(cls, name, bases, attrs):
        for attr, value in attrs.items():
            if attr.startswith("__"):
                continue
            attrs["foo_" + attr] = value
            del attrs[attr]
        return type.__new__(cls, name, bases, attrs)

class MangledClass:
    __metaclass__ = ManglingType

    def __init__(self, value):
        self.value = value

    def test(self):
        return self.value

mangled = MangledClass('test')

>>> mangled.test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MangledClass' object has no attribute 'test'
>>> mangled.foo_test()
'test'
```

## Performance[¶](https://snippets.readthedocs.io/en/latest/performance.html#performance)

Snippets on Python running performance.

### [why does Python code run faster in a function](http://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function)

You might ask why it is faster to store local variables than globals. This is a CPython implementation detail.

Remember that CPython is compiled to bytecode, which the interpreter runs. When a function is compiled, the local variables are stored in a fixed-size array (not a dict) and variable names are assigned to indexes. This is possible because you can’t dynamically add local variables to a function. Then retrieving a local variable is literally a pointer lookup into the list and a refcount increase on the PyObject which is trivial.

Contrast this to a global lookup (`LOAD_GLOBAL`), which is a true dict search involving a hash and so on. Incidentally, this is why you need to specify global i if you want it to be global: if you ever assign to a variable inside a scope, the compiler will issue `STORE_FAST` for its access unless you tell it not to.

By the way, global lookups are still pretty optimised. Attribute lookups foo.bar are the really slow ones!

## Module

Snippets on packages and modules.

### get all module files

```python
def _iter_module_files():
    for module in sys.modules.values():
        filename = getattr(module, '__file__', None)
        if filename:
            if filename[-4:] in ('.pyc', '.pyo'):
                filename = filename[:-1]
            yield filename
```

### dynamic module import

```python
def import_string(import_name):
    """Import a module based on a string.

    :param import_name: the dotted name for the object to import.
    :return: imported object
    """
    if '.' in import_name:
        module, obj = import_name.rsplit('.', 1)
    else:
        return __import__(import_name)
    return getattr(__import__(module, None, None, [obj]), obj)
```

## nput and Ouput

Snippets about input and output.

### [read from stdin](http://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python)

```python
import sys

for line in sys.stdin:
    print line
```

### [print to stderr](http://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python)[¶](https://snippets.readthedocs.io/en/latest/io.html#print-to-stderr)

```python
print >> sys.stderr, 'spam'
```

## URL

Snippets for url.

### url quote

```python
from urllib import quote_plus

quoted = quote_plus(url)
```

### url encode

```python
from urllib import urlencode

encoded = urlencode({'key': 'value'})
encoded = urlencode([('key1', 'value1'), ('key2', 'value2')])
```

## HTTP

Snippets for http.

### simple http web server

```python
$ python -m SimpleHTTPServer [port]
```

### http get

```python
import urllib2
urllib2.urlopen("http://example.com/").read()
```

### [http head](http://stackoverflow.com/questions/107405/how-do-you-send-a-head-http-request-in-python)

```python
>>> import httplib
>>> conn = httplib.HTTPConnection("www.google.com")
>>> conn.request("HEAD", "/index.html")
>>> res = conn.getresponse()
>>> print res.status, res.reason
200 OK
```

### http post

```python
>>> import httplib, urllib
>>> params = urllib.urlencode({'key': 'value'})
>>> headers = {"Content-type": "application/x-www-form-urlencoded",
...            "Accept": "text/plain"}
>>> conn = httplib.HTTPConnection("www.example.com")
>>> conn.request("POST", "", params, headers)
>>> response = conn.getresponse()
>>> print response.status, response.reason
200 OK
>>> conn.close()
```

### [http put](http://stackoverflow.com/questions/111945/is-there-any-way-to-do-http-put-in-python)

```python
import urllib2
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://example.org', data='your_put_data')
request.add_header('Content-Type', 'your/contenttype')
request.get_method = lambda: 'PUT'
url = opener.open(request)
```

## File

Snippets about files and folders manipulation.

### [check if file exists](http://stackoverflow.com/questions/82831/how-do-i-check-if-a-file-exists-using-python)

If you need to be sure it’s a file:

```python
import os.path
os.path.isfile(filename)
```

### [unicode (utf8) reading and writing to files](http://stackoverflow.com/questions/491921/unicode-utf8-reading-and-writing-to-files-in-python)

It is easier to use the open method from the codecs module:

```python
>>> import codecs
>>> f = codecs.open("test", "r", "utf-8")
>>> f.read()
```

### [extracting extension from filename](http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python)

```python
import os
filename, ext = os.path.splitext('/path/to/somefile.ext')
```

### [get file creation & modification date/times](http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python)

ctime() does not refer to creation time on *nix systems, but rather the last time the inode data changed:

```python
import os.path, time
print "last modified: %s" % time.ctime(os.path.getmtime(file))
print "created: %s" % time.ctime(os.path.getctime(file))
```

### [find current directory and file’s directory](http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory)

```python
os.getcwd()
os.path.dirname(os.path.realpath(__file__))
```

### [remove/delete a folder that is not empty](http://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty-with-python)

```python
import shutil

shutil.rmtree('/folder_name')
```

### recursively walk a directory

```python
import os
root = 'your root path here'

# dirs are the directory list under dirpath
# files are the file list under dirpath
for dirpath, dirs, files in os.walk(root):
    for filename in files:
        fullpath = os.path.join(dirpath, filename)
        print fullpath
```

### get file size

```python
>>> import os
>>> statinfo = os.stat('index.rst')
>>> statinfo.st_size
487
```

### [reading binary file](http://stackoverflow.com/questions/1035340/reading-binary-file-in-python)

```python
with open("myfile", "rb") as f:
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        byte = f.read(1)
```

## Email

Snippets about email.

### [sending email with python](http://stackoverflow.com/questions/6270782/sending-email-with-python)

I recommend that you use the standard packages email and smtplib together:

```python
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Create a text/plain message
msg = MIMEText(body)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
```

For multiple destinations:

```python
# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Our family reunion'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = me
msg['To'] = COMMASPACE.join(family)
msg.preamble = 'Our family reunion'

# Assume we know that the image files are all in PNG format
for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
    fp = open(file, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

# Send the email via our own SMTP server.
s = smtplib.SMTP('localhost')
s.sendmail(me, family, msg.as_string())
s.quit()
```

### [sending mail via sendmail from python](http://stackoverflow.com/questions/73781/sending-mail-via-sendmail-from-python)

If I want to send mail not via SMTP, but rather via sendmail:

```python
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

msg = MIMEText("Here is the body of my message")
msg["From"] = "me@example.com"
msg["To"] = "you@example.com"
msg["Subject"] = "This is the subject."
p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
p.communicate(msg.as_string())
```

## Datetime

Snippets about datetime.

### [converting string into datetime](http://stackoverflow.com/questions/466345/converting-string-into-datetime)

```python
from datetime import datetime

date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
```

## Subprocess

Snippets about subprocesses.

### [calling an external command](http://stackoverflow.com/questions/89228/calling-an-external-command-in-python)

```python
from subprocess import call
call(["ls", "-l"])
```

### subprocess input, output and returncode[¶](https://snippets.readthedocs.io/en/latest/subprocess.html#subprocess-input-output-and-returncode)

```python
from subprocess import Popen, PIPE

p = Popen(["ls", "-l"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
std_input = "/"
out, err = p.communicate(std_input)
returncode = p.returncode
```

### use string to call subprocess instead of list

```python
from subprocess import call
import shlex

command = "ls -l"
call(shlex.split(command))
```