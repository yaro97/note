---
title: Cmder的使用说明
date: 2016-12-01 00:07:28
tags:
- Cmder教程
---
## 安装

Cmder是开箱即用的。所以解压，然后双击即可

## 配置

**添加到系统变量**

windows10可直接使用小娜搜索`环境变量`，然后将Cmder.exe`所在目录`加入Path项即可。之后通过`win+r`输入`cmder`即可启动

**添加到右键菜单**

在管理员权限的命令窗口下（可 win+x 选择 命令提示符管理员 打开）输入：

```
Cmder.exe /REGISTER ALL
```

<!-- more -->

## 问题处理

**避免中文字体重叠**

`win+alt+p` 唤出设置界面 > mian > font > monospce,去掉那勾勾即可。

![](https://box.kancloud.cn/68d613a419074a1dd42c8b017eba18ec_760x487.png)

**避免中文乱码**

小于v1.3.0版本,编辑config/aliases.cmd文件，在末尾添加

```        
l=ls --show-control-chars 
la=ls -aF --show-control-chars 
ll=ls -alF --show-control-chars
ls=ls --show-control-chars -F
```

注:貌似最新版已经加上这个代码了,而且没有`aliases.cmd`文件了   

**如果仍有乱码，可尝试 设置界面>Startup>Environment; 添加 `set LANG=zh_CN.UTF-8`设置默认语言**

![](https://box.kancloud.cn/c09e82c54db128ed77910bc8c958a5f3_756x465.png)

**修改命令提示符号`λ`为`$`**

Cmder预设的命列列提示符号是λ;如果用着不习惯，可以将这个字元改成Mac / Linux环境下常见的$符号，具体操作如下：

大于v1.3.0版本编辑Cmder安装目录下的`vendor\clink.lua` 41行：

```
cmder_prompt = "\x1b[1;32;40m{cwd} {git}{hg} \n\x1b[1;30;40m{lamb} \x1b[0m"
```

修改成以下即可：

```
cmder_prompt = "\x1b[1;32;40m{cwd} {git}{hg} \n\x1b[1;30;40m$ \x1b[0m"
```
    
## 其他配置

- 在文件`D:\tools\cmder\config\user-aliases.cmd`中添加`ll=ls -l`,可以实现`ll`命令
- 先将`sublime_text`所在目录加入环境变量,然后在`D:\tools\cmder\config\user-aliases.cmd`中添加`subl=sublime_text $*`可以实现在`cmder`中通过`subl`调用sublime编辑文本.