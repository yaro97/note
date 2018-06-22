# Python时间模块

## A. time 模块（就用它吧！）

> datetime是time模块的重新包装，包装了更多的类，但是用起来貌似也不怎么顺溜。

time模块中时间表现的格式主要有三种：

　　a、timestamp时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量

　　b、struct_time时间元组，共有九个元素组。

　　c、format time 格式化时间，已格式化的结构使时间更具可读性。包括自定义格式和固定格式。

###  1、时间格式转换图：

![img](https://images2015.cnblogs.com/blog/996085/201610/996085-20161026171443546-488752980.png)

 

### 2、主要time生成方法和time格式转换方法实例：

```python
import time

# 生成timestamp
time.time()
# 1477471508.05
#struct_time to timestamp
time.mktime(time.localtime())
#生成struct_time
# timestamp to struct_time 本地时间
time.localtime()
time.localtime(time.time())
# time.struct_time(tm_year=2016, tm_mon=10, tm_mday=26, tm_hour=16, tm_min=45, tm_sec=8, tm_wday=2, tm_yday=300, tm_isdst=0)

# timestamp to struct_time 格林威治时间
time.gmtime()
time.gmtime(time.time())
# time.struct_time(tm_year=2016, tm_mon=10, tm_mday=26, tm_hour=8, tm_min=45, tm_sec=8, tm_wday=2, tm_yday=300, tm_isdst=0)

#format_time to struct_time
time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')
# time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1)

#生成format_time
#struct_time to format_time
time.strftime("%Y-%m-%d %X")
time.strftime("%Y-%m-%d %X",time.localtime())
# 2016-10-26 16:48:41


#生成固定格式的时间表示格式
time.asctime(time.localtime())
time.ctime(time.time())
# Wed Oct 26 16:45:08 2016
```

**struct_time元组元素结构**

```
属性                            值
tm_year（年）                  比如2011 
tm_mon（月）                   1 - 12
tm_mday（日）                  1 - 31
tm_hour（时）                  0 - 23
tm_min（分）                   0 - 59
tm_sec（秒）                   0 - 61
tm_wday（weekday）             0 - 6（0表示周日）
tm_yday（一年中的第几天）        1 - 366
tm_isdst（是否是夏令时）        默认为-1
```

**format time结构化表示**

| **格式** | **含义**                                                     |
| -------- | ------------------------------------------------------------ |
| %a       | 本地（locale）简化星期名称                                   |
| %A       | 本地完整星期名称                                             |
| %b       | 本地简化月份名称                                             |
| %B       | 本地完整月份名称                                             |
| %c       | 本地相应的日期和时间表示                                     |
| %d       | 一个月中的第几天（01 - 31）                                  |
| %H       | 一天中的第几个小时（24小时制，00 - 23）                      |
| %I       | 第几个小时（12小时制，01 - 12）                              |
| %j       | 一年中的第几天（001 - 366）                                  |
| %m       | 月份（01 - 12）                                              |
| %M       | 分钟数（00 - 59）                                            |
| %p       | 本地am或者pm的相应符                                         |
| %S       | 秒（01 - 61）                                                |
| %U       | 一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。 |
| %w       | 一个星期中的第几天（0 - 6，0是星期天）                       |
| %W       | 和%U基本相同，不同的是%W以星期一为一个星期的开始。           |
| %x       | 本地相应日期                                                 |
| %X       | 本地相应时间                                                 |
| %y       | 去掉世纪的年份（00 - 99）                                    |
| %Y       | 完整的年份                                                   |
| %Z       | 时区的名字（如果不存在为空字符）                             |
| %%       | ‘%’字符                                                      |

> 常见结构化时间组合：
>
> ```
> print time.strftime("%Y-%m-%d %X")
> #2016-10-26 20:50:13
> ```

### 3、time加减

```python
#timestamp加减单位以秒为单位
import time
t1 = time.time()
t2=t1+10

print time.ctime(t1)#Wed Oct 26 21:15:30 2016
print time.ctime(t2)#Wed Oct 26 21:15:40 2016
```

### 4、其他

```python
sleep(secs)
# 线程推迟指定的时间运行，单位为秒。
 
clock()
# 这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。
# 而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行
# 时间，即两次时间差。
```

## B. datetime模块

datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。

### 1、date类

datetime.date(year, month, day)

静态方法和字段

```
date.max、date.min：date对象所能表示的最大、最小日期；
date.resolution：date对象表示日期的最小单位。这里是天。
date.today()：返回一个表示当前本地日期的date对象；
date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；
```

方法和属性

```
d1 = date(2011,06,03)#date对象
d1.year、date.month、date.day：年、月、日；
d1.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
d1.timetuple()：返回日期对应的time.struct_time对象；
d1.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
d1.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
d1.isocalendar()：返回格式如(year，month，day)的元组；
d1.isoformat()：返回格式如'YYYY-MM-DD’的字符串；
d1.strftime(fmt)：和time模块format相同。
```

### 2、time类

datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ) 

