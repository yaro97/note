## Linux基础知识及系统管理

Tags: linux, 

[TOC]

### 系统简介

扫描、踩点网站：www.netcraft.com

使用场景：服务器， 嵌入式应用（安卓，智能家电，航空系统，银行系统，卡拉OK等等），娱乐行业后期处理。

学习重点：计划，坚持，专注，练习；而不是收藏。

Linux所有的设备（/dev/下的文件）必须挂在之后（习惯性挂载到/mnt/下）才能使用。

‘lost+found'目录：系统意外崩溃而产生的文件碎片放在这里，系统启动过程中fsck工具会检查这里，并修复已损坏的文件系统，这个目录只在每个分区中出现。

lib目录：系统调用的数据库保存位置。

opt目录：第三方安装的软件保存位置，不过我还是更习惯把软件放置到/usr/local/目录当中。

proc目录和sys目录：这两个是虚拟文件系统，一个保存的是cpu、内存、设备驱动等；另一个是保存内核相关信息的。

srv目录：启动服务后，保存所需的数据。；

tmp目录：临时文件目录，所有用户都可访问和写入，建议不要保存重要文件，也可以删除。

服务器注意事项：1、远程服务器不允许关机，只能重启；2、重启之前应该先关闭服务（数据读取可能导致软件/硬件出问题）；3、服务器访问高峰期不要运行高负载命令（扫描、、备份（压缩、复制）等）；4、防火墙不要把自己踢出服务器；5、合理的密码规范并定期更新；6、合理分配权限；定期备份重要数据和日志文件。

### Linux常用命令

####　1、文件处理命令

```sh
## 目录处理命令
ls  # -l 详细信息显示, -d # 查看当前目录属性,-i inode索引节点；
mkdir -p  # 根据需要创建parent目录；
cp -r -p  # 复制属性；
cat -n /etc/issue  # 显示行号；

## 文件处理命令
tac  # 反向显示cat的命令，哈哈；
more  # 帮助命令就是调用more命令；
less  # 更强大，可以来回查看，还可以用/进行搜索；
head -n 7   # 只查看前7行,默认是10行；
tail  # 和head相反，而且可以使用 -f 选项实时动态显示日志文件末尾增加的内容；

## 链接命令
ln  # 硬链接,类似于`cp -p（属性相同）` 且两个文件同步更新，i节点(`ls -i`)同源文件，特点：无法跨分区，无法针对于目录。
ln -s  # 软连接（类似win的快捷方式，权限取决于源文件）；
```

#### 2、权限相关命令

chmod  # 1、可以使用`,`同时修改u、g、o、a的权限；2、可以使用`+-=`；更常用的是数字格式，如：751。

> 只有文件的所有者和root可以更改文件的权限。

权限深入了解：

文件：r=查看文件内容（cat/more/head）；w=修改文件内容（vim）；x=执行(script,command)。

目录：r=可以列出目录的内容(ls)；w=可以在目录中创建、删除文件(touch/mkdir/rm/rmdir);x=可以进入目录（cd）。

chown 用户 文件/文件夹  # 更改文件的所有者（只有管理员可以更改）；

> 只有root才能修改所有者

chgrp 用户组 文件/文件夹  # 更改文件的所属组（只有管理员可以更改）；

umask -S  # 显示文件（夹）的缺省权限，但是linux中新创建的文件，会去掉x权限；

umask 023  # 默认权限修改为777-023=754（rwx r_x r__）

#### 3、搜索相关命令

find搜索命令：强大，但是占用资源。

> 尽量不要使用find，占用系统资源太严重。

语法： `find [搜索范围] [匹配条件]`

```sh
find /etc -name init  # 只搜索文件名是init的（精准搜索）
find /etc -name *init*  # 搜索文件名中包含init的文件
find /etc -name init???  # init开头，后面三个字符的文件
find /etc -iname init???  # 不区分大小写
find /tmp -size +/-204800（数据块=0.5K=512字节） #  空白表示等于（不常用）
find /home -user/group yaro  # 根据所有者/组
find /etc -amin(access访问时间)/cmin(change文件属性)/m(modify文件内容) -5  # 查看5min内（小于）被修改过的文件（夹）
find /etc -size +163840 -a -size -204800  # -a表示and，-o表示or
find /etc -type f/d/l  #只看某种文件类型
find /etc -name inittab -exec/-ok ls -l {} \;  # -exec/-ok 命令 {} \;
## {}表示前面查找的结果可能为多个   \表示转义符号   ；表示结束符   使用-ok的话会每次都询问
find . -inum 23068714 -exec rm {} \;  # 查找i节点为23068714（ls -i）的文件并删除
```

locate命令：linux上的everything

find 无法实现windows中 everything（根据ntfs文件数据库）的秒搜，需要秒搜的话可以使用locate来实现，常用`locate -ir "...."`,但是有些临时文件，locate数据库是不收录的。

命令搜索命令：which whereis(含帮助文档)

grep：文件内容搜索命令

使用方式：`grep 关键词 文件（夹）`

```sh
grep -ir mutiuser /etc  # （递归）搜索文件夹中的文件含有mutiuser(不区分大小写)的行
grep -v ^# /etc/inittab  # 不显示警号开头的行
```

#### 4、帮助命令

调用more命令显示某个命令的munual，另外**也可以查看系统配置文件的手册**。

```sh
man ls  # 查看ls的munual
man services  # 查看/etc/services的手册
man passwd  # 查看的是命令的帮助文件
man 5 passwd  # 查看配置文件帮助文件；
whereis passwd 查看有两个帮助文件：1=命令，5=配置文件；
whatis ls  # 查看man命令的简短描述信息；
whatis whatis/type/which/whereis/man  # 区分吧，少年；
apropos cd -a change  # search the manual page names and descriptions中含有cd且含有change的manual；
touch --help  # 列出常用的选项；
info date  # 显示命令的相关文档，排版没有man人性化；
which cd  # 可以查看命令是否为shell内置命令；
help umask  # 查看build-in命令的帮助；
```

#### 5、用户管理命令

这里先简单的介绍，后续详细介绍。

```sh
useradd 用户名  # 添加用户，只添加基本信息；
passwd 用户名  # 设置/更改用户密码；
who  # 查看当前登录用户信息，tty表示本地登录，pts表示远程登录；
w  # 查看更为详细的登录用户信息；
## 更复杂的用户管理命令后续介绍
```

#### 6、压缩/解压缩命令

压缩优势：省空间，备份方便，病毒不易感染等。

常用压缩格式：

- .gz格式

```sh
gzip  file # 只能压缩文件，不保留源文件；
gunzip file.gz  # (GNU unzip),解压缩也可以使用gzip -d;
tar -cvf japan.tar dir  # 讲dir打包成japan.tar，c-创建，v-详细信息，f-指定文件名。
gzip japan.tar  # 生成japan.tar.gz的压缩包，对于文件夹需要先打包成一个文件，后压缩。

## 也可以同时执行打包、压缩。
tar -zcvf japan.tar.gz 源目录  # 打包后自动压缩文件，效果等同于先tar -cf打包，再 gzip压缩。
tar -zxvf japan.tar.gz  # 解压缩
```

- .zip格式

古老的压缩协议，win和linux都支持。

```sh
zip boduo.zip 目标文件  # 压缩文件为boduo.zip，保留源文件；
zip -r boduo.zip 目标目录  # 压缩目录；
unzip boduo.zip  # 解压缩;
```

- .bz2格式

bzip2是gzip的升级版本，增加 -k 选项，压缩后保留源文件；压缩比较高，适用于大文件压缩。

```sh
bzip2 -k 文件  # 生成 '文件.bz2'的压缩文件；
tar -cjf japan.tar.bz2 japan  # 压缩文件夹，可以参考上面的 tar -zcf ;
bunzip2 -k 文件.bz2  # 解压缩，并保留源压缩包；
tar -xjf japan.tar.bz2  # 解压缩；
```

#### 7、网络命令

```sh
write yaro  # 给在线用户yaro发送消息，^D完成；
wall [message]  #write all 给所有人发信息；
ping -c 5 192.168.1.156  # ping五次，重点是：丢包率；
ifconfig  # 查看ip地址，ip addr show，l0是回环网卡；
mail yaro  # 给本地用户发邮件（使用内存），^D完成，mail读取邮件，help帮助信息；
last  # 查看所有用户的登录终端、登录ip、登录时间（持续时间）；
lastlog  # 查看所有用户的最近一次登录情况；
lastlog -u 502  # 查看用户uid为502的用户最近登录情况；
tracerout www.baidu.com  # 显示数据包到主机间的路径；
netstat -tuln  # 查看本机坚挺的端口,tcp/udp/listen/numeric(显示为ip和port，不解析)；

## 在iproute2软件包中可以用ss命令替换。 
netstat -an  # 查看本机所有的网络连接，all/numeric,与上一条命令的区别是：可以查看正在建立的连接；
netstat -rn  # 查看本机路由表，ip route；
setup  # 设置网络，只有redhat系列才有的可视化工具，永久生效，ifconfig是临时生效；

```

#### 8、关机和重启

```sh
## 早期的时候只有shutdown会先保存，后关机，更安全。现在习惯使然，推荐使用shutdown；
shutdown -h/r now  # 现在关机/重启，服务器不允许关机哦！；
shutdown -h +10  # 十分钟后关机；
shutdown -c  # 取消之前的关机指令；

## 其他关机命令
halt
poweroff  # 直接断电？
init 0

## 其他重启命令
reboot 
init 6

## 系统运行级别
0 关机；
1 单用户（只有root用户，类似于win的安全模式，启动最小的核心程序）；
2 不完全多用户，不包含NFS服务（network file system，linux系统间的文件共享服务，不安全？）；
3 完全多用户；
4 未分配；
5 图形界面；
6 重启；
# 之前的系统可以使用runlevel命令查询当前运行级别；
# /etc/inittab 文件可以修改系统默认运行级别；

## 退出登录
logout  # 记得离开电脑时退出哦！
```

### vim编辑器

` ：r !date` : 可以将date命令的运行的结果插入到当前位置；

`：map ^P I#<ESC> `:设置`ctrl+p`快捷键为注释当前行，`^P`的正确输入方式：`ctrl + v + p`

`:map ^B 0x`：设置`ctrl+b`快捷键为取消注释；

`ab mymail samlee@163.com`：每次输入`myamail`，空格、回车后就会显示邮箱。

### 软件包管理

软件包分类：源码包（C语言等，需要编译）、二进制包（直接安装，rpm/deb/pkg.tar.xz/exe格式等，不能看到源代码）

源码包优势：效率高出5%，开源，可以自由选择所需要的功能，直接删除即可卸载；

源码包缺点：安装过程步骤多，编译时间长，编译过程出错新手很难解决。

编译过程：./configue（配置、检查、写入/生成makefile）; make(编译，出错的话执行：make clean清除临时文件) ; make install(安装) 

### 用户和用户组管理

#### 1、用户配置文件

- /etc/passwd 用户信息文件

可以使用`man 5 passwd`查看配置文件的帮助：

第一字段：用户名。

第二字段：密码标志，x表示有密码。早期的时候密码（加密的密文）是放在这儿的，后期放在shadow里面，可以查看passwd和shadow的权限。

第三字段：UID；0：超级用户（普通用户改成0便成了`root用户`）；1-499系统用户（伪用户）；500-56635：普通用户。

第四字段：GID（初始组ID）；`初始组`：刚建立就有一个与用户名同名的初始组，不建议修改；`附加组`:后期可以加入很多组。

第五字段：用户说明（别名），可以为空。

