# Python format常用格式示例



## Basic formatting

Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate.

Since the elements are not represented by something as descriptive as a name this simple style should only be used to format a relatively small number of elements.

### Old

```python
'%s %s' % ('one', 'two')
```

### New

```python
'{} {}'.format('one', 'two')
```

### Output

```
one two
```

### Old

```python
'%d %d' % (1, 2)
```

### New

```python
'{} {}'.format(1, 2)
```

### Output

```
1 2
```

With new style formatting it is possible (and in Python 2.6 even mandatory) to give placeholders an explicit positional index.

This allows for re-arranging the order of display without changing the arguments.

> This operation is not available with old-style formatting.

### New

```python
'{1} {0}'.format('one', 'two')
```

### Output

```
two one
```

## Value conversion

The new-style simple formatter calls by default the [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__) method of an object for its representation. If you just want to render the output of `str(...)` or `repr(...)` you can use the `!s` or `!r` conversion flags.

In %-style you usually use `%s` for the string representation but there is `%r` for a `repr(...)` conversion.

### Setup

```python
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'
```

### Old

```python
'%s %r' % (Data(), Data())
```

### New

```python
'{0!s} {0!r}'.format(Data())
```

### Output

```
str repr
```

In Python 3 there exists an additional conversion flag that uses the output of `repr(...)` but uses `ascii(...)` instead.

### Setup

```python
class Data(object):

    def __repr__(self):
        return 'räpr'
```

### Old

```python
'%r %a' % (Data(), Data())
```

### New

```python
'{0!r} {0!a}'.format(Data())
```

### Output

```
räpr r\xe4pr
```

## Padding and aligning strings

By default values are formatted to take up only as many characters as needed to represent the content. It is however also possible to define that a value should be padded to a specific length.

Unfortunately the default alignment differs between old and new style formatting. The old style defaults to right aligned while for new style it's left.

Align right:

### Old

```python
'%10s' % ('test',)
```

### New

```python
'{:>10}'.format('test')
```

### Output

```
      test
```

Align left:

### Old

```python
'%-10s' % ('test',)
```

### New

```python
'{:10}'.format('test')
```

### Output

```
test      
```

Again, new style formatting surpasses the old variant by providing more control over how values are padded and aligned.

You are able to choose the padding character:

> This operation is not available with old-style formatting.

### New

```python
'{:_<10}'.format('test')
```

### Output

```
test______
```

And also center align values:

> This operation is not available with old-style formatting.

### New

```python
'{:^10}'.format('test')
```

### Output

```
   test   
```

When using center alignment where the length of the string leads to an uneven split of the padding characters the extra character will be placed on the right side:

> This operation is not available with old-style formatting.

### New

```python
'{:^6}'.format('zip')
```

### Output

```
 zip  
```

## Truncating long strings

Inverse to padding it is also possible to truncate overly long values to a specific number of characters.

The number behind a `.` in the format specifies the precision of the output. For strings that means that the output is truncated to the specified length. In our example this would be 5 characters.

### Old

```python
'%.5s' % ('xylophone',)
```

### New

```python
'{:.5}'.format('xylophone')
```

### Output

```
xylop
```

## Combining truncating and padding

It is also possible to combine truncating and padding:

### Old

```python
'%-10.5s' % ('xylophone',)
```

### New

```python
'{:10.5}'.format('xylophone')
```

### Output

```
xylop     
```

## Numbers

Of course it is also possible to format numbers.

Integers:

### Old

```python
'%d' % (42,)
```

### New

```python
'{:d}'.format(42)
```

### Output

```
42
```

Floats:

### Old

```python
'%f' % (3.141592653589793,)
```

### New

```python
'{:f}'.format(3.141592653589793)
```

### Output

```
3.141593
```

## Padding numbers

Similar to strings numbers can also be constrained to a specific width.

### Old

```python
'%4d' % (42,)
```

### New

```python
'{:4d}'.format(42)
```

### Output

```
  42
```

Again similar to truncating strings the precision for floating point numbers limits the number of positions after the decimal point.

For floating points the padding value represents the length of the complete output. In the example below we want our output to have at least 6 characters with 2 after the decimal point.

### Old

```python
'%06.2f' % (3.141592653589793,)
```

### New

```python
'{:06.2f}'.format(3.141592653589793)
```

### Output

```
003.14
```

For integer values providing a precision doesn't make much sense and is actually forbidden in the new style (it will result in a ValueError).

### Old

```python
'%04d' % (42,)
```

### New

```python
'{:04d}'.format(42)
```

### Output

```
0042
```

## Signed numbers

By default only negative numbers are prefixed with a sign. This can be changed of course.

