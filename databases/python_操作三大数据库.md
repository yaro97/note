# Python 操作三大数据库

## 数据库基础

关系型数据库： Mysql/MariaDB SQLite postgreSQL SQL-Server Oracle

非关系型数据库（not only sql）：MongoDB Redis Hbase Neo4j Cassandra CouchDB

非关系型数据库分类：文档性（查询性能没有redis高）、key-value型（redis内存存储）、列式数据库（分布式）、图形数据库（图结构相关算法）

## mysql基础

CRUD	Create(insert) Read(Select) Update() Delete

参考：http://www.runoob.com/mysql/mysql-create-database.html

- 操作范例

```sql
-- 创建数据库
CREATE DATABASE `school`;

-- 切换数据库
USE `school`;

-- 创建数据表
CREATE TABLE `students` (
	`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(20) NOT NULL,
	`nick_name` VARCHAR(20),
	`gender` CHAR(1),
	`in_time` DATETIME
);

-- 插入数据
INSERT INTO `students`
VALUES (1, '张三', '三哥', '男', now());

INSERT INTO `students` (`name`, `nick_name`, `gender`, `in_time`)
VALUES ('李四', '四哥', '男', now());

INSERT INTO `students` (`name`, `gender`, `in_time`)
VALUES ('王五', '女', now());

INSERT INTO `students` (`name`, `nick_name`, `gender`, `in_time`)
VALUES ('李四1', '四哥1', '男', now()),
	('李四2', '四哥2', '男', now()),
	('李四3', '四哥3', '男', now());
	
-- 查询数据
SELECT * FROM `students`;
SELECT `name`, `nick_name`, `gender` FROM `students`;
SELECT `id`, `name`, `nick_name`, `gender` FROM `students`;
SELECT `name`, `nick_name`, `gender` FROM `students` WHERE `gender` = '女';
SELECT `id`, `name`, `nick_name`, `gender` FROM `students` ORDER BY `id` DESC;
SELECT `id`, `name`, `nick_name`, `gender` FROM `students` ORDER BY `id` DESC LIMIT 3,2; -- 偏移量，数量

-- ASC = ASCENDING 上升
-- DESC = DESCENDING 下降

-- 更新数据
UPDATE `students` SET `gender` = '女' WHERE `id` < 4;

-- 删除数据
DELETE FROM `students` WHERE `id` >5;
```

- 新闻数据库设计实例

```sql
-- 1. 新建数据库：‘news‘， 编码：utf-8；
-- 2. 新建表：
CREATE TABLE `news`(
	`id` INT NOT NULL AUTO_INCREMENT,  --新闻id
	`title` VARCHAR(200) NOT NULL,  
	`content` VARCHAR(2000) NOT NULL,
	`types` VARCHAR(10) NOT NULL,  -- 新闻类别（娱乐、财经...）
	`image` VARCHAR(300) NULL,  -- 新闻配图
	`author` VARCHAR(20) NULL,
	`view_count` INT DEFAULT 0,  -- 浏览量
	`created_at` DATETIME NULL,  -- 创建日期
	`is_valid` SMALLINT DEFAULT 1,  -- 删除标记（数据库没有删除，只是删除标记）
	PRIMARY KEY(`id`)
) DEFAULT CHARSET = 'UTF8';
```

## MongoDB

pacaur -Sv mongodb

refer to : https://wiki.archlinux.org/index.php/MongoDB  
http://www.mongoing.com/docs/

show dbs;
use xxx;  # 切换数据库，没有则新建并切换；
db;  # 显示当前数据库；
stu = { "name" : "Yaro", "age" : 21 }
db.students.insert(stu)
db.students.find()

## Redis

### 安装配置

linux 直接repo安装

windows使用MS编译的redis

具体参考：http://www.runoob.com/redis/redis-install.html


### 常用操作

参考：http://www.runoob.com/redis/redis-tutorial.html