第六字段：家目录。

第七字段：用户登录后默认的shell，标准的是/bin/bash,还可以是/sbin/nologin等。

- /etc/shadow 影子文件

是/etc/passwd的影子文件，字段如下：

1：用户名；2：加密密码（SHA512散列加密算法，有可能暴力破解哦，如果是`!!`或`*`表示没有密码，禁止登录）；3：最近一次设置密码的时间（时间戳1970.1.1之后的天数）；4：两次密码的修改间隔（间隔内不允许改密码）；5：密码有效期（第三个字段之后的天数）；6：密码修改到期前的警告天数（与第五个字段的比较，提前N天提示修改密码）；7：密码过期后的宽限天数（0：和空白一样，表示立即失效，-1：表示永远不会失效）；8：账号失效时间（N天后账号禁用，使用时间戳表示）；9：保留字段。

- /etc/group组信息文件和/etc/gshadow组密码文件

group文件：

第一字段：组名。

第二字段：组密码标识。

第三字段：GID。

第四字段：组中附加用户。

gshadow文件（用的较少）：

第一字段：组名。

第二字段：组密码，默认只有root可以修改组，当然root可以给每个组设置个“副班长”，用的不多。

第三字段：组管理员用户名。

第四字段：组中的附加用户。

#### 2、用户管理相关文件

- 用户的家目录

普通用户：/home/yaro 默认权限700

超级用户：/root/ 默认权限550

- 用户的邮箱

/var/spool/mail/用户名/,linux自带的客户端，没有服务端。

- 用户模板目录

/etc/skel/，创建用户的时候，用户的家目录自动创建的文件都在这里。

#### 3、用户管理命令

- 用户添加命令：useradd

>  添加用户后，设置了密码才添加完成，添加用户其实就是在上面的`四个配置文件`中写入相应的信息，然后自动创建`家目录`、`邮箱目录`，手动写入也可以实现哦。

格式：`useradd [option] 用户名`

> -u：指定UID号；
>
> -d：指定家目录；
>
> -c：指定用户说明；
>
> -g：指定用户的初始组；
>
> -G：指定用户的附加组，逗号`,`分隔多个组；
>
> -s：指定用户登录的默认shell；

如：`useradd -u 550 -G root,bin -d /home/seth -c'test user' -s /bin/bash seth`

**用户默认值文件`/etc/default/useradd`**

```sh
GROUP=100  # 这个是公有模式，现在都是私有模式，默认使用同名的用户组。
HOME=/home  # 用户家目录
INACTIVE=-1  # 密码宽限天数，shadow文件的7字段
EXPIRE=  # 密码失效时间，第八个字段
SHELL=/bin/bash  # 默认shell
SKEL=/etc/skel  # 模板目录
CREATE_MAIL_SPOOL=no  # 默认是否建立邮箱
```

>  除了这个文件，还有`/etc/login.defs`文件来规定`shadow`的其他几个字段(密码有效期、密码修改间隔、密码最小位数、密码到期警告、最大最小UID范围、加密模式等)。

- 修改用户密码：passwd

添加用户之后，必须设置密码才能正常登录。

格式：`passwd [option] 用户名`

> 用户名可以省略，默认给当前用户修改密码；
>
> -S：查询当前密码状态，其实就是shadow文件中的内容，只能root使用。
>
> -l：锁定用户，其实是在shadow文件的密码前加了`!!`,添加几个感叹号效果是一样的；
>
> -u：解锁用户；
>
> --stdin  如：`echo "123" | passwd --stdin yaro` 将"123"设置为yaro的密码，shell编程常用，批量添加多个用户及密码。



- 修改用户信息：usermod

修改一个已经存在的用户的信息，用法基本同useradd命令。

格式：`passmod [option] 用户名`

>-u：修改UID
>
>-c：修改用户说明
>
>-G：修改附加组
>
>-L：临时锁定用户（lock）
>
>-U：解锁用户锁定（unlock）

TIPS：禁用用户的方法有很多：使用usermod、passwd、手动修改/etc/passwd 或者 /etc/shadow（注释用户，用户对应位置添加`!!`），都可以，随便使用一个就可以了。

- 修改用户密码状态:chage

chage-change user password expiry information。

格式：`chage [option] 用户名`

> -l:列出用户的详细密码状态
>
> -d:密码的最后一次更改日期（shadow3字段）
>
> -m:两次密码修改间隔（4字段）
>
> -M:密码有效期（5字段）
>
> -W:密码过期前警告天数（6字段）
>
> -I:密码过期后宽限天数（7字段）
>
> -E:账号失效时间（8字段）

上面的选项太多，其实用直接修改shadow文件更方便，实际最多的应用如下：

**`chage -d 0 yaro`把用户的密码修改日期归0，这样的话用户第一次登录就要修改密码。**

- 删除用户userdel,查看用户ID命令id，用户切换命令su

1、userdel

常用选项：`userdel -r yaro` # 删除用户的同时移除家目录。

效果等同于手动删除如下对应6个位置：

```sh
vi /etc/passwd; 
vi /etc/shadow; 
vi /etc/group; 
vi /etc/gshadow; 
rm -rf /var/spool/mail/yaro（邮箱）； 
rm -rf /home/yaro/; 
# 当然有些还需要删除 /etc/skel/ 下的模板；
```

2、`id yaro` 查看用户id，组id，和属于哪个组。

3、用户切换命令su

格式：`su [option] [-] [<user> [<argument>..,]]`

> `-` ： 选项只是用`-`表示连带用户的环境变量一起切换；
>
> -c ： 仅执行一次此命令，而不切换用户身份；

```sh
su  # user省略的话，假定是root；
su root  # 切换到root，但是环境变量还是yaro的；
whoami  # 当前用户也切换到root了；
env  # 查看当前环境变量，可以看到环境变量并没有修改；
su -  # 等同于su - root,环境变量也切换；
su - root -c "useradd seth"  # 临时调用root权限，执行添加命令；
```

#### 4、用户组管理命令

相关命令：`groupadd` 和 `groupmod`和`groupdel`和`gpasswd`

```sh
groupadd grp  # 添加grp用户组，可以使用-g选项，手动指定组id；
groupmod -n testgrp group1  # 把组名group1修改为testgrp，也可以使用-g选项指定GID；
groupdel testgrp  # 删除用户组，每个用户必须要个主组，用户存在的时候，不能删除主组,(附加用户可以)；
gpasswd -a yaro grp  # 把用户yaro加入到grp组中；直接修改/etc/group文件也可以；修改的是附加组，当然，主组不建议修改；也可以通过usermod来修改；
gpasswd -d yaro grp  # 把用户yaro从grp组中删除；
```

### 权限管理

#### 1、ACL权限

> 之前我们介绍了基本权限：所有者、所有组、其他人的读写执行权限。

- 1.1 ACL权限简介与开启

简介：**ACL权限**(Access Control List)是为了防止权限不够用的情况，一般的权限有所有者、所属组、其他人这三种，当这三种满足不了我们的需求的时候就可以使用ACL权限；

简而言之：就是忽略之前的UserGroupOther权限，想给某个人什么权限，直接赋予权限即可（和windows权限的思路类似）。

refer to :http://www.cnblogs.com/zengguowang/p/5687499.html

> 比如：一个网络老师，给一个班的学员上课，他在linux的根目录下面建立了一个文件，只允许本班级的 学员对该目录进行上传下载，其他人都不行，这是该目录的权限一般是770（一般我们设置权限都是所有者的权限大于所属组的权限，所属组的权限大于其他人的权限，依次往下），此时有个同学想试听我们的课程，该怎么给他分配权限呢？此时的话所属组、所有者、其他人都不满足，这是就用到ACL权限;

查看分区ACL权限是否开启：`dumpe2fs -h /dev/sda3`,查看`default mount option`含有acl表明已经开启；

临时开启分区ACL权限：`mount -o remount,acl / #重新挂载根分区支持acl权限`

永久开启ACL权限：修改`/etc/fstab #开启自动挂载文件`，现在linux默认的`default`都支持了acl，如果默认不支持的话，需要手动添加`,acl`；然后手动执行`mount -o remount /`重新挂载根分区即可。

- 1.2 查看与设定ACL权限

查看权限：`getfacl 文件名` 

设定权限：`set facl 文件名`

```sh
useradd st
groupadd tgroup
mkdir /project
chown root:tgroup /project # 设定所有者和所有组
chmod 770 /project  # 设定基本权限

setfacl -m u:st:rx /project  # 给project设定acl权限，u-用户（st），权限为rx
ll -d project  # 可以看到基本权限后面有个'+'号
getfacl /project  # 查看acl权限

groupadd tgroup2
setfacl -m g:tgroup2:rwx project  # 给组设定acl权限
```

- 1.3 最大有效权限与删除ACL权限

最大有效权限mask：其实我们给用户赋予的acl权限，是需要和mask的权限‘相与’才能得到用户的真正权限。默认的mask权限是`rwx`。`setfacl -m m:rx /project`可以指定mask权限为`rx`。

删除acl权限：

```sh
setfacl -x u:用户名 文件名  # 删除文件的用户acl权限
setfacl -x g:用户组 文件名  # 删除文件的用户组acl权限
setfacl -b 文件名  # 删除文件的所有acl权限
```

- 1.4 默认ACL权限和递归ACL权限

递归：子目录继承父目录的acl权限，`setfacl -m u:用户名：权限 -R 文件名`，（注意`-R`的位置不能随便修改哦）

> 问题：当文件夹中新建了文件，就需要重新执行上面的命令才能对新文件生效，此时就需要`默认acl权限`。

默认acl权限：`setfacl -m d:u:用户名：权限 文件名`，这样里面再新建文件自动继承父目录的acl权限。

#### 2、文件特殊权限

- 2.1 SetUID

**功能介绍：**

a、只有可以执行的二进制程序才能设定SUID权限；

b、命令执行者要对改程序拥有x权限；

c、命令执行者在执行该程序时获得改命令的文件属主的身份；

d、SetUID权限只在该程序执行过程中有效，也就是说身份改变只在程序执行过程中有效。

> 比如：`/usr/bin/passwd`文件，需改密码时，密码保存在shadow文件中，而shadow文件的权限是000；passwd文件就有SUID权限，当普通用户执行passwd文件时，便会化身为passwd的拥有者（root）身份。

passwd命令拥有SUID权限，所以普通用户可以修改自己的密码，passwd的权限为`-rwsr-xr-x`(注意`s`权限)；

cat命令没有SUID权限，所以普通用户无法查看/etc/shadow文件的内容。

**设定及取消SetUID方法：**

```sh
chmod 4755 文件名  # 赋予SUID权限，4 2 1 用户，用户组，SBIT；设定SUID后会自动添加x权限，没有x权限的话，SUID会显示为`S`（大写的S），即：报错；
chmod u+s 文件名  # 同上。
chmod 755 文件名  # 取消SUID权限；
chmod u-s 文件名： # 同上。
```

**危险的SetUID：**

> 比如`/usr/bin/vim`文件所有者是root，默认权限是`-rwxr-xr-x`，如果赋予SetUID权限，普通用户便可以直接修改root才能修改的文件（比如/etc/passwd的UID），普通用户的UID设置为0便是`root用户`，这十分危险！！

关键目录应严格控制写权限。比如：`/` `usr`等目录；

用户的密码设置严格遵守密码三原则；

对系统中默认应该具有SetUID权限的文件做一个列表，定时检查是否有其他文件被设置了SetUID权限。

- 2.2 SetGID

**SetGID针对文件的作用:**

只有可执行二进制文件才能设置SGID权限；

