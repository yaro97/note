# configpaser模块

`ConfigParser` 可以用来读取配置文件。是一个内置模块，不需要独立安装

来看一个好多软件的常见配置文档格式如下：

> 相关操作特别类似于python的Dict操作。

 ```ini
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
 ```

如果想用python生成一个这样的文档怎么做呢？

## 生成配置文件

 ```python
import configparser
  
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

# 对文件进行修改时，别忘了写入文件
with open('example.ini', 'w') as configfile:
   config.write(configfile)
 ```

## 增删改查

```python
import configparser

config = configparser.ConfigParser()
#-------查
print(config.sections())   #[] ，还没有和配置文件关联
config.read('example.ini')  # 关联配置文件
print(config.sections())   #['bitbucket.org', 'topsecret.server.com']， DEFAULT默认不显示。
print('bytebong.com' in config) # False
print(config['bitbucket.org']['User']) # hg
print(config['DEFAULT']['Compression']) #yes
print(config['topsecret.server.com']['ForwardX11'])  #no

for key in config['bitbucket.org']:
    print(key) 
# 类似字典的打印，只打印字典的key，但是DEFAULT会显示，如下：
# user
# serveraliveinterval
# compression
# compressionlevel
# forwardx11

print(config.options('bitbucket.org'))#['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
# options类似于python的dict的key。

print(config.items('bitbucket.org'))  #[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]
# 类似于Python的dict的items

print(config.get('bitbucket.org','compression')) #yes
# 类似于Python中dict的get方法，列中两个参数表示字典的嵌套

#------删,改,增(config.write(open('i.cfg', "w")))

config.add_section('yuan')  
config.remove_section('topsecret.server.com')
config.remove_option('bitbucket.org','user') # 添加python-dict的key
config.set('bitbucket.org','k1','11111')

# 修改配置文件记得写入
config.write(open('i.cfg', "w"))
```



 

 

 