静态方法和字段

```
time.min、time.max：time类所能表示的最小、最大时间。其中，time.min = time(0, 0, 0, 0)， time.max = time(23, 59, 59, 999999)；
time.resolution：时间的最小单位，这里是1微秒；
```

方法和属性

```
t1 = datetime.time(10,23,15)#time对象
t1.hour、t1.minute、t1.second、t1.microsecond：时、分、秒、微秒；
t1.tzinfo：时区信息；
t1.replace([ hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )：创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性（原有对象仍保持不变）；
t1.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
t1.strftime(fmt)：同time模块中的format；
```

### 3、datetime类

datetime相当于date和time结合起来。
datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )

静态方法和字段

```
datetime.today()：返回一个表示当前本地时间的datetime对象；
datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
datetime.utcnow()：返回一个当前utc时间的datetime对象；#格林威治时间
datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
datetime.combine(date, time)：根据date和time，创建一个datetime对象；
datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；
```

方法和属性

```
dt=datetime.now()#datetime对象
dt.year、month、day、hour、minute、second、microsecond、tzinfo：
dt.date()：获取date对象；
dt.time()：获取time对象；
dt. replace ([ year[ , month[ , day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] ] ] ])：
dt. timetuple ()
dt. utctimetuple ()
dt. toordinal ()
dt. weekday ()
dt. isocalendar ()
dt. isoformat ([ sep] )
dt. ctime ()：返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
dt. strftime (format)
```

### 4.timedelta类，时间加减

使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。

```
#coding:utf-8
from  datetime import *

dt = datetime.now()
#日期减一天
dt1 = dt + timedelta(days=-1)#昨天
dt2 = dt - timedelta(days=1)#昨天
dt3 = dt + timedelta(days=1)#明天
delta_obj = dt3-dt
print type(delta_obj),delta_obj#<type 'datetime.timedelta'> 1 day, 0:00:00
print delta_obj.days ,delta_obj.total_seconds()#1 86400.0
```

###  5、tzinfo时区类

```python
#! /usr/bin/python
# coding=utf-8

from datetime import datetime, tzinfo,timedelta

"""
tzinfo是关于时区信息的类
tzinfo是一个抽象类，所以不能直接被实例化
"""
class UTC(tzinfo):
    """UTC"""
    def __init__(self,offset = 0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)

#北京时间
beijing = datetime(2011,11,11,0,0,0,tzinfo = UTC(8))
print "beijing time:",beijing
#曼谷时间
bangkok = datetime(2011,11,11,0,0,0,tzinfo = UTC(7))
print "bangkok time",bangkok
#北京时间转成曼谷时间
print "beijing-time to bangkok-time:",beijing.astimezone(UTC(7))

#计算时间差时也会考虑时区的问题
timespan = beijing - bangkok
print "时差:",timespan

#Output==================
# beijing time: 2011-11-11 00:00:00+08:00
# bangkok time 2011-11-11 00:00:00+07:00
# beijing-time to bangkok-time: 2011-11-10 23:00:00+07:00
# 时差: -1 day, 23:00:00
```

## C. Calendar模块

此模块的函数都是日历相关的，例如打印某月的字符月历。

星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用`calendar.setfirstweekday()`函数。模块包含了以下内置函数：

| 序号 | 函数及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | `calendar.calendar(year,w=2,l=1,c=6)` 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。 |
| 2    | `calendar.firstweekday( )` 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。 |
| 3    | `calendar.isleap(year)` 是闰年返回True，否则为false。        |
| 4    | `calendar.leapdays(y1,y2)` 返回在Y1，Y2两年之间的闰年总数。  |
| 5    | `calendar.month(year,month,w=2,l=1)` 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。 |
| 6    | `calendar.monthcalendar(year,month)` 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。 |
| 7    | `calendar.monthrange(year,month)` 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。 |
| 8    | `calendar.prcal(year,w=2,l=1,c=6)` 相当于 print calendar.calendar(year,w,l,c). |
| 9    | `calendar.prmonth(year,month,w=2,l=1)` 相当于 print calendar.calendar（year，w，l，c）。 |
| 10   | `calendar.setfirstweekday(weekday)` 设置每周的起始日期码。0（星期一）到6（星期日）。 |
| 11   | `calendar.timegm(tupletime)` 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。 |
| 12   | `calendar.weekday(year,month,day)` 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。 |
