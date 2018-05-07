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

## 和Key相关命令

Redis 键命令用于管理 redis 的键。 

```sh
# 1》 KEYS:返回所有的key，支持通配符（* ? [] \?）
127.0.0.1:6379> KEYS *
1) "testString1"
2) "userInfo"
3) "testString2"
# 2》 EXISTS:检测key是否存在
127.0.0.1:6379> EXISTS name
(integer) 0
# 3》 TYPE:返回key的类型
127.0.0.1:6379> type testString1
string
127.0.0.1:6379> type userInfo
hash
# 4》 EXPIRE:设置过期时间（seconds），再次设置覆盖。
127.0.0.1:6379> SET cache_page 'http://www.baidu.com'
OK
127.0.0.1:6379> EXPIRE cache_page 1000
(integer) 1
127.0.0.1:6379> TTL cache_page
(integer) 994
# 5》 EXPIREAT:设置过期时间（时间戳）
127.0.0.1:6379> EXPIREAT cache_page 1525424900
(integer) 1
127.0.0.1:6379> TTL cache_page
(integer) 133
# 6》 PEXPIRE:设置过期时间（milliseconds）
127.0.0.1:6379> SET cache_page 'http://www.baidu.com'
OK
127.0.0.1:6379> PEXPIRE cache_page 1000000
(integer) 1
127.0.0.1:6379> PTTL cache_page
(integer) 121
# 7》 PEXPIREAT:设置过期时间（milliseconds时间戳）
# 8》 TTL：返回key的剩余时间（秒）-time to live;永久的key返回-1，不存在的key返回-2；
# 9》 PTTL：返回key的剩余时间（毫秒）
# 10》 PERSIST：将含有过期时间的key设置为永久
# 11》 DEL：删除key
127.0.0.1:6379> DEL testString testString0
(integer) 1
# 12》 RANDOMKEY：随机返回一个key
# 13》 RENAME：重命名key名称
127.0.0.1:6379> RENAME key newkey
# 14》 RENAMENX：newkey必须不存在，才生效
# 15》 DUMP：序列化给定的key，返回序列化之后的指
# 16》 RESTORE：反序列化  ## ttl设置为0（毫秒）-代表永久生效
127.0.0.1:6379> SET testDump 'This is a text'
OK
127.0.0.1:6379> DUMP testDump
"\x00\x0eThis is a text\b\x00\xdc\xfcl?\x90%\x9e\xf2"
127.0.0.1:6379> RESTORE testDump1 0 "\x00\x0eThis is a text\b\x00\xdc\xfcl?\x90%\x9e\xf2"
OK
127.0.0.1:6379> get testDump1
"This is a text"
# 17》 MOVE：将当前数据库中的key移动到其他数据库
127.0.0.1:6379> SET testMove aaaa
OK
127.0.0.1:6379> MOVE testMove 1  # 将testMove移动到1数据库
(integer) 1
127.0.0.1:6379> GET testMove
(nil)
127.0.0.1:6379> SELECT 1  # 切换到1数据库
OK
127.0.0.1:6379[1]> GET testMove
"aaaa"
# 18》 其他命令：OBJECT MIGRATE SCAN SORT 后续再讲解
```

## Redis String类型及相关命令

Redis支持五种类型：String/Hash/List/Set/Zset类型

Redis 字符串数据类型的相关命令用于管理 redis 字符串值 

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

## Redis Hash类型及相关命令

Redis hash 是一个string类型的field和value的映射表，hash特别适合用于存储对象。

Redis 中每个 hash 可以存储$2^{32}-1$键值对（40多亿）。

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



## Redis List类型及相关命令

Redis列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

一个列表最多可以包含$2^{32}-1$ 个元素 (4294967295, 每个列表超过40亿个元素)。

内部通过`双向链表`实现，所以获取两端的元素速度较快。

