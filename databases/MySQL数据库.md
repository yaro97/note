# 概述

## 数据库的好处

1. 持久化数据到本地
2. 可以实现结构化查询，方便管理

## 数据库相关概念

1. DB：数据库，保存一组有组织的数据的容器
2. DBMS：数据库管理系统，又称为数据库软件（产品），用于管理DB中的数据
3. SQL:结构化查询语言，用于和DBMS通信的语言, 不仅仅是MySQL;

## 数据库存储数据的特点

1. 将数据放到表中，表再放到库中
2. 一个数据库中可以有多个表，每个表都有一个的名字，用来标识自己。表名具有唯一性。
3. 表具有一些特性，这些特性定义了数据在表中如何存储，类似java中 “类”的设计。
4. 表由列组成，我们也称为字段。所有表都是由一个或多个列组成的，每一列类似java 中的”属性”
5. 表中的数据是按行存储的，每一行类似于java中的“对象”。

## MySQL介绍/安装(熟悉)

- 背景:
    - 前身属于瑞典的一家公司，MySQL AB
    - 08年被sun公司收购
    - 09年sun被oracle收购
- MySQL的优点
    1. 开源、免费、成本低
    2. 性能高、移植性也好
    3. 体积小，便于安装
- MySQL的安装
    - 属于c/s架构的软件，一般来讲安装服务端
    - 企业版
    - 社区版
- windows配置文件`my.ini`

## MySQL服务的启动和停止(熟悉)

- 方式一：计算机——右击管理——服务
- 方式二：通过管理员身份运行
    - net start 服务名（启动服务）
    - net stop 服务名（停止服务）

## MySQL服务的登录和退出(熟悉)

- 方式一：通过mysql自带的客户端:只限于root用户
- 方式二：通过windows自带的客户端
    - 登录：`mysql 【-h主机名 -P端口号 】-u用户名 -p密码`
    - 退出：`exit`或`ctrl+C`

## MySQL常见命令(熟悉)

```sql
SHOW DATABASES; #查看当前所有的数据库
USE 库名 #打开指定的库
SHOW TABLES; #查看当前库的所有表
SHOW TABLES FROM 库名; #查看其它库的所有表
CREATE TABLE 表名( #创建表

    列名 列类型,
    列名 列类型，
    。。。
);
DESC 表名; #查看表结构
SHOW CREATE TABLE 表名; #查看更详细的表结构
STATUS;  # 显示当前MYSQL的VERSION的各种信息
SELECT VERSION(); #查看服务器的版本
# 或者 shell命令: mysql --version
SELECT * FROM 表名; #查询所有列
INSERT INTO 表名 [(field1, field2, ...)] VALUES (val1, val2, ...)
UPDATE 表名 SET field1 = xxx WHERE field_id = yyy;
DELETE FROM field1 WHERE field_id = xxx;
```

## MySQL的语法规范

1. 不区分大小写,但建议关键字大写，表名、列名小写
2. 每条命令最好用分号结尾
3. 每条命令根据需要，可以进行缩进 或换行
4. 注释
    - 单行注释：`#注释文字`
    - 单行注释：`-- 注释文字`
    - 多行注释：`/* 注释文字  */`

# SQL的语言分类(熟悉 👍)

- DQL（Data Query Language）：数据查询语言
    - select 
- DML(Data Manipulate Language):数据操作语言
    - insert
    - update
    - delete
- DDL（Data Define Languge）：数据定义语言
    - create
    - drop
    - alter
- TCL（Transaction Control Language）：事务控制语言
    - commit
    - rollback
- 其他
    - 还有DCL（Data Control Languge）: 权限管理相关
    - 视图/流程控制/函数等

# DQL语言(`SELECT`)(熟悉 👍)

## 进阶1:基础查询

- 语法：`SELECT 要查询的东西 FROM 表名`;
- 特点:
    - 要查询的东西 可以是`常量值`/`表达式`/`字段`/`函数`
    - 通过`SELECT`查询完的结果 ，是一个虚拟的表格，不是真实存在
- 示例:
    1. 查询单个字段: `SELECT 字段名 FROM 表名;`
    2. 查询多个字段: `SELECT 字段名，字段名 FROM 表名;`
    3. 查询所有字段: `SELECT * FROM 表名`
    4. 查询常量: `SELECT 常量值;`
        >注意：字符型和日期型的常量值必须用单引号引起来，数值型不需要
    5. 查询函数: `SELECT 函数名(实参列表);`
    6. 查询表达式: `SELECT 100/1234;`
    7. 起别名: 
        - 语法:使用`AS`或者`空格`
        - 便于理解;
        - 如果要查询的字段有重名,可以区分;
        - 别名中有`空格`或其他特殊字符(如:`#`),使用`单/双引号`;
    8. 去重: `SELECT DISTINCT 字段名 FROM 表名;`
    9. `+`的作用: **做加法运算, 不能拼接字符串**
        - `SELECT 数值+数值`; 直接运算
        - `SELECT 字符+数值`;先试图将字符转换成数值，如果转换成功，则继续运算；否则转换成0，再做运算
        - `SELECT NULL+值`;结果都为NULL
    10. 【补充】CONCAT函数-拼接字符: `SELECT CONCAT(字符1，字符2，字符3,...);`,参数有NULL,结果一定为NULL
    11. 【补充】IFNULL函数: 
        - 功能：判断某字段或表达式是否为NULL，如果为NULL 返回指定的值，否则返回原本的值
        - `SELECT IFNULL(COMMISSION_PCT,0) FROM EMPLOYEES;`
    12. 【补充】ISNULL函数-判断某字段或表达式是否为NULL，如果是，则返回1，否则返回0

```sql
USE myemployees; #切换数据库
SELECT last_name FROM employees; #查询一个字段
SELECT last_name,salary,email FROM employees; #查询多个字段
SELECT last_name AS 员工,salary,email FROM employees; #查询结果字段重命名
SELECT e.last_name,e.salary,e.email FROM employees e; #查询过程中重命名表名
SELECT*FROM employees; #所有field(field顺序遵循原表)

#查询常量
SELECT 100; 
SELECT 'yaro';

#查询表达式
SELECT 100*3; 
SELECT 100%3; #余数

#查询函数
SELECT VERSION(); #mysql版本

#为结果字段起别名
SELECT VERSION() AS 版本;
SELECT first_name AS 名, last_name AS 姓 FROM employees;
SELECT first_name 名, last_name 姓 FROM employees; #省略 AS

#去重: 案例: 查询员工表中涉及到的所有部门ID
SELECT DISTINCT department_id FROM employees; 

#`+`的作用
SELECT '90'+'10'; #100, 试图把varchar转换成int
SELECT 'yaro'+10; #10, varchar转换失败,当做0
SELECT NULL+10; #Null, 只有null参与运算,结果一定为null

#CONCAT用法:案例:查询表中所有的列,并组合输出(如果是null用'0'代替)
SELECT CONCAT(last_name,' - ',first_name,',',job_id,',',IFNULL(commission_pct,'0')) AS 查询结果 FROM employees;
```

## 进阶2:条件查询

- 语法：`SELECT 要查询的字段|表达式|常量值|函数 FROM 表 WHERE 筛选条件;`
- 执行顺序: `FROM子句 > WHERE子句 > SELECT子句`
- 筛选条件分类:
    1. 条件表达式筛选: `> < >= <= = != <>`(`!=`和`<>`都是不等于,后者是mysql原生的)
    2. 逻辑表达式筛选(用于连接条件表达式): 
        - mysql中推荐的: `AND, OR, NOT`
        - 兼容其他编程语言: `&& || !`
    3. 模糊表达式筛选:
        - LIKE 和 通配符 配合:
            - `%` 对应通配符中的 `*`
            - `_` 对应通配符中的 `?`
            - **通配符不包含`NULL`**
            - 5.5版本以上可以匹配`字符`和`int`类型
            - 可以使用系统转义字符`\`,也可以使用`ESCAPE`关键字自定义转义字符(推荐);
        - REGEXP 和 正则:`WHERE last_name REGEXP '[1-5]ee.*'`
        - `BETWEEN AND`
        - `IN`
        - `IS NULL`, `IS NOT NULL` (**mysql不能用`=`判断`NULL`**, `IS`只能配合`NULL`使用)
            - 安全等于: `<=>` 具有`=`的特性, 而且还可以判断`NULL`,只不过可读性差点;

```sql
#条件表达式
#查询工资>12000的员工信息
SELECT * FROM employees WHERE salary>12000;
#查询部门编号!=90的员工名,部门ID
SELECT last_name, department_id FROM employees WHERE department_id!=90;

#逻辑表达式
#查询工资在10000-20000之间的员工名,工资以及奖金
SELECT last_name,salary,commission_pct FROM employees WHERE salary>10000 AND salary<20000;
#查询部门编号不是在90-110之间,或者工资高于15000的员工信息
SELECT * FROM employees WHERE department_id<90 OR department_id>110 OR salary >15000;
SELECT * FROM employees WHERE NOT(department_id>90 AND department_id<110) OR salary >15000;#同上

#模糊查询
#查询员工名中包含字符a的员工信息
SELECT * FROM employees WHERE last_name LIKE '%a%';
#查询员工名中第二个字符为a,第五个字符为e的员工信息
SELECT * FROM employees WHERE last_name LIKE '_a__e%';
#使用转义字符 \ (系统自带)
SELECT * FROM employees WHERE last_name LIKE '_\_%';
#使用自定义转义字符(如: `$`)
SELECT * FROM employees WHERE last_name LIKE '_$_%' ESCAPE '$';
#查询员工编号在100-120之间的员工信息
SELECT * FROM employees WHERE employee_id BETWEEN 100 AND 120; #左小右大,包含临界值
#查询员工编号为100或120的员工信息
SELECT * FROM employees WHERE employee_id IN (100, 120); #枚举100,200两个数
#myql不能用 = 判断 NULL;
SELECT * FROM employees WHERE commission_pct IS NULL;
SELECT * FROM employees WHERE commission_pct IS NOT NULL;
#安全等于
SELECT * FROM employees WHERE commission_pct <=> NULL;

