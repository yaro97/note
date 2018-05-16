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

#关于ID的问题：在MongoDB集合中的每一行记录都会自动生成一个"_id"，他是由：时间戳、机器码、进程PID、计数器生成的。这是MongoDB自动生成的，不重复，不可修改；

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

var deptData = {
    "deptno":20,
    "dname":"研发部",
    "loc":"20",
    "count":"20"
}; # 定义一个文档（对象）
db.dept.insert(deptData);  # 插入对象

#insert 可以插入单个document（对象{}），也可以插入多个documents（数组[]），返回插入的统计结果。
#insertOne 插入单个document{}，返回插入的document。
#inserMany 插入多个documents[]，返回插入的多个documents。

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

## 4、查:find
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

例4: db.stu.find({gender:’male’},{name:1,_id:0}).count();
返回查询结果的数量。
```

## 深入查询表达式

 查询表达式:

1: 最简单的查询表达式

{filed:value} ,是指查询field列的值为value的文档

2: $ne --- != 查询表达式

{field:{$nq:value}}

作用--查filed列的值 不等于 value 的文档

3: $nin --> not in

4: $all

语法: {field:{$all:[v1,v2..]}}  

是指取出 field列是一个数组,且至少包含 v1,v2值

5: $exists  

语法: {field:{$exists:1}}

作用: 查询出含有field字段的文档

6: $nor,

{$nor,[条件1,条件2]}

是指  所有条件都不满足的文档为真返回

7:用正则表达式$regex查询 以”诺基亚”开头的商品

例:db.goods.find({goods_name:{$regex:^诺基亚.*}},{goods_name:1});

8: 用$where 表达式来查询

例: db.goods.find({$where:'this.cat_id != 3 && this.cat_id != 11'});

> 注意: 用$where查询时, mongodb是把bson结构的二进制数据转换为json结构的对象,
> 然后比较对象的属性是否满足表达式.regex和where效率都不高，速度较慢

```bash
# 1:主键为32的商品
db.goods.find({goods_id:32});
# 2:不属第3栏目的所有商品($ne)
db.goods.find({cat_id:{$ne:3}},{goods_id:1,cat_id:1,goods_name:1});
# 3:本店价格高于3000元的商品{$gt}
db.goods.find({shop_price:{$gt:3000}},{goods_name:1,shop_price:1});
# 4:本店价格低于或等于100元的商品($lte)
db.goods.find({shop_price:{$lte:100}},{goods_name:1,shop_price:1});
# 5:取出第4栏目或第11栏目的商品($in)
db.goods.find({cat_id:{$in:[4,11]}},{goods_name:1,shop_price:1});
# 6:取出100<=价格<=500的商品($and)
b.goods.find({$and:[{price:{$gt:100},{$price:{$lt:500}}}]);
# 7:取出不属于第3栏目且不属于第11栏目的商品($and $nin和$nor分别实现)
db.goods.find({$and:[{cat_id:{$ne:3}},{cat_id:{$ne:11}}]},{goods_name:1,cat_id:1})
db.goods.find({cat_id:{$nin:[3,11]}},{goods_name:1,cat_id:1});
db.goods.find({$nor:[{cat_id:3},{cat_id:11}]},{goods_name:1,cat_id:1});
# 8:取出价格大于100且小于300,或者大于4000且小于5000的商品()
b.goods.find({$or:[{$and:[{shop_price:{$gt:100}},{shop_price:{$lt:300}}]},{$and:[{shop_price:{$gt:4000}},{shop_price:{$lt:5000}}]}]},{goods_name:1,shop_price:1});
# 9:取出goods_id%5 == 1, 即,1,6,11,..这样的商品
b.goods.find({goods_id:{$mod:[5,1]}});
# 10:取出有age属性的文档
b.stu.find({age:{$exists:1}});
含有age属性的文档将会被查出
```

## 游标(cursor)操作

游标是什么?
通俗的说,游标不是查询结果,而是查询的返回资源,或者接口.
通过这个接口,你可以逐条读取.
就像php中的fopen (也像python中的file对象)打开文件,得到一个资源一样, 通过资源,可以一行一行的读文件.


声明游标:
`var cursor =  db.collectioName.find(query,projection);`
`Cursor.hasNext() `,判断游标是否已经取到尽头
`Cursor. Next()` , 取出游标的下1个单元

```sh
# 一次性插入100条数据
for(var i=0;i<1000;i++){ 
   db.bar.insert({_id:i+1,title:"hello world",content:'aaa'+i}); 
}
db.bar.find()  # mongodb只会返回20条数据，实际业务逻辑中，如：网页的显示数据也不会全部显示1000条数据。此时可以借用cursor来自由查询。（类似python中的file对象）

# 查询到前5条数据，赋值给mycursor。
> var mycursor  = db.bar.find({_id:{$lte:5}})  
> print(mycursor.next())  # 打印第一条数据类型（BSON二进制）
[object BSON]
> printjson(mycursor.next())  # 打印第二条数据的json格式
{ "_id" : 2, "title" : "hello world", "content" : "aaa1" }

# 重新赋值mycursor
> var mycursor=db.bar.find({_id:{$lte:5}}) 
```

通过JS语句的循环遍历/迭代游标里面的内容

```sh
# 用while来循环游标
> while(mycursor.hasNext()){
... printjson(mycursor.next());
... }  # 使用js语句查询所有5条数据
{ "_id" : 1, "title" : "hello world", "content" : "aaa0" }
{ "_id" : 2, "title" : "hello world", "content" : "aaa1" }
{ "_id" : 3, "title" : "hello world", "content" : "aaa2" }
{ "_id" : 4, "title" : "hello world", "content" : "aaa3" }
{ "_id" : 5, "title" : "hello world", "content" : "aaa4" }

# 用for来循环游标
> for (var mycursor=db.bar.find({_id:{$lte:5}}); mycursor.hasNext(); ){
    printjson(mycursor.next())
}
```

其实游标里面自带了遍历/迭代的功能：

游标有个迭代函数,允许我们自定义回调函数来逐个处理每个单元.
`cursor.forEach(回调函数);`

```sh
# 重新赋值mycursor
> var mycursor=db.bar.find({_id:{$lte:5}}) 
# 定义一个回调函数以供forEach使用
> var foo = function(obj){print("The id is: "+obj._id)}
# 通过forEach调用foo函数
> mycursor.forEach(foo)
The id is: 1
The id is: 2
The id is: 3
The id is: 4
The id is: 5
```

游标在分页中的应用：
比如查到1000行,跳过10页,取10行.
一般地,我们假设每页N行, 当前是page页
就需要跳过前 (page-1)*N 行, 再取N行, 在mysql中, 通过limit offset,N来实现
在mongo中,用skip(), limit()函数来实现的

```sh
# 查询集合bar所有数据，并跳过前995条数据
mycursor=db.bar.find().skip(995)；
# 重新赋值mycursor,并跳过前995条数据
> var mycursor=db.bar.find().skip(995)；
# 通过forEach调用匿名函数
> mycursor.forEach(function(obj){printjson(obj)})；
{ "_id" : 996, "title" : "hello world", "content" : "aaa995" }
{ "_id" : 997, "title" : "hello world", "content" : "aaa996" }
{ "_id" : 998, "title" : "hello world", "content" : "aaa997" }
{ "_id" : 999, "title" : "hello world", "content" : "aaa998" }
{ "_id" : 1000, "title" : "hello world", "content" : "aaa999" }
# 重新赋值mycursor,并跳过前950条数据，每5条显示一页
> var mycursor=db.bar.find().skip(950).limit(5);
# 通过forEach调用匿名函数
> mycursor.forEach(function(obj){printjson(obj)});
{ "_id" : 951, "title" : "hello world", "content" : "aaa950" }
{ "_id" : 952, "title" : "hello world", "content" : "aaa951" }
{ "_id" : 953, "title" : "hello world", "content" : "aaa952" }
{ "_id" : 954, "title" : "hello world", "content" : "aaa953" }
{ "_id" : 955, "title" : "hello world", "content" : "aaa954" }
# 重新赋值mycursor,并跳过前950条数据，每2条显示一页
> var mycursor=db.bar.find().skip(950).limit(2);
> mycursor.toArray()  # 直接返回Array数组
[
	{
		"_id" : 951,
		"title" : "hello world",
		"content" : "aaa950"
	},
	{
		"_id" : 952,
		"title" : "hello world",
		"content" : "aaa951"
	}
]
> var mycursor=db.bar.find().skip(950).limit(2);
> printjson(mycursor.toArray()[1]);
{ "_id" : 952, "title" : "hello world", "content" : "aaa951" }
```

> 注意: 不要随意使用toArray()
> 原因: 会把所有的行立即以对象形式组织在内存里.
> 可以在取出少数几行时,用此功能.

## 索引

索引通常能够极大的提高查询的效率，如果没有索引，MongoDB在读取数据时必须扫描集合中的每个文件并选取那些符合查询条件的记录。

索引提高查询速度,降低写入速度,权衡常用的查询字段,不必在太多列上建索。

索引是特殊的数据结构，索引存储在一个易于遍历读取的数据集合中，索引是对数据库表中一列或多列的值进行排序的一种结构。

在mongodb中,索引可以按字段升序/降序来创建,便于排序

默认是用btree来组织索引文件,2.4版本以后,也允许建立hash索引.

```sh
# 向集合stu插入1000条数据
> for(var i=1;i<=1000;i++){
... db.stu.insert({sn:i,name:"student"+i})
... }
> db.stu.find({sn:99}).explain(); #查看有无使用索引（默认没有使用）,从第一条逐条搜索 {sn:99} 的数据。

#查看当前索引状态: 
db.collection.getIndexes();

#创建普通的单列索引:
db.collection.ensureIndex({field:1/-1});  # 1是升续 2是降续

#删除单个索引
db.collection.dropIndex({filed:1/-1});

#一次性删除所有索引
db.collection.dropIndexes();

#创建多列索引  
db.collection.ensureIndex({field1:1/-1, field2:1/-1});

#创建子文档索引
#子文档：{name:"yaro",spec:{hobby:"nba",face:"beauty"}}
db.collection.ensureIndex({filed.subfield:1/-1});

#创建唯一索引（保证field唯一性）:
db.collection.ensureIndex({field:1/-1}, {unique:true});
#指定field为unique之后，当name:yaro存在时，不能再插入name为yaro的数据；

#创建稀疏索引:
稀疏索引的特点------如果针对field做索引,针对不含field列的文档,将不建立索引.
与之相对,普通索引,会把该文档的field列的值认为NULL,并建索引.
适宜于: 小部分文档含有某列时.
db.collection.ensureIndex({field:1/-1},{sparse:true});

> db.tea.find();
{ "_id" : ObjectId("5275f99b87437c610023597b"), "email" : "a@163.com" }
{ "_id" : ObjectId("5275f99e87437c610023597c"), "email" : "b@163.com" }
{ "_id" : ObjectId("5275f9e887437c610023597e"), "email" : "c@163.com" }
{ "_id" : ObjectId("5275fa3887437c6100235980") }
#如上内容,最后一行没有email列；如果分别加普通索引,和稀疏索引；
#对于最后一行的email分别当成null 和 忽略最后一行来处理.
#根据{email:null}来查询,前者能查到,而稀疏索引查不到最后一行.

#创建哈希索引(2.4新增的)
#哈希索引速度比普通索引快,但是,无能对范围查询进行优化.
#适宜于---随机性强的散列
db.collection.ensureIndex({file:’hashed’});

#重建索引
#一个表经过很多次修改后,导致表的文件产生空洞,索引文件也如此.
#可以通过索引的重建,减少索引文件碎片,并提高索引的效率.
#类似mysql中的optimize table
db.collection.reIndex()
```

## 用户管理（DBA必须）

> 这里只是简单的介绍相关命令，DBA需要进一步学习。
>
> 更详细请参考官网：https://docs.mongodb.com/manual/reference/security/

MongoDB 默认直接连接，无须身份验证。

在mongodb中,有一个admin数据库, 牵涉到服务器配置层面的操作,需要先切换到admin数据.
即 `use admin` , -->相当于进入超级用户管理模式.

mongo的用户是以数据库为单位来建立的, **每个数据库有自己的管理员.**

```sh
# 添加管理员用户
> use admin;  # 切换到admin数据库
> db.createUser(
  {
    user: "yaro",
    pwd: "123456",
    roles: [ { role: "root", db: "admin" } ]
  }
);
> db.getUsers();  # 查看所有用户

# 使用 --auth 选项，重启mongod服务
mongod --auth
#--------------
# 倘若是使用systemctl服务启动，需要修改/etc/mongodb.conf选项
# 添加“auth = true”

#================
# 身份验证
#方法1:启动客户端时验证
#mongo --port 27017 -u "adminUser" -p "adminPass" --authenticationDatabase "admin" 
#方法2：连接客户端后验证
mongo
use admin  # 切换到admin数据库
db.auth("adminUser","adminPass")

#============
# 添加普通用户
use foo
db.createUser(
  {
    user: "simpleUser",
    pwd: "simplePass",
    roles: [ { role: "readWrite", db: "foo" },
             { role: "read", db: "bar" } ]
  }
)  # 权限：读写数据库 foo， 只读数据库 bar。

# 普通用户身份验证
use foo
db.auth("simpleUser", "simplePass")
use bar
show collections

# 2. 查看所有用户
> db.getUsers();

# 3. 修改用户密码
> use test
> db.changeUserPassword(用户名, 新密码);

# 4. 删除用户
> use test
> db.dropUser(用户名);
> db.dropAllUsers();
```

> 当忘记管理员密码，或其他无法进入mongodb的情况。可以通过如下方法解决：
> 注释/etc/mongodb.conf中的`auth = true`选项，重启mongodb服务，重新连接客户端，删除（所有）用户。重新添加用户即可。

## mongoDB备份与恢复

**1: 导入/导出可以操作的是本地的mongodb服务器,也可以是远程的.**
所以,都有如下通用选项:
-h host   主机
--port port    端口
-u username 用户名
-p passwd   密码

**2: mongoexport 导出json/csv格式的文件**
问: 导出哪个库,哪张表,哪几列,哪几行?

-d  库名
-c  表名
-f  field1,field2...列名
-q  查询条件
-o  导出的文件名
-- csv  导出csv格式(便于和传统数据库交换数据)

```sh
#导出test数据库，news集合所有列
mongoexport -d test -c news -o test.json
mongoexport -u "yaro" -p "123456" -d test -c news -o test.json
#只导出goods_id,goods_name列
mongoexport -d test -c goods -f goods_id,goods_name -o goods.json
#只导出价格低于1000元的行
mongoexport -d test -c goods -f goods_id,goods_name,shop_price -q '{shop_price:{$lt:200}}' -o goods.json
#导出csv格式
mongoexport -d stu -c stu -f goods_id,goods_name --type=csv -o test.csv

#注: _id列总是导出
```

**3: mongoimport 导入json/csv格式的文件**

-d 待导入的数据库
-c 待导入的表(不存在会自己创建)
--type  csv/json(默认)
--file 备份文件路径

```sh
#导入json
mongoimport -d test -c goods --file ./goodsall.json
#导入csv（会把csv文件的首行列信息导入）
mongoimport -d test -c goods --type csv -f goods_id,goods_name --file ./goodsall.csv 
#忽略csv文件的首行列信息
mongoimport -d test -c goods --type csv --headline -f goods_id,goods_name --file ./goodsall.csv 
```

**4：mongodump 导出二进制bson结构的数据及其索引信息**

>Bson格式用于MongoDB的日常备份/恢复；Json格式用于和其他数据库交互；
>二进制备份,不仅可以备份数据,还可以备份索引;
>备份数据比较小;

-d  库名
-c  表名
-f  field1,field2...列名

```sh
mongodump -d test  [-c 表名]  默认是导出到mongo下的dump目录
#规律: 
#1:导出的文件放在以database命名的目录下
#2: 每个表导出2个文件,分别是bson结构的数据文件, json的索引信息
#3: 如果不声明表名, 导出所有的表
```

**5：mongorestore 导入二进制文件**

```sh
mongorestore -d test dump/test/ #(mongodump时的备份目录)
```

## Replication Set副本集

MongoDB复制是将数据同步在多个服务器的过程。

复制提供了数据的冗余备份，并在多个服务器上存储数据副本，提高了数据的可用性， 并可以保证数据的安全性。

复制还允许您从硬件故障和服务中断中恢复数据。

![](http://www.runoob.com/wp-content/uploads/2013/12/replication.png)



```sh
#步骤一：创建目录（这里以一个主机两个副本集为例）
mkdir -p /data/r17 /data/r18 /data/r19 /data/mlog

#步骤二：启动3个实例，切声明属于哪个副本集
./bin/mongod --port 27017 --dbpath /data/r17 --smallfiles --replSet rsa --fork --logpath /data/mlog/log17
./bin/mongod --port 27018 --dbpath /data/r18 --smallfiles --replSet rsa --fork --logpath /data/mlog/log17
./bin/mongod --port 27019 --dbpath /data/r19 --smallfiles --replSet rsa --fork --logpath /data/mlog/log17
#--smallfiles 默认mongodb启动需要占用3G硬盘，此参数可以占用400M硬盘；
#--replSet rsa 声明属于rsa副本集

#步骤三：配置
mongo --port 27017 #连接primary服务器
use admin
var rsconf = {
...     _id:'rsa',
...     members:
...     [
...         {_id:0,
...         host:'192.168.1.201:27017'
...         }
...     ]
... }  # 声明rsconf变量

#步骤四：根据配置文件初始化
> rs.initiate(rsconf);

#步骤五：添加/删除节点
> rs.add('192.168.1.201:27018');
> rs.add('192.168.1.201:27019');
> rs.remove('192.168.1.201:27019');
> re.reconfig();  #重新加载配置文件
> rs.status(); # 查看状态

#步骤六：主节点插入数据(27017)
> use test
> db.user.insert({name:'world'})
#只能主节点插入数据

#步骤七：从节点查看数据（需要稍等片刻-同步时间）
./bin/mongo --port 27019
> rs.slaveOk(); # 默认从节点只备份，不能进行crud操作；此命令运行读取数据库；
> show dbs;
> db.user.find();
```

## Sharding分片

详细参考：http://www.runoob.com/mongodb/mongodb-sharding.html 

官网：https://docs.mongodb.com/manual/sharding

在Mongodb里面存在另一种集群，就是分片技术,可以满足MongoDB数据量大量增长的需求。

当MongoDB存储海量的数据时，一台机器可能不足以存储数据，也可能不足以提供可接受的读写吞吐量。这时，我们就可以通过在多台机器上分割数据，使得数据库系统能存储和处理更多的数据。

**为什么使用分片**

- 复制所有的写入操作到主节点
- 延迟的敏感数据会在主节点查询
- 单个副本集限制在12个节点
- 当请求量巨大时会出现内存不足。
- 本地磁盘不足
- 垂直扩展价格昂贵

 **分片集群结构分布**

![](https://www.runoob.com/wp-content/uploads/2013/12/sharding.png)

上图中主要有如下所述三个主要组件：

- Shard:

  用于存储实际的数据块，实际生产环境中一个shard server角色可由几台机器组个一个replica set承担，防止主机单点故障

- Config Server:

  mongod实例，存储了整个 ClusterMetadata，其中包括 chunk信息。

- Query Routers:

  前端路由，客户端由此接入，且让整个集群看上去像单一数据库，前端应用可以透明使用。

## 副本集和分片的结合



## GUI软件管理工具

推荐 `Robomongo` 已经改名为 `Robo 3T,` ，跨平台，有社区版本；使用Jetbrains家的IDE的话可以使用 `mongo plugin` 插件。

