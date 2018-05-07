# MongoDB备忘

## MongoDB简介

参考官网：https://docs.mongodb.com/

参考菜鸟教程：http://www.runoob.com/mongodb/mongodb-update.html

MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

Redis/Memcached：key-value数据库；

MongoDB：文档数据库，存储的是文档（Bson->Json的二进制化）。

特点：内部执行引擎为JS解释器，把文档存储为Bson结构，再查询时，转换为JS对象，并可以通过我们熟悉的JS语法来操作。

![1.png](https://i.loli.net/2018/05/06/5aee3e0c146fb.png)

传统数据库（Mysql等）：结构化数据，设计好表结构后，每一行内容都符合表结构；

文档型数据库：表下的每篇文档都可以有自己的独特的结构（JSON对象都可以由自己独特的属性和值）

思路: 如果有电影, 影评, 影评的回复, 回复的打分

在传统型数据库中, 至少要4张表, 关联度非常复杂.

在文档数据库中,通过1篇文档,即可完成.  体现出文档型数据库的反范式化.

```json
{
    "film": "天龙八部",
    "comment":
     [{
        "content": "王家卫的电影风格",
        "reply": ["支持", "好"]
    }]
}
```

## MongoDB安装/启动

官网下载地址：https://www.mongodb.com/download-center?jmp=nav#community

- LInux安装、配置及启动

1、下载二进制安装包直接运行；

2、下载源码包，编译安装；

3、Repo yum安装

![官网安装说明](https://i.loli.net/2018/05/07/5aefbafa859c5.png)

相应文件简介：

```sh
#核心:
mongod: 数据库核心进程
mongos: 查询路由器,集群时用
mongo:   交互终端(客户端)
#二进制导出导入:
mongodump:导出bson数据
mongorestore: 导入bson
bsondump: bson转换为json
monoplog:
#数据导出导入
mongoexport: 导出json,csv,tsv格式
mongoimport: 导入json,csv,tsv
#诊断工具:
mongostats
mongotop
mongosniff  用来检查mongo运行状态
```

启动/连接mongod服务：

```sh
./mongod -h  # 查看相应命令的帮助
参数解释:
--dbpath 数据存储目录
--logpath 日志存储目录
--port 运行端口(默认27017)
--fork 后台进程运行
================

## 1、简单启动（不推荐）
mkdir --dbpath /usr/local/MongoDB/db  # 创建数据库文件夹
mongod --dbpath /usr/local/MongoDB/db  # 默认端口
mongod --dbpath /usr/local/MongoDB/db --port=27000  # 指定端口
./bin/mongod --dbpath /path/to/database --logpath /path/to/log --fork --port 27017 # --fork是以服务后台启动
=============

## 2、配置文件启动（推荐）
mkdir -p /usr/local/MongoDB/db /usr/local/MongoDB/log/ # 创建创建数据/日志文件夹
touch /usr/local/MongoDB/mongodb.conf  # 创建日志文件/配置文件
# 配置文件内容如下：
-----------
# 设置数据路径
dbpath = /usr/local/MongoDB/db
# 设置日志路径，同时指定日志文件名 
logpath = /usr/local/MongoDB/log/mongodb.log
# 打开日志输出操作
logappend = true
# 进行用户管理设置如下内容
noauth = true #不适用任何认证
port = 27001
------------
mongod -f D:\MongoDB\mongodb.conf  # 指定配置文件启动
===============

## 3、Repo安装使用systemctl启动
systemctl start mongod.service  # repo安装可选启动，默认配置文件/etc/mongod.conf；也可以按照上面的方式启动。
===============

## 连接数据库服务器
mongo --port=27001  # 连接数据库
```

- Windows安装、配置及启动

基本同Linux，其他参考官网：https://www.mongodb.com/download-center#community

```sh
MongoDB程序PATH目录 D:\MongoDB\bin ；
# 配置文件启动如下设置
- 创建创建数据文件 D:\MongoDB\db ；
- 创建日志文件 D:\MongoDB\log\mongodb.log ；
- 创建配置文件 D:\MongoDB\mongodb.conf ；

在配置文件中填写如下内容：
    # 设置数据路径
    dbpath = D:\MongoDB\db
    # 设置日志路径
    logpath = D:\MongoDB\log\mongodb.log
    # 打开日志输出操作
    logappend = true
    # 进行用户管理设置如下内容
    noauth = true #不适用任何认证
    port = 27001

mongod -f D:\MongoDB\mongodb.conf # 根据配置文件启动MongoDB数据库服务：
mongo --port=27001  # 连接数据库 
```

> mongodb非常的占磁盘空间, 刚启动后要占3-4G（具体可以到数据库文件夹查看）左右,
>
> 如果你用虚拟机练习,可能空间不够,导致无法启动.
>
> 可以用 --smallfiles 选项来启动, 
>
> 将会占用较小空间  400M左右.

















## MongoDB入门命令

```mysql
> show dbs; # (兼容mysql的databases)
> use shop; #切换到shop数据库，不需要先创建，Mongodb(隐式)自动创建shop数据库
switched to db shop
> show collectios; # 查看所有集合(兼容mysql的tables)

> db.createCollection('user');#创建集合集合，可以隐式创建，不需要这句话；
{ "ok" : 1 }

> db.user.insert({name:'yaro', age:22});  # 插入数据（文档），自动创建集合
WriteResult({ "nInserted" : 1 })

> db.user.find() #查找所有数据
{ "_id" : ObjectId("5aefe8802c78db929067b99e"), "name" : "yaro", "age" : 22 }

> db.user.insert({_id:2,name:'poly',age:23})
WriteResult({ "nInserted" : 1 })

> db.user.insert({_id:3,name:'hmm',hobby:['basketball','footbal'],intro:{title:'My intro',content:'from china'}})
WriteResult({ "nInserted" : 1 })

> db.user.find()
{ "_id" : ObjectId("5aefe8802c78db929067b99e"), "name" : "yaro", "age" : 22 }
{ "_id" : 2, "name" : "poly", "age" : 23 }
{ "_id" : 3, "name" : "hmm", "hobby" : [ "basketball", "footbal" ], "intro" : { "title" : "My intro", "content" : "from china" } }

db.user.findOne(); #查看集合的一个文档
db.user.remove({"_id":objectId("....")}) # 删除数据
var userData1 = {...}; db.dept.updata({原数据ID}, deptData1) #更新数据，最麻烦，意义不大
db.user.drop(); # 删除集合
db.dropDatabase(); #删除当前数据库
```

## CRUD操作详解

```sh
## 1、增：insert
====================
介绍: mongodb存储的是文档,. 文档是json格式的对象.
语法: db.collectionName.isnert(document);

db.collectionName.insert({title:’nice day’});  # 增加单篇文档
db.collectionName.insert({_id:8,age:78,name:’lisi’}); # 增加单个文档,并指定_id

db.collectionName.insert(
[
{time:'friday',study:'mongodb'},
{_id:9,gender:'male',name:'QQ'}
]
)  #增加多个文档(还可以无限嵌套)

## 2、删：remove
==========================
语法: db.collection.remove(查询表达式, 选项);
选项是指  {justOne:true/false},是否只删一行, 默认为false

注意:
1: 查询表达式依然是个json对象
2: 查询表达式匹配的行,将被删掉.
3: 如果不写查询表达式,collections中的所有文档将被删掉.

e.g.:
db.stu.remove({sn:’001’}); #删除stu表中 sn属性值为’001’的文档 
db.stu.remove({gender:’m’},true); #删除stu表中gender属性为m的文档,只删除1行.

## 3、改:update
=======================
改谁? --- 查询表达式
改成什么样? -- 新值 或 赋值表达式
操作选项 ----- 可选参数

语法: db.collection.update(查询表达式,新值,选项);

例:
db.news.update({name:'QQ'},{name:'MSN'});
是指选中news表中,name值为QQ的文档,并把其文档值改为{name:’MSN’},
结果: 文档中的其他列也不见了,改后只有_id和name列了.
即--新文档直接替换了旧文档,而不是修改

如果是想修改文档的某列,可以用$set关键字
db.collectionName.update(query,{$set:{name:’QQ’}})

修改时的赋值表达式
$set  修改某列的值
$unset 删除某个列
$rename 重命名某个列
$inc 增长某个列
$setOnInsert 当upsert为true时,并且发生了insert操作时,可以补充的字段.

Option的作用:
{upsert:true/false,multi:true/false}
Upsert---是指没有匹配的行,则直接插入该行.(和mysql中的replace一样)

例:db.stu.update({name:'wuyong'},{$set:{name:'junshiwuyong'}},{upsert:true});
如果有name=’wuyong’的文档,将被修改
如果没有,将添加此新文档

例:
db.news.update({_id:99},{x:123,y:234},{upsert:true});
没有_id=99的文档被修改,因此直接插入该文档

multi: 是指修改多行(即使查询表达式命中多行,默认也只改1行,如果想改多行,可以用此选项)
例:
db.news.update({age:21},{$set:{age:22}},{multi:true});
则把news中所有age=21的文档,都修改

## 4、查:update
=======================
语法: db.collection.find(查询表达式,查询的列);
Db.collections.find(表达式,{列1:1,列2:1});

例1:db.stu.find()
查询所有文档 所有内容

例2: db.stu.find({},{gendre:1})
查询所有文档,的gender属性 (_id属性默认总是查出来)

例3: db.stu.find({},{gender:1, _id:0})
查询所有文档的gender属性,且不查询_id属性

例3: db.stu.find({gender:’male’},{name:1,_id:0});
查询所有gender属性值为male的文档中的name属性

```

## 深入查询表达式









insert 可以插入单个document（对象`{}`），也可以插入多个documents（数组`[]`），返回插入的统计结果。

insertOne 插入单个document`{}`，返回插入的document。

inserMany 插入多个documents`[]`，返回插入的多个documents。





###### GUI软件管理工具

推荐 `Robomongo` 已经改名为 `Robo 3T,` ，跨平台，有社区版本；使用Jetbrains家的IDE的话可以使用 `mongo plugin` 插件。

###### MongoDB基础操作

具体参照上面的常用命令。

> 在MondogDB数据库里面是存在有数据库的概念的，但是没有模式（集合没有结构的，根据插入的内容动态改变结构；所有的信息都是按照文档保存的），保存数据的结构就是JSON结构，只不过在进行一些数据处理的时候才会使用到MongoDB自己的的一些操作符。

- 使用mldn数据库： `use mldn`

这个时候并没有创建mldn数据库，只有在数据库里面保存集合数据之后才会创建

- 创建一个集合(类似于表)--创建一个emp集合： `db.createCollection("emp");`
- 但是按照以上代码进行操作会很不正常，因为正常人使用MongoDB都是直接向里面保存一个数据。
  `db.dept.insert({"deptno":10,"dname":"财务部","loc":"北京"})`
- 查看所有集合： `show collectios;` MongoDB中的集合是自动创建的。
- 查看dept集合（表）的数据： `db.dept.find();` 括号内可以使用条件

传统数据库的表一旦创建，必须严格按照表的结构插入数据；但是MongoDB的集合是可以随意扩充的。

- 增加不规则数据：

```mysql
var deptData = {
    "deptno":20,
    "dname":"研发部",
    "loc":"20",
    "count":"20"
};
db.dept.insert(deptData);
```

- 关于ID的问题：在MongoDB集合中的每一行记录都会自动生成一个"_id"，他是由：时间戳、机器码、进程PID、计数器生成的。这是MongoDB自动生成的，不重复，不可修改；
- 查看单独的一个文档信息：`db.dept.findOne();`
- 删除一个文档信息：`db.dept.remove({"_id":objectId("....")}) # 删除数据`
- 更新数据，比较麻烦，操作意义不大：`var deptData1 = {...}; db.dept.updata({原数据ID}, deptData1)`
- 删除集合： `db.dept.drop();`
- 删除当前数据库： `db.dropDatabase();`