命令执行者要对该文件拥有x权限；

命令执行者在执行改文件（程序）时，组身份升级为改程序文件的属组；

SetGID权限（组身份的改变）同样只在改程序执行过程中有效；

> 比如：`l /var/lib/mlocate/mlocate.db`文件的权限是`-rw-r----- 1 root locate`,其他用户的权限是`000`，按理说其他用户是无法索引这个数据库文件的。
>
> 但是，`/usr/bin/locate`的权限是`-rwxr-sr-x 1 root locate`(具有SGID权限)，当其他用户执行locate命令时，会变成`locate组`，而`mlocate.db`文件的组权限是`-r-`，所以其他用户才能访问这个数据库。

**SetGID针对目录的作用**（SUID无此特征）

普通用户必须对此目录拥有r和x权限，才能进入此目录；

普通用户在此目录中的有效组会变成此目录的属组；

若普通用户对此目录拥有w权限时，新建的文件默认属组是这个目录的属组。

```sh
pwd  # /root
mkdir /tmp/test
chmod 2777 /tmp/test/
ll -d /tmp/test/  # drwxrwsrwx root root 
su - yaro  
pwd  # /home/yaro
touch abc 
ll abc  # yaro yaro，用户和用户组都是yaro
cd /tmp/test/
touch bcd 
ll bcd  # yaro root , 用户是yaro，但是用户组是root
## 感觉SetGID对目录的作用用途不大。(⊙o⊙)…
```

**设置和取消SetGID**

```sh
chmod 2755 文件名or目录  # 4 2 1 
chmod g+s 文件名or名录
chmod 755 文件名or目录  # 4 2 1 
chmod g-s 文件名or名录
```

- 2.3 Sticky BIT(粘着位)

**SBIT作用**

粘着位目前只对目录有效（所以对特殊权限设置为7不合适，因为有的针对文件，有的针对目录）；

普通用户对该目录拥有w和x权限（创建/删除文件和进入权限）；

如果没有粘着位，普通用户可以删除该目录下面的所有文件（包括其他用户创建的文件），**一旦赋予`粘着位`，只有root可以删除所有文件，普通用户就算拥有w权限，只能删除自己建立的文件**（不能删除其他用户建立的文件）。

```sh
ll -d /tmp  # drwxrwxrwt  14 root root t表示粘着位
```

**设置与取消粘着位**

```sh
## 只能root操作

chmod 1755 目录  # 设置SBIT 4 2 1 
chmod o+t 目录

chmod 777 目录  # 取消SBIT
chmod o-t 目录

# 在此说明：特殊权限位很少设置为7，因为 4 2 1 有的针对文件，有的针对目录；而且特殊权限有风险，最好不要设置为7。
```

#### 3**、文件系统属性chattr权限**

**chattr命令（change attributes）格式**

```sh
chattr [+-=] [选项] 文件or目录
+ ： 增加权限
- ： 删除权限
= ： 等于权限 
---------------------
i：（immutable不可变）对文件设置i属性，表示不能对文件进行删除、更名、修改数据；对目录设置i属性，表示只能修改目录下文件的数据，不能创建和删除文件。
## 用途：可以防止文件误删除
pwd  # /root
touch abc
chattr +i abc  # 添加i属性，即使是root用户，也不能修改，删除。
lsattr -a abc  # 查看所有文件attr属性，类似 ls -a ，e表示分区我ext4；
----------------------
a：（append）文件设置a属性，表示只能对文件增加内容，不能删除和修改数据；如果对目录设置a属性，只允许目录中建立和修改文件，但是不能删除文件。
## 用途：保护文件原来的数据。
```

#### 4、系统命令sudo权限

**sudo权限简介**

> 场景：root很忙，大部分都是一般用户，但是一般用户有时候需要特殊的权限（比如很多服务器的关机or重启）。

root用户把只能超级用户执行的命令赋予普通用户来执行。

sudo的操作对象是系统命令（前面讲的很多权限都是针对文件or目录的）。

**sudo的使用**

```sh
visudo  # 管理员执行，实际修改的是/etc/sudoers文件
root ALL=(ALL) ALL
# 用户名 被管理主机的地址=（可使用的身份） 授权命令（绝对路径）；
#### 注意是被管理主机的地址，及，yaro用户可以使用的用户（root，还是all？）。
----------------------
%wheel ALL=(ALL) ALL
#%组名 被管理主机的地址=（可使用的身份） 授权命令（绝对路径）；
## 记得组名前有百分号（%）；
---------------
yaro ALL= /sbin/shutdown -r now  # 授权重启（如果只写shutdown，权限比较大，可以关机等）命令
---------------
# yaro 执行重启如下：
sudo /sbin/shutdown -r now
sudo -l  # 可以查看yaro用户被赋予了哪些命令。
---------------
## 温馨提示：不要给一般用户赋予vim类似的工具sudo权限，否则一般用户可以修改系统的任何东西。
```

### 文件系统管理

#### 1、回顾分区和文件系统

**分区**

主分区：总共最多只能分4个；

扩展分区：为了突破4个主分区的限制，把其中一个主分区拿出来当做扩展分区；只能有一个，主分区加扩展分区最多四个；但是扩展分区不能存储数据和格式化，必须再划成逻辑分区才能使用。

逻辑分区：IDE接口硬盘linux最多支持59个逻辑分区，SCSI硬盘linux最多支持11个逻辑分区。

> 例如：主分区1-sda1、主分区2-sda2、主分区3-sda3、**扩展分区-sda4**（逻辑分区1-sda5、逻辑分区2-sda6...）；
>
> 但是1 2 3 4 只能给主分区or扩展分区使用，如：主分区1-sda1、扩展分区-sda2**（逻辑分区1-sda5、逻辑分区2-sda6...）

**文件系统**

硬盘有了分区，必须格式化才能使用，即写入文件系统。

et2:最大支持16TB分区和最大2TB的文件；

et3：最大支持16TB分区和最大2TB的文件，带有日志功能，提高了文件的可靠性；

et4:最大支持1EB分区和最大16TB的文件、无限数量子目录、在线碎片整理、向下兼容等等；

#### 2、文件系统常用命令

**df命令**

```sh
df -h 
df -ah  # 所有，包括/proc /sysfs等
```

**du命令**

```sh
du -h /etc
du -sh /etc  # 只查看文件夹的总大小
du -hd 1 /etc  # max-depth为1
du -ha /etc  # all file
```

> du面向文件，只计算文件和目录的占用；df命令面向文件系统，除了所有文件，还有系统和进程占用的文件（系统长期不重启、高负载、游戏服务器、下载服务器等，都需要定期维护，及重启）。

**fsck命令**

fsck：文件系统修复命令。

```sh
fsck -a 分区设备文件名  # 不显示用户提示，自动修复文件系统；
fsck -y 分区设备文件名  # 和-a作用一致，自动修复，不过有些文件系统只支持-y；
# tips：不需要手动执行，系统启动时自动执行；属于底层命令，手动执行还可能出现问题。
```

**dumpe2fs命令**

dumpe2fs : dump ext2/ext3/ext4 filesystem information。

```sh
dumpe2fs -h /dev/sda1
# 输出内容很多，主要查看分区的默认挂载选项、Block size 等,-h只显示超级块内容。
```

**挂载命令**

```sh
mount -l  # 查询系统已挂载的设备，-l可以省略；
mount -a  # 挂载配置文件/etc/fstab中所有的文件系统，系统启动时已经挂载；
mount [-t 文件系统] [-L卷标名] [-o 特殊选项] 设备文件名 挂载点  # 完整的格式
# -t 文件系统可以是ext3、ext4、iso9660（光盘）、fat（fat16）、vfat（fat32）等
# -o 特殊选项，较多，如：noatime（不更新访问时间）、remount（重新挂载）、enoxec（不允许可执行文件执行）；如：
mount -o remount,noexec /home/  # 重新挂载/home并且不允许/home下的可执行文件执行，哪怕是root用户；实际生产中如果服务器用于上传下载，便可以把/home分区设置为不允许执行，防止客户上传病毒执行。
# 其实平时使用时，中括号内的东西都可以省略。
```

挂载光盘

```sh
mkdir /mnt/cdrom  # 建立挂载点,其实只要是空目录都可以当做挂载点；
mount -t iso9660 /dev/cdrom /mnt/cdrom  # 挂载；
mount /dev/sr0 /mnt/cdrom  # cdrom是sr0软链接；
umount 设备文件名or挂载点  # 卸载；
```

挂载U盘

```sh
# 如果是虚拟机的话，需要先激活（鼠标点击）linux虚拟机，再插入U盘；
fdisk -l  # 查看U盘设备文件名，lsblk也可以查询；
mount -t vfat /dev/sdb1 /mnt/usb  # fat（fat16）、vfat（fat32）；
# 注意linux默认不支持NTFS文件系统；
```

挂载iso/img文件

```sh
mount -o loop disk1.iso /mnt/disk  # 挂载iso文件
cp /dev/cdrom xxx.iso  # 直接制作光盘iso文件，太简单了！！
```