#综合案例
#查询部门编号为90的员工姓名和年薪
SELECT last_name,salary*12*(1+IFNULL(commission_pct,0)) 年薪 FROM employees WHERE department_id=90;
#查询job_id不等于'IT'或工资等于12000的员工信息
SELECT * FROM employees WHERE job_id != 'IT' OR salary = 12000;
SELECT * FROM employees WHERE job_id <> 'IT' OR salary = 12000;
#查询departments设计的位置id
SELECT DISTINCT location_id FROM departments;
```

## 进阶3:排序查询

- 语法: `SELECT 查询列表 FROM 表 WHERE 筛选条件 ORDER BY 排序列表 [ASC|DESC]`
- 执行顺序: FROM子句 > WHERE子句 > SELECT子句 > ORDER BY子句 
- 特点: 
    1. 默认升序(`ASC`), 降序: `DESC`(该关键字是descend,也是describe);
    2. 排序列表支持: `单个字段、多个字段、函数、表达式、别名`
    3. `ORDER BY` 的位置一般放在查询语句的最后（除`LIMIT`语句之外）

```sql
#排序查询
SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM employees WHERE department_id>=90 ORDER BY hiredate;#按字段排序
SELECT *,salary*12*(1+IFNULL(commission_pct,0)) 年薪 FROM employees ORDER BY salary*12*(1+IFNULL(commission_pct,0)); #按表达式
SELECT *,salary*12*(1+IFNULL(commission_pct,0)) 年薪 FROM employees ORDER BY 年薪; #按别名
SELECT LENGTH(last_name),last_name,salary FROM employees ORDER BY LENGTH(last_name); #按函数
SELECT * FROM employees ORDER BY salary,employee_id DESC; #按多个字段排序(工资相同的话按照员工ID排序)
SELECT last_name,salary FROM employees WHERE salary NOT BETWEEN 8000 AND 17000 ORDER BY salary;
```

## 进阶4:常见函数

### 单行函数

1. 字符函数
    - LENGTH(str) 传入一个字符串,返回其字节数
    - CONCAT(str1,str2,...)  传入多个字符串,返回拼接后的字符串
    - UPPER(str) 传入一个字符串,返回大写的字符串
    - LOWER(str) 传入一个字符串,返回小写的字符串
    - SUBSTR() 有以下四种形式:
        - SUBSTR(str,pos) 从pos开始截取到最后
        - SUBSTR(str,pos,len) 从pos开始截取len个字符数
        - SUBSTR(str FROM pos FOR len)
        - SUBSTR(str FROM pos)
        - SUBSTRING() 和SUBSTR相同
    - INSTR(str,substr) 返回sub第一次出现的索引,未找到返回0
    - TRIM([remstr FROM] str) 从str中取出两边的restr(默认去除'空格')
        - LTRIM() 去左边空格
		- RTRIM() 去右边空格
    - LPAD(str,len,padstr) 为str的左边填充padstr,是总长度为len
    - RPAD(str,len,padstr) 为str的右边填充padstr,是总长度为len
    - REPLACE(str,from_str,to_str) 替换str中所有的from_str为to_str
    - SELECT PASSWORD('yaro'); 转换str为密文形式
    - SELECT MD5('yaro'); 转换str为MD5编码

```sql
SELECT LENGTH('张三丰yaro'); #utf8中汉字占三个字节
SHOW VARIABLES LIKE '%char%'; #utf8mb4
SELECT CONCAT(first_name,'-', last_name) FROM employees;
SELECT UPPER('Wang');
SELECT LOWER('Wang');
SELECT SUBSTR('李莫愁爱上了陆展元',7) 截取结果; #index从1开始
SELECT SUBSTR('李莫愁爱上了陆展元',1,3) 截取结果;
SELECT CONCAT(UPPER(SUBSTR(last_name,1,1)),LOWER(SUBSTR(last_name,2))) FROM employees; #首字母大写
SELECT INSTR('杨不悔爱上了殷六侠','殷六侠') AS 索引位置;
SELECT TRIM('  张无忌  ');
SELECT TRIM('a' FROM 'aa 张无忌 aa ');
SELECT LPAD('赵敏敏',2,'****');
SELECT REPLACE('赵敏爱张无忌爱赵敏','赵敏','张翠山');
SELECT PASSWORD('yaro');
SELECT MD5('yaro');
```

2. 数学函数

    ```sql
    #四舍五入
    SELECT ROUND(-1.55); 
    SELECT ROUND(-1.4568,3); #小数点后3位

    #向上取整(>= 的整数)
    SELECT CEIL(1.002);

    #向下取整(<= 的整数)
    SELECT FLOOR(1.999);

    #截断小数
    SELECT TRUNCATE(1.3456,2); #保留两位小数

    #取余
    SELECT MOD(10,3);
    SELECT 10%3;

    #随机数
    SELECT RAND(); #0-1之间的随机数
    ```

3. 日期函数

    ```sql
    #获取当前日期/时间
    SELECT NOW(); #日期+时间
    SELECT CURDATE(); #日期
    SELECT CURTIME(); #时间

    #获取指定的部分
    SELECT YEAR(NOW()); #年
    SELECT MONTH('2008-2-25'); #月
    SELECT MONTHNAME('2008-2-25'); #英文二月
    SELECT DAY('20081225'); #日
    SELECT DAY('2008/12/25');
    SELECT HOUR(NOW()); #小时
    SELECT MINUTE(NOW()); #分钟
    SELECT SECOND(NOW()); #秒

    #字符串-日期转换
    SELECT STR_TO_DATE('9月-23 1999','%m月-%d %Y'); #字符串到日期:1999-09-23
    #用途: 网站需要用户输入日期(字符串), 查询数据库需要转换成 日期格式;
    SELECT DATE_FORMAT('2018/7/6','%m月%d日%Y年'); #日期到字符串:07月06日2018年
    ```

    - 格式符如下:
        - `%Y` 代表 四位年份
        - `%y` 代表 两位年份
        - `%m` 代表 月份(01,02,...12)
        - `%c` 代表 月份(1,2,...12)
        - `%d` 代表 日(1,2,...12)
        - `%H` 代表 小时(24小时制)
        - `%h` 代表 小时(12小时制)
        - `%i` 代表 分钟(00,01,...59)
        - `%s` 代表 秒(00,01,...59)

4. 其他函数(系统函数)

    ```sql
    SELECT VERSION(); #当前mysql版本
    SELECT DATABASE(); #当前使用的数据库
    SELECT USER(); #当前登陆的用户名:root@localhost
    SELECT CURRENT_USER(); #当前登陆用户对应在user表中的哪一个:root@localhost
    ```

5. 流程控制函数

    - if函数(三元运算符)
        ```sql
        SELECT IF(10<5,'小','大'); #第一个表达式成立,返回第二个,否则返回第三个
        SELECT *, IF(commission_pct IS NULL,'没奖金!呜呜','有奖金!哈哈') 备注 FROM employees;
        ```

    - case函数
        - 案例1:查询员工的工作,要求:如果
            - 部门号=30,显示的工资为1.1倍;
            - 部门号=40,的工资为1.2倍;
            - 部门号=50,的工资为1.3倍;
            - 其他部门显示工资为原工资;
            ```sql
            SELECT salary 原始工资 ,department_id,
            CASE department_id
                WHEN 30 THEN salary*1.1
                WHEN 40 THEN salary*1.2
                WHEN 40 THEN salary*1.3
                ELSE salary
            END
            AS 新工资
            FROM employees;
            ```

        - 案例2:查询员工的工资情况,要求:如果
            - 工资>20000,显示A级别;
            - 工资>15000,显示B级别;
            - 工资>10000,显示C级别;
            - 否则,显示D级别;
            ```sql
            SELECT salary 原始工资,
            CASE
                WHEN salary>20000 THEN 'A级别'
                WHEN salary>15000 THEN 'B级别'
                WHEN salary>10000 THEN 'C级别'
                ELSE 'D级别'
            END
            AS 工资级别
            FROM employees;
            ```

### 统计(多行/分组/聚合)函数

- 作用: 统计多行记录的数据;
- 分类:
    - max 最大值
    - min 最小值
    - sum 和
    - avg 平均值
    - count 计算个数
- 语法: `select max(字段) from 表名;`
- 支持的类型:
    - `sum`和`avg`一般用于处理`数值`型
    - `max`、`min`、`count`可以处理`任何数据类型`
- 以上分组函数都忽略null
- 都可以搭配distinct使用，实现去重的统计:`select sum(distinct 字段) from 表;`
- count函数深入:
    - count(字段)：统计该字段非空值的个数
    - count(*):统计结果行数(含null) - 所有列中只要有不是null就统计;
    - count(1):统计结果行数(含null) - 查询虚拟表中额外添加一列,值全为`1`,并统计行数;
    - 效率上：
        - MyISAM存储引擎，`count(*)`最高(自带计数器)
        - InnoDB存储引擎，`count(*)`和`count(1)`效率>`count(字段)`
- 和`分组函数(结果只有一行)`一同查询的`字段`，必须是`group by(分组查询)`后出现的字段;

```sql
SELECT SUM(salary) 总和 FROM employees;
SELECT AVG(salary) 平均值FROM employees;
SELECT MIN(salary) 最小值 FROM employees;
SELECT MAX(salary) 最大值 FROM employees;
SELECT COUNT(salary) 总个数 FROM employees;
SELECT DATEDIFF(MAX(hiredate),MIN(hiredate)) 天数差 FROM employees; #入职日期最早/迟相差多少
SELECT COUNT(*) 个数 FROM employees WHERE department_id=90;
```

## 进阶5:分组查询

> 背景: 如何查询每个部门的平均工资?

- 分组查询一般同时用到`分组函数`和`GROUP BY`子句;
- 语法: `SELECT 分组函数,分组的字段 FROM 表 [WHERE 分组前筛选条件] GROUP BY 分组的字段 [HAVING 分组后的筛选条件] [ORDER BY 排序列表]`
    > 和`分组函数(结果只有一行)`一同查询的`字段`，必须是`GROUP BY(分组查询)`后出现的字段;
- 执行顺序: `FROM子句` > `WHERE子句` > `GROUP BY子句` > `HAVING子句` > `SELECT子句` > `ORDER BY子句`
- 关于筛选条件:
    - 分组前筛选:`WHERE关键字`   根据`分组前的原始数据`筛选 	放在`GROUP BY的前面`
    - 分组后筛选:`HAVING关键字`  根据`分组后得到的结果`筛选	    放在`GROUP BY 的后面`

### 按照字段分组查询

```sql
#查询每个工种的最高工资
SELECT MAX(salary),job_id FROM employees GROUP BY job_id; #注意前面的job_id必须出现在GROUP BY之后
#查询每个位置上的部门个数
SELECT COUNT(*),location_id FROM departments GROUP BY location_id;
#查询每个部门的平均工资
SELECT AVG(salary),department_id FROM employees GROUP BY department_id;
```

### 分组配合筛选

- 分组前筛选(WHERE)如下:

```sql
#查询每个部门中邮箱中包含e字符的员工的平均工资
SELECT AVG(salary),department_id FROM employees WHERE email LIKE '%e%' GROUP BY department_id;
#查询各领导手下有奖金员工的最高工资
SELECT MAX(salary),manager_id FROM employees WHERE commission_pct IS NOT NULL GROUP BY manager_id;
```

- 分组后筛选(HAVING)如下:

```sql
#查询哪些部门的员工个数>2
SELECT COUNT(*),department_id FROM employees GROUP BY department_id HAVING COUNT(*)>2;
#查询各工种有奖金员工的最高工资(且>12000)的工种编号和最高工资
SELECT MAX(salary),job_id FROM employees WHERE commission_pct IS NOT NULL GROUP BY job_id HAVING MAX(salary)>12000;
#查询领导编号>102的各领导手下的最低工资>5000的领导编号和最低工资
SELECT manager_id,MIN(salary) FROM employees WHERE manager_id>102 GROUP BY manager_id HAVING MIN(salary)>5000;
```

### 按照表达式/函数分组查询

```sql
#按员工姓名的长度分组,查询每组员工的个数,筛选员工概述>5的有哪些?
SELECT LENGTH(last_name) 姓名长度,COUNT(*) 员工个数 FROM employees GROUP BY LENGTH(last_name) HAVING 员工个数>5;
```

### 按照多个字段分组

多个字段都相同才分到一个组

```sql
#查询每个部门每个工种的员工的平均工资
SELECT department_id,job_id,AVG(salary) FROM employees GROUP BY department_id,job_id;
```

### 分组查询后排序

```sql
#查询每个部门每个工种的员工的平均工资
SELECT department_id,job_id,AVG(salary) FROM employees GROUP BY department_id,job_id ORDER BY AVG(salary);

SELECT job_id,MAX(salary),MIN(salary),AVG(salary),SUM(salary) FROM employees GROUP BY job_id ORDER BY job_id DESC;
```

## 进阶6:连接(多表)查询

本质: 之前都是查询一张表, 如果需要`查询的数据`涉及到多张表, 就需要**把多张表通过`连接条件`/`连接方式`组成`一张新的虚拟表`**;

![各连接查询应用场景](https://i.loli.net/2019/03/22/5c94dda47482f.png)

### 含义及笛卡尔乘积现象

当查询中涉及到了多个表的字段，需要使用多表连接查询:`SELECT 字段1，字段2 FROM 表1，表2,...WHERE 连接条件;`

笛卡尔乘积现象：
- 描述:当查询多个表时，没有添加有效的连接条件，导致多个表所有行实现完全连接,如,表1有m行,表2有n行,查询结果为m*n行;
- 解决：添加有效的连接条件;

```sql
SELECT * FROM departments; #27行记录:27个不同部门,分布在7个地方
SELECT * FROM locations; #23行记录:23个不同地方
SELECT * FROM departments d,locations l WHERE d.`location_id`=l.`location_id`; #两个表合并(按照location_id取交集),27行记录:27个不同部门7个重复的地方
SELECT * FROM departments d,locations l; #621(23*27)行记录:笛卡尔乘积现象-每行都与另外一张表所有的行搭配;
```

### 分类

- 按功能分类
    - 内连接(交集)
        - 等值连接
        - 非等值连接
        - 自连接
    - 外连接
        - 左外连接(交集 + 左差集[为NULL])
        - 右外连接(交集 + 右差集[为NULL])
        - 全外连接(msql不支持)(交集 + 左差集[为NULL] +  右差集[为NULL])
    - 交叉连接(笛卡尔乘积现象)
- 按年代分类
    - sql92标准: mysql中`仅`支持`内连接`; 也支持部分`外连接`(oracle/sqlserver支持,但不稳定)
    - sql99标准[推荐]: mysql中支持内连接 + 外连接(左外+右外) + 交叉连接

### SQL92语法(内连接)(交集)(不推荐)

解释: 根据`连接条件`连接多个表形成`新虚拟表`,不满足的`连接条件`过滤掉;

语法：

```sql
SELECT 查询列表
FROM 表1 别名,表2 别名
WHERE 等值/非等值筛选条件
[AND 筛选条件]
[GROUP BY 分组字段]
[HAVING 分组后的筛选]
[ORDER BY 排序字段]
```

#### 内连接-等值连接

- 特点：
	- 一般为表起别名
	- 多表的顺序可以调换
	- n表连接至少需要n-1个连接条件
	- 等值连接的结果是多表的交集部分

```sql
#案例1:查询女神名和对应的男神名
SELECT NAME,boyName FROM beauty,boys WHERE beauty.`boyfriend_id`=boys.`id`;
#案例2:查询员工名和对应的部门名
SELECT last_name,department_name FROM employees,departments WHERE employees.`department_id`=departments.`department_id`;

#可以起别名,原名不可再使用
#案例1:查询员工名\工种号\工种名
SELECT last_name,e.job_id,job_title FROM employees e,jobs j WHERE e.`job_id`=j.`job_id`; 

#可以交换表的位置:
#案例1:查询员工名\工种号\工种名
SELECT last_name,e.job_id,job_title FROM employees e,jobs j WHERE e.`job_id`=j.`job_id`; 

#可以配合筛选条件查询
#案例1:查询有奖金的员工名\部门名
SELECT last_name,department_name,commission_pct FROM employees e,departments d WHERE e.`commission_pct` IS NOT NULL AND e.`department_id`=d.`department_id`;
#案例2:查询城市名中第二个字符为"o"的部门名和城市名
SELECT department_name,city FROM departments d,locations l WHERE d.`location_id`=l.`location_id` AND city LIKE '_o%';

#可以配合分组查询
#案例1:查询每个城市的部门个数
SELECT COUNT(*) 个数,city FROM departments d,locations l WHERE d.`location_id`=l.`location_id` GROUP BY city;
#案例2:查询有奖金的每个部门的部门名,部门领导编号,该部门的最低工资
SELECT department_name,d.manager_id,MIN(salary)
FROM departments d,employees e
WHERE d.`department_id` = e.`department_id`
AND commission_pct IS NOT NULL
GROUP BY department_name,d.department_id;

#可以添加排序
#案例1:查询每个工种的工种名和员工的个数,并按员工个数排序
SELECT job_title,COUNT(*) 
FROM jobs j,employees e
WHERE e.`job_id`=j.`job_id`
GROUP BY job_title
ORDER BY COUNT(*) DESC;

