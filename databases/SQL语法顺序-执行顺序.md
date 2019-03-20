# SQL 的语法并不按照语法顺序执行

SQL 语句有一个让大部分人都感到困惑的特性，就是：SQL 语句的执行顺序跟其语句的语法顺序并不一致。

## SQL 语句的语法顺序是：

- SELECT[DISTINCT]
- FROM
- WHERE
- GROUP BY
- HAVING
- UNION
- ORDER BY

为了方便理解，上面并没有把所有的 SQL 语法结构都列出来，但是已经足以说明 SQL 语句的语法顺序和其执行顺序完全不一样，

## SQL 语句的执行顺序是：

就以上述语句为例，其执行顺序为：

- FROM
- WHERE
- GROUP BY
- HAVING
- SELECT
- DISTINCT
- UNION
- ORDER BY

关于 SQL 语句的执行顺序，有三个值得我们注意的地方：

1. FROM 才是 SQL 语句执行的第一步，并非 SELECT 。数据库在执行 SQL 语句的第一步是将数据从硬盘加载到数据缓冲区中，以便对这些数据进行操作。（译者注：原文为“The first thing that happens is loading data from the disk into memory, in order to operate on such data.”，但是并非如此，以 Oracle 等常用数据库为例，数据是从硬盘中抽取到数据缓冲区中进行操作。）
2. SELECT 是在大部分语句执行了之后才执行的，严格的说是在 FROM 和 GROUP BY 之后执行的。理解这一点是非常重要的，这就是你不能在 WHERE 中使用在 SELECT 中设定别名的字段作为判断条件的原因。
3. 无论在语法上还是在执行顺序上， UNION 总是排在在 ORDER BY 之前。很多人认为每个 UNION 段都能使用 ORDER BY 排序，但是根据 SQL 语言标准和各个数据库 SQL 的执行差异来看，这并不是真的。尽管某些数据库允许 SQL 语句对子查询（subqueries）或者派生表（derived tables）进行排序，但是这并不说明这个排序在 UNION 操作过后仍保持排序后的顺序。

> 注意：并非所有的数据库对 SQL 语句使用相同的解析方式。如 MySQL、PostgreSQL和 SQLite 中就不会按照上面第二点中所说的方式执行。

## 我们学到了什么？

既然并不是所有的数据库都按照上述方式执行 SQL 预计，那我们的收获是什么？我们的收获是永远要记得： SQL 语句的语法顺序和其执行顺序并不一致，这样我们就能避免一般性的错误。如果你能记住 SQL 语句语法顺序和执行顺序的差异，你就能很容易的理解一些很常见的 SQL 问题。
