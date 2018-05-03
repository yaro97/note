# Redis备忘

## 简介

NoSQL数据库：key-value，文档型...

Redis: [Remote Directory Server] 远程服务器字典。

保存在内存中，读取速度快，支持持久化（周期性保存到磁盘）

**官网参考**：https://redis.io/documentation

## 下载、安装、启动

3.x   x为偶数为稳定版本，奇数为测试版本。

```sh
wget http://download.redis.io/releases/redis-4.0.9.tar.gz
tar xzf redis-4.0.9.tar.gz
cd redis-4.0.9
make  # 编译、安装
make install # 写入/usr/local/bin/目录。可选。
```

启动

```sh
redis-server  # 前提：写入到/usr/local/bin/
redis-server /etc/redis.conf  # 前提，把redis.conf复制到/etc/
redis-server /etc/redis.conf --port 6666  # 指定端口（覆盖conf文件中的配置端口）
redis-cli  # 默认：本地主机+默认端口（6379）
redis-cli -h localhost -p 6666
# 修改redis.conf中daemonize == yes，可以以服务的方式运行；
```

结束

```sh
shutdown  # 在redis-cli端输入，会让服务端终止所有连接，并根据配置文件进行持久化，并结束服务；
# 或者，直接结束redis-server进程
```

## 命令返回值

1》状态回复

```sh
# 不区分大小写，建议系统命令大写。
127.0.0.1:6379> SET a b
OK
127.0.0.1:6379> ping
PONG
```

2》错误回复

```sh
# 以error开头
127.0.0.1:6379> nothing
(error) ERR unknown command 'nothing'
```

3》整数回复

```sh
127.0.0.1:6379> DBSIZE
(integer) 1
```

4》字符串回复

```sh
127.0.0.1:6379> SET name yaro
OK
127.0.0.1:6379> GET name
"yaro"
127.0.0.1:6379> GET test
(nil)  # 表示空结果
```

5》多行字符串回复

```sh
127.0.0.1:6379> KEYS  *  # 返回所有键值
1) "a"
2) "name"
```

## Redis配置选项相关内容

1》动态设置/获取配置选项的值

```sh
# 1、启动时设置日志级别
redis-server redis.conf --loglevel warnig  
# 2、启动后动态的设置、获取
127.0.0.1:6379> CONFIG GET loglevel  # 获取日志级别
1) "loglevel"
2) "notice"
127.0.0.1:6379> CONFIG GET port
1) "port"
2) "6379"
127.0.0.1:6379> CONFIG SET loglevel warning  # 设置日志级别
OK
127.0.0.1:6379> CONFIG GET loglevel
1) "loglevel"
2) "warning"
# 3、提前设置redis.conf配置文件-启动时加载。
# ======================== 通用/连接选项
daemonize yes  # 是否以daemon方式启动。
port 6379  # 默认端口
bind 127.0.0.1  # 默认绑定的主机地址
timeout 0  # 当客户端闲置多久关闭连接，0代表未启用该选项。
loglevel notice  # 默认的日志级别（debug:很详细信息，适合开发和调试；verbos：很多不太有用的信息；notice：适合生产环境信息；warning：只提示警告的信息。）
logfile ""  # 日志的记录方式，默认为标准输出。
databases 16  # 默认数据库的数量（0-15），默认使用第0个数据库，可以使用 “SELECT 1” 使用第1个数据库。
# ==========SNAPSHOTTING========= 快照相关（保存数据到磁盘）
save 900 1  # 900s内有1个改变，写入磁盘
save 300 10  # 300s内有10个更改，。。。
save 60 10000  # 60s内有10000个更改，。。。。
rdbcompression yes  # 写入 .rdb数据文件时，是否压缩，压缩会增加cpu负载。
dbfilename dump.rdb  # 指定数据库文件名。
dir ./  # 指定数据库文件保存目录（默认是当前目录）。
# =======其他高级选项=====自己研究
```

## Redis String类型及相关命令

Redis支持五种类型：

- String类型：