#三表也可以连接
#案例1:查询员工名,部门名和所在的城市
SELECT last_name,department_name,city 
FROM employees e,departments d,locations l
WHERE e.`department_id`=d.`department_id`
AND d.`location_id`=l.`location_id`
AND city LIKE 's%k%';
```

#### 内连接-非等值连接

如: 有以下工资等级表`grade_level`:

```
grade_level  lowest_sal  highest_sal  
-----------  ----------  -------------
A                  1000           2999
B                  3000           5999
C                  6000           9999
D                 10000          14999
E                 15000          24999
F                 25000          40000
```

有如下非等值连接查询:

```sql
#案例1:查询员工的工资和工资级别
SELECT salary,grade_level
FROM employees e,job_grades g
WHERE salary BETWEEN g.`lowest_sal` AND g.`highest_sal`
AND g.`grade_level`='E';
```

#### 内连接-自连接

如: 查询员工名以及其上级的名字,(其中`员工名`和`上级名字`都在`employees`表中);

查找过程如下:先查找`employees`表中`last_name`对应的`manager_id`,然后通过上级员工的 `employee_id`在`employees`表中查找对应的`last_name`;

解决思路: 把`employees`表通过`别名`虚拟成两张表!

```sql
#查询员工名以及其上级的名字
SELECT e.last_name 员工,m.`last_name` 领导
FROM employees e, employees m
WHERE e.`manager_id`=m.`employee_id`;
```

### SQL99语法(`join`关键字)(推荐)

语法：
```sql
SELECT 查询列表
FROM 表1 别名
连接类型 JOIN 表2 别名 ON 连接条件
WHERE 筛选条件
GROUP BY 分组列表
HAVING 分组后的筛选
ORDER BY 排序列表
LIMIT 子句;
```

#### 内连接(交集)

解释: 根据`连接条件`连接多个表形成`新虚拟表`,不满足的`连接条件`过滤掉;

- 语法：
    ```sql
    SELECT 查询列表
    FROM 表1 别名
    [INNER] JOIN 表2 别名 ON 连接条件
    WHERE 筛选条件
    GROUP BY 分组列表
    HAVING 分组后的筛选
    ORDER BY 排序列表
    LIMIT 子句;
    ```

- 特点：
    - 表的顺序可以调换(前提:相邻的两个表有交集)
    - 内连接的结果=多表的交集
    - `INNER` 关键字可以省略
    - n表连接至少需要n-1个连接条件(JOIN)

- 分类：
    - 等值连接
    - 非等值连接
    - 自连接

- 1)内连接-等值连接
    ```sql
    #案例1:查询员工名/部门名
    SELECT last_name,department_name
    FROM employees e
    INNER JOIN departments d 
    ON e.department_id=d.department_id;

    #案例2:查询名字中包含e的员工名和工种名(添加筛选)
    SELECT last_name,job_title
    FROM employees e
    INNER JOIN jobs j ON e.job_id=j.job_id
    WHERE last_name LIKE '%e%';

    #案例3:查询部门个数>3的城市名和部门个数(添加分组+筛选)
    SELECT city,COUNT(*) 部门个数
    FROM departments d
    INNER JOIN locations l ON d.location_id=l.location_id
    GROUP BY city
    HAVING COUNT(*)>3;

    #案例4:查询员工人数>3的部门的 部门名和员工个数,并按个人降序排序(添加排序)
    SELECT department_name,COUNT(*) 员工数
    FROM employees e
    INNER JOIN departments d ON d.`department_id`=e.`department_id`
    GROUP BY department_name
    HAVING COUNT(*)>3
    ORDER BY COUNT(*) DESC;

    #案例4:查询员工名/部门名/工种名,并按部门名降序(三表联合)
    SELECT last_name,department_name,job_title
    FROM employees e
    INNER JOIN departments d ON e.department_id=d.department_id
    INNER JOIN jobs j ON e.job_id=j.job_id
    ORDER BY department_name;
    ```
- 2)内连接-非等值连接
    ```sql
    #查询员工表的工资级别
    SELECT salary,grade_level
    FROM employees e
    JOIN job_grades g ON salary BETWEEN g.lowest_sal AND g.highest_sal;

    #查询每个工资级别对应的人数,并按工资降序排序
    SELECT COUNT(*),grade_level
    FROM employees e
    INNER JOIN job_grades g ON salary BETWEEN g.lowest_sal AND g.highest_sal
    GROUP BY grade_level
    HAVING COUNT(*)>20
    ORDER BY grade_level DESC;
    ```
- 3)内连接-自连接
    ```sql
    #查询名字中含有"k"的员工及其领导的名字
    SELECT e.last_name,m.last_name
    FROM employees e
    INNER JOIN employees m ON e.manager_id=m.employee_id
    WHERE e.last_name LIKE '%k%';
    ```

#### 外连接(交集 + 差集)

- 应用场景:(交集 + 差集) - 查询一个表中含有,另一个表没有的数据;
- 语法：
    ```sql
    SELECT 查询列表
    FROM 表1 别名
    LEFT/RIGHT/FULL[OUTER] JOIN 表2 别名 ON 连接条件
    WHERE 筛选条件
    GROUP BY 分组列表
    HAVING 分组后的筛选
    ORDER BY 排序列表
    LIMIT 子句;
    ```
- 分类：
    - 左外连接(`左-右`):总行数同`左`,`左右`交集显示`左`的数据,`左`有`右`没有显示null;
    - 右外连接(`右-左`):总行数同`右`,`右左`交集显示`右`的数据,`右`有`左`没有显示null;
    - 全外连接(msql不支持):总行数同`左`和`右`之和,结果: `二者交集` + `左-右` + `右-左`;
- 特点：
    - 查询的结果 = `主表`中所有的行，如果`从表`和它匹配的将显示匹配行，如果从表没有匹配的则显示`NULL`
    - `LEFT JOIN` 左边的就是主表，`RIGHT JOIN` 右边的就是主表,`FULL JOIN` 两边都是主表
- 1)外连接-左外连接(交集 + 左差集[为NULL])
    ```sql
    #查询哪个部门没有员工
    SELECT d.*,e.employee_id
    FROM departments d
    LEFT JOIN employees e ON d.department_id=e.department_id
    WHERE e.employee_id IS NULL;
    ```
- 3)外连接-右外连接(交集 + 右差集[为NULL])
    ```sql
    #查询哪个部门没有员工
    SELECT d.*,e.employee_id
    FROM employees e
    RIGHT JOIN departments d ON d.department_id=e.department_id
    WHERE e.employee_id IS NULL;
    ```
- 3)外连接-右外连接(msql不支持)(交集 + 左差集[为NULL] +  右差集[为NULL])
    ```sql
    #查询哪个部门没有员工
    SELECT d.*,e.employee_id
    FROM employees e
    FULL JOIN departments d ON d.department_id=e.department_id
    WHERE e.employee_id IS NULL;
    ```

#### 交叉连接(笛卡尔乘积现象)

等价于笛卡尔乘积现象

- 语法：
    ```sql
    SELECT 查询列表
    FROM 表1 别名
    CROSS JOIN 表2 别名;
    
    #等价于
    SELECT 查询列表
    FROM 表1,表2
    ```

![各连接查询应用场景](https://i.loli.net/2019/03/22/5c94dda47482f.png)

## 进阶7:子查询

- 解释:
    - 从本质上来说: 把`子查询`的结果作为`主查询`的一部分(条件/表...),exists例外;
        - 子查询结果为标量(一个固定的值);
        - 子查询结果一列值(列表);
        - 子查询的结果为一行值(不常用)
        - 子查询的结果为一个虚拟表(不常用)
    - 从形式上来说: 嵌套在其他语句内部的select语句称为`子查询`或`内查询`，外面的语句可以是insert、update、delete、select等，一般select作为外面语句较多,外面如果为select语句，则此语句称为`外查询`或`主查询`

### 分类(熟悉 👍)

- 按结果集的行列
    - 标量子查询(子查询结果为`某一特定值`),常用,和`> < = <> >= <=` 搭配,又叫"单行子查询" 👍**常用**;
    - 列子查询(子查询结果为`一列值`,即`类型相同的列表`),常用,和`in,not in,any|some(任何一个),all`搭配,又叫"多行子查询"👍**常用**;
    - 行子查询：(子查询结果为`一行值`,即`一条记录`),**不常用**!
    - 表子查询：(子查询结果为`多行值`,即`多条记录`),**不常用**!
- 按出现位置
    - select后面：仅仅支持`标量子查询`
    - from后面：仅仅支持`表子查询`
    - where或having后面(👍**最重要!**👍):
        - 标量子查询(单行子查询👍)
        - 列子查询(多行子查询👍)
        - 行子查询(多行一列/多列)
    - exists后面(又叫相关子查询):
        - 支持所有查询语句
        - 验证子查询结果是否存在/为空
        - 可以用条件子查询中的`IN`关键字实现;
        - 不同于上面三个子查询,`主查询`和`exists子查询`的执行顺序是`交互执行`,所以又叫`相关子查询`;

### 特点

1. 子查询都放在小括号内;
2. 子查询可以放在from后面、select后面、where后面、having后面，但`一般放在条件(where/having)的右侧`;
3. 子查询优先于主查询执行，主查询使用了子查询的执行结果
	

### where或having后面的子查询(熟悉 👍)

- 1.标量子查询(某个具体的值)
    ```sql
    #案例1:查询谁的工资比Abel高?
    SELECT * 
    FROM employees 
    WHERE salary>(SELECT salary FROM employees WHERE last_name='Abel'); 

    #案例2:查询job_id与141号员工相同,salary比143号员工多的 员工姓名/job_id/工资
    SELECT last_name,job_id,salary
    FROM employees
    WHERE job_id=(SELECT job_id FROM employees WHERE employee_id=141)
    AND salary>(SELECT salary FROM employees WHERE employee_id=143);

    #案例3:查询公司工资最少的员工的 last_name/job_id/salary
    SELECT last_name,job_id,salary 
    FROM employees
    WHERE salary=(SELECT MIN(salary) FROM employees);

    #案例4:查询最低工资大于(50号部门最低工资)的部门id和最低工资;
    #步骤1:查询50号部门的最低工资
    SELECT MIN(salary) FROM employees WHERE department_id=50;
    #步骤2:嵌套
    SELECT department_id,MIN(salary)
    FROM employees
    GROUP BY department_id
    HAVING MIN(salary)>(SELECT MIN(salary) FROM employees WHERE department_id=50);
    ```
- 2.列子查询(一行多列)
    ```sql
    #案例1:返回location_id是1400或1700的部门中的所有员工姓名
    SELECT last_name,department_id
    FROM employees 
    WHERE  department_id IN (SELECT DISTINCT department_id FROM departments WHERE location_id IN (1400,1700));
    #也可以用连接查询实现(IN 和 =ANY 效果相同)
    SELECT last_name,e.department_id,location_id
    FROM employees e
    INNER JOIN departments d ON e.`department_id`=d.`department_id`
    WHERE  location_id IN (1400,1700);

    #案例2:返回其他工种中比(job_id为"IT_PROG"工种)任一工资低的员工的 员工号/姓名/job_id/salary
    SELECT employee_id,last_name,salary
    FROM employees
    WHERE salary < ANY (SELECT DISTINCT salary FROM employees WHERE job_id='IT_PROG')
    AND job_id <> 'IT_PROG';
    #any可以用max替换
    SELECT employee_id,last_name,salary
    FROM employees
    WHERE salary < (SELECT DISTINCT MAX(salary) FROM employees WHERE job_id='IT_PROG')
    AND job_id <> 'IT_PROG';

    #案例3:返回其他工种中比(job_id为"IT_PROG"工种)所有工资低的员工的 员工号/姓名/job_id/salary
    SELECT employee_id,last_name,salary
    FROM employees
    WHERE salary < ALL (SELECT DISTINCT salary FROM employees WHERE job_id='IT_PROG')
    AND job_id <> 'IT_PROG';
    ```
- 3.行子查询(一行多列, 或 多行多列)
    ```sql
    #案例1:查询员工编号最小且工资最高的员工信息(不一定存在)
    #运用之前的知识实现
    SELECT *
    FROM employees
    WHERE employee_id=(SELECT MIN(employee_id) FROM employees)
    AND salary=(SELECT MAX(salary) FROM employees);
    #使用行子查询实现(前提: 两个条件运算符相同,这里都是"=")
    SELECT *
    FROM employees
    WHERE (employee_id,salary)=( SELECT MIN(employee_id),MAX(salary) FROM employees );
    ```

### select后面的子查询

仅支持标量子查询,即,`子查询的结果`必须是`某个特定的值`(一行一列)

```sql
#案例1:查询departments表中每个部门的员工个数(在departments表后面追加一列"员工个数")
SELECT d.*, (SELECT COUNT(*) FROM employees e WHERE e.`department_id`=d.`department_id`) 员工个数
FROM departments d;

#案例2:查询员工号=102的部门名
SELECT 
(
	SELECT department_name
	FROM departments d
	WHERE d.department_id=e.`department_id`
) 部门名
FROM employees e
WHERE employee_id=102;
#或者搭配连接查询
SELECT (
	SELECT department_name
	FROM departments d
	INNER JOIN employees e ON d.department_id=e.`department_id`
	WHERE e.`employee_id`=102
) 部门名;
#或者使用where后面的子查询
SELECT d.department_name
FROM departments d
WHERE d.department_id=(SELECT e.department_id FROM employees e WHERE e.`employee_id`=102);
```

### from后面的子查询

`from`关键字后面跟的是`表`,所以`from后面的子查询`的结果应该是一个`表`,而且**必须起别名**;

```sql
#案例1:查询每个部门的平均工资的工资等级
#步骤: 1.查询每个部门的平均工资,得到一张表 avg_table;2.把avg_table表和job_grades表合并;3.查询合并后的虚拟表
SELECT avg_table.*,g.`grade_level`
FROM (SELECT AVG(salary) 平均工资,department_id FROM employees GROUP BY department_id) avg_table
INNER JOIN job_grades g ON avg_table.平均工资 BETWEEN g.`lowest_sal` AND g.`highest_sal`;

#案例2:查询各部门中工资比本部门评价工资高的员工信息
#步骤1:查询各部门的平均工资
SELECT AVG(salary),department_id
FROM employees
GROUP BY department_id;
#步骤2:把步骤1的结果集合employees表合并,进行连接查询,并筛选
SELECT *
FROM employees e
INNER JOIN (
	SELECT AVG(salary) 平均工资,department_id
	FROM employees
	GROUP BY department_id
) 平均工资表 ON e.`department_id`=平均工资表.`department_id`
WHERE e.`salary`>平均工资表.平均工资;
```

### exists后面的子查询(相关子查询)

- `exists`用于判断`子查询`结果是否为空,如果为空返回`0(false)`,否则返回`1(true)`;
- 能用`exists子查询`实现的,一定能用上面`条件子查询` 中 `IN`的方式实现;
- 注意: 与上面的`子查询`不同, 包含`exists子查询`的`查询语句`并不是先执行`exists子查询`,而是与`主查询`配合,所以叫`相关子查询`;

```sql
#查询(验证)子查询的结果是否存在(不为空);
SELECT EXISTS (SELECT * FROM employees) 表中是否有值; #1
SELECT EXISTS (SELECT * FROM employees WHERE salary>100000) "工资否有>1w的"; #0

#案例1:查询有员工的部门名
SELECT d.department_name
FROM departments d
WHERE EXISTS(
	SELECT *
	FROM employees e
	WHERE e.`department_id`=d.`department_id`
);
#使用IN的方式实现
SELECT d.department_name
FROM departments d
WHERE d.`department_id` IN (
	SELECT `department_id`
	FROM employees
);

#案例2:查询没有女朋友的男神信息
SELECT bo.*
FROM boys bo
WHERE NOT EXISTS (
	SELECT *
	FROM beauty b
	WHERE b.`boyfriend_id`=bo.`id`
);
#使用IN的方式实现
SELECT bo.*
FROM boys bo
WHERE bo.id NOT IN (
	SELECT boyfriend_id
	FROM beauty
);
```

### 子查询经典案例

```sql
#案例1:查询工资最低的员工信息:last_name,salary

#步骤1:查询最低工资
SELECT MIN(salary) FROM employees
#步骤1:查询最终信息
SELECT last_name,salary
FROM employees
WHERE salary=(SELECT MIN(salary) FROM employees);

#案例2:查询平均工资最低的部门信息

