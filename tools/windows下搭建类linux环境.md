---
title: windows下搭建类linux环境
date: 2017-01-07 15:02:47
tags:
- Linux环境
- babun
- conEmu
- cmder
---
Windows下有很多工具可以实现类linux环境，我采用的是conEmu+babun来实现。

## 一.简介

conEmu 是window下的多标签命令行工具，可以方便的新建cmd、cmd admin、powershell、powershell admin多种命令行，设置很多，功能强大。
babun 如果你不想折腾，又想在windows下有像linux一样的命令行，那就试试这个吧，比cygwin、git bash、cmder 方便。
更详细的说明自己去这两个软件的官网看吧。

## 二.下载

babun : http://babun.github.io/
conEmu : https://code.google.com/p/conemu-maximus5/

## 三.安装

conEmu 安装不多说了，一路next
babun 安装
下载好babun后解压，执行： babun.bat /t c:\cmd , 安装过程中注意一下有没有错误，如果是删掉后重新安装的，经常会遇一堆error,一般重启一下电脑就可以，安装好之后会在c:\cmd下生成一个.babun的目录，babun所有文件都在这个目录中。
注意安装目录不要有空格，这个是cygwin要求的。

## 四.一些配置

### 1.windows cmd内置命令显示中文

在babun自带的shell(mintty)右上角右键--options-text,在character set 选择default或者GBK。
之后执行ipconfig等cmd内置的命令时就正常显示中文了。

### 2.去掉命令提示符乱码

babun内置两个shell，默认是zsh,另一个是bash,设置成中文后命令提示符最后会有一个乱码字符，看着很不爽，要修改PS1变量去掉。把乱码字符替换为：`>>`

bash：

```
vi /usr/local/etc/babun.bash   
PS1="\[\033[00;34m\]{ \[\033[01;34m\]\W \[\033[00;34m\]}\[\033[01;32m\] \$( git rev-parse --abbrev-ref HEAD 2> /dev/null || echo "" ) \[\033[01;31m\]>>\[\033[00m\]"
```

<!-- more -->

zsh :

```
vi .oh-my-zsh/custom/babun.zsh-theme
PROMPT='%{$fg[blue]%}{ %c } \
%{$fg[green]%}$(  git rev-parse --abbrev-ref HEAD 2> /dev/null || echo ""  )%{$reset_color%} \
%{$fg[red]%}%(!.#.>>)%{$reset_color%} '
```

这样改好后命令提示符就变成：` { ~ } >>`

### 3. 整合conEmu

在conEmu窗口右上角右键--settings--startup--tasks,点“+”号添加一个新task，task parameters留空，也按照babun官网介绍中配置图标等信息，在下面的commands中加入：
`C:\CMD.babun\cygwin\bin\mintty.exe -t C:\CMD.babun\cygwin\etc\minttyrc`

### 4. 常用软件安装

```bash
pact install tmux        #安装tmux
pact install screen      #安装screen 有了这两个不用conEmu也可以了
pact install zip         #安装zip
pact install subversion  #安装svn相关的命令
pact install lftp        #lftp命令
pact install p7zip       # p7zip命令
pact install connect-proxy # 基于openssh的socks https代理
pact install util-linux    #安装linux基础命令行工具 more/col/whereis等等命令
pact install bind-utils    #安装dig命令
pact install inetutils     #安装Telnet等常用网络命令
pact install python        #python环境
pact install python-crypto #python 环境
```

这个包管理很方便，用法也简单，按照自己需要安装吧

## 五.一些不足

设置好window cmd显示中文后，还是有部分中文不正常显示
例如 ：ls -al /cygdrive/c/Users/will.w/Desktop/ 之后tab补全会正常显示中文，但是敲回车执行后中文文件名会显示乱码。看了一下应该是环境变量的问题

粘贴不能用
从windows复制内容后，在conEmu下无法粘贴

目前就是这两点让我不爽，还在想办法解决，不过就功能而言，完爆windows下其它类linux环境，当然我平时还是用虚拟机多一些。。。。