```sh
# 1》 LPUSH:向List左端依次添加元素,key不存在会自动创建
127.0.0.1:6379> LPUSH myList a b c
(integer) 3
127.0.0.1:6379> LPUSH myList c d e
(integer) 6
127.0.0.1:6379> LRANGE myList 0 -1
1) "e"
2) "d"
3) "c"
4) "c"
5) "b"
6) "a"
# 2》 RPUSH:向List右端依次添加元素
RPUSH myList1 test1 test2 test3
# 3》 LPUSHX:只有key存在才会添加
# 4》 RPUSHX:只有key存在才会添加
# 5》 LPOP:弹出左侧元素。删除并返回
# 6》 RPOP:弹出右侧元素。删除并返回
# 7》 LLEN:返回列表长度
# 8》 LLEN:返回列表片段
LRANGE key start stop  # 0开始，-1结束
127.0.0.1:6379> LRANGE testList -2 -1
1) "b"
2) "c"
# 9》 LREM:删除指定value
LREM key count value
	# count>0 从左到右搜索，删除count个；
	# count<0 从右到左搜索，删除count个；
	# count=0 删除所有值为value的key；
# 10》 LINDEX:获取指定key的value
LINDEX key index
# 11》 LSET:设置指定key的value
LSET key index value
# 12》 LTRIM:对一个列表进行修剪(trim)，只保留指定区间内的元素，其他元素都将被删除。
LTRIM key start stop
# 13》 LINSERT:插入元素
LINSERT key BEFORE|AFTER pivot value
127.0.0.1:6379> LINSERT x BEFORE 'b' king
(integer) 5
127.0.0.1:6379> LRANGE x 0 -1
1) "d"
2) "c"
3) "king"
4) "b"
5) "a"
# 14》 RPOPLPUSH:将一个元素从一个列表转移到另一个列表
RPOPLPUSH source destination  # 源列表和目标列表相同
# 14》 BLPOP:LPOP的阻塞版本
BLPOP key [key ...] timeout  # TO为0表示阻塞时间无限大
127.0.0.1:6379> EXISTS myList3 # myList3不存在
(integer) 0
BLPOP myList3 0  # 会一直阻塞，知道LPUSH一个值（另外开启一个redis-cli）
```

## Redis Set类型及相关命令

Redis 的 Set 是 String 类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为$2^{32}-1$ (4294967295, 每个集合可存储40多亿个成员)。

```sh
# 1》 SADD:向集合添加元素
SADD key member [member ...]
# 2》 SMEMBERS:返回集合的成员
SMEMBERS key
# 3》 SISMEMBER:检查元素是否是集合的成员
SISMEMBER key member
# 4》 SREM:删除集合的元素
SREM key member [member ...]
# 5》 SPOP:随机弹出集合的一个元素（删除并返回）
SPOP key [count]
# 6》 SRANDMEMBER:随机返回集合中的元素（不删除）
SRANDMEMBER key [count]
	# count>0,返回随机元素
	# count<0,返回数组（成员可重复）（count可以大于元素个数）
# 7》 SDIFF：返回差集
SDIFF key [key ...]
# 8》 SINTER：返回交集
SINTER key [key ...]
# 9》 SUNION：返回并集
SUNION key [key ...]
# 10》 SCARD：返回集合元素的个数
# 11》 SDIFFSTORE：SDIFF之后并保存到destination
SDIFFSTORE destination key [key ...]
# 12》 SINTERSTORE：SDIFF之后并保存到destination
SINTERSTORE destination key [key ...]
# 13》 SUNIONSTORE：SDIFF之后并保存到destination
SUNIONSTORE destination key [key ...]
# 14》 SMOVE:将元素移动到另一个集合中
SMOVE source destination member
	#SMOVE 是原子性操作。
	#如果 source 集合不存在或不包含指定的 member 元素，则 SMOVE 命令不执行任何操作，仅返回 0 。否则， member 元素从 source 集合中被移除，并添加到 destination 集合中去。
	#当 destination 集合已经包含 member 元素时， SMOVE 命令只是简单地将 source 集合中的 member 元素删除。
```

## Redis Zset（Sorted Set）类型及相关命令

Redis 有序集合和集合一样也是string类型元素的集合,且不允许重复的成员。

不同的是**每个元素都会关联一个double类型的分数**。redis正是通过分数来为集合中的成员进行从小到大的排序。

**有序集合的成员是唯一的,但分数(score)却可以重复。**

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。 集合中最大的成员数为 $2^{23}-1$(4294967295, 每个集合可存储40多亿个成员)。

比List查询更快，但是更占用内存。