#步骤1:生成各部门的平均工资表, 按工资排序,limit 1,只查询其department_id
SELECT department_id 
FROM employees GROUP BY department_id ORDER BY AVG(salary) LIMIT 1;
#步骤2:获取目标部门信息
SELECT * FROM departments
WHERE department_id=(
	SELECT department_id 
	FROM employees GROUP BY department_id ORDER BY AVG(salary) LIMIT 1
);

#案例3:查询平均工资最低的部门信息和该部门的平均工资

#步骤1:查询最低工资的部门的 工资和编号
SELECT AVG(salary),department_id 
FROM employees GROUP BY department_id ORDER BY AVG(salary) LIMIT 1;
#步骤2:连接查询
SELECT d.*, 平均工资
FROM departments d
INNER JOIN (
	SELECT AVG(salary) 平均工资,department_id 
	FROM employees GROUP BY department_id ORDER BY AVG(salary) LIMIT 1
) ag_table ON ag_table.department_id=d.`department_id`;

#案例4:查询平均工资最高的job信息

#步骤1:查询个job的平均工资
SELECT AVG(salary),job_id FROM employees GROUP BY job_id;
#步骤2:查询1中最高工资对应的 job_id
SELECT job_id FROM employees GROUP BY job_id
ORDER BY AVG(salary) DESC LIMIT 1;
#步骤3:查询目标信息
SELECT * FROM jobs
WHERE job_id=(
	SELECT job_id FROM employees GROUP BY job_id
	ORDER BY AVG(salary) DESC LIMIT 1
);

#案例5:查询平均工资高于公司平均工资的部门有哪些?

#步骤1:查询平均工资
SELECT AVG(salary) FROM employees;
#步骤2:查询高于公司平均工资的 各部门的 平均工资/department_id
SELECT AVG(salary),department_id 
FROM employees 
GROUP BY department_id
HAVING AVG(salary)>(SELECT AVG(salary) FROM employees);

#案例6:查询公司中所有的manager的详细信息

#步骤1:查询所有的manager_id
SELECT DISTINCT manager_id FROM employees;
#步骤2:
SELECT * 
FROM employees
WHERE employee_id IN (SELECT DISTINCT manager_id FROM employees);

#案例7:查询各部门的最高工资中 最低的那个部门的 最低工资是多少

#步骤1:查询各部门的最高工资
SELECT MAX(salary) FROM employees
GROUP BY department_id;
#步骤2:排序,limit 1 -> 定位目标部门department_id
SELECT department_id FROM employees
GROUP BY department_id
ORDER BY MAX(salary) LIMIT 1;
#步骤3:
SELECT MIN(salary),department_id FROM employees 
WHERE department_id=(
	SELECT department_id FROM employees
	GROUP BY department_id
	ORDER BY MAX(salary) LIMIT 1
);
```

## 进阶8:分页查询(**重点!** 👍)

- 应用场景：实际的web项目中需要根据需求提交对应的分页查询的sql语句
- 本质:截取查询的结果,部分显示;
- 语法:
    ```sql
    select 字段|表达式,...
    from 表
    [where 条件]
    [group by 分组字段]
    [having 条件]
    [order by 排序的字段]
    limit [offset,] size;
    ```
- 特点：
	1. 起始条目索引从0开始
	2. `limit子句`放在查询语句的最后
	3. 公式：`select * from  表 limit （page-1）*sizePerPage,sizePerPage`

## 进阶9:UNION联合查询(多张表之间没有连接关系)

- 解释: union：合并、联合，**将多次查询结果合并成一个结果**
- 应用场景:
    - 要查询的结果来自于多张表,且多张表之前没有直接的连接关系,但是查询的信息是一致的;
    - 筛选条件过多,可以通过联合查询将一条复杂的查询语句拆分成多条语句;
- 语法:
    ```sql
    SELECT 字段列表 FROM 表 WHERE 过滤条件
    UNION [ALL]
    SELECT 字段列表 FROM 表 WHERE 过滤条件
    UNION [ALL]
    ...
- 意义
    - 
    - 适用于查询多个表的时候，查询的列基本是一致
- 需要注意的事项:
    1. 要求多条查询语句的查询字段必须一致
    2. 要求多条查询语句的查询的各字段类型、顺序最好一致
    3. `UNION` 去重，`UNION ALL`包含重复项
- 案例
    ```sql
    #案例1(筛选条件过多):查询部门编号>90或邮箱中包含"a"的员工信息
    #之前的实现方法:
    SELECT * FROM employees WHERE department_id>90 OR email LIKE '%a%';
    #联合查询的实现:
    SELECT * FROM employees WHERE department_id>90
    UNION
    SELECT * FROM employees WHERE email LIKE '%a%';

    #案例2(多个表表头类似):查询中国用户表中 和 外国用户表中 男性的信息
    SELECT c_id,c_name,c_sex FROM c_user WHERE c_sex='男'
    UNION
    SELECT u_id,u_name,u_sex FROM u_user WHERE u_sex='male';

    #案例3:网站全站搜索--也是通过关键字把所有的表都搜索 -> 联合查询
    ```

## 查询总结:`关键字`书写/执行顺序(熟悉 👍)

- 书写顺序
    ```sql
    SELECT 查询字段列表
    FROM 表1
    连接类型 JOIN 表2 ON 连接条件
    WHERE 分组前筛选条件
    GROUP BY 分组字段
    HAVING 分组后筛选条件
    ORDER BY 排序字段列表
    LIMIT [OFFSET,] SIZE;
    #另外, 字段/条件/表 中可以使用子查询的结果
    ```
- 执行顺序(从DBMS使用者角度)
    ```sql
    5   SELECT 查询字段列表
    1   FROM 表1  (生成原始虚拟表)
        连接类型 JOIN 表2 ON 连接条件 (JOIN 之后生成"笛卡尔乘积虚拟表", ON 之后生成连接后的虚拟表)
    2   WHERE 分组前筛选条件
    3   GROUP BY 分组字段
    4   HAVING 分组后筛选条件
    6   ORDER BY 排序字段列表
    7   LIMIT [OFFSET,] SIZE;
    #另外, 字段/条件/表 中可以使用子查询的结果
    ```
    - FROM子句: 组装来自不同数据源的数据;
    - WHERE子句: 按指定的条件对数据行进行筛选;
    - GROUP BY子句: 将上面过筛选的数据分组,并使用`分组(统计)函数`进行计算;
    - HAVING子句: 对上面各分组的统计数据进行再次筛选;
    - SELECT子句: 查看最终数据的哪些字段(或字段的计算结果);
    - ORDER BY子句: 按照什么样的顺序来查看数据;
    - LIMIT子句: 显示最终数据的全部还是部分;

# DML语言(INSERT/UPDATE/DELETE)(熟悉 👍)

数据库的最小单元是一条记录(`行`), 故 DML语言的最小操作单位也是`行`;

## 插入(INSERT)

### 方式1: 经典的插入方式(用的较多)

- 语法：`INSERT INTO 表名(字段名，...) VALUES(值1，...),(值1，...)...;`
- 特点：
	1. 插入的值的类型要与列的类型一致或兼容(隐式转换);
	2. Nullable的列，可以不用插入值，或用NULL填充;
	3. 列的顺序可以颠倒,对应即可;
	4. 列和值的个数必须一致;
	5. 列可以省略,默认是表中所有的列,而且顺序同原表;

```sql
#1.插入的值的类型要与列的类型一致或兼容(隐式转换)
INSERT INTO beauty (id,NAME,sex,borndate,phone,photo,boyfriend_id) VALUES (13,'唐艺昕','女','1990-4-23','1385544123',NULL,2);

#2.Nullable的列如何插入值
#方式1:传入NULL
INSERT INTO beauty (id,NAME,sex,borndate,phone,photo,boyfriend_id) VALUES (13,'唐艺昕','女','1990-4-23','1385544123',NULL,2);
#方式2:不写
INSERT INTO beauty (id,NAME,sex,borndate,phone,boyfriend_id) VALUES (14,'金星','女','1998-4-23','1332546823',2);
INSERT INTO beauty (id,NAME,sex,phone) VALUES (15,'娜扎','女','1332546823');

#3.列的顺序可以颠倒,对应即可
INSERT INTO beauty (NAME,sex,id,phone) VALUES ('蒋欣','女',16,'110');

#4.列和值的个数必须一致
INSERT INTO beauty (NAME,sex,id,phone,boyfriend_id) VALUES ('关晓彤','女',17,'220'); #报错

#5.列可以省略,默认是表中所有的列,而且顺序同原表
INSERT INTO beauty VALUES (18,'张飞','男',NULL,'119',NULL,NULL);
INSERT INTO beauty VALUES (19,'张飞','男',,'119',NULL,NULL);
```

### 方式2: SET插入方式

```sql
INSERT INTO beauty
SET id=19,`name`='刘涛',phone='999';
```

### 两种插入方式PK: 

1. 方式1支持一次插入多行,方式2不支持

```sql
INSERT INTO beauty
VALUES
	( 23, '唐艺昕1', '女', '1990-4-23', '1385544123', NULL, 2 ),
	( 24, '唐艺昕2', '女', '1990-4-23', '1385544123', NULL, 2 ),
	( 25, '唐艺昕3', '女', '1990-4-23', '1385544123', NULL, 2 );
```

2. 方式1支持子查询,方式2不支持

```sql
案例1:插入一条数据
INSERT INTO beauty (id,name,phone)
SELECT 26,'朱茜','11822345462'; #不需要VALUES,也可以从其他表查询,然后插入另一个表

案例2:插入多条数据
INSERT INTO beauty
SELECT 23, '唐艺昕1', '女', '1990-4-23', '1385544123', NULL, 2 UNION
SELECT 24, '唐艺昕2', '女', '1990-4-23', '1385544123', NULL, 2 UNION
SELECT 25, '唐艺昕3', '女', '1990-4-23', '1385544123', NULL, 2;
```

## 修改(UPDATE)

- 修改单表语法：`UPDATE 表名 SET 字段=新值,字段=新值 [WHERE 条件]`
    ```sql
    #案例1:修改 beauty 表中姓唐的女神的电话为 13333333
    UPDATE beauty SET phone='13333333'
    WHERE name LIKE '唐%';

    #案例2:修改 boys 表中id为2的名称为"张飞",魅力值为 10
    UPDATE boys SET boyName='张飞',userCP=10
    WHERE id=2;
    ```
- 修改多表语法(级联更新)(补充)(与`连接查询`对应)：
    - 92语法: 仅支持 `INNER` 连接
        ```sql
        UPDATE 表1 别名1,表2 别名2 
        SET 字段=新值，字段=新值 
        WHERE 连接条件 AND 筛选条件
        ```
    - 99语法(推荐):
        ```sql
        UPDATE 表1 别名1 INNER|LEFT|RIGHT JOIN 表2 别名2 ON 连接条件
        SET 字段=新值，字段=新值 
        WHERE 筛选条件
        ```
    - 案例:
        ```sql
        #案例1:修改张无忌的女朋友的手机号为114
        UPDATE boys bo INNER JOIN beauty b ON b.boyfriend_id=bo.id
        SET b.phone='114'
        WHERE bo.boyName='张无忌';

        #案例2:修改没有男朋友的女神的 男朋友编号都为 2
        UPDATE boys bo RIGHT JOIN beauty b ON b.boyfriend_id=bo.id
        SET b.boyfriend_id=2
        WHERE b.id IS NULL;
        ```

## 删除(DELETE)

### delete语句(删除n行)

> 没有 `[WHERE 筛选条件]`会删除所有数据;

- 单表的删除(★)：`DELETE FROM 表名 [WHERE 筛选条件]`
    ```sql
    #案例1:删除手机号尾数为 9 的女神信息
    DELETE FROM beauty WHERE phone LIKE '%9';
    ```
- 多表的删除：
    - 92语法: 仅支持 `INNER` 连接
        ```sql
        DELETE 别名1，别名2 #(删除哪个表,添加哪个别名)
        FROM 表1 别名1，表2 别名2
        WHERE 连接条件 AND 筛选条件;
        ```
    - 99语法(推荐):
        ```sql
        DELETE 别名1，别名2 #(删除哪个表,添加哪个别名)
        FROM 表1 别名1 INNER|LEFT|RIGHT JOIN 表2 别名2 ON 连接条件
        WHERE 筛选条件;
        ```
    - 案例:
        ```sql
        #案例1:删除张无忌的女朋友信息
        DELETE b
        FROM beauty b INNER JOIN boys bo ON bo.id=b.boyfriend_id
        WHERE bo.boyName='张无忌';

        #案例2:删除黄晓明及其女朋友的信息
        DELETE b,bo
        FROM beauty b INNER JOIN boys bo ON bo.id=b.boyfriend_id
        WHERE bo.`boyName`='黄晓明';
        ```

### truncate语句(删除所有行,清空表):
	
- 语法: `TRUNCATE TABLE 表名`


### 两种删除方式的区别【面试题】
	
1. truncate不能加where条件，而delete可以加where条件
2. truncate的效率高一丢丢(没有过滤条件)
3. truncate 删除带自增长的列的表后，如果再插入数据，数据从1开始; delete 删除带自增长列的表后，如果再插入数据，数据从上一次的断点处开始;
4. truncate删除没有返回值,delete删除有返回值("n行数据受影响");
5. truncate删除不能回滚，delete删除可以回滚;

# DDL语言(CREATE/DROP/ALTER)(掌握)

- DDL语言: 数据定义语言;
- 主要分为 `数据库`/`表` 两大部分;
- 具体的操作为 `创建(CREATE)`/`修改(ALTER)`/`删除(DROP)`

## 数据库的管理

- 创建库: `CREATE DATABASE [IF NOT EXISTS] 库名 [CHARACTER SET 字符集名];`
- 修改库:
    - 重命名:(不建议,不安全)
        - MYSQL曾经的版本支持: `RENAME DATABASE 旧数据库名 TO 新数据库名`,后取消;
        - 直接手动修改 数据库名 对应的 磁盘中文件夹名字;
    - 修改字符集: `ALTER DATABASE 库名 CHARACTER SET 字符集名;`
- 删除库: `DROP DATABASE [IF EXISTS] 库名;`

## 表的管理(重点 👍)

- 创建表(重点):
    ```sql
    CREATE TABLE [IF NOT EXISTS] 表名(
        字段名 字段类型[(长度) 约束],
        字段名 字段类型[(长度) 约束],
        ...
        字段名 字段类型[(长度) 约束],
        表级约束
    )

    # 如:
    CREATE TABLE IF NOT EXISTS stuinfo(
		stuId INT,
		stuName VARCHAR(20),
		gender CHAR,
		bornDate DATETIME
	);
	DESC studentinfo;
    ```