> Since you want to mount a file, you must first create a `loop` block device that is backed by the file. This can be done using `losetup`, but `mount -o loop` is a shortcut that handles that behind the scenes.
>
> In [Unix-like](https://en.wikipedia.org/wiki/Unix-like) operating systems, a **loop device**, **vnd** (vnode disk), or **lofi** (loop file interface) is a [pseudo-device](https://en.wikipedia.org/wiki/Device_file#Pseudo-devices) that makes a [file](https://en.wikipedia.org/wiki/Computer_file) accessible as a [block device](https://en.wikipedia.org/wiki/Device_file_system#Block_devices).

**支持NTFS文件系统**

linux内核编译时已经集成了很多硬件（显卡，声卡等）的驱动，但是没有集成NTFS的驱动。so，支持NTFS解决方法：1、重新编译内核（额..）；2、利用第三方软件（NTFS-3G插件）。

安装：官网下载源码包，安装即可；当然也可以使用distr的repo安装。

使用：`mount -t ntfs-3g 分区设备名 挂载点`即可挂载NTFS的设备。

#### 3、fdisk分区

**fdisk分区过程**

```sh
# 添加新的硬盘
fdisk -l  # 查看所有fixed disk(固定磁盘、硬盘)分区状况；
disk /dev/sdb  # 对/dev/sdb磁盘进行分区；
-------------
# 之后进入fdisk界面。常用如下：
m 帮助；
p 查看已有分区；
d 删除一个分区；
n 新建分区；
l 显示已知的文件系统类型；
t 改变分区的文件系统类型；
w 保存退出；
q 不保存退出；
--------------
#若保存时遇到提示：“分区正在使用，请重启linux”，此时可以执行如下命令：
partprobe  # 重新读取分区表信息；
```

**格式化分区**

```sh
mkfs -t ext4 /dev/sdb1  # 把sdb1分区格式化为ext4格式；
# 注意扩展分区的功能只是包含逻辑分区，不能修改，不能格式化！
```

**创建挂载点、挂载**

```sh
mkdir /disk1
mount /dev/sdb1 /dist1/
df -h  # 查看已经挂载的分区
mount  # 查看已经挂载的分区
```

**分区自动挂载与fstab文件修复**

分区后用mount命令进行挂载，但是每次重启后，就得重新手动挂载；若想自动挂载，就需要写入`/etc/fstab`文件。

```sh
第一字段：分区设备文件名orUUID（硬盘通用唯一识别码） # 通过dumpe2fs -h 查询UUID；
第二字段：挂载点；
第三字段：文件系统名称；
第四字段：挂载参数  # 同mount挂载选项；
第五字段：指定分区是否被dump备份，0代表不备份，1代表每天备份，2代表不定期备份 # 即每个分区下的“lost+found”；
第六字段：指定分区是否被fsck检测，0代表不检测，其他数字代表检测的优先级，1比2的优先级高  # 其他分区的优先级应该低于根分区。
--------------
# 比如写入如下内容：
/dev/sdb1	/disk1	ext4	default	0 2 
# 测试挂载是否正确
mount -a
# 便可以开机自动挂载sdb1分区
```

> /etc/fstab 文件是系统开机加载的重要文件，写错的话，可能导致系统崩溃。所以为了保险起见，修改`/etc/fstab`文件后，记得执行`mount -a`测试一下，看是否有错。

`/etc/fstab`文件的修复：

假如我们确实写错了`/etc/fstab`文件，重启之后，可以根据错误提示用root进入系统，但是无法修改`/etc/fstab`文件，这是因为，此时挂载的是只读权限。需要执行：

```sh
mount -o remount,rw /  # 重新以rw权限挂载根分区；
# 修复的局限性：前提是还能进入系统，即根分区挂载正常。
```

#### 4、分配swap分区

分区时，swap分区必须设置哦。

**free命令**

作用：查看内存与swap分区使用状况。

`cached（缓存）`：是指把读取出来的数据保存到内存当中，当在此读取时，可以直接从内存（而不是硬盘）读取，加速数据的读取速度。

`buffer（缓冲）`：是指在写入数据时，先把分散的写入操作保存到内存中，当大道一定程度再集中写入硬盘，减少硬盘碎片和硬盘的反复寻道，加速数据的写入速度。

> free 命令里面的参数请参考：https://www.linuxatemyram.com/

**新建/格式swap分区**

```sh
fdisk /dev/sdb  # 记得把分区好改成82；
# 分区完成后，若提示错误，记得执行；
partprobe  # 提示警告/报错，不用理会，实在不行还得重启系统额；
mkswap /dev/sdb6  # 格式化为swap分区；
```

**加入swap分区**

```sh
swapon /dev/sdb6  # 加入swap分区；
swapoff /dev/sdb6  # 取消swap分区；
---------------
# 当然我们也需要开机自动挂载,写入/etc/fstab文件，写入如下内容（即使原来有swap分区，也可以重写一遍增加swap分区）：
/dev/sdb6 	swap	swap	default	0	0  # 挂载点不是 “/swap”哦
```

### Shell基础

#### 1、shell概述

shell（命令解释器）： 硬件 》内核 》Shell命令解释器 》外层应用程序。

Shell还是一个功能强大的变成语言，shell是解释执行的脚本语言，在shell中可以直接调用linux系统命令。

**分类：**

Bourne Shell家族只要包括：sh、ksh、Bash、psh、zsh；

> 现在linux中主要使用的`Bash`，与`sh`兼容

C Shell（主要在BSD进本的unix）主要包括：csh、tcsh

#### 2、shell脚本执行方式

**`echo`命令：**

`-e`选项可以开启特殊的解释：如`\t`制表符，`-b`退格符。还可以指定输出的颜色:

```sh
echo -e "\033[背景色代码;字体色代码m需要显示的内容\033[0m"
# -e表示可以颜色显示解析，背景色可以省略，字体色代码后面必须加m，后面的[0m是选项，如：          
echo -e "\033[32mWhat the fuck\033[0m"
# 参考网页：http://www.techug.com/post/shell-console-color-setting.html
```

**第一个脚本**

`vim hello.sh`，写入如下内容：

```sh
#!/bin/bash
#sh文件功能描述
#by author yaro 20171108 (Email:xxx@163.com)
echo -e "Mr. Yaro is a honest man"
```

**脚本执行**

```sh
# 方法一
chmod 755 hello.sh
./hello.sh  # 或者是绝对路径
# 方法二
bash hello.sh  # 不需要执行权限
```

> 由于win下的回车符和linux不同（可以使用`cat -A 查看`），so，win中编辑的shell文件，在linux无法执行，这是需要使用`dos2unix`命令（需要先安装）转换。

#### 3、Bash基本功能

**历史命令history**

```sh
history -c  # 清除缓存及./bash_history里面的命令;
history -w  # 将缓存中的历史命令写入./bash_history;
# 默认保存1000条历史命令，可以在/etc/profile中修改
```

**命令别名**

```sh
alias  # 查看当前的别名列表
alias vi='vim'
alias l="ls -lah --color=auto"
alias cp='cp -i'
unalias cp  # 取消alias
# 以上命令只会临时生效，若想别名永久生效，需要写入.bashrc。
```

命令的执行顺序：1、绝对路径or相对路径；2、别名alias；3、bash内部命令（shell自带，没有执行文件）；4、$PATH变量找到的第一个命令。

> 其实linux默认都是执行绝对路径的命令执行文件，之所以可以直接运行命令，是因为系统通过`$PATH`变相的查找。

**输入/输出重定向**

1. 标准输入输出：

| 设备   | 设备文件名       | 文件描述符 | 类型     |
| ---- | ----------- | ----- | ------ |
| 键盘   | /dev/stdin  | 0     | 标准输入   |
| 显示器  | /dev/stdout | 1     | 标准输出   |
| 显示器  | /dev/stderr | 2     | 标准错误输出 |

2. 输出重定向

```sh
command > file  # 标准输出重定向-覆盖
command >> file  # 追加
error_command 2> file  # 标准错误输出重定向
error_command 2>> file
-------------
# 但是日常工作中，我们无法判断命令输入是否正确，所以经常使用如下命令：
(error_)command &> file  # 正确输出和错误输出都写入file；
(error_)command &>> file  # 常用
# 以下方式相同功能：
(error_)command > file 2>&1  # 先将错误输出2写入正确输出1  
(error_)command >> file 2>&1
# 还可以将正确输出和错误输出分开保存:
(error_)command >>file1 2>>file2  # 常用
-------------
# 实用例子：
command &> /dev/null  # 无论输出什么都丢到垃圾箱。
```

3. 输入重定向

定义：本来命令的参数应该通过键盘（stdin）来写入，但是现在输入的来源，通过文件来输入参数。一般情况使用的不多（一般在源码包打补丁时用到）。下面以wc命令讲解：

```sh
wc [option] [file_name]
-c 统计字节数
-w 统计单词数
-l 统计行数
# 不加选项的话，统计（ctrl+d）输入字符的行数、单词书、字符数。
wc < abc.txt  # 统计文件的详细信息；
# wc << hello  # 以hello开始统计，不是以ctrl+d结束，而是在此遇到hello结束。 
```

4、多命令顺序执行与管道符

**多命令顺序执行**

`;`:多个命令顺序执行，命令之间没有任何逻辑联系；

`&&`:逻辑与，只有前面的命令执行成功，后面的才执行；

`||`:逻辑或，前有两个命令只执行一个；

```sh
dd if=输入文件 of=输出文件 bs=字节数 count=个数  
#-------------
if:指定源文件or源设备
of：指定目标文件or目标设备
bs：指定一次输入/输出多少字节，即把这些字节看做一个数据块
court：指定输入/输出多少个数据块
# 不同于cp，cp命令只能copy文件，dd命令可以看作是磁盘对拷命令。
date;dd if=/dev/zero of=~/testfile bs=1k count=10000;date  # 可以查看创建100M的文件需要多少时间；
./configure && make && make install
ls abc && echo yes || echo no
```

**管道符`|`：命令1的正确输出作为命令2的对象**

```sh
ls -ah /etc/ | more  # more默认只能跟文件；
ss -an | grep -i estab  # 查看正在连接的远程连接
```

5、通配符及其他特殊字符

**通配符**

```sh
?  # 一个任意字符
*  # 零个换任意多个字符
[abc]  # 匹配中括号中的一个 
[a-z]  # 匹配范围
[^0-9]  # 匹配0-9之外的内容
------------
cd /tmp/
rm *
ls *abc*
# 通配符是用来匹配文件名，regex用来匹配文件内容。
```

**其他特殊字符**

```sh
‘’  # 单引号，里面的所有内容都没有特殊意义；
“”  # 双引号，除了$（变量） `（引用命令） \（转义符），其他同单引号；
``  # 里面的是系统命令，先执行里面的命令；
$()  # 同反引号，单引号容易和单引号混淆；
警号  # 注释；
$  # 调用变量；
\  # 把特殊字符变成普通符号（转义字符；）

echo '$(date)'
echo "$(date)"
```

#### 4、Bash变量

**4.1 用户自定义变量**

定义：又称作`本地变量`，用户自己控制，最自由；

```sh
aa=123  # 定义变量；
aa="$aa"456  # 变量的追加（叠加）；
aa=${aa}789  # 同上；
echo $aa  # 调用变量；
set  # 查看所有变量（本地变量、环境变量等）；
unset aa  # 删除aa变量 ；
```

**4.2 环境变量**

定义：主要保存的是和系统操作环境相关的数据（变量名习惯性用大写字母）；

`用户自定义变量`只在当前shell中生效。而`环境变量`会在当前`shell`和`子shell`中生效；如果把环境变量写入配置文件，那么这个环境变量就会在所有的shell中生效。

> `pstree`可以查看进程树，查看各个shell的父子关系。

```sh
name=yaro  # 声明本地变量
export 变量名=变量值  # 声明环境变量；
export name  # 把本地变量声明为环境变量
echo $name  # 调用环境变量；
env  # 查询环境变量；
unset 变量名  # 删除变量；
```

**系统常见环境变量**

`PATH变量`：系统查找命令的路径；Tab补全，及`which`搜索都是依托于PATH变量。

```sh
PATH="$PATH":/home/yaro/.yaro  # 追加新的PATH路径，永久生效的话需要写入配置文件；
```

`PS1变量`：定义系统提示符的变量,terminal里面的默认显示的项目。

```sh
\d ：代表日期，格式为weekday month date
\H ：完整的主机名
\h ：主机的第一个名字
\t ：显示时间为24小时格式(HH:MM:SS)
\T ：显示时间为12小时格式
\A ：显示时间为24小时格式(HH:MM)
\u ：当前用户的账户名
\v ：BASH的版本信息
\w ：完整的工作目录名
\W ：利用basename取得工作目录名称，所以只会列出最后一个目录
\# ：第几个命令
\$ ：提示字符，如果是root时，提示符为：#;普通用户为：$
# 参考网页：http://blog.csdn.net/zhangxuechao_/article/details/52016770
```

> 挺好玩的，但是没卵用。。。

**4.3 位置参数变量**

定义：主要用来向脚本传递参数or数据，变量名不能自定义，变量的作用是固定的。

作用：在脚本运行时，向脚本传递我们的参数，但是只有脚本作者本身才知道需要传递几个参数。

> `位置参数变量`本质上属于`预定义变量`。

`$n` :n为数字，0代表命令本身，3代表第3个参数，大于10的需要用`{10}`表示 

`$*` :命令中所有的参数，把所有参数当做一个整体；

`$@` :命令中所有的参数，把每个参数区分对待；

`$#` :命令行中所有参数的个数。

```sh
# 新建sum.sh文件，写入如下内容：
# -----------
#!/bin/bash
sum=$(( $1+$2 ))  # 数字计算必须用$(( ... )) 
echo "the sum is: $sum"
#------------
chmod 755 sum.sh
./sum.sh 7 5  #将会计算7和5的和；
#---------------

```

**4.4预定义变量**

**预定义变量**

定义：是Bash中已经定义好的变量，变量名不能自定义，变量作用也是固定的。

`$?`: 最后一次执行的命令返回状态。如果为0，表明上一条命令正确执行；如果非0（具体那个数值，由写命令的人决定），则表明上一条命令执行不正确。

`$$`: 当前进程的进程号（PID），即当前脚本执行的PID；

`$!`: 后台运行的最后一个进程的进程号（PID）

```sh
ls 
echo $?  # 显示0，表示ls执行成功，其实 && 和 || 也是通过这个判断的。
# --------
# 创建如下test.sh文件
echo "The current process is $$"  # 即test.sh执行的PID；
find /roo -name test.sh &  # 后台运行这个查找命令，类似win的最小化？；
echo "The last one Daemon process is $!"  # 显示find命令的PID
```

**接收键盘输入**

之前的`$0`，`$n` 只有脚本作者知道应该给予的参数，其实使用`read`命令合适。

语法：`read [选项] [变量名]`

`-p "提示信息"`：在等待read输入时，输出的提示信息；

`-t 秒数`：指定等待输入的时间；

`-n 字符数`：read命令只接受指定的字符数，就会执行；

`-s` ： 隐藏输入的数据，适用于机密信息的输入；

```sh
#!/bin/bash
# by author :yaro
read -t 30 -p "Please input your name: " name
echo "Name is $name"

read -s -t 30 -p "Please enter your age: " age
echo -e "\n"  
echo "Age is $age"

read -n 1 -t 30 -p "Please select your gender[M/F]: " gender
echo -e "\n"
echo "Sex is $gender"
```

#### 5、数值运算和运算符

shell编程中，默认的变量都是字符型，如：

```sh
a=1
b=2
c=$a+$b
echo $c  # 结果为：“1+2”，都是字符串；
```

**5.1 数值运算**

**declare声明变量类型**

语法：`declare [+/-] [选项]`

`-` ：给变量设定类型属性；

`+` :取消变量的类型属性；

`-i` :将变量声明为整数型（integer）；

`-x`: 将变量声明为环境变量，效果同`export`；

`-p` :　显示指定变量的被声明的类型；

数值运算方法如下：

- 方法一

```sh
a=1; b=2
declare -i c=$a+$b
echo $c  # 3，不再是“1+2”
```

- 方法二

```sh
a=1; b=2
d=$(expr $a + $b)  # 加号两边必须有空格
echo $d
# expr 和let格式一样。
```

- 方法三（推荐）

格式：`$((运算表达式))`or`$[运算表达式]`

```sh
a=1; b=2
f=$(($a+$b))  # 加号两侧可以有空格，单双引号是先执行里面的命令。
echo $f
```

**运算符**

基本同大多数语言，最常用的莫过于：加减乘除、模(%)、and(&&)、or(||)、非(!)等,*放在双小括号中即可*

**5.2 变量测试与内容替换**

平时我们判断时，可以使用if语句来实现，系统提供更简洁的方式来判断，**但是不容易记忆,其实能看懂就可以**。

| 变量配置方式           | str 没有配置         | str 为空字符串        | str 已配置非为空字符串  |
| ---------------- | ---------------- | ---------------- | -------------- |
| var=${str-expr}  | var=expr         | var=             | var=$str       |
| var=${str:-expr} | var=expr         | var=expr         | var=$str       |
| var=${str+expr}  | var=             | var=expr         | var=expr       |
| var=${str:+expr} | var=             | var=             | var=expr       |
| var=${str=expr}  | str=exprvar=expr | str 不变var=       | str 不变var=$str |
| var=${str:=expr} | str=exprvar=expr | str=exprvar=expr | str 不变var=$str |
| var=${str?expr}  | expr 输出至 stderr  | var=             | var=$str       |
| var=${str:?expr} | expr 输出至 stderr  | expr 输出至 stderr  | var=$str       |

> 参考鸟哥教程：http://cn.linux.vbird.org/linux_basic/0320bash_2.php

```sh
unset y  # 删除变量y
x=${y-new}  # 进行测试
echo $x  # new，因为变量y不存在，所以x=new
y=""  # 变量y为空
x=${y-new}  # 进行测试
echo $x  # new，因为变量y不存在，所以x=new
```

#### 6、环境变量配置文件

不写入配置文件，变量只是临时生效。比如： `PATH="$PATH":/root`可以追加PATH变量的位置，但是只是临时生效。

6.1 简介

- source命令

作用：默认修改了配置文件需要注销用户重新登录，`source`命令可以取代这个过程。

使用：`source config_file` OR `. config_file`

- 系统变量配置文件简介

系统变量配置文件主要是定义对系统的操作环境生效的系统默认环境变量，比如：PATH、 HISTSIZE、 PS1、 HOSTNAME、等默认环境变量（通过`set`命令可以查看）。主要配置文件如下：

```sh
/etc/profile
/etc/profile.d/*.sh
~/.bash_profile
～/.bashrc
/etc/bashrc
# /etc/目录下的配置文件所有用户都可使用；
```

6.2 环境变量配置文件作用

环境变量调用流程图如下（后边的优先级高）：

![系统变量调用流程图](https://leanote.com/api/file/getImage?fileId=5903fb6aab64415b6c004a42)

参考：https://leanote.com/api/file/getImage?fileId=5903fb6aab64415b6c004a42

```sh
# /etc/profile文件的作用：
USER变量：
LOGNAME变量：
MAIL变量：
PATH变量：
HOSTNAME变量：
HISTSIZE变量：
umask：
调用/etc/profile.d/*.sh文件
# 其他配置文件请参考google
```

6.3 其他配置文件和登录信息

- 注销时生效的环境变量配置文件：`.bash_logout`,注销用户时执行的命令；
- 其他配置文件：`~/bash_history`:记录bash命令；默认写入内存，注销时写入此文件，可以通过`history-w`手动写入。
- shell登录信息：

`/etc/issue`:本地终端欢迎（警告）信息；

```sh
\d  # current date;
\s  # OS name;
\l  # 登录的终端号，这个比较常用；
\m  # 硬件体系结构，如i386\i686等；
\n  # 主机名；
\o  # 域名；
\r  # 内核版本；
\t  # 当前系统时间；
\u  # 当前登录用户序列号；
```

`/etc/issue.net`远程登录环境（警告）信息；

```sh
不同于本地终端登录信息，转义字符在/etc/issue.net中不能使用，只能使用纯文本信息；
是否显示此欢迎信息，由ssh配置文件/etc/ssh/sshd_config决定，加入“Banner /etc/issue.net”行才能显示（记得重启ssh服务）
```

> 本地登录和远程登录信息单独设置，好扯！！then，有没有同时生效的方法呢？往下看：

`/etc/motd`**登录后**欢迎信息：不管是远程登录，还是本地登录，都可以显示此欢迎（警告）信息。

### shell编程

#### 1、正在表达式

- linux中正则和通配符的区别

通配符：`? & [] [^ ]` ,匹配符合条件的文件名；是完全匹配；ls、find、cp这些命令不支持正在，只能使用shell自带的通配符。

正在表达式：`* . ^ $ [] [^] \ \{n\} \{n,\} \{n,m\}`，匹配文件中符合条件的字符串；是包含匹配（只要含有条件就匹配）；grep、awk、sed等命令支持正则。

```sh
grep "a*" test_file  # a出现一次or零次，没有任何意义，匹配所有行；
grep "s..d" test_file  # 任意字符；
grep "s.*d" test_file  # 任意字符0-n次；
grep "^M" test_file  # M开头的行
grep "n$" test_file  # n结尾的行
grep "s[aeiou]d" test_file  # 其中一个
grep "s[a-z]d" test_file  # 范围
grep "^[^a-z]d" test_file  # 取反
grep "\.$" test_file  # 转义字符
grep "a\{3,\}" test_file  # 连续出现3个以上a的行
```

#### 2、字符截取命令

grep命令提取匹配的**行**，cut和awk提取匹配的**列**。

2.1 cut字段提取命令

用法：`cut [option] file_name`

`-f 列号field`：提取第几列；

`-d 分隔符delimiter`：按照指定分隔符分隔列；

```sh
# 准备文件file
vim file  
# ------(下表中必须是制表符，才能使用cut命令)
id	name	gender	mark
1	yaro	M	86
2	wyzh	F	90
3	seth	M	77
# -----
cut -f 2 file  # 提取file文件的第二列；
cut -f 2,4 file  # 提取2,4列；
cut -d ":" -f 1,3 /etc/passwd  # 指定分隔符，提取对应的列；
# 使用场景：批量提取新添加的普通测试用户，为后续删除做准备。
cat /etc/passwd | grep /bin/bash | grep -v root | cit -d ":" -f 1
# cut命令通常和grep命令配合使用。
```

> cut命令只能识别tab键，比如`df -h`输出结果（eg. 提取磁盘使用率）使用的是“不确定的空格（一个OR多个）”分隔符。cut命令便不再适用，此时只能使用awk。

2.2 printf命令

语法：`printf '输出类型[输出格式]' 输出内容`

输出类型：

`%ns` ：输出字符串，n指输出几个字符；

`%ni` ：输出整数，n指输出几个数字；

`%m.nf` ：输出浮点数，总共m位数，n个小数位；

输出格式：

`\n` : 换行；

`\r`： 回车；

`\t`：Tab键；

另外还有：`\a`警告音，`\b`退格键（backspace），`\f`清屏，`\v`垂直退格键（TAB）

```sh
printf %s 1 2 3 4 5 6  # 123456，cat命令可以读取文件里面的tab和换行等，printf不能；
printf %s %s %s 1 2 3 4 5 6  # %s%s123456
printf '%s %s %s‘ 1 2 3 4 5 6  # 1 2 34 5 6 ，也可用双引号 
printf '%s %s %s\n‘ 1 2 3 4 5 6  # 1 2 3 \n 4 5 6,有了换行；
# --------
# 准备文件file
vim file  
# ------(下表中必须是制表符，才能使用cut命令)
id	name	gender	mark
1	yaro	M	86
2	wyzh	F	90
3	seth	M	77
# -----
printf '%s' $(cat file)  # 不调整输出格式
# printf不能接收文件名OR管道符，只能这样接收；
printf '%s\t%s\t%s\t%s\n' $(cat file)  # 调整输出格式
```

> printf远没有cat、echo等命令智能，用起来好复杂，但是awk命令需要这个命令。额。。

在awk命令的输出中支持print和printf命令

- print：会在每个输出之后自动加入一个换行符（linux默认没有print命令,只能在awk命令中使用，linux中不能使用）；
- printf：是标准格式输出命令，但是需要自己添加换行符`\n`。

2.3 awk命令

awk命令比cut命令功能强大的多，但是也复杂的多，简单的截取使用cut命令，cut不能完成是在考虑awk。

语法：`awk '条件1{动作1} 条件2{动作2}...' file_name`

`条件（pattern）`：一般使用关系表达式作为条件，如：大于、大于等于..

`动作（action）`：格式化输出，流程控制语句..

```sh
# 准备文件file
vim file  
# ------(下表中必须是制表符，才能使用cut命令)
id	name	gender	mark
1	yaro	M	86
2	wyzh	F	90
3	seth	M	77
# -----
awk '{printf $2 "\t" $6 "\n"}' file  # 没有条件，代表true；$n代表第n列（0代表所有列），逐行读取；因为单引号被awk占用，里面使用双引号；

df -h | awk '{print $1 "\t" $5 "\t" $6}'  # 这里awk可以处理(多个)空格，制表符等，而cut命令就只能处理制表符；print会自动在行尾添加换行，但是只能在awk中使用；

df -h | awk '{print $1 "\t" $5}' | grep sda8 | awk '{printf $2}' | cut -d "%" -f 1  # 提取sda8的磁盘占有率。

awk 'BEGIN{printf "This is a transcript \n"} {print $2 "\t" $3}' file  # 在执行所有数据之前执行BEGIN条件对应的动作；
# 同样也有END条件。

awk '{FS=":"} {print $1 "\t" $3}' /etc/passwd  # 默认awk识别空格和制表符，用FS指定分隔符；但是awk是先读取第一行，再处理（逐行处理），所以第一行不会用分隔符“:”处理。

# 所以应该添加BEGIN条件。so:
awk 'BEGIN{FS=":"} {print $1 "\t" $3}' /etc/passwd # 或者是：
awk -F: '{print $1 "\t" $3}' /etc/passwd  # 缩写版

# 条件中含有条件运算符
cat file | grep -v name | awk '$4>=85{printf $2 "\n"}'  # 看看谁的成绩大于85；
```

> 其实awk可以实现很多东西，甚至函数调用、流程控制等等，它更像一门语言；但是我们它没有shell语言直观、亲切，所以我们主要使用shell语言编程，再shell语言无法实现的时候（如字符截取），再使用awk语言实现即可。

2.4 sed命令

grep和cut、awk都是进行字段（field）截取，而sed是一种几乎所有UNIX平台支持的**轻量级流编辑器**，主要用来进行数据的选取、替换、删除、新增的命令。

vim、nano编辑的只能编辑文件，对于命令的执行结果需要先重定向写入文件后在编辑；但是sed可以用管道符`|`来直接接收命令的输出结果。

平时使用的不多，但是shell脚本中使用的比较多。

语法：`sed [选项] '[动作]' file_name` 当然也可以使用管道符接收命令的结果。

选项：

`-n` ： 一般sed命令会把所有数据都输出到屏幕，添加`-n`后只把经过sed处理的行输出到屏幕；

`-e` ： 允许对输入数据应用多条sed命令编辑；

`-i` ： 用sed的修改结果的同时，写入原文件；

动作：

`a \`:追加行；

`c \`:行替换；

`i \`:插入行；

`d`:删除行；

`p`:打印行；

`s`:字符串替换（类似vim）；

```sh
# 准备文件file
vim file  
# ------(下表中必须是制表符，才能使用cut命令)
id	name	gender	mark
1	yaro	M	86
2	wyzh	F	90
3	seth	M	77
# -----
sed '2p' file  # 打印第二行，且全部行也打印出来，若想只打印第二行，需要加入-n选项；
sed -n '2p' file  # 只打印第二行；
df -h | sed -n '2p'  # 还可以接收命令的输出；
sed '2,4d' file  # 删除第二行到第四行的数据并把剩余行打印，但不修改源文件，加入-i才修改原文件；
# -i 选项修改原文件（貌似使用vim更合适吧），无此选项，只是处理命令的输出。
sed '2a hello' testfile  # 在第二行后面添加hello行；
sed '2i hello \
world' testfile  # 在第二行之前添加hello \world两行；
sed '4c no such person' file  # 把第四行替换成"no such person"
sec '4s/77/99/g' file  #  把第四行的“77”替换成“99”
sec -e '4s/77/99/g; 4s/seth/coco' file   # 同时替换两个内容；
```

#### 3、字符处理命令

3.1 sort排序命令

语法：`sort [options] file_name`

options:

-f：忽略大小写；

-n：以数值类型排序，默认是字符串；

-r：反向排序；

-t：指定分隔符，默认是制表符

-k n[,m]：按照指定的字段范围排序，默认从n到行尾；

```sh
sort /etc/passwd
sort -n -t ":" -k 3,3 /etc/passwd  # 以冒号分隔，按照第三列排序，并且识别为数字；
```

3.2 wc统计命令

```sh
wc /etc/passwd  # 统计line/word/字符(m)；
dh -h | wc  
```

#### 4、条件判断（测试语句）

4.1 按照文件类型进行判断

常用的如下：

```sh
-d # 是否是目录；
-f # 是否是文件；
-e # 是否存在；
-L # 是否是链接(ln)文件；
# refer to:http://www.cnblogs.com/sunyubo/archive/2011/10/17/2282047.html
```

两种判断格式

```sh
# method 1
test -e /root/install.log
# method 2
[ -e /root/install.log ]  # 切记中括号和内容直接必须有空格；

# shell中常用的是method 2，查看结果可以通过下面的语句；
[ -e /root/install.log ]  # 查看是否存在；
echo $?  # 查看上一条命令是否成功，存在输出0，不成功输出其他；
[ -e /root/install.log ] && echo yes || echo no # 貌似比上一条命令更好用；

```

4.2 按照文件权限进行判断

```sh
-r # 是否拥有r权限（ugo有一个r权限即可）；
-w # 是否拥有w权限；
-x # 是否拥有x权限；
-u # 是否拥有SUID权限；
-g # 是否拥有SGID权限；
-k # 是否拥有SBit权限；
```

4.3 按照两个文件进行比较

```sh
file1 -nt file2 # file1 newer than file2 修改时间; 
file1 -ot file2 # file1 older than file2;
file1 -ef file2 # file1 equivalent file file2(硬链接，inode号);
```

4.4 两个整数之间的比较

```sh
integer1 -eq integer2  # integer1 equivalent integer2; 
integer1 -ne integer2  # integer1 no equivalent integer2; 
integer1 -gt integer2  # integer1 greater than integer2; 
integer1 -lt integer2  
integer1 -ge integer2  # integer1 greater or equivalent integer2; 
integer1 -le integer2  
```

4.5 字符串的判断

```sh
-z 字符串  # 字符串是否为空（为空反正true）；
-n 字符串  # 字符串是否为非空（非空反正true）；
字符串1 == 字符串2  # 相等返回true；
字符串1 != 字符串2  
```

4.6 多重条件判断

```sh
判断1 -a 判断2  # 逻辑与and；
判断1 -o 判断2  # or；
!判断1  # 逻辑非；
aa=11  # 赋值aa为11；
[ -n "$aa" -a "$aa" -gt 23 ] && echo yes || echo "no"
```

#### 5、流程控制

5.1 if语句

**单分支if条件语句**

```sh
if [ 条件判断 ];then
	程序
fi
# ------或者
if [ 条件判断 ]
	then
		程序
fi
```

统计某分区磁盘使用率脚本：

```sh
#!/bin/bash
# 统计根分区使用率；
# by author:yaro(mail:ss@163.com)
rate=$(df -h | grep "/dev/sda3" | awk '{print $5}' | cut -d "%" -f 1)  # 取出根分区使用率；

if [ rate -ge 80 ];then
	echo "Warnig! /dev/sda3 if full!"
fi
```

> 将以上脚本加入可定期执行计划即可，执行计划后续介绍。

**双分支if条件语句**

```sh
if [ 条件判断式 ]
	then
		程序1
	else
		程序2
fi
```

备份mysql数据库脚本：

```sh
#!/bin/bash
# backup mysql data;
# author:yaro(mail:xxx)

ntpdate asia.pool.ntp.org &>/dev/null  # 同步系统时间；
date=$(date +%y%m%d)  # 把当前系统时间按照“年月日”格式赋予变量date;
size=$(du -sh /var/lib/mysql)  # 统计数据库大小，并赋予变量size；

if [ -d /tmp/dbbak ]
	then
		echo "Date:$date!" > /tmp/dbbak/dbinfo.txt
		echo "Size:$size!" >> /tmp/dbbak/dbinfo.txt
		cd /tmp/dbbak
		tar -cvf mysql-lib-$date.tar.gz /var/lib/mysql dbinfo.txt &>/dev/null # 压缩这两个文件，不需要输出；
		rm -rf /tmp/dbbak/dbinfo.txt
	else
		mkdir /tmp/dbbak
		echo "Date:$date!" > /tmp/dbbak/dbinfo.txt
		echo "Size:$size!" >> /tmp/dbbak/dbinfo.txt
		cd /tmp/dbbak
		tar -cvf mysql-lib-$date.tar.gz /var/lib/mysql dbinfo.txt &>/dev/null
		rm -rf /tmp/dbbak/dbinfo.txt
```

判断apache是否启动脚本：

```sh
#!/bin/bash
#判断apache是否启动
# author:yaro(mail:xxx)

port=$(nmap -sT 192.168.1.156) | grep tcp | grep http | grep awk '{print $2}'  # 使用nmap工具扫描服务器，并截取apache服务状态，赋予port；
if [ "$port" == "open" ]
	then
		echo "$(date) httpd is ok!" >> /tmp/autostart-acc.log
	else
		/etc/rc.d/init.d/httpd start &>/dev/null
		echo "$(date) restart httpd!!" >> /tmp/autostart-err.log
fi

# 然后将脚本每15min执行一次即可。
```

**多分支if条件语句**

```sh
if [ 条件判断式 ]
	then
		程序
elif
	then
		程序
elif
	then
		程序
# 更多条件...
else
	程序
fi
```

5.2 case语句

```sh
case $变量名 in
	"value1")
		程序1
		;;
	"value2")
		程序2
		;;
	# 更多分支....
	*)
		程序n
		;;
