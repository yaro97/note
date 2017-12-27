---
title: Ubuntu安装及调试记录
date: 2016-11-20 09:08:16
tags:
- Ubuntu安装
- Ubuntu快捷键
- Shandowsocks配置
---
老婆的笔记本有两个显卡,安装win10的时候总是自动更新显卡;但是同时安装两个显卡,重启之后立马黑屏,蛋好疼…没办法,只能试试linux系统了,网上参考了下,Ubuntu算是比较容易入门的了,于是乎就折腾了好几天.现在用着感觉还不错的说,嘿嘿^_^..本文主要是个人操作过程的记录,其中对于新手来说还是有很多坑的,亲们可以参考下.

## 安装Ubuntu

Ubuntu[官网下载](http://cn.ubuntu.com/download/)镜像文件，可直接拖动链接到迅雷下载；

制作启动U盘：一定使用要**使用最新版**的**[UltraISO 软碟通](http://cn.ezbsystems.com/ultraiso/)**,否则可能出现错误，原因参考[U盘刻录无法启动原因](http://www.ubuntukylin.com/news/shownews.php?lang=cn&id=362)；

设置电脑BIOS（F2进入）通过U盘启动，倘若无法启动，可尝试开启UEFI；

通过U盘安装Ubuntu.

## 分区

总的来说,linux的分区可以分为`系统分区`和`数据分区` ,`系统分区`包括`/`和`swap`, `数据分区`包括`/home`和`其他数据`

分区建议:  
根分区/（系统主要文件）大小建议50G，`swap`交换分区大小参考物理内存,数据`/home`分区500G，剩下空间分两个区不挂载

我的实际分区情况：`/`40G，`swap`4g，`其他`全部给`home`分区。

<!-- more -->

## 配置及安装软件

### 解决桌面闪屏问题

倘若鼠标不间断闪动，鼠标可以移动到桌面右边界之外，可如下解决：`设置`=>`显示`=>`关闭unkwon display`即可。

### ubuntu安装软件的常见方式

软件安装参考[这个网页](http://www.cnblogs.com/dubaokun/p/3558848.html).

**直接通过`apt-get`安装**

有些软件都是包含在相应的库中,通过添加库,便可以直接安装.这种方法安装的程序版本可能不是最新版(比如`node.js`).

**下载`.deb`安装包手动安装**

通过手动或`wget`等命令下载安装包,调用`dpkg -i package`安装

**直接下载二进制文件解压即可用**

- 下载二进制文件(Binaries)
- 下载后将安装包移动到要安装到的文件夹下，根据个人喜好设置即可,这里我放在了`/home/kun/mysofltware/ `下面
- 解压到当前文件夹下运行 
- 进入 解压后的目录bin目录下，执行ls会看到两个文件`node`,`npm`. 然后执行`./node -v `，如果显示出 版本号说明我们下载的程序包是没有问题的(这里以`node.js`的安装为例)  
- 添加到PATH实现任意目录访问  

	> 因为 `/home/kun/mysofltware/node-v0.10.26-linux-x64/bin`这个目录是不在环境变量中的，所以只能到该目录下才能node的程序。如果在其他的目录下执行node命令的话 ，必须通过绝对路径访问才可以的.  

	> 如果要在任意目录可以访问的话，需要将node 所在的目录，添加`PATH环境变量`里面，或者通过软连接的形式将`node`和`npm`链接到系统默认的`PATH目录`下的一个，以下分别介绍:  

	- 软连接方式  
		在终端执行`echo $PATH`可以获取`PATH变量`包含的内容，系统默认的`PATH环境变量`包括`/usr/local/bin`:`/usr/bin`:`/bin`:`/usr/local/sbin`:`/usr/sbin`:`/sbin`:，冒号为分隔符。所以我们可以将`node`和`npm`链接到`/usr/local/bin `目录执行如下命令  

		```bash
		ln -s /home/kun/mysofltware/node-v0.10.26-linux-x64/bin/node /usr/local/bin/node
		ln -s /home/kun/mysofltware/node-v0.10.26-linux-x64/bin/npm /usr/local/bin/npm
		```

		通过如此，就可以访问Node了，同时node部署也已经完毕。

	- 环境变量配置  
		在node目录下执行pwd 获取node所在的目录，要把这个目录添加到PATH环境变量
		执行su 输入密码切换到root用户。通过命令打开`vi /etc/profile`profile文件,添加如下代码:

		```bash
		PATH=$PATH:/home/kun/mysofltware/node-v0.10.26-linux-x64/bin
		```

		执行命令`source/etc/profile`可以使变量生效，然后执行`echo $PATH`，看看输出内容是否包含自己添加的内容
		然后到任意目录下去执行一次执行`node -v`,`npm -v`,尝试是否OK? 

**下载源码,手动编译二进制**

- 安装编译环境,安装依赖
- 进入`cd`源码路径,执行里面的`configure文件`,即`./configure --prefix=/`生成二进制文件路径.  

	> **命令解释:**`--prefix=/`用于指定安装路径,  
	若不指定prefix，则可执行文件默认放在`/usr /local/bin`，库文件默认放在`/usr/local/lib`，配置文件默认放在`/usr/local/etc`,其它的资源文件放在`/usr /local/share`。你要卸载这个程序，要么在原来的make目录下用一次`make uninstall`（前提是make文件指定过uninstall）,要么去上述目录里面把相关的文件一个个手工删掉。
	若指定prefix，直接删掉一个文件夹就够了。  

- 运行`make`命令，这个是编译过程，运行的时间可能稍长一些
- 执行`install`命令。如果在第第一步骤中配置的程序安装路径不在系统的环境量PATH中，需要自己添加（下面会介绍在centos下修改环境变量）
- 关于源码的编译也可以参考[这篇博客](http://blog.csdn.net/zhaoweitco/article/details/12677089).

### 安装chrome

直接访问[官网](https://www.google.com/chrome/browser/desktop/index.html)下载Linux`.deb`安装包安装即可.

也可先尝试运行如下代码：

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

注意：若重启电脑后，chrome等软件提示：`账号登录信息已过期，需重新登录`，这是ubuntu的`密钥环`导致的；`bash`启动`密码和秘钥`，在`密码-登录`右键-`修改密码`，新密码置空即可。

### 安装SS

在未FQ之前,通过百度很难找到SS的教程,这时可以利用`简书`或`必应`搜索

#### SS-qt5(GUI)

建议不使用GUI版本,安装命令行工具即可,见下一节.

- 安装

	```bash
	sudo add-apt-repository ppa:hzwhuang/ss-qt5  #加入源
	sudo apt-get update #更新源
	sudo apt-get install shadowsocks-qt5 #安装SS
	```

- 参数设置

	```json   
	{
	"server":"",
	"server_port":443,
	"local_address": "127.0.0.1",
	"local_port":1080,
	"password":"",
	"timeout":600,
	"method":"aes-256-cfb"
	}
	```

	可以访问搬瓦工[国内镜像](http://banwagong.cn/)查看最新SS相关配置参数。另外,服务器端重新安装系统难道SS会更快?有待证实.

- 全局代理设置

	`System Setting > Network > Network proxy > Method > ManualSocket Host 127.0.0.1 1080`。 备注：这样chrome就可以FQ了，但是firefox还需要进一步设置（此处略）。

- PAC代理

	安装`genpac`

	```bash
	sudo pip install genpac
	```

	倘若提示没有`pip`命令，可以尝试输入`pip --help`，其他命令遇到类似情况同理。

	生成autoproxy.pac文件

	```bash
	genpac -p "SOCKS5 127.0.0.1:1080" --gfwlist-proxy="SOCKS5 127.0.0.1:1080" --gfwlist-url=https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt --output="autoproxy.pac"
	```

	更改系统代理设置 `System settings > Network > Network ProxyMethod > AutomaticConfiguration URL 是 autoproxy.pac文件的路径，设置为/home/yaro/autoproxy.pac`

#### SS或者SS-libev

执行以下命令安装

```bash
sudo apt install shadowsocks
```

上述命令会同时安装`sslocal`和`ssserver`两个程序,客户端用前者,服务器用后者.

可以用`whereis`(查找程序命令)查找`sslocal`位置

```bash
whereis sslocal
#默认返回如下:
sslocal: /usr/local/bin/sslocal
```

创建配置文件

```bash
sudo vim /home/yaro/Documents/shadowsocks/shadowsocks.json   ##创建.json文件,任意目录,内容如下:
```

```json
{ 
"server":"", 
"server_port":443, 
"local_address": "127.0.0.1", 
"local_port":1080,
"password":"", 
"timeout":600, "
method":"aes-256-cfb" 
}
```

启动客户端

```bash
sslocal -c  /home/yaro/Documents/shadowsocks/shadowsocks.json #在终端运行,不能停止不能关闭
sudo sslocal -c /home/yaro/Documents/shadowsocks/shadowsocks.json -d start #后台运行
#其他参数可以`sslocal --help`.
```

开机启动

> 早期的ubuntu版本可以通过写入`rc.local`的方式实现开机运行代码.
> 
> ```bash
> sudo sslocal -c /home/yaro/Documents/shadowsocks/shadowsocks.json -d start
> ```

ubuntu15.04后,`rc.local`无效,开始使用systemd管理开机启动,可通过写入服务的方式实现开机运行:

注:`sslocal`初始位置为`/usr/local/bin/sslocal`.

创建服务文件

```bash
sudo vim /lib/systemd/system/sslocal@myserver.service
```

内容如下:

```bash
[Unit]
Description=Shadowsocks Client Start
After=network.target

[Service]
Type=simple
User=yaro
ExecStart=/usr/local/bin/sslocal -c /home/yaro/Documents/shadowsocks/shadowsocks.json

[Install]
WantedBy=multi-user.target
```

**注意:**地址记得用绝对地址,不要用`~/`地址.

将这个文件软连接到`/etc/systemd/system/multi-user.target.wants/`

```bash
sudo ln -s /lib/systemd/system/sslocal@myserver.service /etc/systemd/system/multi-user.target.wants/sslocal@myserver.service
```

查看软连接文件权限(需要可执行):

```bash
ls -l /etc/systemd/system/multi-user.target.wants/sslocal@myserver.service
```

重启电脑,OK! 访问google,或通过如下命令查看服务运行状态(查找问题)

```bash
sudo systemctl status sslocal@myserver.service
```

局部代理/全局代理设置同上.

[参考1](https://www.linuxbabe.com/desktop-linux/how-to-install-and-use-shadowsocks-command-line-client)-ubuntu安装SS 

[参考2](http://www.linuxidc.com/Linux/2016-04/129727.htm)-Ubuntu systemd添加开机启动

#### proxychains

proxychains支持http/https/socks4/socks5代理方式之间的切换.

安装

```bash
sudo apt install proxychains
```

配置

```bash
sudo vi /etc/proxychains.conf
#将socks4 127.0.0.1 9095改为socks5  127.0.0.1 1080
```

使用

```bash
wget google.com   #直接连google
proxychains wget google.com #通过sock5代理链接google
sudo proxychains wget google.com #注意proxy要紧挨这功能命令
sudo proxychains apt install typora #前提要能访问typora的资源站(先FQ)
```

其他说明

proxychains配置文件中可以设置三种代理方式:动态代理(依次选择设定的代理方式,有一个可用即可),严格代理(依次选择,但是必须都能用),随机代理(随机选择设定的代理方式)

类似软件:proxychains是只适用于linux/iOS系统,类似的还有polipo(让所有的程序全部走socks5代理),windows平台可以考虑Proxifier.

### 卸载不常用软件

卸载libreoffice

```bash
sudo apt-get purge libreoffice-common
```

删除amazon链接

```bash
sudo apt purge unity-webapps-common
```

删除不用的软件

```bash
sudo apt-get purge thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines cheese transmission-common gnome-orca webbrowser-app gnome-sudoku  landscape-client-ui-install onboard deja-dup
#上述软件以此是:邮件客户端 多媒体播放 音乐mp3播放 IM通讯 刻录光盘 扫描软件 麻将(gnome-mahjongg) 纸牌(aisleriot) 扫雷(gnome-mines) 象棋 bt下载软件 屏幕阅读器(gnome-orca) 自带浏览器 数字游戏 远程桌面 虚拟键盘(onboard) 备份软件
```

### 安装常用软件

**常用软件:**sogou输入法/typora(可以用sublime插件实现MD)/坚果云/网易云音乐/sublime，以及源自带的vim(记得安装`vim-gnome`)/goldendict,终端工具zsh/oh-my-zsh([参考官网](https://github.com/robbyrussell/oh-my-zsh)).

**安装方法**

- 源自带的软件 `sudo apt-get install filename` 若是不知道软件名称，可以如下查看 `sudo dpkg -l *filename*`（`*`)为通配符

- 第三方软件 下载`.deb`格式安装包，如下安装 `sudo dpkg -i filename`

备注1:Goldendict的配置及字典可以[参考网站](https://blog.yuanbin.me/posts/2013/01/goldendictxia-san-da-you-zhi-ci-ku-shi-yong-xiao-ji.html)  
备注2:sublime无法输入中文可以[参考网站1](https://github.com/lyfeyaj/sublime-text-imfix)和[参考网站2](http://www.jianshu.com/p/bf05fb3a4709)  
备注3:sublime字体设置,打开`sublime`的`Preference-setting`在其中加入如下代码
`{font_face": "Droid Sans Fallback", "font_size": 14}`   
备注4:查看中文字体名称可以输入`fc-list :lang=zh-cn`,`fc-list`(查看所有字体)

### 设置开机启动常用项

需要开机启动的项目如搜狗输入法（依托于fcitx，启动fcitx）/SS/坚果云等

将相关程序复制到用户自定义的开机项即可,也可以参考SS章节中通过添加服务的方式实现开机启动.

```bash
sudo cp /usr/share/applications/fcitx.desktop ~/.config/autostart/fcitx.desktop
```

增加可执行权限

```bash
sudo chmod +x ~/.config/autostart/fctix.desktop
```

### 设置`~/`下文件名为英文

在安装是若选择中文安装，文件夹全部为中文，如`下载`/`音乐`等，这在终端中很不方便输入。

依次运行如下命令 

```bash
export LANG=en_US
xdg-user-dirs-gtk-update
export LANG=zh_CN
```

或者是通过设置-语言支持-设置英文，再重启/注销。

### 卸载系统内置软件

不需要的软件：firefox/libreoffic*/系统自带浏览器/邮件客户端/gedit等

倘若不清楚软件的名称,可以 `sudo dpkg -l libreoffice*`

或者,利用`tab`自动补全功能 `sudo apt purge libreoffice` 然后按`两次Tab`即可.

### 安装思源字体

思源字体可以[点击此处](https://github.com/adobe-fonts/source-han-sans/tree/release)下载

将`思源字体`安装包放入`~/.fonts`重启即可.双击安装的话会安装在系统文件夹.

话说系统自带的字体`Droid Sans Fallback`也挺好O(∩_∩)O哈哈~

## 其他问题

### Ubuntu出现了内部错误

```bash
sudo apt-get remove apport
```

### nautilus文件管理器打开“最近使用的”出错

在文件`/usr/lib/systemd/user/gvfs-daemon.service`中添加一行`Environment=DISPLAY=:0`即可

### Ubuntu root 和user切换

[参考网站1](http://www.cnblogs.com/weiweiqiao99/archive/2010/11/10/1873761.html)

**从user切换到root用户**

ubuntu默认登录user,可以用`sudo`临时授权使用root权限;此时可以使用`sudo su`切换到root用户

注意:默认的ubuntu的root用户没有固定密码,是动态随机变动的,直接使用`su`是不可以的,因为我们不知道root的密码.

**从root用户切回user用户**

使用`su yaro`即可,或输入`exit`,也可以`ctrl+D`快捷键.

**给root设定一个密码**

默认root用户无固定密码,且被锁定,可以通过`sudo passwd root`设定密码.

**禁用/启用root登录**

禁用:`sudo passwd -l root`(禁用而已,密码还在);

启用:`sudo passwd -u root` .

## Ubuntu 快捷键

注：在普通 PC 上，Super 键通常就是 Win 键， Numpad 表示数字小键盘。

**Launcher (启动器)**

`Super`（按住）- 调用启动器。`Super-1` 或 `2`或 `3`直至`0`\- 打开或聚焦到应用程序。`Super-T`\- 打开垃圾箱。`Alt-F1`\- 把键盘聚焦在启动器上.`Alt-F2`\- 以“特殊模式”调用托盘，用来运行命令。`Ctrl-Alt-T` \- 启动终端窗口。

**Dash (托盘）**

`Super`(敲击) - 敲击打开托盘。`Super-A`\- 打开应用程序托盘。`Super-F` \- 打开文件及文件夹托盘。

**Panel (面板）**

F10 - 打开面板上的第一个菜单。`Window Management` （窗口管理）`Super-?` \- 扩展模式，缩小所有窗口到所有工作区。`Super-D` -最小化所有窗口; 再次使用该快捷键的话恢复所有窗口。（不起作用时，可以尝试再按住`Ctrl` ）

**Window Placement （窗口放置）**

假如你反复点击某个组合键，Unity 会循环改变窗口宽度，例如 `Ctrl-Alt-numpad 5`:`Ctrl-Alt-Numpad 7` \- 放置窗口到屏幕左上角。`Ctrl-Alt-Numpad 8` \- 放置窗口到屏幕上半部分。`Ctrl-Alt-Numpad 9` \- 放置窗口到屏幕右上角。`Ctrl-Alt-Numpad 4` \- 放置窗口到屏幕左侧。`Ctrl-Alt-Numpad 5` \- 在屏幕中间位置居中/最大化窗口。`Ctrl-Alt-Numpad 6` \- 放置窗口到屏幕右侧。`Ctrl-Alt-Numpad 1` \- 放置窗口到屏幕左下角。`Ctrl-Alt-Numpad 2` \- 放置窗口到屏幕下半部分。`Ctrl-Alt-Numpad 3` \- 放置窗口到屏幕右下角。`Ctrl-Alt-Numpad 0` \- 最大化窗口。

**Workspace Management （工作区管理）**

`Super-W` \- 平铺模式列出所有窗口`Super-S` \- 浏览模式，缩小所有工作区，让你管理窗口。`Ctrl-Alt-← / → / ↑ / ↓` \- 切换工作区。`Ctrl-Alt-Shift-← / → / ↑ / ↓` \- 放置窗口到新工作区。

**Mouse Tricks （鼠标技巧）**

最大化 - `拖动`窗口到顶部面板就会最大化该窗口。  
最大化按钮上`中击` - 垂直最大化窗口。  
最大化按钮上`右击` - 水平最大化窗口。  
平铺 - `拖动`窗口到左边/右边边缘，会自动在屏幕的一边平铺窗口。  
恢复 - 在顶部面板会把最大化的窗口的标题栏往下`拖动`会自动还原到原始大小。  
在应用程序的启动器图标上`中击` - 如果之前已打开过此程序，此操作会为该程序再打开一个新的独立进程。  
在窗口标题栏上`中击`（不是菜单）- 把当前窗口放置到所有窗口的最后面。  

**Nautilus快捷键**

`CTRL + 1`: 图标视图  
`CTRL + 2`: 列表视图  
`CTRL + T`: 新建标签页  
`CTRL + W`: 关闭标签页  
`CTRL + D` 收藏到书签  
`CTRL + Q`: 退出  
`Win+E`: 显示所有的工作空间，可轻松进行切换  
`Win + Mousewheel`: 桌面上的缩放操作，使用滚轮鼠标操作更方便  

**Terminal终端快捷键**

`CTRL + ALT + T`: 打开终端  
`TAB`: 自动补全命令或文件名  
`CTRL + SHIFT + V`: 粘贴（Linux中不需要复制的动作，文本被选择就自动被复制）  
`CTRL + SHIFT + T`: 新建标签页  
`CTRL + D`: 关闭标签页  
`CTRL + L`: 清楚屏幕  
`CTRL + R` + 文本: 在输入历史中搜索  
`CTRL + A`: 移动到行首  
`CTRL + E`: 移动到行末  
`CTRL + C`: 终止当前任务  
`CTRL + Z`: 把当前任务放到后台运行（相当于运行命令时后面加&）  
`~`: 表示用户目录路径  