- 修改表:
    - 1. 添加列: `ALTER TABLE 表名 ADD COLUMN 列名 类型 [FIRST|AFTER 字段名];`
    - 2. 修改列的类型或约束: `ALTER TABLE 表名 MODIFY COLUMN 列名 新类型 [新约束];`
    - 3. 修改列名: `ALTER TABLE 表名 CHANGE COLUMN 旧列名 新列名 类型;`
    - 4. 删除列: `ALTER TABLE 表名 DROP COLUMN 列名;`
    - 5. 修改表名: `ALTER TABLE 表名 RENAME TO 新表名;`
- 删除表: `DROP TABLE [IF EXISTS] 表名;`
- 复制表
    - 仅仅复制表的 结构: `CREATE TABLE 新建表名 LIKE 被复制的表名;`
    - 复制表的 结构+数据: `CREATE TABLE 新建表名 SELECT 查询列表 FROM 被复制的表名 [WHERE 筛选];`
        - 复制所有字段,所有数据: `CREATE TABLE 新建表名 SELECT * FROM 被复制的表名;`
        - 复制部分字段,部分数据: `CREATE TABLE 查询列表 SELECT * FROM 被复制的表名 WHERE 筛选;`
        - 复制部分字段,空数据: `CREATE TABLE 查询列表 SELECT * FROM 被复制的表名 WHERE 0;`

## MySQL中的数据类型

### 数据类型选用原则

- 选择的类型越简单越好;
- 能满足需求的数值类型占用字节越小越好(节约空间);

### 数值型

- 整型
    - 分类:
        - tinyint: 1字节
        - smallint: 2字节
        - mediumint: 3字节 
        - int/integer: 4字节
        - bigint: 8字节
    - 特点：
        1. 都可以设置无符号和有符号，默认有符号，通过unsigned设置无符号;
        2. 如果超出了范围，会报out or range异常，插入临界值;
        3. 长度可以指定, 可以不指定，默认会有一个长度: int(11), 无符号int(10)...此长度仅代表查询结果显示的最大宽度，如果不够则左边用0填充，但需要搭配zerofill，并且设置zerofill后,默认变为无符号整型;
- 浮点型
    - 分类:
        - 浮点数:
            - float(M,D):4字节
            - double(M,D):8字节
        - 定点数：decimal(M,D) 或 dec(M,D)
    - 特点：
        - M代表整数部位+小数部位的个数，D代表小数部位
        - 如果超出范围，则报out or range异常，并且插入临界值
        - M和D都可以省略，如果是定点数，M默认为10，D默认为0;如果浮点数,则会根据插入的数值的精度来决定精度;
        - 如果精度要求较高(如货币的运算)，则优先考虑使用定点数;
- 字符型(含二进制)
    - char:固定长度的字符，写法为char(M)，M代表`字符数`不是`字节数`,最大长度不能超过M，占用`M`个字符,性能比`varchar`高一点点,其中M可以省略，默认为1
    - varchar:可变长度的字符，写法为varchar(M)，M代表`字符数`不是`字节数`,最大长度不能超过M，占用`<M`个字符,性能比`char`低一点点,其中M不可以省略
    - text:较长的文本
    - enum('python','java','js'):枚举,根据成员数分配占用字的节数(`2字节数:可存储255-65535个成员`),可保存0-65535个成员,一次只能插入一个成员,不区分大小写;
    - set('python','java','js'):集合,根据成员数分配占用字的节数(`字节数=ceil(成员数/8)`),可保存0-64个成员,一次可以一次插入多个成员,不区分大小写;
    - binary:(较短的)固定二进制
    - varbinary:(较短的)可变二进制
    - blob:较大的二进制(图片/音频/视频)
- 日期型(`需要引号包裹`)
    - year:年,1字节
    - date:日期,4字节
    - time:时间,3字节
    - datetime:日期+时间,8字节 
    - timestamp:日期+时间,4字节, 比较容易受时区、mysql语法模式/版本的影响，更能反映当前时区(`SET time_zone='+8:00';`)的真实时间
    
## MySQL中常见的约束

### 概述

- 目的: 用于限制表中的数据,为了保证表中的数据的准确/可靠性;
- 添加约束的时机:(应该在添加数据之前)
    - 创建表时;
    - 修改表时;
- 分类:
    - 列级约束: 语法上六大约束都支持,但`外键`/`CHECK`约束没有效果;
    - 表级约束: 除了 `NOT NULL`,`DEFAULT`,其他都支持;
- 查看表的约束信息:
    - `DESC 表名;` 查看字段信息
    - `SHOW INDEX FROM 表名;` 查看索引信息

### 常见的约束:六大约束("三键,非空,默认")

- `NOT NULL`：非空，该字段的值必填,如:姓名/学号
- `DEFAULT`：默认值,如:性别
- `CHECK`：检查，[mysql不支持,不报错但是没效果],比如:限制年龄>18岁
- `UNIQUE`：唯一,如:座位号
- `PRIMARY KEY`：主键，`UNIQUE`+`NOT NULL`,如: 编号/ID
- `FOREIGN KEY`：外键，用于约束某从表某列的值必须来自于主表的关联列的值,比如:员工表的部门编号字段

> `CHECK`：检查，[mysql不支持,不报错但是没效果],比如:限制性别`gender CHAR(1) CHECK(gender IN('男','女'))`,所以以下简称MySQL的"五大约束"

### 创建表时添加约束

- 列级约束(在各字段的后面添加):
    - MySQL支持的列级约束: `五大约束`除了`外键约束`(语法上六大约束都支持,但`外键`约束没有效果;)
    - 语法: `字段名 数据类型 约束1 约束2...`
    ```sql
    CREATE TABLE 表名(
        id INT PRIMARY KEY, #主键
        stu_name VARCHAR(20) NOT NULL, #非空
        gender CHAR(1),
        seat_id INT UNIQUE, #唯一键
        age INT DEFAULT 18, #默认
        major_id INT REFERENCES, major(id) #外键在列级约束没有效果
    )
    ```
- 表级约束(在所有字段的下面添加):
    - MySQL支持的表级约束: `三键约束`(主键/唯一键/外键)
    - 语法: `[CONSTRAINT 约束名] 约束(字段),`(约束的名字可以不起,默认是字段名,主键默认是`PRIMARY`)
    ```sql
    CREATE TABLE stuinfo(
        id INT,
        stu_name VARCHAR(20),
        gender CHAR(1),
        seat_id INT,
        age INT,
        major_id INT,
        CONSTRAINT pk PRIMARY KEY(id), #主键
        CONSTRAINT uq UNIQUE(seat), #唯一键
        CONSTRAINT fk_stuinfo_major FOREIGN KEY(major_id) REFERENCES major(id) #外键
    );
    ```
- 列级/表级约束对比
    - 列级约束:	支持:五大约束除外键,不可以起约束名;
    - 表级约束:	支持:三键约束(主键/唯一键/外键),可以起约束名，但对主键一直是`PRIMARY`;
- 常用的写法:
    - **`外键`使用`表级约束`,其他`四种约束`使用`列级约束`;**
    - `外键约束` 使用 `表级约束`: `[CONSTRAINT 约束名] FOREIGN KEY(字段名) REFERENCES 主表(被引用列)`
    - `其他约束` 使用 `列级约束`: `字段名 数据类型 约束1 约束2...`
    ```sql
    CREATE TABLE IF NOT EXISTS 表名(
        字段名 字段类型 约束1 约束2 ..., #常规通用格式
        id INT PRIMARY KEY,#主键
        stu_name VARCHAR(20) NOT NULL,#非空
        sex CHAR(1),
        age INT DEFAULT 18,#默认
        seat INT UNIQUE,#唯一键
        major_id INT,
        CONSTRAINT fk_stuinfo_major FOREIGN KEY(major_id) REFERENCES major(id), #外键
    )
    ```
- `主键`和`唯一键`对比
    - `UNIQUE`：唯一键
        - 唯一(行行之间不重复),可以为`NULL`,(注意,两个`NULL`也属于重复)
        - 一个表可以有多个`UNIQUE`列,
        - 允许`组合UNIQUE`(`UNIQUE(字段1,字段2)`)但不推荐(不稳定),
        - 如:座位号
    - `PRIMARY KEY`：主键
        - `UNIQUE`+`NOT NULL`,
        - 一张表只能有一个`主键`列,
        - 允许`组合主键`(`PRIMARY KEY(字段1,字段2)`)但不推荐(不稳定),
        - 如: 编号,ID
- `外键`详解
    1. 要求在从表设置外键关系,从表的字段值引用了主表的某字段值;
    2. 外键列和主表的被引用列要求类型一致或兼容，意义一样，名称无要求;
    3. 主表的被引用列要求是一个key（一般就是`主键`,也可以是`唯一键`,`外键`也不会报错,但是没有意义）;
    4. 插入数据，先插入主表;删除数据，先删除从表;可以通过以下两种方式来删除主表的记录:
        - 方式一：级联删除:`ALTER TABLE stuinfo ADD CONSTRAINT fk_stu_major FOREIGN KEY(majorid) REFERENCES major(id) ON DELETE CASCADE;`
        - 方式二：级联置空:`ALTER TABLE stuinfo ADD CONSTRAINT fk_stu_major FOREIGN KEY(majorid) REFERENCES major(id) ON DELETE SET NULL;`

### 修改表时 添加 或 删除 (列级)约束

1. 非空:
    - 添加非空: `ALTER TABLE 表名 MODIFY COLUMN 字段名 字段类型 NOT NULL;`
    - 删除非空: `ALTER TABLE 表名 MODIFY COLUMN 字段名 字段类型;`
2. 默认:
    - 添加默认: `ALTER TABLE 表名 MODIFY COLUMN 字段名 字段类型 DEFAULT 值;`
    - 删除默认: `ALTER TABLE 表名 MODIFY COLUMN 字段名 字段类型;`
3. 主键:
    - 添加主键: `ALTER TABLE 表名 ADD [CONSTRAINT 约束名] PRIMARY KEY(字段名);`
    - 删除主键: `ALTER TABLE 表名 DROP PRIMARY KEY;`
4. 唯一键:
    - 添加唯一: `ALTER TABLE 表名 ADD [CONSTRAINT 约束名] UNIQUE(字段名);`
    - 删除唯一: `ALTER TABLE 表名 DROP INDEX 索引名;`
5. 外键:
    - 添加外键: `ALTER TABLE 表名 ADD [CONSTRAINT 约束名] FOREIGN KEY(字段名) REFERENCES 主表(被引用列);`
    - 删除外键: `ALTER TABLE 表名 DROP FOREIGN KEY 约束名;`

> 主键/唯一键 添加/删除约束的写法 同时支持 列级约束和表级约束(如上); 外键虽然也支持 列级约束 写法,但是无效;


### 标识列(自增长列)

- 含义: 又称"自增长列",可以不用手动的插入值,系统提供默认的序列号;
- 特点：
    1. 自增长列必须为一个key(不一定是主键);
    2. 一个表最多有一个自增长列;
    3. 自增长列只能支持数值型(int/float/decimal);
    4. 关于初始值/步长:
        - 默认初始值为1,步长为1
        - 查看初始值/步长:`SHOW VARIABLES LIKE '%auto_increment%';`
        - 设置步长: `SET auto_increment_increment=3`
        - 不能设置初始值,但是可以变相实现:`INSERT INTO 表名(id...) VALUES(10,...)`,从10开始;

- 1)创建表时设置自增长列: `CREATE TABLE 表(	字段名 字段类型 约束 AUTO_INCREMENT)`
- 2)修改表时设置自增长列: `ALTER TABLE 表 MODIFY COLUMN 字段名 字段类型 约束 AUTO_INCREMENT`
- 3)删除自增长列: `ALTER TABLE 表 MODIFY COLUMN 字段名 字段类型 约束 `

# TCL语言(事务/交易)(了解)

## 概述

- TCL: Transaction Control Language 事务控制语言
- 事务: 是数据库管理系统执行过程中的一个逻辑单位，由一条或多条SQL语句组成,在这个单元中,每个SQL语句是相互依赖的;这个单元是一个不可分割的整体,要么执行完,要么一条都不执行(回滚);
- 存储引擎: 在MySQL中数据支持不同的技术(引擎)存储,通过`SHOW ENGINES`查看MySQL支持的存储引擎; 常用的存储引擎有:innodb/myisam/memory..., 其中只有innodb支持事务;

## 事务的特性

数据库事务具有以下四个特性(ACID特性):
- 原子性(Atomicity): 事务作为一个整体被执行，包含在其中的对数据库的操作要么全部被执行，要么都不执行。
- 一致性(Consistency): 事务应确保数据库的状态从一个`一致状态`转变为另一个`一致状态`。`一致状态`的含义是数据库中的数据应满足`完整性约束`(如: 之前两人存款和为200,转账完成后两人存款和还是200)。
- 隔离性(Isolation): 多个事务并发执行时，一个事务的执行不应影响其他事务的执行。
- 持久性(Durability): 已被提交的事务对数据库的修改应该永久保存在数据库中。

## 事务的使用步骤 👍

- 分类(了解):
    - 隐式（自动）事务：没有明显的开启和结束，本身就是一条事务可以自动提交，比如insert、update、delete;
    - 显式事务：具有明显的开启和结束;

- 使用显式事务：
    ```sql
    # 1. 开启事务
    SET AUTOCOMMIT=0; #关闭自动提交, (只是)开启当前回话的事务
    START TRANSACTION; #可以省略

    # 2. 编写一组SQL语句逻辑单元:可以设置回滚点
    DELETE FROM account WHERE id=25;
    SAVEPOINT 回滚点名; # 设置回滚点(配合 ROLLBACK TO 使用)
    DELETE FROM account WHERE id=29;
    ...

    # 3. 结束事务: 提交/回归
    COMMIT; #提交
    ROLLBACK; #全部回滚
    ROLLBACK TO 回滚点名; #回滚到指定的位置
    ```

## 并发事务/隔离级别

1. 事务的并发问题是如何发生的?
    - 多个事务 同时 操作 同一个数据库的相同数据时
2. 并发问题都有哪些?
    - `脏读`：B事务读取了A事务`已更新`但还`没有提交`的数据,如果A事务回滚,B事务读取的内容就是临时无效的;
    - `不可重复读`：由于A事务`更新`但还`没有提交`的数据, 会导致B事务多次读取某字段的结果会不同;
    - `幻读`：如果A事务在该表`插入`了一些新行但还`没有提交`,则B事务再次读取,就会多出几行;
3. 如何解决并发问题?
    - 通过设置隔离级别来解决并发问题
4. 隔离级别:
    ```sql
                                脏读		    不可重复读	    	幻读
    read uncommitted:读未提交     ×                ×              ×        
    read committed：读已提交      √                ×              ×
    repeatable read：可重复读     √                √              ×
    serializable：串行化          √                √              √
    ```
