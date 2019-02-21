---
title: Mysql基本操作
tags:
- mysql
- 数据库
---
## 安装相关

msyql分为`mysql`和 `mysql-server`和 `mysql-dev` （库）

以下为ubuntu下安装`mariadb-server`

```sh
apt-cache search mariadb-server -n #查找maria相关软件包，-n为--names-only 
apt-cache show mariadb-server #查看rep中的mariadb默认版本
apt install mariadb-server
dpkg -l | grep mariadb-server #查看安装的相应软件包及版本
mysql #进入
```

## 数据库基础

SQL语言基础：
数据库 》 表 》 { 列：属性，行：记录 }

数据类型：
- 数字（integer,smallint,tinyint;decimal,numeric），
- 时间(date)，
- 字符串(char,varchar(可变长度))，
- 其他

## sql基础语句

### 常用语句

```mysql
mysql -h localhost -u root -p 
quit 或 exit 都可退出
SHOW DATABASES;
CREATE DATABASE xxx;
DROP DATABASE xxx;
RENAME DATABASE xxx TO yyy;（其中一个版本有效，但是已经不支持了）

USE XXX; #选择某个数据库
SHOW TABLES; #查看当前数据库有哪些表格；

#创建ic_course表，（需要保存课程名称、课程长度、课程讲师、课程分类）：
CREATE TABLE ic_course(
    id int,
    course_name varchar(50),
    course_length int(10), #可以不设置10
    teacher varchar(50),
    category varchar(50)
);

DESCRIBE ic_course; #显示表结构
# 可以简写为：DESC ic_course; 

DROP TABLE ic_course; #删除一个表格
```

### TABLE操作

```mysql
- 重命名表名：
    ALTER TABLE ic_course RENAME course;
- 向表中添加一列：
    ALTER TABLE ic_course ADD link varchar(100);
- 删除表中的一列：
    ALTER TABLE ic_course DROP COLUMN link;
- 修改一个列的数据类型：
    ALTER TABLE ic_course MODIFY teacher varchar(100);
- 重命名一个列：
    ALTER TABLE ic_course CHANGE COLUMN teacher lecture varchar(100);
```

### 向表格中插入数据

```mysql
# 插入所有所有属性对应的值，字符串必须用单引号包裹；
INSERT INTO 表名称 VALUES(值1，值2，...);

# 或者只插入某些属性
INSERT INTO 表名称(列1，列2) VALUES(值1，值2);
```

### 查询数据

```mysql
SELECT * FROM 表名称;

#或者 只查询某些特定属性
SELECT 列名称1，列名称2... FROM 表名称;

#当数据库的内容很多时，全部显示不现实，这时需要根据我们的需求查询特定的信息

# 从表格中按条件查询一条记录
SELECT 列名称 RROM 表名称 WHERE 列 运算符 值;

# 如：以下查找course表中的course_length>10的所有列
SELECT * RROM course WHERE course_length>10;
SELECT * RROM course WHERE course_name='linux';

# 支持的运算符有：=(等于),<>(不等于),>(大于),<(小于),>=(大于等于),<=(小于等于),BETWEEN(在某范围内),LIKE(搜索某种模式)
```

### 删除一条记录

```mysql
DELETE FROM 表名称 WHERE 列 运算符 值;
# 或者表中的所有信息
DELETE * FROM 表名称；
```

### 更新一条记录

```mysql
UPDATE 表名称 SET 列名称 = 新值 WHERE 列=值;
# WHERE条件是唯一的主键，如：
UPDATE course SET lecture = 'lee' WHERE id=3;
```

### DISTINCT返回结果删除重复项

```mysql
SELECT DISTINCT 列名称 FROM 表名称；

#如：
SELECT lecture FROM course;
#假如lecture（讲师）只有三个，但是有很多记录，我们就可以使用如下过滤重复项：
SELECT DISTINCT lecture FROM course; 
```

### WHERE条件使用逻辑组合AND & OR

```mysql
SELECT * FROM 表名称 WHERE 条件1 AND 条件2;
SELECT * FROM 表名称 WHERE 条件1 OR 条件2;
UPDATE course SET lecture = 'lee' WHERE id=3 AND course_name='linux';
```

### 对查询结果进行排序

```mysql
SELECT * FROM 表名称 ORDER BY 列名称;
# 倒序排序
SELECT * FROM 表名称 ORDER BY 列名称 DESC;

SELECT * FROM sourse ORDER BY course_length;
```

## msyql用户管理基础

mysql默认只有root用户，用户的信息保存在mysql数据库（不要随便修改）的user表中；`select HOST,USER from user;`可以查询user表中的部分信息；可以看到默认用户只有`root`。