```sh
# 1》 ZADD:将分数/元素添加到Zset
ZADD key [NX|XX] [CH] [INCR] score member [score member ...]
ZADD phpScore 100 king 96 queen 98 mazi 80 test # 重复添加会刷新分数
ZADD phpScore 99.9 yaro
ZADD phpScore +inf maxInt -inf minInt
# 2》 ZSCORE:获取成员的分数
ZSCORE key member
# 3》 ZRANGE:按照元素分数从小到大，返回元素（包含两端，可以使用左括号`(`表示不包含端点）
ZRANGE key start stop [WITHSCORES]  # 当分数相同时，按照元素的ASCII码排序
127.0.0.1:6379> ZRANGE phpScore 0 2 WITHSCORES
1) "minInt"
2) "-inf"
3) "test"
4) "80"
5) "queen"
6) "96"
# 4》 ZREVRANGE:按照元素分数从大到小
ZREVRANGE key start stop [WITHSCORES]
# 5》 ZRANGEBYSCORE:获得指定分数范围内的元素，从小到大（含两端）。
	# [LIMIT offset count] 第一个offset为0，count指数量。
ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]
127.0.0.1:6379> ZZRANGEBYSCORE phpScore (80 (100  # 左括号表示不包含端点
1) "queen"
2) "mazi"
3) "yaro"
# 6》 ZREVRANGEBYSCORE:获得指定分数范围内的元素，从大到小（含两端）。
ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]
# 7》 ZINCRBY:增加元素的分数，返回增加后的结果
ZINCRBY key increment member  # 可以使用负数。
127.0.0.1:6379> ZSCORE phpScore test  # 获得分数
"80"
127.0.0.1:6379> ZINCRBY phpScore 5 test  # 增加5分
"85"
# 8》 ZCARD:获得zset中元素的数量
ZCARD key
# 9》 ZCOUNT:获得zset中指定分数范围内的数量
ZCOUNT key min max
# 10》 ZREM:删除指定的元素，返回删除的数量
ZREM key member [member ...]
# 11》 ZREMRANGEBYRANK:按照分数从小到大的顺序删除指定排名范围内的所有元素
ZREMRANGEBYRANK key start stop
ZREMRANGEBYRANK phpScore 0 3  # 删除前四个元素
# 12》 ZREMRANGEBYSCORE:删除指定分数范围内的所有元素
ZREMRANGEBYSCORE key min max
# 13》 ZRANK:获得指定成员的排名（分数从小到大）
ZRANK key member
127.0.0.1:6379> ZRANK phpScore yaro
(integer) 4
# 14》 ZRANK:获得指定成员的排名（分数从大到小）
ZREVRANK key member
# 15》 ZINTERSTORE:求Zset之间的交集,并保存
ZINTERSTORE destination numkeys key [key ...] [WEIGHTS权重 weight weight...] [AGGREGATE合并选项 SUM | MIN | MAX]
127.0.0.1:6379> ZADD testZset1 1 a 2 b 3 c  # 设置testZset1
(integer) 3
127.0.0.1:6379> ZADD testZset2 10 a 20 b 30 c # 设置testZset2
(integer) 3
127.0.0.1:6379> ZINTERSTORE resultZset1 2 testZset1 testZset2 # 交集
(integer) 3
127.0.0.1:6379> ZRANGE resultZset1 0 -1 WITHSCORES # 查看交集结果（默认分数求和）
1) "a"
2) "11"
3) "b"
4) "22"
5) "c"
6) "33"
127.0.0.1:6379> ZINTERSTORE resultZset1 2 testZset1 testZset2 AGGREGATE max
(integer) 3
127.0.0.1:6379> ZRANGE resultZset1 0 -1 WITHSCORES
1) "a"
2) "10"
3) "b"
4) "20"
5) "c"
6) "30"
127.0.0.1:6379> ZINTERSTORE resultZset1 2 testZset1 testZset2 WEIGHTS 0.1 2  # 分别指定权重系数为0.1 和 2
(integer) 3
127.0.0.1:6379> ZRANGE resultZset1 0 -1 WITHSCORES
1) "a"
2) "20.100000000000001"
3) "b"
4) "40.200000000000003"
5) "c"
6) "60.299999999999997"
# 16》 ZUNIONSTORE:求Zset之间的并集,并保存
ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS weight] [AGGREGATE SUM|MIN|MAX]
```