5. 相关知识点;
    - 隔离级别越高,安全性越好,并发性越低
    - MySQL支持四种隔离级别,默认是`repeatable read`级别;
    - Oracle只支持两种隔离级别:`read committed`和`serializable`;
    - 查看当前隔离级别: `SHOW VARIABLES LIKE '%tx_isolation%'`;或`SELECT @@tx_isolation;`
    - 设置隔离级别:
        - 当前会话: `SET SESSION TRANSACTION ISOLATION LEVEL xxx`
        - 全局: `SET GLOBAL TRANSACTION ISOLATION LEVEL xxx`
    - 注意: 演示事务的隔离级别需要两个CMD窗口,GUI软件多个查询页面属于一个回话(SESSION);

## 事务中truncate和delete的不同

truncate删除操作不能回滚，delete删除操作可以回滚;

# 视图(掌握 👍)

## 概述

- 应用场景:多个地方用到同样的查询结果,且该查询结果使用的SQL语句比较复杂,就可以把该复杂的sql逻辑封装成视图;

- 本质: 之前使用多表连接查询,可以把 `SELECT 字段列表 FROM 多表连接成一个虚拟表`得到的`虚拟表`, 把该段`SQL`语句块封装， 即`视图`,;

- `VIEW`的操作基本同之前`TABLE`的操作;

- 含义: MySQL从5.0.1版本开始提供视图的功能, 视图是一种虚拟存在的表, 此虚拟表行/列的数据来自于数据库中的原始表, 并且是在使用视图时**动态生成**,**只保存了sql逻辑, 不保存查询的结果**;

- 视图的优点: 
    1. 封装可以提高了sql的重用性;
    2. 封装后,再次使用更简洁;
    3. 封装后值开放特定的字段,保护基表的数据，提高了安全性

## 创建视图

- 语法：`CREATE VIEW  视图名 AS 复杂的查询语句;`
- 案例:
    ```sql
    #案例1:查询姓名中包含"a"字符的员工名/部门名/工种信息
    #定义视图
    CREATE VIEW myv1
    AS
    SELECT last_name,department_name,job_title
    FROM employees e
    JOIN departments d ON e.department_id=d.department_id
    JOIN jobs j ON j.job_id=e.job_id
    WHERE e.salary>3000;
    #使用视图
    SELECT * FROM myv1 WHERE last_name LIKE '%a%';

    #案例2:查询各部门的平均工资级别
    #定义视图
    CREATE VIEW myv2
    AS
    SELECT AVG(salary) ag,department_id
    FROM employees
    GROUP BY department_id;
    #使用视图
    SELECT myv2.`ag`,g.grade_level
    FROM myv2
    JOIN job_grades g ON myv2.`ag` BETWEEN g.`lowest_sal` AND g.`highest_sal`; 

    #案例3:查询平均工资最低的部门信息
    SELECT * FROM departments
    WHERE department_id=(SELECT department_id FROM myv2 ORDER BY ag LIMIT 1);
    ```

## 查看视图结构

- `DESC test_v7;`
- `SHOW CREATE VIEW test_v7;`

## 修改视图

- 方式一：
    ```sql
	CREATE OR REPLACE VIEW test_v7
	AS
	SELECT last_name FROM employees
	WHERE employee_id>100;
	```
- 方式二:
    ```sql
	ALTER VIEW test_v7
	AS
	SELECT employee_id FROM employees
    WHERE employee_id>100;
    ```

## 删除视图

`DROP VIEW test_v1,test_v2,test_v3;`

## 视图之虚拟表中数据的增删改查

- 注意: 视图在功能上是一个虚拟表, 理论可以对其进行CRUD操作, 但是**对该虚拟表的操作, 会映射到相关原始表, 并受原始表的限制**; 即,如果该虚拟表的操作逻辑无法映射到原始表,则不能对该虚拟表进行这些操作;
- 所以: 建议只对视图中的数据进行`读`操作,而不进行`增删改`操作;

1. 读取数据 👍(同基表操作)
    ```sql
    SELECT * FROM my_v4;
    SELECT * FROM my_v1 WHERE last_name='Partners';
    ```
2. 插入数据(不建议)
    ```sql
    INSERT INTO my_v4(last_name,department_id) VALUES('虚竹',90);
    ```
3. 修改数据(不建议)
    ```sql
    UPDATE my_v4 SET last_name ='梦姑' WHERE last_name='虚竹';
    ```
4. 删除数据(不建议)
    ```sql
    DELETE FROM my_v4 WHERE last_name LIKE '%e%';
    ```
5. 补充： 以下视图之虚拟表不能进行`增删改`操作
	- 包含以下关键字的sql语句：分组函数、DISTINCT、GROUP  BY、HAVING、UNION或者UNION ALL
	- 常量视图
	- SELECT中包含子查询
	- JOIN
	- FROM一个不能更新的视图
	- WHERE子句的子查询引用了FROM子句中的表

## 视图之虚拟表和表的区别

```
        关键字          是否占用物理空间            常用操作
视图     view         占用较少,只保存SQL逻辑       一般用于查询
表      table         占用较多,保存实际的数据       增删改查
```

# 变量

## 分类

- 系统变量
    - 全局变量(GLOBAL)
    - 会话变量(SESSION)
- 自定义变量
    - 用户变量
    - 局部变量

## 系统变量

### 全局变量

系统默认提供,必须拥有super权限更改全局变量，所有连接(会话)都可使用; 重启后恢复默认(重新加载配置文件);

```sql
#查看所有全局变量
SHOW GLOBAL VARIABLES;

#查看部分全局变量
SHOW GLOBAL VARIABLES LIKE '%char%';

#查找指定的某个全局变量
SELECT @@global.autocommit;
SELECT @@tx_isolation;

#设置指定的某个全局变量
SET @@global.autocommit=0; #或者
SET GLOBAL @@global.autocommit=0; #1-on; 0-off
```

### 会话变量

只是针对当前回话(连接)有效, `SESSION变量`包含`GLOBAL变量`;

```sql
#查看所有会话变量
SHOW [SESSION] VARIABLES;

#查看部分会话变量
SHOW [SESSION] VARIABLES LIKE '%char%';

#查找指定的某个会话变量
SELECT @@global.autocommit;
SELECT @@tx_isolation;

#设置指定的某个会话变量
SET @@global.autocommit=0; #或者
SET [SESSION] @@global.autocommit=0; #1-on; 0-off
```

## 自定义变量

### 用户变量

作用域：针对于当前连接（会话）生效;

位置：任意位置 -- `begin...end`里面或外面

```sql
#声明并赋值更新用户变量: 支持以下三种方式
SET @变量名=值;或
SET @变量名:=值;或
SELECT @变量名:=值;

#更新用户变量:支持如下四种方式
    #方式一：
	SET @变量名=值;或
	SET @变量名:=值;或
	SELECT @变量名:=值;
    #方式二：
	SELECT XX INTO @变量名 FROM 表; #查询的结果要求为一个特定值

#使用用户变量
SELECT @变量名;
```

### 局部变量

作用域：仅仅在定义它的`begin...end`中有效;

位置：只能放在`begin...end`中，而且只能放在第一句

```sql
#声明局部变量
DECLARE 变量名 类型 [DEFAULT 值];

#赋值或更新局部变量:支持如下四种方式
    #方式一：
	SET 变量名=值;或
	SET 变量名:=值;或
	SELECT @变量名:=值;
    #方式二：
	SELECT XX INTO 变量名 FROM 表;
#使用局部变量
SELECT 变量名;
```

# 存储过程与函数

## 概述

### 定义

- 存储过程: 把经常使用的`SQL语句`或`业务逻辑`封装起来,`预编译`保存在数据库中,当需要的时候从数据库中直接调用,省去了编译的过程,
提高效率;同时降低网络数据传输量(只传输存储过程名字)和请求次数(组需要请求一次`传输过程`);常常用于插入上万条数据,才能体现存储过程的优越性;
- 函数:同样,SQL的函数也是把经常使用的`SQL语句处理逻辑`封装起来, 但是有且仅有一个返回值,即,现有数据通过逻辑处理得到一个目标数据,以备他用. 使用方式/作用同系统内置函数;

### 函数和存储过程的区别

```
             关键字		    调用语法	    返回值			应用场景
函数		FUNCTION	SELECT 函数()	 有且仅有一个		处理数据并返回一个结果
存储过程	PROCEDURE	CALL 存储过程()	  可以有0个或多个	批量插入/更新/删除
```

### SQL客户端支持现状

- `Sqlyog`不支持使用SQL命令的方式创建 `函数/存储过程`;
- MySQL Shell(CMD命令行界面)支持,但是由于Shell默认使用`;`作为分隔符, 需要使用`DELIMITER $`语句重新声明`$`为MySQL Shell的 `结束标记`;以后所有的SQL语句必须使用`$`作为分隔符;
- `Navicat`支持使用SQL命令的方式创建 `函数/存储过程`,不需要改变分隔符为`$`, 操作时只需要`选中代码块`执行即可;

### 自定义函数和存储过程保存再哪里?

MySQL数据库服务器把所有的自定义`函数/存储过程`保存在`mysql数据库`的`proc 表`中.

## 存储过程

### 创建存储过程

- 语法:
    ```sql
    CREATE PROCEDURE 存储过程名(IN|OUT|INOUT 参数名  参数类型,...)
	BEGIN
		sql语句1;
		sql语句2;
        ...
	END $  #MySQL Shell需要修改分隔符
    ```
- 注意: 
    - 参数的格式如下: `参数模式 参数名 参数类型`,参数模式如下:
        - in:该参数只能作为输入 （该参数不能做返回值）
	    - out：该参数只能作为输出（该参数只能做返回值）
	    - inout：既能做输入又能做输出
    - 存储过程体中可以有多条sql语句，如果仅仅一条sql语句，则可以省略`BEGIN END`
    - 由于`SQL语句`使用`;`作为`结束标记`,`存储过程`需用要`DELIMITER $`语句重新声明`$`为MySQL Shell的 `结束标记`;

### 调用存储过程

```sql
CALL 存储过程名(实参列表) $
```

### 创建/调用存储过程-案例

- 空参-存储过程-案例
    ```sql
    # 案例1: 插入5条数据到admin表中
    #定义存储过程
    CREATE PROCEDURE myp1()
    BEGIN
        INSERT INTO admin(username,`password`) 
        VALUES('john1','000'),('lily','000'),('rose','000'),('yaro','000'),('tom','000');
    END $

    #调用存储过程
    CALL myp1() $

    #查看修改后的数据
    SELECT * FROM admin $
    ```
- IN模式参数-存储过程-案例
    ```sql
    #案例1:创建存储过程实现: 根据女神名,查询对应的男神信息
    #定义存储过程
    CREATE PROCEDURE myp2(IN beautyName VARCHAR(20))
    BEGIN
        SELECT bo.*
        FROM boys bo
        RIGHT JOIN beauty b ON bo.id=b.boyfriend_id
        WHERE b.`name`=beautyName;
    END $

    #调用存储过程
    CALL myp2('金星') $

    #案例2:创建存储过程实现: 判断用户是否登陆成功
    #定义存储过程
    CREATE PROCEDURE myp3(IN unsername VARCHAR(20),IN `password` VARCHAR(20))
    BEGIN
        DECLARE result INT DEFAULT 0; #声明变量并初始化
        SELECT COUNT(*) INTO result #变量赋值
        FROM admin
        WHERE admin.username=username AND admin.`password`=`password`;
        SELECT IF(result>0,'成功','失败'); #使用
    END $

    #调用存储过程
    CALL myp3('张飞','8888') $
    ```
- OUT模式参数-存储过程-案例
    ```sql
    #案例1:根据女神名,返回对应的男神名
    #定义存储过程
    CREATE PROCEDURE myp4(IN beautyName VARCHAR(20),OUT boyName VARCHAR(20))
    BEGIN
        SELECT bo.boyName INTO boyName
        FROM boys bo
        INNER JOIN beauty b ON bo.id=b.boyfriend_id
        WHERE b.name=beautyName;
    END$

    #调用存储过程
    CALL myp4('小昭',@bName)$  #得到返回值 @bName
    SELECT @bName$  #查看返回值
    ```
- INOUT模式参数-存储过程-案例
    ```sql
    #案例:传入a,b两个值,最终a,b翻倍并返回
    #定义存储过程
    CREATE PROCEDURE myp5(INOUT a INT,INOUT b INT)
    BEGIN
        SET a=a*2;
        SET b=b*2;
    END $

    #调用存储过程
    SET @m=10 $
    SET @n=20 $
    CALL myp5(@m,@n) $
    SELECT @m,@n $
    ```
### 查看存储过程信息

```sql
SHOW CREATE PROCEDURE myp1;
# 不能使用 DESC 语句
```

### 删除存储过程

```sql
DROP PROCEDURES 存储过程名字;
DROP PROCEDURES myp1,myp2; #会报错,一次不能删除多个
```

### 存储过程没有修改的命令

## 函数

### 函数的创建

- 语法:
    ```sql
    #创建函数
    CREATE FUNCTION 函数名(参数列表) RETURNS 返回值的类型
    BEGIN
        函数体;
    END $  #MySQL Shell需要修改分隔符
    ```
- 注意: 
    - 参数的格式如下: `参数名 参数类型`;
    - 必须有`RETURN`语句,习惯性放在`函数体`的最后(不放最后也不会报错);
    - 存储过程体中可以有多条sql语句，如果仅仅一条sql语句，则可以省略`BEGIN END`
    - 由于`SQL语句`使用`;`作为`结束标记`,`函数`需要`DELIMITER $`语句重新声明`$`为MySQL Shell的`结束标记`;

### 函数的调用

`自定义函数`的调用同`系统内置函数`的调用;

```sql
SELECT 函数名(实参列表)
```

### 创建/调用函数-案例

- 1)无参数有返回
    ```sql
    #案例1:返回公司员工的个数
    #定义函数
    CREATE FUNCTION myf1() RETURNS INT
    BEGIN
        DECLARE c INT DEFAULT 0; #定义局部变量
        SELECT Count(*) INTO c #赋值
        FROM employees;
        RETURN c;
    END $

    #调用函数
    SELECT myf1();
    ```
- 2)有参数有返回
    ```sql
    #案例1:根据员工名,返回他的工资;
    #定义
    CREATE FUNCTION myf2(name VARCHAR(20)) RETURNS DOUBLE
    BEGIN
        SET @sal=0; #定义用户变量
        SELECT salary INTO @sal #赋值
        FROM employees
        WHERE last_name=name;
        RETURN @sal; #返回查询的工资
    END $

    #调用
    SELECT myf2('Popp');
    ```