### Old

```python
'%+d' % (42,)
```

### New

```python
'{:+d}'.format(42)
```

### Output

```
+42
```

Use a space character to indicate that negative numbers should be prefixed with a minus symbol and a leading space should be used for positive ones.

### Old

```python
'% d' % ((- 23),)
```

### New

```python
'{: d}'.format((- 23))
```

### Output

```
-23
```

### Old

```python
'% d' % (42,)
```

### New

```python
'{: d}'.format(42)
```

### Output

```
 42
```

New style formatting is also able to control the position of the sign symbol relative to the padding.

> This operation is not available with old-style formatting.

### New

```python
'{:=5d}'.format((- 23))
```

### Output

```
-  23
```

### New

```python
'{:=+5d}'.format(23)
```

### Output

```
+  23
```

## Named placeholders

Both formatting styles support named placeholders.

### Setup

```python
data = {'first': 'Hodor', 'last': 'Hodor!'}
```

### Old

```python
'%(first)s %(last)s' % data
```

### New

```python
'{first} {last}'.format(**data)
```

### Output

```
Hodor Hodor!
```

`.format()` also accepts keyword arguments.

> This operation is not available with old-style formatting.

### New

```python
'{first} {last}'.format(first='Hodor', last='Hodor!')
```

### Output

```
Hodor Hodor!
```

## Getitem and Getattr

New style formatting allows even greater flexibility in accessing nested data structures.

It supports accessing containers that support `__getitem__` like for example dictionaries and lists:

> This operation is not available with old-style formatting.

### Setup

```python
person = {'first': 'Jean-Luc', 'last': 'Picard'}
```

### New

```python
'{p[first]} {p[last]}'.format(p=person)
```

### Output

```
Jean-Luc Picard
```

### Setup

```python
data = [4, 8, 15, 16, 23, 42]
```

### New

```python
'{d[4]} {d[5]}'.format(d=data)
```

### Output

```
23 42
```

As well as accessing attributes on objects via `getattr()`:

> This operation is not available with old-style formatting.

### Setup

```python
class Plant(object):
    type = 'tree'
```

### New

```python
'{p.type}'.format(p=Plant())
```

### Output

```
tree
```

Both type of access can be freely mixed and arbitrarily nested:

> This operation is not available with old-style formatting.

### Setup

```python
class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]
```

### New

```python
'{p.type}: {p.kinds[0][name]}'.format(p=Plant())
```

### Output

```
tree: oak
```

## Datetime

New style formatting also allows objects to control their own rendering. This for example allows datetime objects to be formatted inline:

> This operation is not available with old-style formatting.

### Setup

```python
from datetime import datetime
```

### New

```python
'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))
```

### Output

```
2001-02-03 04:05
```

## Parametrized formats

Additionally, new style formatting allows all of the components of the format to be specified dynamically using parametrization. Parametrized formats are nested expressions in braces that can appear anywhere in the parent format after the colon.

Old style formatting also supports some parametrization but is much more limited. Namely it only allows parametrization of the width and precision of the output.

Parametrized alignment and width:

> This operation is not available with old-style formatting.

### New

```python
'{:{align}{width}}'.format('test', align='^', width='10')
```

### Output

```
   test   
```

Parametrized precision:

### Old

```python
'%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182)
```

### New

```python
'{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
```

### Output

```
Gib = 2.718
```

Width and precision:

### Old

```python
'%*.*f' % (5, 2, 2.7182)
```

### New

```python
'{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)
```

### Output

```
 2.72
```

The nested format can be used to replace *any* part of the format spec, so the precision example above could be rewritten as:

> This operation is not available with old-style formatting.

### New

```python
'{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3')
```

### Output

```
Gib = 2.72
```

The components of a date-time can be set separately:

> This operation is not available with old-style formatting.

### Setup

```python
from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)
```

### New

```python
'{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')
```

### Output

```
2001-02-03 04:05
```

The nested formats can be positional arguments. Position depends on the order of the opening curly braces:

> This operation is not available with old-style formatting.

### New

```python
'{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3)

```

### Output

```
     +2.72
```

And of course keyword arguments can be added to the mix as before:

> This operation is not available with old-style formatting.

### New

```python
'{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+')
```

### Output

```
     +2.72
```

## Custom objects

The datetime example works through the use of the `__format__()` magic method. You can define custom format handling in your own objects by overriding this method. This gives you complete control over the format syntax used.

> This operation is not available with old-style formatting.

### Setup

```python
class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'
```

### New

```python
'{:open-the-pod-bay-doors}'.format(HAL9000())
```

### Output

```
I'm afraid I can't do that.
```