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

-- 更新数据
UPDATE `students` SET `gender` = '女' WHERE `id` < 4;

-- 删除数据
DELETE FROM `students` WHERE `id` >5;