### 查看函数信息

```sql
SHOW CREATE FUNCTION myf1;
# 不能使用 DESC 关键字
```

### 删除函数

```sql
DROP FUNCTION 存储过程名字;
DROP FUNCTION myf1,myf2; #会报错,一次不能删除多个
```

### 函数没有修改的命令

# 流程控制结构(主要在`函数/存储控制`中使用)

流程控制结构分三种: 顺序结构,分支结构,循环结构;

## 分支结构

### if函数

- 功能: 实现简单双分支, 类似三元运算符
- 使用场景：可以用在任何位置
- 语法：`if(条件，值1，值2)`,条件成立返回值1,否则返回值2;

### case语句

- 功能: 实现多分支
- 使用场景：
	- 可以放在任何位置，
    - 如果放在begin end 外面，作为表达式结合着其他语句使用
    - 如果放在begin end 里面，一般作为独立的语句使用
- 语法：
    - 情况一：类似于switch...case语句
        ```sql
        case 表达式
        when 值1 then 结果1或语句1(如果是语句，需要加分号) 
        when 值2 then 结果2或语句2(如果是语句，需要加分号)
        ...
        else 结果n或语句n(如果是语句，需要加分号)
        end [case]（如果是放在begin end中需要加上case，如果放在select后面不需要）
        ```
    - 情况二：类似于多重if
        ```sql
        case 
        when 条件1 then 结果1或语句1(如果是语句，需要加分号) 
        when 条件2 then 结果2或语句2(如果是语句，需要加分号)
        ...
        else 结果n或语句n(如果是语句，需要加分号)
        end [case]（如果是放在begin end中需要加上case，如果放在select后面不需要）
        ```

### if else语句

- 功能: 实现多分支
- 使用场景：只能用在begin end中 ！！!!
- 语法：
    ```sql
	if 情况1 then 语句1;
	elseif 情况2 then 语句2;
	...
	else 语句n;
	end if;
    ```

## 循环结构

- 使用场景: 三种循环只能在`begin end`中使用(即,只能在`存储控制`或`函数`中使用) !!!
- MySQL的循环包括三类: while, loop, repeat
    - loop 一般用于实现简单的死循环
    - while 先判断后执行
    - repeat 先执行后判断，无条件至少执行一次
- 循环控制: `iterate` 类似于 `continue`(结束本次循环,继续下一次循环); `leave` 类似于 `break`(跳出所有循环);
- 可以为循环起名称,如果循环中使用了`循环控制`,则必须为循环起名称;

- 1)while语法:
    ```sql
    [名称:]WHILE 循环条件 DO
        循环体;
    END WHILE [名称];
    ```
- 2)loop语法:
    ```sql
    [名称：]LOOP
        循环体;
    END LOOP [名称];
    ```
- 3)repeat语法:
    ```sql
    [名称:]REPEAT
        循环体;
    UNTIL 结束条件 
    END REPEAT [名称];
    ```

```sql
#===案例1: 根据传入的次数批量在admin表中插入多条记录
#定义存储控制
CREATE PROCEDURE pro_while(IN insert_count INT)
BEGIN
	DECLARE i INT DEFAULT 1; #定义局部变量
	WHILE i<insert_count DO
		INSERT INTO admin(username,`password`) VALUES(CONCAT('Rose',i),'666');
		SET i=i+1;
	END WHILE;
END $

#调用存储控制
CALL pro_while(100);

#查看批量插入的数据
SELECT * FROM admin;

#===案例2: 根据传入的次数批量在admin表中插入多条记录,但是次数>20则停止
TRUNCATE TABLE admin; #删除admin表所有数据
DROP PROCEDURE pro_while; #删除pro_while存储控制

#定义存储控制
CREATE PROCEDURE pro_while(IN insert_count INT)
BEGIN
	DECLARE i INT DEFAULT 1; #定义局部变量
	Tag_A:WHILE i<insert_count DO
		INSERT INTO admin(username,`password`) VALUES(CONCAT('Rose',i),'666');
		IF i>=20 THEN LEAVE Tag_A;
		END IF;
		SET i=i+1;
	END WHILE Tag_A;
END $

#调用存储控制
CALL pro_while(100);

#查看批量插入的数据
SELECT * FROM admin;

#===案例3: 根据传入的次数批量在admin表中插入多条记录,但只插入i为偶数的记录
TRUNCATE TABLE admin; #删除admin表所有数据
DROP PROCEDURE pro_while; #删除pro_while存储控制

#定义存储控制
CREATE PROCEDURE pro_while(IN insert_count INT)
BEGIN
	DECLARE i INT DEFAULT 0; #定义局部变量
	Tag_A:WHILE i<insert_count DO
		SET i=i+1;
		IF	MOD(i,2)!=0 THEN ITERATE Tag_A;
		END IF;
		INSERT INTO admin(username,`password`) VALUES(CONCAT('Rose',i),'666');
	END WHILE Tag_A;
END $

#调用存储控制
CALL pro_while(100);

#查看批量插入的数据
SELECT * FROM admin;

#===案例4: 通过存储控制(循环)向random_str表中插入 长度/字符 皆随机的 字符串
#创建表random_str
DROP TABLE IF EXISTS random_str;
CREATE TABLE random_str(
	id INT PRIMARY KEY auto_increment,
	content VARCHAR(20)
);

#创建存储控制:向random_str表中插入 长度/字符 皆随机的 字符串
CREATE PROCEDURE random_str_pro(IN insert_count INT)
BEGIN
	DECLARE i INT DEFAULT 1; #定义变量i, 表示插入次数
	DECLARE str VARCHAR(26) DEFAULT 'abcdefghijklmnopqrstuvwxyz';
	DECLARE start_index INT DEFAULT 1; #代表起始索引
	DECLARE len INT DEFAULT 1; #代表截取长度
	
	WHILE i<insert_count DO
		SET len=FLOOR(RAND()*(20-start_index+1)+1); #产生一个随机整数,代表截取长度,1-(26-start_index+1)
		SET start_index=FLOOR(RAND()*26+1); #产生一个1-26的随机整数
		INSERT INTO random_str(content) VALUES(SUBSTR(str,start_index,len));
		SET i=i+1;
	END WHILE;
	
END

#调用存储控制
CALL random_str_pro(10);

#查看插入结果
SELECT * FROM random_str;
```

# 索引

## 概述

[参考文章](https://segmentfault.com/a/1190000003072424)

MySQL官方对索引的定义为：索引（Index）是帮助MySQL高效获取数据的`数据结构`。

> 数据库查询是数据库的最主要功能之一。我们都希望查询数据的速度能尽可能的快，因此数据库系统的设计者会从查询算法的角度进行优化。最基本的查询算法当然是顺序查找（linear search），这种复杂度为O(n)的算法在数据量很大时显然是糟糕的，好在计算机科学的发展提供了很多更优秀的查找算法，例如二分查找（binary search）、二叉树查找（binary tree search）等。
> 如果稍微分析一下会发现，**每种查找算法都只能应用于特定的数据结构之上**，例如二分查找要求被检索数据有序，而二叉树查找只能应用于二叉查找树上，但是数据本身的组织结构不可能完全满足各种数据结构（例如，理论上不可能同时将两列都按顺序进行组织），所以，在数据之外，数据库系统还维护着满足特定查找算法的数据结构，这些数据结构以某种方式引用（指向）数据，这样就可以在这些数据结构上实现高级查找算法。这种数据结构，就是索引。
> 创建索引时，将获取要创建索引的列，并对其进行排序。然后，将一个指针连同每一行的索引值存储起来，组成键值对（目录名和页码）。使用索引时，系统首先通过已排序的列值执行快速搜索，然后使用相关联的指针值来定位具有所要查找值的行。
> 一旦创建了索引，MySQL会自动维护和使用它们。

- 优点:
    - 大大加快数据的检索速度;
    - 创建唯一性索引，保证数据库表中每一行数据的唯一性;
    - 加速表和表之间的连接;
    - 在使用分组和排序子句进行数据检索时，可以显著减少查询中分组和排序的时间。
- 缺点:
    - 索引需要占物理空间
    - 当对表中的数据进行增加、删除和修改的时候，索引也要动态的维护，降低了数据的维护速度。

## 索引的存储分类

索引是在MYSQL的存储引擎层中实现的，而不是在服务层实现的。所以每种存储引擎的索引都不一定完全相同，也不是所有的存储引擎都支持所有的索引类型。MYSQL目前提供了一下4种索引:
- B-Tree 索引：最常见的索引类型，大部分引擎都支持B树索引。
- HASH 索引：只有Memory引擎支持，使用场景简单。
- R-Tree 索引(空间索引)：空间索引是MyISAM的一种特殊索引类型，主要用于地理空间数据类型。
- Full-text (全文索引)：全文索引也是MyISAM的一种特殊索引类型，主要用于全文索引，InnoDB从MYSQL5.6版本提供对全文索引的支持。

MyISAM、InnoDB引擎、Memory三个常用引擎类型比较: 
```
索引	      MyISAM引擎    InnoDB引擎    Memory引擎
B-Tree 索引	    支持	     支持	       支持
HASH 索引	    不支持	     不支持	        支持
R-Tree 索引	    支持	     不支持	       不支持
Full-text 索引	不支持	     暂不支持	   不支持
```

B-TREE索引类型:
- 普通索引: 这是最基本的索引类型，而且它没有唯一性之类的限制。普通索引可以通过以下几种方式创建：
    - （1）创建索引: `CREATE INDEX 索引名 ON 表名(列名1，列名2,...);`
    - （2）修改表: `ALTER TABLE 表名ADD INDEX 索引名 (列名1，列名2,...);`
    - （3）创建表时指定索引：`CREATE TABLE 表名 ([...], INDEX 索引名 (列名1，列名 2,...));`
- UNIQUE索引: 表示唯一的，不允许重复的索引，如果该字段信息保证不会重复例如身份证号用作索引时，可设置为unique：
    - （1）创建索引：`CREATE UNIQUE INDEX 索引名 ON 表名(列的列表);`
    - （2）修改表：`ALTER TABLE 表名ADD UNIQUE 索引名 (列的列表);`
    - （3）创建表时指定索引：`CREATE TABLE 表名([...], UNIQUE 索引名 (列的列表));`
- 主键：PRIMARY KEY索引: 主键是一种唯一性索引，但它必须指定为“PRIMARY KEY”。
    - （1）主键一般在创建表的时候指定：`CREATE TABLE 表名([...], PRIMARY KEY (列的列表));` 。
    - （2）也可以通过修改表的方式加入主键：`ALTER TABLE 表名ADD PRIMARY KEY (列的列表);`。
    - 每个表只能有一个主键。 （主键相当于聚合索引，是查找最快的索引）
    > 注：不能用CREATE INDEX语句创建PRIMARY KEY索引

## 创建索引

- 可以在执行`CREATE TABLE语句`时可以创建索引,也可以单独用`CREATE INDEX`或A`LTER TABLE`来为表增加索引。

1. ALTER TABLE - ALTER TABLE用来创建普通索引、UNIQUE索引或PRIMARY KEY索引。
    - ALTER TABLE table_name ADD INDEX index_name (column_list)
    - ALTER TABLE table_name ADD UNIQUE (column_list)
    - ALTER TABLE table_name ADD PRIMARY KEY (column_list)
2. CREATE INDEX - CREATE INDEX可对表增加普通索引或UNIQUE索引。
    - CREATE INDEX index_name ON table_name (column_list)
    - CREATE UNIQUE INDEX index_name ON table_name (column_list)

##  查看索引

```sql
show index from tblname;
show keys from tblname;
```

- Table：表的名称
- Non_unique：如果索引不能包括重复词，则为0。如果可以，则为1
- Key_name：索引的名称
- Seq_in_index：索引中的列序列号，从1开始
- Column_name：列名称
- Collation：列以什么方式存储在索引中。在MySQL中，有值‘A’（升序）或NULL（无分类）。
- Cardinality：索引中唯一值的数目的估计值。通过运行ANALYZE TABLE或myisamchk -a可以更新。基数根据被存储为整数的统计数据来计数，所以即使对于小型表，该值也没有必要是精确的。基数越大，当进行联合时，MySQL使用该索引的机会就越大。
- Sub_part：如果列只是被部分地编入索引，则为被编入索引的字符的数目。如果整列被编入索引，则为NULL。
- Packed：指示关键字如何被压缩。如果没有被压缩，则为NULL。
- Null：如果列含有NULL，则含有YES。如果没有，则该列含有NO。
- Index_type：用过的索引方法（BTREE, FULLTEXT, HASH, RTREE）。
- Comment：更多评注。

## 索引列选择的原则

1. 较频繁的作为查询条件的字段应该创建索引
2. 唯一性太差的字段不适合单独创建索引，即使频繁作为查询条件
3. 更新非常频繁的字段不适合创建索引
4. 不会出现在 WHERE 子句中的字段不该创建索引

## 关于全文索引

前面查询数据时,使用`LIKE`和`REGEXP`可以通过`通配符/正则`来匹配文本内容,但是MySQL尝试匹配表中所有行（而且这些搜索极少使用表索引）。因此，高版本的mysql支持中文的全文索引.

- 创建全文索引
    - 1)创建表的同时创建全文索引
        ```sql
        CREATE TABLE articles (
            id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            title VARCHAR (200),
            body TEXT,
            FULLTEXT (title, body) WITH PARSER ngram
        ) ENGINE = INNODB;
        ```
    - 2)通过 alter table 的方式来添加
        ```sql
        ALTER TABLE articles ADD FULLTEXT INDEX ft_index (title,body) WITH PARSER ngram;
        ```
    - 3)直接通过create index的方式
        ```sql
        CREATE FULLTEXT INDEX ft_index ON articles (title,body) WITH PARSER ngram;
        ```
- 使用全文索引
    ```sql
    SELECT * FROM articles
    WHERE MATCH (title,body)
    AGAINST ('一路 一带' IN NATURAL LANGUAGE MODE);

    # 不指定模式，默认使用自然语言模式
    SELECT * FROM articles
    WHERE MATCH (title,body)
    AGAINST ('一路 一带');
    ```
- 删除全文索引
    - DROP INDEX full_idx_name ON tommy.girl;
    - ALTER TABLE tommy.girl DROP INDEX ft_email_abcd;

## 关于 键 和 索引

- 键(key): 包含 主键/外键/唯一键
- 主键：主键的唯一作用就是唯一标识表中的某一行数据,分为:单一主键和联合主键
    - 单一主键: 用一列就能唯一标识一行
    - 联合主键: 当使用一列已经不能唯一标示一行的时候，就要采用多列唯一标识一行