esac
```

```sh
#!/bin/bash
# 判断用户输入
# author:yaro(mail:...)
read -p "Please input yes/no: " -t 30 cho
case $cho in
	"yes")
		echo "Your choose is yes!"
		;;
	"no")
		echo "Your choose is no!"
		;;
	*)
		echo "Your choose is erro"
		;;
esac
```

5.3 for循环

语法1：

```sh
for 变量 in value1 value2 value3 ...
	do
		程序
	done
# 如：----------
#!/bin/bash
# 打印变量
# author:yaro
for i in 1 2 3 4 5
	do
		echo $i
	done
# 再如：----------
#!/bin/bash
# 批量解压缩脚本
# author:yaro
cd /lamp
ls *.tar.gz > ls.log
for i in $(cat ls.log)  # 自动以换行符显示，for识别空格和换行符以及tab等。
	do
		tar -zxf $i &>/dev/null
	done
rm -rf /lamp/ls.log
```

语法2：

```sh
for (( 初始值;循环控制条件;变量变化 ))  # 数学运算必须使用双小括号；
	do
		程序
	done
# 如：----------
#!/bin/bash
# 从1加到100
# author:yaro
s=0
for ((i=1;i<=100;i=i+1))
	do
		s=$(($s+$i))
	done
echo "the sum 1+2+...+100 is: $s"
# 再如：----------
#!/bin/bash
# 批量添加用户
# author:yaro
read -p "输入用户名： " -t 30 name
read -p "输入用户的个数： " -t 30 num
read -p "输入用户的密码： " -t 30 pass
if [ ! -z "$name" -a ! -z "$num" -a ! -z "$pass" ]
	then
		y=$(echo $num | sed 's/[0-9]//g')  # 判断输入的数字，包含的数字替换为空；
			if [ -z "$y" ]  # 如果为空，即为数字；
				then
					for ((i=1;i<=$num;i=i+1))
						do
							/usr/sbin/useradd $name$i &>/dev/null
							echo $pass | /usr/bin/passwd --stdin $name$i &>/dev/null
						done
			fi