```sh
一个建最大能存储512M，
# 1》SET：设置key对应的值为value
语法： SET key value [EX seconds] [PX miliseconds] [NX|XX]  # EX PX是同类型参数，重复设置的话，后面的覆盖前面的。
注意：如果key存在，同名会产生覆盖。
eg: SET testStr1 "This is a string"
EX - 过期时间-秒
PX - 过期时间-毫秒
NX - key不存在时设置
XX- key存在时设置
# 2》GET：根据key找到对应的值
语法：GET key
127.0.0.1:6379> GET testStr1
"THis is a tes"
注意：如果key不存在，会返回nil；如何key不是字符串，会报错。
# 3》GETRANGE：返回字符串中一部分。
语法：GETRANGE key start end
eg:GETRANGE testStr1 -1 4  # 0开始，可以使用负数。
127.0.0.1:6379> GETRANGE testStr1 0 -2
"THis is a tes"
# 4》 GETSET:返回旧的值，并设置指定key值
语法：GETSET key value
127.0.0.1:6379> SET testStr3 'king'
OK
127.0.0.1:6379> GETSET testStr3 'queen'
"king"
127.0.0.1:6379> GET testStr3
"queen"
# 5》 MSET:一次性设置多个
127.0.0.1:6379> MSET testStr5 'king' testStr6 'yaro' testStr7 'queen'
OK
# 6》 MGET:一次性获得多个
127.0.0.1:6379> MGET testStr5 testStr7 coco
1) "king"
2) "queen"
3) (nil)
# 7》 STRLEN：获取字符串长度
127.0.0.1:6379> STRLEN testStr5
(integer) 4
127.0.0.1:6379> STRLEN testStr5_nil
(integer) 0
# 8》SETRANGE：设定（改变）字符串的一部分
redis> SET key1 "Hello World"
"OK"
redis> SETRANGE key1 6 "Redis"
(integer) 11
redis> GET key1
"Hello Redis"
redis> SETRANGE key2 6 "Redis"
(integer) 11
redis> GET key2
"\u0000\u0000\u0000\u0000\u0000\u0000Redis"  # 没有的位置填充\u0000
# 9》 SETNX：不存在时设置，存在时忽略，防止覆盖之前设定的值。
127.0.0.1:6379> EXISTS key1  # 检测是否存在
(integer) 1
127.0.0.1:6379> SETNX key1 'bb'  # 返回0，表示设置失败。
(integer) 0
Time to live:设置key的过期时间（s），过期失效。相当于SET 和 EXPIRE 命令的结合。
127.0.0.1:6379> SETEX expireStr 60 'xxx'
OK
127.0.0.1:6379> GET expireStr
"xxx"
127.0.0.1:6379> TTL expireStr  # 查看还有多久过期 Time to live
(integer) 42
127.0.0.1:6379> TTL expireStr
(integer) 38
# 10》 MSETNX：MSET和SETNX的结合，所有key都不存在才设置成功，只要有一个存在，设置失败。
# 11》 PSETEX：类似SETEX，但是用毫秒（milliseconds）计算。
redis> PSETEX mykey 1000 "Hello"
"OK"
redis> PTTL mykey
(integer) 999
redis> GET mykey
"Hello"
# 12》 INCR：自增+1
127.0.0.1:6379> SET number 1
OK
127.0.0.1:6379> INCR number  # 不设置key自动设置为0.key不是数字会报错。
(integer) 2
127.0.0.1:6379> INCR number
(integer) 3
127.0.0.1:6379> GET number
"3"
# 13》 INCRBY：指定增量。
127.0.0.1:6379> INCRBY key3 4  # 默认为0
(integer) 4
127.0.0.1:6379> GET key3
"4"
# 14》INCRBYFLOAT：增量为浮点数（整数）
127.0.0.1:6379> INCRBYFLOAT key3 0.8
"4.8"
127.0.0.1:6379> INCRBYFLOAT key3 0.8
"5.6"
# 15》DECR/DECRBY：自减  # 没有DECRBYFLOAT(可以通过自增负数实现)
# 12》APPEND：追加到字符串后面，没有字符串的话，等同于SET命令。
127.0.0.1:6379> SET testString 'hello'
OK
127.0.0.1:6379> APPEND testString 'World'
(integer) 10
127.0.0.1:6379> GET testString
"helloWorld"
```

- Hash类型：



```sh
# redis.conf中的Hash配置
hash-max-ziplist-entries 512  # 512字节
hash-max-ziplist-value 64  # 字段数目

# 1》 HSET：将设哈希表key中的某个field设置成制定的value，可以重新赋值。
127.0.0.1:6379> HSET userInfo username 'king'
(integer) 1
127.0.0.1:6379> HSET userInfo password '123456'
(integer) 1
127.0.0.1:6379> HSET userInfo email '3333@qq.com'
(integer) 1
# 2》 HGET：获得哈希表指定key中的某个field的value。
127.0.0.1:6379> HGET userInfo email
"3333@qq.com"
# 3》 HSETNX：只有field不存在才设置成功
127.0.0.1:6379> HSETNX testHash1 test 'a'
(integer) 1
127.0.0.1:6379> HSETNX testHash1 test '11'
(integer) 0  # 返回0，表示不成功
127.0.0.1:6379> HGET testHash1 test
"a"  # 依然是‘a’
# 4》 HMSET：设置多个field，也会重新赋值
127.0.0.1:6379> HMSET userInfo2 username 'king' password '123' nickname 'dupy'
OK
# 5》 HMGET：获得多个field
127.0.0.1:6379> HMGET userInfo2 username nickname  foo
1) "king"
2) "dupy"
3) (nil)
# 6》 HGETALL：获得所有的field和value
127.0.0.1:6379> HGETALL userInfo
1) "username"
2) "king"
3) "password"
4) "123456"
5) "email"
6) "3333@qq.com"
# 7》 HKEYS:获取所有的field
127.0.0.1:6379> HKEYS userInfo2
1) "username"
2) "password"
3) "nickname"
4) "email"
# 8》 HVALS:获取所有的value
127.0.0.1:6379> HVALS userInfo2
1) "king"
2) "123"
3) "dupy"
4) "@@@"
# 9》 HEXISTS:检查field是否存在
127.0.0.1:6379> HEXISTS userInfo2 name
(integer) 0
# 10》 HLEN:获取field数量
127.0.0.1:6379> HLEN userInfo2
(integer) 4
# 11》 HINCRBY:对某个field（Integer）进行增量计算
127.0.0.1:6379> HINCRBY userInfo2 password 5
(integer) 128
# 12》 HINCRBYFLOAT:对某个field（Integer）进行增量浮点计算
127.0.0.1:6379> HINCRBYFLOAT userInfo2 password -5.1
"122.9"
# 13》 HDEL:删除指定的field
127.0.0.1:6379> HDEL userInfo2 nickname email
(integer) 2
127.0.0.1:6379> HKEYS userInfo2
1) "username"
2) "password"

```



List类型：

Set类型

Zset有序集合类型