### 创建新的用户

```mysql
CREATE USER 用户名 IDENTIFIED BY '密码';
CREATE USER yaro IDENTIFIED BY 'password';
# 新用户创建后是不能登陆的，因为没有设置权限

# 使用如下命令可以查看创建的新用户
SELECT HOST,USER FROM user;
```

### 删除/重命名用户

```mysql
# 删除用户
DROP USER yaro_db;

# 重命名用户名
RENAME USER yaro_db TO yaro;
```

### 修改用户密码

```mysql
# 修改当前用户密码（PASSWORD函数加密）
SET PASSWORD = PASSWORD('新密码')；
# 修改指定用户密码
SET PASSWORD FOR yaro = PASSWORD('新密码')；

# 使用如下命令可以看到密码是加密保存的
SELECT USER,PASSWORD FROM user;
```

## mysql权限管理基础

mysql权限系统控制一个用户能否进行连接，以及连接后能够针对哪些对象进行什么操作。

mysq权限控制包含两个阶段：

1、检查用户是否能够连接；
2、检查用户是否具有所执行动作的权限；

mysql授予权限可以分为以下几个层级：
1、全局层级
2、数据库层级
3、表层级
4、列层级
5、子程序层级

mysql通过GRANT授予权限，REVOKE撤销权限；

### 授权GRANT

```mysql
GRANT ALL PRIVILEGES ON 层级 TO 用户名@主机 IDENTIFIED BY 密码;

# 如：授予yaro用户全局级(*.* 第一个星号代表数据库，第二个星号代表表)全部权限
GRANT ALL PRIVILEGES ON *.* TO 'yaro'@'%' IDENTIFIED BY 'password';

# 如：授权yaro用户针对于yaro_db数据库的全部权限；
GRANT ALL PRIVILEGES ON yaro_db.* TO 'yaro'@'%' IDENTIFIED BY 'password';
```

### 删除权限REVOKE

```mysql
REVOKE ALL PRIVILEGES FROM 用户名;

# 如：撤销yaro用户的全部权限
REVOKE ALL PRIVILEGES FROM yaro;
```

### mysql链接认证

<img src="https://i.loli.net/2017/07/19/596edc06995b5.png">

>注意,`%`不包含`localhost`;

一般我们都是创建一个数据库,给它他个特定的用户管理,root用户权限太大;而且root用户默认不能远程登陆(只能本机连接),需要授权`GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';`;但是不安全;
如:

```mysql
CREATE DATABASE yaro_db;
CREATE USER yaro IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON yaro_db.* TO 'yaro'@'%' IDENTIFIED BY 'password';
```

## mysql简单的备份恢复

### 备份

mysql使用最为广泛的备份工具是mysql自带的`mysqldump`linux命令;

```sh
# 备份一个指定的数据库
mysqldump -u root -p 数据库名称 > 备份文件.sql
# 如:
mysqldump -u root -p yaro_db > yaro_db.sql

# mysqldump备份出来的是纯文本的SQL文件,可以修改后为其他数据库使用
```

### 恢复

```sh
msyql -u root -p 数据库名称 < 备份文件.sql
# 如:
mysql -u root -p yaro_db < yaro_db.sql
```

## 设置mysql数据库编码

数据库使用一个特定编码保存数据,如latin Big5 GB2312 UTF8 等,不同语言一般使用不同编码保存。

编码主要赢下一下两个方面：

1.数据库保存相同内容占用的空间大小。
2.数据库与客户端通信（两端编码不同会乱码）。

mysql数据库的默认编码是：

```mysql
# CentOS特定版本
character set :latin1
collation : latin1_swedish_ci
```

使用`SHOW CHARACTER SET;`查看mysql支持的编码种类;

使用`SHOW VARIABLES LIKE 'character_set%';`和`SHOW VARIABLES LIKE 'collation%';`查询mysql当前使用的编码(`SHOW VARIABLES`可以查询所有参数变量,`LIKE 'character_set%'`限制以'character_set%'开头);

创建数据库是可以指定其编码

```mysql
CREATE DATABASE yaro_db 
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
```

也可以通过如下命令修改其编码:

```mysql
ALTER DATABASE yaro_db CHARACTER SET utf8 COLLATE utf8_general_ci;
# 但是如果原数据库有内容,修改编码可能导致原数据异常显示;
```

通过修改配置文件`my.conf`设置mysql的默认编码

```mariadb
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
[mysqld]
default-character-set = utf8
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8
```

修改之后重启mysql服务,通过`SHOW VARIABLES LIKE 'character_set%';`查看默认编码是否修改成功;