fi
```

5.4 while循环和until循环

**while循环**

```sh
while [ 条件判断式 ]
	do
		程序
	done
# 如：----------
#!/bin/bash
# 从1加到100
# author:yaro
i=1
s=0
while [ $i -le 100 ]  # 小于等于100；
	do
		s=$(($s+$i))
		i=$(($i+1))
	done
echo "the sum is: $s"
```

**until循环**

```sh
# 如：----------
#!/bin/bash
# 从1加到100
# author:yaro
i=1
s=0
until [ $i -gt 100 ]  # 大于100；
	do
		s=$(($s+$i))
		i=$(($i+1))
	done
echo "the sum is: $s"
```

> shell编程是“脚本语言”，所见即所得，不需要编译即可执行；相对于c语言、java语言，更简单，当然执行效率较低，不适合大型的程序；只是方便管理员日常维护。

### Linux服务管理

#### 1、服务简介与分类

**服务的分类：**

linux服务=`RPM包安装的服务`（`独立的服务`+`基于xinetd服务`）+`源码包安装的服务`

> xinetd (*extended Internet daemon*)

`独立的服务`：比如apache，一直运行的内存中，响应快；

`基于xinetd服务`：没有运行的内存中，而是由xinetd服务管理，当调用时，需要首先调用xinetd服务，响应慢，但是不会一直占用内存，当然`xinetd服务`本身是`独立的服务`；

**查询已安装的服务**

RPM包安装的服务：`chkconfig --list` 查看服务自启动状态，可以看到所有RPM包安装的服务；

源码包安装的服务：查看服务安装位置，一般是`/usr/local`下；

> SysVinit to Systemd Cheatsheet参考：
>
> https://fedoraproject.org/wiki/SysVinit_to_Systemd_Cheatsheet
>
> https://wiki.archlinux.org/index.php/systemd

**服务的管理**

也就是控制服务的状态：start/stop/restart/status...

#### 2、RPM包安装服务的管理

相关目录如下：

```sh
/etc/init.d/  # 启动脚本位置；
/etc/sysconfig/  # 初始化环境配置文件位置;
/etc/  # 配置文件位置；
/etc/xinetd.conf  # xinetd配置文件；
/etc/xinetd.d/  # 基于xinetd服务的启动脚本；
/var/lib/  # 服务产生的数据放在这里；
/var/log/  # 日志；
```

**独立的服务**

```sh
# 启动：
/etc/init.d/独立服务名 start|stop|status|restart
service 独立服务名 start|stop|status|restart