- 唯一键：设置了UNIQUE的列：
- 外键: 用于连接两个表的键,从表的外键一定是某个主表的主键;
- 索引：索引的作用就是提高数据的检索速度，分为单一索引和联合索引：
    - 单一索引: 用某一列数据作为索引，默认是`index索引`，这一列可以包含重复数据；如果某一列不存在重复数据最好设置成`unique索引`，比`index索引`速度更快，在text数据上要使用`fulltext索引`。
    - 联合索引：为了更进一步提高检索速度，每次检索都需要用多列同时进行时，就可以把这多列设为联合索引，提高索引速度，根据多列是否唯一，也分为index索引和unique索引。
- 键一定是索引，但是索引不一定是主键。一个表只能有一个主键或联合主键，但是可以有多个索引。


# 触发器(trigger)


## 概述

- 触发器: 类似JS中的事件监听, 当某些事件(表的 insert，delete， update 操作)发生时, 触发目标sql语句的执行;
- 触发器是一种特殊类型的`存储过程`，它不同于我们前面介绍过的存储过程。触发器主要是通过事件进行触发而被执行的，而存储过程可以通过存储过程名字而被直接调用。
- 尽量少使用触发器，甚至不建议使用: 触发器很消耗资源，如果使用的话要谨慎的使用，确定它是非常高效的;
- 只有表才支持触发器，视图不支持（临时表也不支持）。
- 每个表最多支持6个触发器（每条 INSERT 、 UPDATE和 DELETE 的之前和之后）。

## 创建触发器

在创建触发器时，需要给出4条信息: 
- 唯一的触发器名；
- 触发器关联的表；
- 触发器应该响应的活动（ DELETE 、 INSERT 或 UPDATE ）；
- 触发器何时执行（处理之前或之后）。

```sql
CREATE TRIGGER <触发器名称>
{ BEFORE | AFTER }
{ INSERT | UPDATE | DELETE }
ON <表名称>
FOR EACH ROW
<触发的SQL语句>
```

## 查看触发器

```sql
SHOW TRIGGERS\G;
```

## 删除触发器

```sql
DROP TRIGGER [IF EXISTS] [schema_name.]trigger_name;
```

# 游标(CURSOR)

## 概述

- 游标（cursor）是一个存储在MySQL服务器上的数据库查询，它不是一条 SELECT 语句，而是被该语句检索出来的结果集。在存储了游标之后，应用程序可以根据需要滚动或浏览其中的数据
- 只能用于`存储过程` 不像多数DBMS，MySQL游标只能用于`存储过程（和函数）`。

## 创建/使用游标

```sql
create procedure simplecursor3()
begin
    declare done boolean default 0; -- 定义一个循环标记默认值为false
    declare tmp int; -- 定义局部变量
    declare youbiao3 cursor for select name from user; -- 定义游标
    -- 当出现02000错误时把局部变量的值设为true
    declare continue handler for sqlstate '02000' set done 1; 
    
    open youbiao3;

    REPEAT
        fetch youbiao3 into tmp;
    until done end REPEAT;    -- 当done为true时结束repeat，
    
    close youbiao3;
end;
```

# MySQL安全管理

MySQL服务器的安全基础是：用户应该对他们需要的数据具有适当的访问权，既不能多也不能少。

## 管理用户

- 查看所有用户: 
    ```sql
    USE MYSQL;
    SELECT USER FROM USER;
    ```
- 创建用户
    ```sql
    CREATE USER 用户名 IDENTIFIED BY '密码';
    CREATE USER yaro IDENTIFIED BY 'password';
    # 新用户创建后是不能登陆的，因为没有设置权限

    # 使用如下命令可以查看创建的新用户
    SELECT HOST,USER FROM user;
    ```
- 删除/重命名用户
    ```sql
    # 删除用户
    DROP USER yaro_db;

    # 重命名用户名
    RENAME USER yaro_db TO yaro;
    ```
- 更改密码
    ```sql
    # 修改当前用户密码（PASSWORD函数加密）
    SET PASSWORD = PASSWORD('新密码')；
    # 修改指定用户密码
    SET PASSWORD FOR yaro = PASSWORD('新密码')；

    # 使用如下命令可以看到密码是加密保存的
    SELECT USER,PASSWORD FROM user;
    ```

## 设置访问权限

### 权限概述

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

### 查看权限

```sql
SHOW GRANTS FOR benku
# 结果
# GRANT USAGE ON *.* TO 'benku'@'%'表示任何权限
```

### 赋予权限

```sql
GRANT ALL PRIVILEGES ON 层级 TO 用户名@主机 IDENTIFIED BY 密码;

# 如：授予yaro用户全局级(*.* 第一个星号代表数据库，第二个星号代表表)全部权限
GRANT ALL PRIVILEGES ON *.* TO 'yaro'@'%' IDENTIFIED BY 'password';

# 如：授权yaro用户针对于yaro_db数据库的全部权限；
GRANT ALL PRIVILEGES ON yaro_db.* TO 'yaro'@'%' IDENTIFIED BY 'password';
```

### 删除权限REVOKE

```sql
REVOKE ALL PRIVILEGES FROM 用户名;

# 如：撤销yaro用户的全部权限
REVOKE ALL PRIVILEGES FROM yaro;
```

### mysql链接认证

<img src="https://i.loli.net/2017/07/19/596edc06995b5.png">

>注意,`%`不包含`localhost`;

一般我们都是创建一个数据库,给它他个特定的用户管理,root用户权限太大;而且root用户默认不能远程登陆(只能本机连接),需要授权`GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';`;但是不安全;
如:

```sql
CREATE DATABASE yaro_db;
CREATE USER yaro IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON yaro_db.* TO 'yaro'@'%' IDENTIFIED BY 'password';
```

# mysql简单的备份恢复

## 备份

mysql使用最为广泛的备份工具是mysql自带的`mysqldump`linux命令;

```sh
# 备份一个指定的数据库
mysqldump -u root -p 数据库名称 > 备份文件.sql
# 如:
mysqldump -u root -p yaro_db > yaro_db.sql

# mysqldump备份出来的是纯文本的SQL文件,可以修改后为其他数据库使用
```

## 恢复

```sh
msyql -u root -p 数据库名称 < 备份文件.sql
# 如:
mysql -u root -p yaro_db < yaro_db.sql
```

# 设置mysql数据库编码

数据库使用一个特定编码保存数据,如latin Big5 GB2312 UTF8 等,不同语言一般使用不同编码保存。

编码主要赢下一下两个方面：

1.数据库保存相同内容占用的空间大小。
2.数据库与客户端通信（两端编码不同会乱码）。

- 查看mysql支持的编码种类: `SHOW CHARACTER SET;`

- 查询mysql当前使用的编码: 
    - `SHOW VARIABLES LIKE 'character_set%';`和
    - `SHOW VARIABLES LIKE 'collation%';`

- 创建数据库时指定其编码
    ```sql
    CREATE DATABASE yaro_db 
        DEFAULT CHARACTER SET utf8
        DEFAULT COLLATE utf8_general_ci;
    ```

- 创建后也可修改其编码:
    ```sql
    ALTER DATABASE yaro_db CHARACTER SET utf8 COLLATE utf8_general_ci;
    # 但是如果原数据库有内容,修改编码可能导致原数据异常显示;
    ```

- 通过修改配置文件`my.conf`设置mysql的默认编码
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
    > 修改之后重启mysql服务,通过`SHOW VARIABLES LIKE 'character_set%';`查看默认编码是否修改成功;

# 数据库设计

## 关系数据库设计步骤

### 需求分析

尽可能地收集需求，以及定义你的数据库的最终目的。 比如要开发书店查询应用，就要先知道应用有什么需求，

如: 如何添加书籍，如何查询现有书籍，如何查询订单，生成的报告格式如何，等等。

在这个阶段的分析中，在纸上画出输入表单，以及查询和报告的草图，通常会有不少帮助。

### 收集数据，组织表并设定主键

一旦需求明确，接下来就要确定有哪些数据需要存储到数据库中。通常我们都是将数据基于分类存储到不同的表中。
比如设计一个书店的数据库，就需要对书本，作者，出版社，顾客，订单等分类进行分表;而对每个表，
则要定义好需要哪些列（记录），以书本为例，需要有标题，作者，出版社，出版日期，ISBN，价格等信息。
对于每一个表，我们需要选择一列（或者多列）作为主键（primary key）。

### 建立关系

在关系数据库中包含独立且不相关的表格通常没有太大意义，如果真是这种情况你可以考虑使用NoSQL或者电子表格来存储这些内容。

关系数据库的魅力所在就是“关系”二字，甚至可以说设计关系数据库的成败所在就是明确各个表之间的关系。表间关系的类型有如下三种：

- 一对多(one-to-many): `母亲-孩子`
    ```sql
    CREATE TABLE `Mothers` ( 
        `MotherID` INTEGER NOT NULL AUTO_INCREMENT,
        `Name` VARCHAR(100) NOT NULL,
        `Age`  SMALLINT NOT NULL,
        `BloodType` VARCHAR(2) NOT NULL,
        PRIMARY KEY (`MotherID`)
    );
    CREATE TABLE `Children` ( 
        `ChildrenID` INTEGER NOT NULL AUTO_INCREMENT,
        `MotherID` INTEGER NOT NULL,
        `Name` VARCHAR(100) NOT NULL,
        `Age`  SMALLINT NOT NULL,
        `Sex` VARCHAR(50) NOT NULL,
        `BloodType` VARCHAR(2) NOT NULL,
        PRIMARY KEY (`ChildrenID`),
        FOREIGN KEY (`MotherID`) REFERENCES `Mothers` (`MotherID`)
    );
    ```
- 多对多(many-to-many): `订单-产品`
    ```sql
    CREATE TABLE `Orders` (
        `OrderID` INTEGER NOT NULL AUTO_INCREMENT,
        `OrderDate` DATETIME DEFAULT CURRENT_TIMESTAMP,
        `CustomerID` INTEGER NOT NULL,
        PRIMARY KEY (`OrderID`)
    );

    CREATE TABLE `Products` (
        `ProductID` INTEGER NOT NULL AUTO_INCREMENT, 
        `Name` VARCHAR(100) NOT NULL,
        `Stock` INTEGER DEFAULT 0,
        PRIMARY KEY (`ProductID`)
    );

    CREATE TABLE `OrderDetails` ( #关系表
        `OrderID` INTEGER NOT NULL,
        `ProductID` INTEGER NOT NULL, 
        FOREIGN KEY (`OrderID`) REFERENCES `Orders` (`OrderID`),
        FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`),
        PRIMARY KEY (`OrderID`,`ProductID`) #联合主键
    );
    ```
- 一对一(one-to-one): `产品基本信息 - 产品其他信息`(除了产品名称等基本信息外，还需要保存图片等富文本详情信息),分表!
    ```sql
    CREATE TABLE `Products` (
        `ProductID` INTEGER NOT NULL AUTO_INCREMENT,
        `Name` VARCHAR(50) NOT NULL,
        PRIMARY KEY (`ProductID`)
    );
    CREATE TABLE `ProductDetails` (
        `ProductID` INTEGER NOT NULL AUTO_INCREMENT,
        `DetailInfo` VARCHAR(65535),
        FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`), #共享主键
        PRIMARY KEY (`ProductID`)
    );
    ```

### 精炼及规格化

当设计好一个数据库或者拿到已有的数据库时，我们可能会想要：

- 增加更多的列
- 为某个表中的可选数据创建一个新表并建立一对一关系
- 将一个大表分裂为两个小表
- 在进行这些操作时，下列的规则就可以作为参考;
- 根据用户需求做其他更改;

## 数据库设计三范式

数据库设计三范式: 设计数据库`表`的时候所依据的规范(只是建议,不一定要遵循),共三个规范:

### 第一范式: 

要求**有主键**,并且要求每个**字段原子性**不可再分;

![第一范式.png](https://i.loli.net/2019/03/25/5c98cb48b34b1.png)

- 主键不重复 -> 各行都不重复;
- 主键采用数值型或定长字符串(索引快);
- 如联系方式,应该拆分为: email/电话/...

### 第二范式(满足第一范式前提上): 

要求所有非主键字段完全依赖主键,**不能产生部分依赖**;

![第二范式.png](https://i.loli.net/2019/03/25/5c98cb48db5cb.png)

- 基本上是说: `不要使用联合主键`,因为两个字段联合起来做主键,会造成其他字段只依赖联合主键的一部分
- `一张表内`有`多对多`关系(学生 - 老师),如果使用`学生id`和`老师id`作为联合主键,老师姓名便部分依赖此联合主键;
- 不符合第二范式的表很容易产生数据冗余(各字段有很多重复记录),浪费空间;
- 有些不符合第二范式的表虽然数据冗余,但是查询更简单(不需要联合查询),具体要不要满足第二范式以客户需求为目的;

### 第三范式(满足第二范式前提上): 

所有非主键字段与主键字段之间**不能产生传递依赖**;

![第三范式.png](https://i.loli.net/2019/03/25/5c98cb48e0b34.png)

- `一张表内`有`一对多`关系(班级 - 学生) ,如果使用`学生id作为主键`;
- 则会导致`班级名`依赖`班级id`,`班级id`依赖`学生id`,即,传递依赖;

### 几个比较经典的设计:

- 一对一:
    - 第一种方案: 分两张表存储,共享主键;
        ```
        t_husband
        h_no(pk)  h_name
        --------------------
        1          张三
        2          李四
        3          王五

        t_wife
        W_no(pk)   w_name    [w_no 同时也也是 fk, 引用t_husband.h_no]
        --------------------
        3          王五的老婆
        2          李四的老婆
        1          张三的老婆
        ```
    - 第二种方案:  分两张表存储,外键唯一(有外键说明是一对多, `多`添加唯一性约束便是一对一);
        ```
        t_husband
        h_no(pk)   h_name  wife_no(fk-unique)
        ---------------------------
        1          张三     100
        2          李四     200
        3          王五     300

        t_wife
        W_no(pk)     w_name
        -----------------------------
        100          张三的老婆
        200          李四的老婆
        300          王五的老婆
        ```
- 一对多:分两张表存储,在`多`的一方添加外键,这个外键字段引用`一`的主键字段;
- 多对多:分三张表存储,在`学生表`中存储`学生信息`,在`课程表`中存储`课程信息`,在`学生选课表`中存储`学生和课程的关系信息`;

### 实际开发中是怎样的?

- 在实际开发中,数据库设计尽量遵循三范式;
- 但是还是要根据实际情况进行取舍;
- 有事可能会拿冗余换速度;
- 最终以满足客户需求为目的;

## 其他设计规范

参考"MySQL推荐使用规范.md"文件