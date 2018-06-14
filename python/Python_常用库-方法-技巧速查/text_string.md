string模块的很多功能都被添加到python的str类方法中了。

有以下常量还是比较有用的：
3
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.

string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.

string.digits
The string '0123456789'.

string.hexdigits
The string '0123456789abcdefABCDEF'.

string.octdigits
The string '01234567'.

string.punctuation
String of ASCII characters which are considered punctuation characters in the C locale.

string.printable
String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.

string.whitespace
A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