# 自启动：
chkconfig [--level 2345] httpd on/off  # 默认就是2345；
vim /etc/rc.d/rc.local：  # 添加如下启动命令，这个才是根本，推荐！
service 独立服务名 start
使用ntsysv命令  # redhat系列专有工具；
```

> /etc/init.d/mongod (1)
> /lib/systemd/system/mongod.service (2)

**基于xinetd服务**

```sh
# 随着linux的更新，基于xinetd的服务越来越少，需要先安装xinetd；
# telnet 服务便是基于xinetd的服务，不安全，仅做试验；

# 启动：
vim /etc/xinet.d/telnet  # 修改其中的disable=no，重启xinetd服务即可启动telnet；
netstat -tupln  # 看到23端口便是telnet服务；

# 自启动：
chkconfig telnet on
ntsysv  # redhat系列专有工具；
```

> 但是xinetd服务的启动和自启动是混淆的：启动时便会自启动，自启动时便会启动；

#### 3、源码包安装服务的管理

```sh
# 使用绝对路径启动
/usr/local/apache2/bin/apachectl start|stop  # port:80,这个执行文件的位置需要查看源码包说明。

# 自启动
vim /etc/rc.d/rc.local  # 加入如下内容：
/usr/local/apache2/bin/apachectl start

# 通过软链接让源码包服务被service命令管理
ln -s /usr/local/apache2/bin/apachectl /etc/init.d/apache

# 让源码包服务被chkconfig与ntsysv命令管理自启动；
vim /etc/init.d/apache  # 刚刚的软连接追加如下内容（开头星号不能省）：
# chkconfig: 35 86 76 # 运行级别，启动顺序，关闭顺序，顺序不能和系统/etc/rc.d/里面的顺序重复；
# description:source package apache # 说明内容：随便写；
chkconfig --add apache  # 加入apache服务；

# 不建议将源码包的服务修改成默认的RPM服务。
```

#### 4、服务管理总结

**独立服务**

启动：`/etc/init.d/httpd start` or `service httpd start`

自启动：`/etc/rc.d/rc.local文件中加入启动脚本` or `chkconfig httpd on`

**基于xinetd服务**

启动：`修改/etc/xinetd.d/telnet文件中的disable=no,重启xinetd服务`

自启动：`chkconfig telnet on|off`

**源码包服务**

启动：`/usr/local/apache2/bin/apachectl start`

自启动：`/etc/rc.d/rc.local文件中加入启动脚本`

### Linux系统管理

#### 1、进程管理

**进程查看**

运行的程序or命令便会产生进程，一个程序最少有一个进程；

`ls`命令也会产生进程，只不过释放的太快，无法捕捉；

进程管理的目的：判断服务器健康状态、是否有危险进程、杀死进程（当进程无法正常关闭）；

查看所有进程：`ps aux`（使用BSD操作系统格式） OR `ps -le`(使用linux标准命令格式)；

查看系统健康状态：`top`命令；

查看进程树：`pstree`命令`-p`显示pid，`-u`显示uid；

**进程管理**

杀死进程：

`kill`，默认是`-15`信号（正常关闭），`-1`信号代表重启，`-9`信号代表强制关闭；

`killall [options] [sign] 进程名`，`-i`交互式，询问是否杀死，`-I`忽略进程名大小写；

`pkill [options] [sign] 进程名`，类似与`killall`命令，而且可以使用`-t 终端号`按照终端号踢出用户；如：

```sh
w  # 查看有哪些用户登录；
pkill -9 -t pts/1  # 踢出pts/1用户；
```

#### 2、工作管理

**把程序放入后台**

```sh
tar -zcf etc.tar.gz /etc &  # 后台依然在运行；
top  # 然后ctrl+z，后台暂停；
```

**查看后台的工作**

```sh
jobs  # 查看后台工作，及工作号等；
jobs -l  # 查看PID；
# “+” 代表最近一个放入后台的进程，恢复默认先恢复它；“-”代表第二个放入后台的进程；
```

**恢复进程运行**

```sh
fg %工作号  # 恢复到前台运行,%可以省略；
bg %工作号  # 恢复后台的进程运行,%可以省略；
```

#### 3、系统资源查看

```sh
vmstat 2 3 # 监控系统资源,监听3次，每次间隔2s；
dmesg | grep CPU  # 查看开机时内核自检信息；
free -h  # 查看内存使用状态；
cat /proc/cpuinfo  # 查看cpu信息；
uptime  # 查看运行时间，同top第一行，和w命令第一行；
uname -a  # 查看内核所有信息；
file /bin/ls  # 判断当前系统的位数，任何非shell命令都可以；
lsb_release -a  # 查看系统发行版本；
lsof [-c 字符串] [-u 用户名] [-p PID]  # 列出进程调用or打开的文件，-c 字符串开头的进程；
```

#### 4、系统定时任务

```sh
service crond restart
chkconfig crond on
ps aux | grep crond  # 确保开启进程；

# ------
crontab -e/l/r  # 编辑/列出/删除所有当前用户的定时任务；
# -e 编辑定时任务，其实是编辑/var/spool/cron/yaro下的对应文件；

