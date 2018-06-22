# random模块

## 1. 常用实例

ranodm模块有以下常用实例：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yaro

import random

# 返回0-1的浮点数
print(random.random())

# 返回1-3的浮点数
print(random.uniform(1, 3))

# 返回1-3的整数(包含1和3)
print(random.randint(1, 3))

# 返回1-3的整数（不包含3），可以制定step
print(random.randrange(1, 3))

# 返回序列中的一个随机值
print(random.choice([1, 3]))

# 返回序列中的3个随机元素组成的序列
print(random.sample([1, 2, 3, 4], 3))

# 类似于扑克牌的洗牌（修改原列表）
items = [1, 2, 3, 4]
random.shuffle(items)
print(items)


# 应用举例：随机生成5位验证码
def v_code():
    """验证码生成函数"""
    result = ''
    for i in range(5):
        num = random.randint(0, 9)
        alphabet = chr(random.randint(65, 122))
        s = str(random.choice([num, alphabet]))
        result += s
    return result


verify_code = v_code()
print(verify_code)
```

## 2. 其他高级用法

random模块还可以有更高级的用法：

choices可以指定权重；

真值分布：三角形分布随机数、Beta分布、指数分布、gamma分布、高斯分布、对数正态分布等等，

详情请参考：https://www.cnblogs.com/feixuelove1009/p/6863153.html