# 格式
* * * * * 执行的任务  
# 分(0-59) 时(0-23) 天(1-31) 月(1-12) 周(0-7)，0和7都是周日；
# 星号（*）表示"每";
# 逗号（,）表示不连续的时间；
# 杠（-）表示连续的时间范围;
# */n 表示每隔多久执行一次；;
45 22 * * * command  # 每天22:45执行；
0 17 * * 1 command  # 每周117:00执行；
* 17 * * 1 command  # 每周117:00开始，每分钟执行一次；
0 5 1,15 * * command  # 每月1号和15号5:00执行；
40 4 * * 1-5 command  # 每周1到5的4:40执行；
*/10 4 * * * command  # 每天4:00,每隔10min执行；
0 0 1,15 * 1 command  # 每月1号和15号，每周1的00:00都会执行，但是不建议天和周同时出现，很容易让管理员混淆；
#------------
* * * * * /bin/echo "11" >> /tmp/test  # 每分钟写一个"11"；
*/5 * * * * /bin/echo "11" >> /tmp/test  # 每5分钟写一个"11"；
5 5 * * 2 /sbin/shutdown -h now  # 每周二5:05关机；
0 5 1,10,15 * * /root/sh/autobak.sh  # 每月的1,10,15的5:00执行备份脚本；
```

> 执行定时任务备份时，倘若备份文件名中带有时间，不能使用`date +%y%m%d`，必须使用`date +\%y\%m\%d`，百分号必须使用转移符，否则会报错。

### 日志管理

#### 1、 日志管理简介

类似与摄像头，平时用途不大，但是一旦出现问题，十分重要。

> syslog-ng软件包，rsyslog软件包，现在的systemd又有不同的日志系统。
>
> 现在有了 systemd 之后，由于这玩意儿是核心唤醒的，然后又是第一支执行的软件，它可以主动调用 systemd-journald 来协助记载登录文件～ 因此在开机过程中的所有信息，包括启动服务与服务若启动失败的情况等等，都可以直接被记录到 systemd-journald 里头去！
>
> 参考：https://wizardforcel.gitbooks.io/vbird-linux-basic-4e/content/160.html



>  rsyslogd（the **r**ocket-fast **sys**tem for **log** processing）是syslogd的升级版，并兼容syslogd。

**确定服务是否运行**

```sh
ps aux | grep rsyslogd
chkconfig --list | grep rsyslog  # 2345开启；
```

**常见日志的作用**

```sh
/var/log/cron  # 记录了系统定时任务相关日志；
/var/log/cups  # 记录打印信息的日志；
/var/log/dmesg  # 记录了系统在开机时内核自检的信息，同dmesg命令；
/var/log/btmp  # 记录了错误登录的日志。这个文件是二进制的，不能使用vim查看，只能使用lastb命令查看，一旦有人尝试登录系统错误，便可以看到；
/var/log/lastlog  # 记录系统中所有用户最后一次的登录时间。也是二进制文件，只能使用lastlog命令查看；
/var/log/mailog  # 记录邮件信息；
/var/log/message  # 记录系统重要信息的日志。这个日志惠济路linux系统的绝大多数重要信息，一旦系统出现问题，首先检查的就应该是这个文件；
/var/log/secure  # 记录验证和授权方面的信息，只要设置账号和密码的程序都会记录。如系统登录、ssh、su、sudo等等；
/var/log/wtmp  # 永久记录所有用户的登录、注销信息，同时记录系统的启动、重启、关机时间。同样是二进制文件，使用last命令查看；
/var/log/utmp  # 记录当前已经登录的用户信息。这个文件会随着用户的登录和注销而不断变化，只记录当前登录用户的信息。也是二进制文件，使用w、who、users等命令查看；
```

> 除了系统默认的日志外，采用RPM
> 方式安装的系统服务也会默认把日志保存在`/var/log/`目录下，不过这些日志不是有rsyslogd服务来记录和管理的，而是由各个服务使用自己的日志管理文档来记录服务本身的日志。
>
> 当然源码包的日志是我们指定的位置下,如：`/usr/locol/`。

#### 2、 rsyslogd日志服务

日志文件内容包括四列：事件产生的时间、发生事件的服务器的主机名、产生事件的服务器名or程序名、事件具体信息；

rsyslog配置文件：`/etc/rsyslog.conf`,格式：`服务名称.日志等级	日志记录位置`；

#### 3、 日志轮替

场景：针对于apache服务的日志，一个ip为1w的网站，一个月产生的日志文件可能就几百兆，不光造成硬盘资源占用，还导致查看日志文件很困难（大的文本文件打开不易）。

处理：a、日志切割（比如：安装每天切割为一个单独入职），b、轮替（只需要最近30天的日志，之前的可以清空，方便新的日志的记录）

> apache服务本身提供日志的切割，但是不支持日志的轮替。linux本身支持日志的轮替。

**日志文件命名规则**

如果配置文件拥有“dateext”参数，那么日志会使用日期作为日志文件名后缀，如：“secure-20160102”；如果没有“dateext”参数，会自动以此重命名为“secure.1”、"secure.2"。。。

**logrotate日志轮替配置文件**

```sh
vim /etc/logrotate.conf  # 配置文件位置，内容解释如下：
# 里面默认是全局配置，最下面可以指定特殊日志文件的特殊配置；
daily/weekly/monthly  # 日志轮替周期为天/周/月；
rotate 4  # 保留的日志文件的个数为4,0表示没有备份。
compress  # 旧日志是否压缩；
create mode owner group  # 指定新日志的权限、所有者、所属组；
dateext  # 自动为日志轮替文件添加日期后缀
# 其他使用 man logrotate查看详细内容；
```

**把apache日志加入系统的轮替**

RPM包默认会使用linux的日志轮替功能，但是源码包需要手动加入。

```sh
# 网络访问的服务产生的日志很大。
vim /etc/logrotate.conf
/usr/local/apache2/logs/acces_log{
  daily  # 按天记录；
  create  # 日志权限默认；
  rotate 30  # 只保留30天日志；
  dateext
}
# 其实这个类似于crontab定时执行（用户），系统也有类似的一套定时执行系统（一般是在凌晨4-6点）。
```

**logrotate命令**

> 上面实现了日志的轮替，到时间后便会执行日志轮替，但是我们希望马上就能看到日志轮替的效果，怎么实现呢？

```sh
logrotate -v /etc/logrotate.conf  # 详细显示日志的轮替过程，查看日志轮替的状态。修改时间可以查看效果，date -s xxxx；
logrotate -f /etc/logrotate.conf  # 强制现在轮替，便会在/usr/local/apache2/logs/中看到轮替产生的新日志文件。
```

### 启动管理

#### 1、 CentOS 6.3启动管理

**运行级别**

```sh
0 关机；
1 单用户模式（类似win的安全模式，只启动基本服务，用于系统修复）；
2 不完全的命令行模式，不含NFS服务（linux之间的共享服务）；
3 完全的命令行模式，就是标准字符界面；
4 系统保留；
5 图形模式；
6 重启；
# ------
init 0  # 改变运行级别为0，即poweroff,不保存正在运行的程序，不安全；
init 5  # 切换到图形界面；
init 6  # 重启；
runlevel  # 查看运行级别：N 3 ,现在正在3级别中，之前的级别为None；
# -----
vim /etc/inittab  # 修改系统默认运行级别，即开机后进入到哪个级别；
```

> systemd does not use the `/etc/inittab` file.

**系统启动过程**

BIOS - MBR - 加载MBR中的启动引导程序（GRUB） - 加载内核（多系统会选择系统） - 内核解压并自检 - 找到initramfs(/boot/中，提供硬盘驱动，否则无法访问硬盘中的其他驱动) - 建立仿真报目录 - 加载驱动 - 挂载真正系统根目录 - 调用/sbin/init - 调用/etc/init/rcS.conf - 调用 /etc/inittab/ - 传入运行级别/etc/init/rc.conf - 调用/etc/rc.d/rc - 按照运行级别调用/etc/rc[0-6].d - 按照优先级启动和关闭相应脚本 - 启动和关闭/etc/rc.d/rc.local中的程序 - 登录界面 - 输入用户信息 - 进入系统。

参考：http://www.ruanyifeng.com/blog/2013/08/linux_boot_process.html

#### 2、 启动引导程序grub

linux中的第一块硬盘第一个分区为`sda1`,第二块硬盘的第2个分区为`sdb2`;

Grub中的第一块硬盘第一个分区为`hd(0,1)`,第二块硬盘的第2个分区为`hd(1,1)`;

**Grub配置文件**

```sh
vim /boot/grub/grub.conf  # grub配置文件，里面的参数解释如下：
# ------
default=0  # 默认启动第一个系统；
timeout=5  # 等待5s；
splashimage  # 启动界面；
hiddenmenu  # 启动是按上下键，才能显示选择界面，默认隐藏；
root(hd0,0)  # 启动程序的保存分区；
kernel /vmlinuz-2.6.3xxxx  # 定义内核加载时的选项；
initrd /initramfs-2.6.3xxx.img  # 指定initramfs内存文件系统镜像文件的所在位置；
```

> 假如安装win和linux双系统的话，需要先安装windows；因为win的启动引导程序会覆盖linux的引导程序，导致linux无法启动；而linux的grub覆盖win的引导程序后可以重新识别win的引导程序；

**Grub加密与字符界面分辨率调整**

默认在grub界面可以按`e`进入编辑模式，甚至可以破解当前root的密码。

```sh
grub-md5-crypt  # 生成加密密码串，要求输入密码，然后生成加密后的密码串；
vim /boot/grub/grub.conf  # 在splshimage=（hd0,0）xxx行前面，添加密码项：
# ----
password --md5 生成的密码串  # 需要添加的内容；
# ----
# 重启之后便不能输入e编辑，只能输入p，再输入密码才可进入编辑项；

```

“本地”使用服务器时，会出现字符界面分辨率太低的现象，即字体太小。其实我们平时都是使用xshell等客户登录的，所以意义不大。当然确实需要修改的话，百度即可。

参考：http://blog.csdn.net/yutao52shi/article/details/6223340

#### 3、 系统修复模式

**单用户模式**

grub界面按`e` - 进入编辑项 - 选中kernel行再按`e`编辑 - 后面追加`空格 1`选择单用户模式 - 回车 - 按`b`启动系统 - 便可以进入单用户模式（不需要用户名和密码）；

单用户模式作用：a、修改遗忘的root密码：`passwd root`；b、修改系统默认运行级别`vim /etc/inittab`；

**光盘修复模式**

通过进入单用户模式可以修改root密码，好不安全！当然我们可以给grub添加密码限制进入单用户模式，那我们是否可以修复grub密码呢？答案是肯定的，通过光盘修复模式即可。

光盘修复作用：a、修改root密码；b、修改grub密码；c、修复系统；

```sh
# 通过光盘（U盘）启动系统；
# 默认的是光盘的根目录；
ls  # 查看的是光盘的根目录；
chroot /mnt/sysimage  # 挂载并进入真正的硬盘的系统根目录；
ls  # 查看真正的系统根目录；
vim /boot/grub/grub.conf  # 便可以删除掉grub的密码；
passwd root  # 也可以修改root密码，额！！；
cd /root  
# --加入系统某个文件损坏无法启动，比如/etc/inittab损坏，修复如下：
rpm -qf /etc/inittab  # 查询/etc/inittab文件属于哪个包,比如是initscripts-xxx包；
mkdir /mnt/cdrom  # 为光盘建立挂载点，之前已经进入到硬盘根目录了；
mount /dev/sr0 /mnt/cdrom  # 挂载光盘；
rpm2cpio /mnt/cdrom/Packages/initscripts-xxx | cpio -idv ./etc/inittab  # 提取包里的文件，复制到指定的目录即可。
```

**linux的安全性**

- 用户密码：单用户模式可以破解；
- grub密码：光盘修复模式可以破解；
- bios加密：拔出主板电池（每个主板上都有个电池）；
- 锁起来：螺丝刀撬锁；

貌似咋看都不安全呢。。

其实我们所说的安全是指网络安全；既然电脑本身是我的，我就拥有绝对的控制权；所以以上的这些”后门“是linux系统故意预留的。

其实所有的系统都有这样的”破解后门“，包括windows、路由器、交换机等等，否则密码忘记，难道只能把电脑扔了！！？？

### 备份与恢复

**linux中需要备份的数据**

```sh
# 系统文件
/root/目录；
/home/目录；
/var/spool/mail/目录；
/etc/目录；
其他目录（/var/log/等等）；

# 安装的服务数据
apache需要备份的数据：配置文件、网页主目录、日志文件
mysql需要备份的数据：1、源码包（`/usr/local/mysql/date/`），2、repo包（`/var/lib/mysql`）
```

**备份策略**

完全备份：例如：备份整个目录、分区、硬盘、服务器；但需要的存储设备更大、备份时间更长、耗费系统资源(类似与find命令)。

增量备份：第一次完全备份，以后只备份"与前一次相比"新增加的数据；但是恢复起来就比较麻烦了（先恢复完全备份，然后恢复每次的增量备份）。

差异备份：第一次完全备份，以后只备份"与第一次完全备份的数据相比"增加的数据;带来的好处有限。

**dump和restore命令**

假如我们只是简单的备份，只需要使用tar命令打包，然后cp到相应位置，或者使用crontab定时执行即可备份脚本。但是若实现增量备份的话，脚本实现起来就很麻烦。这就需要系统提供的dump备份命令和restore恢复命令。

dump语法：`dump [option] 备份之后的文件名 源文件or目录`

> -level  ：就是我们说的0-9是个备份级别（-0代表完全备份，-1代表第一次增量备份...，只有分区才支持增量备份，文件or目录只支持完全备份）；
>
> -f 文件名 ：指定备份之后的文件名；
>
> -u ：备份成功之后，把备份的时间记录在/etc/dumpdates文件，一般都使用；
>
> -v ：显示备份过程的详细输出信息；
>
> -j ：调用bzlib库压缩备份文件，其实就是把备份文件压缩为.bz2格式，一般都使用；
>
> -W ：查询各个分区的备份时间及备份级别；

```sh
# 备份/boot分区
dump -0uj -f /root/boot.bak.bz2 /boot/  # 完全备份，记录时间，压缩；
cat /etc/dumpdates  # 查看之前的备份的记录时间；
dump -1uj -f /root/boot.bak1.bz2 /boot/  # 增量备份/boot分区，并压缩；
cat /etc/dumpdates  # 查看之前的备份的记录时间；
dump -W  # 查询各个分区的备份时间及备份级别；
# --------
# 备份文件or目录
dump -0j -f /root/etc.dump.bz2 /etc/  # 完全备份/etc/目录，目录只能使用0级别进行完全备份，而不再支持增量备份；
```

restore语法：`dump [模式选项] [option]`

> 模式选项：常用的模式有四种，不能混用；
>
> -C ：比较备份数据和实际数据的变化；
>
> -i ：进入交互模式，手工选择需要回复的文件；
>
> -t ：查看模式，用户查看备份文件中拥有那些数据；
>
> -r ：还原模式，用于数据还原；
>
> -j ：调用bzlib库压缩备份文件，其实就是把备份文件压缩为.bz2格式，一般都使用；
>
> -W ：查询各个分区的备份时间及备份级别；

```sh
mv /boot/testfile /boot/testfile.bak  # 修改文件，手动创建变化；
restore -C -f /root/boot.bak.bz2  # 比较备份的分区数据和源分区是否有变化；
restore -t -f /root/boot.bak.bz2  # 查看备份压缩包有哪些数据；
# 还原模式-----
mkdir boot_test  # 先创建一个文件夹；
cd boot_test
restore -r -f /root/boot.bak.bz2   # 恢复备份压缩包到当前目录；
restore -r -f /root/boot.bak1.bz2   # 恢复增量备份数据到当前目录；
restore -r -f /root/etc.dump.bz2  # 恢复备份的文件（夹）到当前目录；
```

