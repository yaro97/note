## linux网络服务管理

网络服务的主要内容：

part one：linux网络设置和远程控制；

part two：linux文件服务器（文件的共享及共享文件权限控制）；

part three：常见的linux服务（服务太多，只是简单的介绍）；

part four：web开发环境搭建与维护（LAMP），收费！！；

### linux网络设置及远程管理

#### 网络基础知识

1、互联网接入方法

- ADSL(非对称数字用户环路)：

  最高上行1Mbps，最高下行8Mbps；最新的ADSL2+技术可以提供24Mbps下行，使得adsl用途更广泛，每月128元（电信）；

  优点：使用电话线，节约布网成本；上网同时可以打电话，节约了电话费；

  缺点：铜材昂贵，带宽限制，动态IP地址（不适合服务器）；

- FTTH（光纤入户）：
  是升级版的ADSL，使用二氧化硅，更便宜，带宽也基本不限制，也是动态IP；

- 小区宽带：

  小区宽带十个一大局域网，所有客户都在同一个网段中。外网接口可以是FTTH，也可以是固定IP的光纤。但是是共享带宽，也不安全，比ADSL更便宜，每月86元（电信），太不靠谱！！

- 固定IP光纤：

  本质是也是光纤，但是IP是固定的，带宽自由申请，价格最贵，每月8000-40000元（电信）。因为IP固定，所以可以搭建企业服务器。

2、OSI/ISO七层模型和TCP/IP四层模型

- OSI/ISO七层模型

只是一个标准，实际中并没有使用，真正使用的是TCP/IP四层模型。

七层：应用层（APDU、用户接口） - 表示层（PPDU、编码、加密） - 会话层（SPDU、是否需要回话还是本地保存） - 传输层（TPDU、TCP还是UDP、传输前错误检测） - 网络层（报文、提供IP地址、路由） - 数据链路层（帧、MAC地址、错误检测） - 物理层（比特、物理接口）；

两个计算机之间的传输：A计算机先把数据传输至最底层（物理层），然后计算机A、B通过物理层（网线）传输，B计算机把数据从物理层传输到应用层，各层之间通过接口传输数据；

- TCP/IP协议四层模型

实际使用中采用的是TCP/IP模型，包括：应用层（FTP、
TELNET、http协议等）、传输层（TCP协议、UDP协议）、网络互联层（ip协议、IGMP协议、ICMP协议）、网络接口层（帧）；

四层与七层的对应关系：应用层（应用层+表示层+会话层）、传输层（传输层）、网络互联层（网络层）、网络接口层（数据链路层+物理层）。

- 比较：

OSI模型是在协议开发前设计的，具有通用性；TCP/IP是现有协议集然后建立模型，不适用于非TCP/IP网络；OSI只是理论模型，TCP/IP是实际中的国际网络模型。

3、网络层协议

网络层协议主要包括：网际协议（IP）、网联网控制报文协议（ICMP）

IP包头为32位（0.0.0.0-255.255.255.255）。

IP地址分类：A类（1-126）、B类（128-191）、C类（192-223）。127网段只有127.0.0.1任何计算机都有，ping这个IP的话只能证明TCP/IP协议没有问题。为了解决IP数量有限的问题，IP分为公网IP和私有IP地址；详细请百度。

#### linux网络基础

1、Linux的IP配置

方法一：ifconfig命令：为网卡添加ip`ifconfig eth0 192.168.3.251`，禁用/启用ip`ifconfig eth0:0 down/up`

方法二：修改网络配置文件:

方法三：setup工具（red hat自带）

方法四：图形界面配置ip地址

2、Linux网络配置文件

网卡信息文件、主机名文件、DNS配置文件；

3、常用网络命令

```sh
ifconfig
ifconfig eth0 192.168.3.251  # 重启就失效；
ifconfig eth0:0 down/up  # 虚拟机/无限网卡/等
hostname  # 查看主机名，也可以更改，也是重启失效；
ifdown/ifup 网卡设备名  # 禁用/启用网卡 同ifconfig lo down/up；
netstat -tuln  # 查看网络连接状态；
netstat -an
netstat -ar
route -n  # 查看路由列表（可以看到网关）；
nslookup  # 查看本机DNS服务器；
nslookup [主机名/IP]  # 进行域名、ip地址解析；
ping -c baidu.com
telnet 192.168.0.252 80  # 端口23，连接远程管理，明文传输（抓包工具），不安全；现在用SSH代替；还可用于端口探测，看看远程对应端口(80/22...)开没有，当然也可以用扫描工具更智能实现；
traceroute -n  # 路由跟踪，-n表示不解析域名，速度更快；
wget http://xxx/xxx.tar.gz  # 下载文件；
```

4、虚拟机网络参数配置

a.设置ip；

b.启动网卡：`/etc/sysconfig/network-scripts/ifcfg-eth0` 把ONBOOT设置为yes；

c.设置虚拟机网络连接方式：

- 桥接（设置简单，与真实机物理网卡通讯，占用局域网IP，ip与真实机IP在同一个网段）；
- NAT（ip与真实机虚拟网卡VMnet8的IP在同一个网段）；
- Host-only（ip与真实机虚拟网卡VMnet1的IP在同一个网段）；

d.修改桥接网卡：当选择桥接时，由于真实机有可能使用有线网卡or无限网卡，所有需要设置桥接网卡；

e.修改UUID（唯一识别符），只有复制虚拟机镜像需要设置（手动安装的话UUID自动生成，每台电脑不可能重复，类似于windows不能使用ghost系统），删除`/etc/sysconfig/network-scripts/ifcfg-eth0`的MAC地址行，删除网卡和MAC地址的绑定文件`rm -rf /etc/udev/rules.d/70-persistent-net.rules`，重启虚拟机。

### SSh远程登录管理

#### 1、ssh简介

ssh（Secure Shell）建立在应用层和传输层基础上的安全协议；

古老的telnet协议是明文传输，不安全，现在都是使用ssh替代telnet(port:23)；

其实ftp(prot:21)也是明文传输，不过危害性要低的多，可以演示ftp的抓包过程：

```sh
# tcpdump是linux的抓包工具；
tcpdump -i eth0 -nnX port 21 # -i指定网卡，-nn用ip地址的方式监听，-X使用16进制解析数据包；
# 然后使用其他客户端登录这个主机的时候，便可以实时查看明文的账号和密码；
```

> 其实：我们平时大多数网络协议都是明文的，包括访问网站，除了https协议，其他都是明文的，好可怕！！
>
> 公共网络不要输入敏感信息哦！！家庭网络相对安全，因为拨号进入公网之后有大量的混淆数据包，被截获的概率较小。

ssh相关信息：

- port：22；
- 守护进程：sshd；
- 安装程序：openssh;
- 服务端主程序：/usr/sbin/sshd;
- 客户端主程序：/usr/bin/ssh;
- 服务端配置文件：/etc/ssh/sshd_config;
- 客户端配置文件：/etc/ssh/ssh_config;

#### 2、ssh加密原理

**对称加密算法**

单秘钥加密：加密、解密使用同一个密码；

非对称加密（公开秘钥加密算法）：每个人都用密码生成自己的“公钥（锁）”和“私钥（钥匙）”；对文件加密时，使用公钥和私钥配合；数据发给其他人时，需要其他（多）人的公钥来加密；其他人也可以从“文件筒”的另一端(使用其私钥)打开加密数据；优点：只需要自己的密码即可，不需要知道别人的密码。

SSH加密：非对称加密初期是针对于文件加密的，SSH是其衍生品。

#### 3、配置文件

客户端配置文件：/etc/ssh/ssh_config;

服务端配置文件：/etc/ssh/sshd_config;

linux本身既可以登录ssh，又可以当做ssh服务器，我们这里主要讲解ssh服务端配置文件；

```sh
# port 22  # 默认就是22端口,建议在服务器端修改端口号；
# ListenAddress 0.0.0.0  # 监听任何ip，适用于一个网卡多个ip的情况；
Protocal 2  # ssh协议选择，第一代ssh协议有漏洞；
# HostKey /etc/ssh/ssh_host_rsa_key # 私钥保存位置；
# ServerKeyBits 1024  # 私钥的位数；
SyslogFacility AUTH  # 启用日志记录SSH登录情况；
LogLevel INFO  # 日志等级，越低记录的越详细；
GSSAPIAuthentication yes  # GSSAPI认证开启，会启用DNS解析IP和主机名，但是又没有
DNSDNS服务器，所以登录要等待一段时间，建议关闭（客户端？）；
PermitRootLogin yes  # 是否允许root的ssh登录，建议关闭，但是可以用普通用户使用 su - 切换root用户，最好使用公钥验证更安全；
Pubkey Authentication yes  # 是否使用公钥验证；
AuthorizedKeysFile .ss/authorized_keys  # 公钥的保存位置；
PasswordAuthentication yes  # 是否允许密码登录，可以使用秘钥登录；
PermitEmptyPasswords no  # 不允许空密码登录；

```

#### 4、常用ssh命令

linux管理linux服务器。

```sh
ssh root@192.168.44.5  # 使用root用户登录，前提允许root登录ssh；
-----
# scp文件传输；
scp root@182.168.44.2:/root/test.txt .  # 下载远程的文件到本地当前目录；
scp -r ./test/ root@182.168.44.2:/root/  # 上传本地当前文件夹到远程的/root/目录； 
----------
# sftp文件传输；
sftp root@182.168.44.2  # sftp文件传输，可用如下命令：
help  # 查看支持的命令；
ls  # 查看服务器数据；
cd
lls  # 查看本地数据；
lcd
get file /root/  # 下载到本地目录；
put  # 上传
```

#### 5、ssh连接工具

putty、SecureCRT（收费！额）、xshell（社区版，推荐！）、WinSCP等工具。

#### 6、密钥对登录

服务既然开启了ssh服务，黑客就可以通过尝试or暴力破解root的密码，如何处理呢？

- 修改了端口：可以使用端口扫描工具；
- 防火墙：只允许某些固定的IP（如：公司ip）登录22端口，但是下班了呢？出差了呢？需要先访问公司ip（端口转发），间接的访问服务器；问题：好复杂，速度慢，不灵活，公司ip一直开机；
- 密钥对登录：不需要密码登录，可以禁用密码登录；只要保护好私钥，在哪儿都能登录（导入私钥库即可）；相对更安全、更灵活；实现如下：

```sh
# 公钥是锁，私钥是钥匙；客户端想要看服务端的数据（请求服务器），服务端用客户端公钥加密；

# 实现原理-----
1. ssh客户机创建密钥对：私钥文件（id_rsa）和公钥文件（id_rsa.pub）;
2. 客户端用户yaro上传公钥文件(id_rsa.pub)到ssh服务器;
3. 导入到服务端用户seth的公钥数据库,公钥库文件：/home/seth/.ssh/authorized_keys # 可以用seth登录服务器ssh；
4. 本地用户yaro以客户端seth的身份进行登录；

# 实现步骤：

Step One--------
# 客户端
ssh-keygen -t rsa  # 指定key的type为rsa，rsa是密钥对的算法；
# 过程中不需要设置密码；
-------
# 服务端
scp id_rsa.pub root@45.25.23.11:/root/  # 先上传 id_rsa.pub 到服务端对应的用户目录下；
cat id_rsa.pub >> /root/.ssh/authorized_keys  # 导入到root用户的公钥数据库；
# .ssh目录没有的话需要创建，authorized_keys文件名绝对不要写错了哦！
# 多个用户管理的话，继续追加公钥即可；
chmod 600 /root/.ssh/authorized_keys  # 默认是644权限，改成600更安全，必须！；

Step Two--------
# 修改服务器端ssh配置文件
RSAAuthentication yes  # 开启RSA验证；
PubkeyAuthentication yes  # 开启公钥验证；
AuthorizedKeyFile .ssh/authorized_keys  # 公钥保存位置 ；
PasswordAuthentication no  # 建议禁用密码登录，记得保存好私钥哦；

Step Three--------
# 服务器关闭SELinux服务,SELinux对系统的服务影响巨大，建议关掉；
vim /etc/selinux/config
SELINUX=disabled  # 禁用SELinux;
reboot  # 重启linux系统生效SELinux；
service sshd restart  # 服务器端重启ssh服务；

Step Four--------
# 其他计算机登录服务器ssh；
1. 把备份好的私钥文件id_rsa拷贝到windows上；
2. 打开xshell新建回话，不使用password，选择pub_key登录；
3. 导入备份的id_rsa即可（生成密钥时无密码），所以这里不需要密码；
# 切记！保存好私钥！！
```



### DHCP服务

DHCP服务器（Dynamic Host Configuration Protocal）.

作用：a、为大量客户机自动分配地址，提供集中管理；b、减轻管理和维护成本、提高网络配置效率；

过程：a、客户端寻找服务器（广播）；b、服务器提供地址信息；c、接收并广播（我已经找到DHCP了）；d、服务器确认；e、客户端重新登录；f、服务器确认。

> 家里的路由器一般都自带DHCP服务，其占用资源很小，所以我们使用RPM包安装DHCP服务即可，没有必要使用源码包安装。

端口号：ipv4(udp67/udp68)、ipv6(udp546/udp547)

服务名：dhcpd

主配置文件：/etc/dhcp/dpcpd.conf (默认为空，可以从模板文件cp过来)

模板文件：/usr/share/doc/dhcp-4.2/dhcpd.conf.sample

DHCP配置文件详解：http://blog.csdn.net/haibusuanyun/article/details/11559173

配置：服务端配置+客户端配置。

### ftp服务

主动模式、被动模式（主流）；

vsftp服务端软件；

参考evernote里面的记录；

### Samba服务

#### 1、samba简介

samba：文件共享服务器，和ftp对比，可以和windows的网上邻居通用，局域网使用比较多；

早期的名称叫做SMB（server message block，==>进程名为smbd），基于IBM的NetBIOS协议（局域网内少数PC通讯）开发，但是SMB无法注册，就取名Samba（桑巴舞）。

Samba的应用：文件共享，打印服务器（很少用，貌似windows更方便），

#### 2、安装

主安装包：samba，客户端：samba-client，通用工具：samba-common，库：samba4-libs 等等。

守护进程：smbd（提供资源共享 端口139/445）、nmbd（提供基于NetBIOS主机名称的解析 端口137/138,提供主机名/网上邻居访问的功能，默认只能ip访问）

启动：service smb/nmb start

#### 3、配置文件

/etc/samba/smb.conf

/etc/samba/lmhosts 对应NetBIOS名与主机ip的文件;

/etc/samba/smbpasswd  samba密码保存文件；

....

#### 4、samba基本使用

修改配置文件；

建立共享目录；

共享文件读写权限最终由NFS系统权限、linux系统权限中较严格的权限决定；

### NFS服务

> 数据共享方法总结：
>
> 1、windows网上邻居：只能局域网使用，只能在windows之间使用；
>
> 2、linux中类似的服务是NFS服务器，常在linux之间使用，可以公网使用；
>
> 3、samba可以实现windows和linux简介的数据共享，局域网使用；
>
> 4、FTP可以跨平台，跨网络使用，但是不能在线修改，只能先下载、修改、再上传。
>
> ssh最安全，但是速度最慢；ftp比ssh（sftp）快，不加密；nfs最快，但是不加密；samba速度挺快，windows使用也方便，但是不加密；
>
> windows网上邻居的特点：图形界面很简单，但是别人可以下载、上传，若上传病毒和密码的话，对windows本身的危害很大。

#### 1、简介

NFS（network file system）,可以让客户端直接把服务器的共享目录挂载到本机使用，配置简单，linux对linux（windows），速度快，但是权限没有samba和ftp明确。

NFS是被RPC服务管理的，所以必须安装RPC（远程调用）的主程序rpcbind。

NFS端口：2049；

RPC端口：111；

NFS daemon端口：随机；

> C访问S的时候先去访问RPC的111端口，而S的所有NFS daemon端口都会在RPC注册，然后RPC把指定的daemon端口告诉C。

#### 2、权限

共享文件读写权限最终由`NFS系统权限`、`linux系统权限`中较严格的权限决定；

#### 3、服务端

NFS主程序：nfs-utils

RPC主程序：rpcbind(旧版本：portmap)

配置文件：/etc/exports  (好难记！)

启动：先启动RPC，service rpcbind start;service nfs start;

守护进程：ps aux | grep -E "nfs|rpc"

> `gpre -E` 等效于 `egrep`(支持扩展的正则，比如 `|` 表示或的意思)
>
> nfsd:NFS守护进程；
>
> rpcbind:RPC守护进程；
>
> rpc.rquotad:NFS配额；
>
> rpc.mountd:处理客户端挂载；

PRC服务注册情况（端口）：`rpcinfo -p [IP或主机名]`

#### 4、配置文件

``` sh
vim /etc/exports 
格式：共享目录 客户端（权限） 客户端（权限）...
/home/yaro *(rw) # 不限制ip，rw权限；
/home/yaro 192.168.44.4(rw) *(ro) #指定的ip读写，其他ip只读；
/home/soft 192.168.44.0/24(rw)  # 指定网段rw权限；
# 24表示24个1，即255.255.255.0.
/home/soft 192.168.44.0/24(rw) 192.168.44.4(rw) 
```

加载配置文件：重启服务（会把正在传输的用户踢掉）or `exportfs -arv`（软重启）。

```sh
exportfs -auv  # 卸载全部目录；
exportfs -arv  # 加载全部目录；
showmount -e  # 查看本机共享（挂载）目录；
```

#### 5、客户端

```sh
service rpcbind start  # 客户端需要启动rpcbind；
showmount -e 192.168.44.2  # 查看服务端共享目录；
# 记得关闭防火墙哦。
----
# 把服务器共享目录挂载到本地；
mkdir /home/client
mount -t nfs 192.168.44.2:/home/soft /home/client
mount  # 查看挂载；
umount /home/client  # 卸载
```

### DNS服务

DNS（domain name system）：因为ip不容易记忆，通过URL来记忆；

正向解析：域名到IP；  
反向解析：IP到域名；

> 发件人发垃圾邮件时，会购买动态ip服务器，但是若想在发信时显示为域名，就需要额外的购买域名费用；所以大多数垃圾邮件的`发件人`一般是ip地址，即，没有反向解析为域名。

域名：xdl.com  
主机名：www.xdl.com(FQDN名称)

**发展过程：**

- 第一阶段：通过文件维护：类似于/etc/hosts;
- 第二阶段：DNS服务器，只需要把dns指向服务器即可，服务器压力好大；
- 第三阶段：分布式服务器，主服务器和下级服务器数据同步时间差，管理复杂；

**域名结构**：根域名`.` - 一级域名`.com` - 二级域名`.com.cn` - 三级域名`sina.com.cn` - 主机名`www.sina.com.cn`

**解析过程**：

递归查询：1、查找hosts； 2、没有的话查找网络里面设置的DNS服务器（查找自己的数据库/缓存）；3、找不到的话自动向其他dns服务转发请求。特点：客户机等待，压力在服务器。

迭代查询：1、访问www.baidu.com，查找hosts；2、询问设置的dns服务器；3、dns查不到的话，告诉我们`.`根dns服务器的地址；4、根dns服务器告诉`.com`服务器的地址；5、然后查找`baidu.com`DNS服务器的地址。特点：压力在客户端，根DNS服务器压力好大。

> DNS服务器默认开启递归查询的，如果压力太大，可以考虑关闭。
>
> 根DNS服务器全球有13台，美国10台，欧洲2台，日本1台；根DNS不支持递归查询。

**DNS实现：**

通过`BIND`软件可以实现DNS服务。

软件名：bind；  
服务名：named；  
端口：53；  

bind软件配置：

- 修改主配置文件（软件的基本设置）；
- 修改区域文件（DNS服务器为哪个区域服务）；
- 修改解析数据文件（主机名和IP的对应关系）；

```sh
iptables -F  # 关掉防火墙；
setenforce   # 清理selinux；
yum -y install bind
vim /etc/named.conf  # 主配置文件；
----
# 详细配置请参考google；
----
vim /etc/named.rfc1913.zones  # 区域配置文件；
----
# 详细配置请参考google；
----
cp -p /etc/named.localhost /etc/xdl.localhost  # 正向解析数据文件；
cp -p /etc/named.empt /etc/xdl.empty  # 反向解析数据文件；
vim /etc/xdl.localhost  # 解析数据文件；
vim /etc/xdl.empty  # ；
----
# 详细配置请参考google；
----

# 测试解析
nslookup
>www.baiduc.om   # 测试正向解析；
>61.135.169.121  # 测试反向解析；
```

### Postfix邮件服务

#### 1、常见邮件服务器：

Sendmail：古老，linux默认支持的，只有一个二进制文件，需要设置SID，配置文件复杂，适合老用户；

Qmail：体积小，模块化设置，功能齐全，配置更加简单，用户也不少，但社区很多年没有更新了，对新技术支持不是太好，最好懂一些编程，能够自助更新些东西；

Postfix：最早是Sendmail里面的组件，后期独立，解决了Sendmail的确定，优点多多，比Sendmail提升不少。

-----------以上是三大开源邮件软件

商业软件也有：

Exchange：微软开发的，必须运行在windows；

Notes/Domino:必须运行在IBM服务器，IBM服务器已经退出中国市场。；

Coremail：国内的商业软件，性价比比Exchange好点，不局限于windows。

#### 2、相关理论

**邮件系统角色**

MUA（邮件用户代理）：foxmail；

MTA（邮件传输代理）：postfix;

MDA（邮件分发代理）：集成到MTA了；

MRA（邮件检索代理）：负责帮用户在服务器检索有无自己的邮件，并返回给用户；

**邮件应用协议**

SMTP：简单邮件传输协议，发送方使用的协议，TCP25端口，加密使用TCP465端口；

POP3：邮局协议3，收件时使用的协议，TCP110端口，加密使用995端口，先从服务器下载相应邮件，在本地操作；

IMAP4，互联网消息访问协议，收件时使用的协议，TCP143端口，加密时使用993端口，客户端与服务器交互，对服务器压力更大；

**邮件收发流程**

参考：http://blog.sina.com.cn/s/blog_98452b2b0101ee39.html

![](http://s3.sinaimg.cn/large/001rmKWozy6IFHw3hlg32&690)

#### 3、postfix实现

配置DNS服务器；

配置postfix；

使用dovecot收信；

Extmail邮件服务器实现web版的邮件（类似163），底层是postfix；

搭建web服务器（apache）；

### Rsync

#### 1、简介

`cp dd tar dump` 等命令都可以实现本地（分区之间的）备份，但是本地备份有自己的缺陷。

`samba ftp nfs ssh` 等服务可以实现远程备份，但是需要自己手动备份。

当然我们可以通过计划任务`crontab`来实现定时自动备份。

但是假如生产环境下，我们需要备份的数据有2G，甚至2T，如何实现：**远程备份、实时备份**，这时就需要`rsync`来实现。

Rsync：用于取代rcp工具，通过rsync算法实现数据对比、增量备份，是一个快速增量备份工具，Remote Sync，远程同步，支持本地复制，或者与其他ssh、rsync主机同步，官网：http://rsync.samba.com。

**rsync实现的是增量备份，需要配合inotify实现实时备份；rsync是单向备份，需要配合unison实现双向备份。**

#### 2、特点

能更新整个目录、树、文件系统；

可以有选择的保持符号链接、硬链接、文件属性、权限、设备以及时间等；

等于安装来说， 无任何特殊权限要求；

能使用rsh、ssh或直接端口作为传输的端口；

支持匿名rsync同步文件，是理想的镜像工具；

#### 3、同步源和发起端

客户端=发起端,服务器=同步源；

有两种同步源：基于ssh的同步源、基于rsync的同步源；

#### 4、基于ssh同步源实现

场景：服务器A上的网站目录备份到另一台服务器B；

```sh
# 首先服务器A创建yaro用户；
useradd yaro
passwd yaro
---------------
# 服务器B执行下行同步，A到B；
rsync -avz yaro@192.168.2.a:/var/www/html/* /backup/  # -a递归保留对象所有属性；-v详细过程；-z压缩提高传输效率；
---------------
# 服务器B执行上行同步；
## 在服务器A执行：
setfacl -m u:yaro:rwx /var/www/html/  # 首先在服务器A上给yaro用户写权限，用chmod和chown不安全。
## 在服务器B上新建文件
touch /backup/B.txt  # 新建测试文件B.txt
rsync -avz /backup/ yaro@192.168.2.a:/var/www/html/*   # 上行同步，B到A；
```

> ssh同步源缺点：需要添加特定的用户。但是运维的原则是：尽量少用多余的用户，否则会不安全。

#### 5、基于rsync同步源实现

```sh
服务端A操作如下
========
vim /etc/rsyncd.conf  # 手动创建rsyncd.conf文件,内容如下：
-----
address = 192.168.12.1  # 当前ip；
port 873
pid file = /var/run/rsyncd.pid
log file = /var/log/rsyncd.log

[share]
	comment = soft
	path = /server/rsync
	read only = yes  # 这里yes的话，客户端B只能下行备份，不能上行，改成no便可以上行和下行备份；
	dont compress = *.gz *.bz2 *.zip
	auth users = wang  # 指定虚拟用户，不需要为服务器B创建新用户；
	secrets file = /etc/rsyncd_user.db
----

vim /etc/rsyncd_user.db# 手动创建rsyncd.conf文件,内容如下：
---
wang:123456
---
chmod 600 /etc/rsyncd_user.db  # 密码文件权限必须600；

rsync --daemon  # 启动服务，这是xinet托管的小服务；
netstat -tuln | grep rsync  # 看看有没有83端口；

客户端B同步如下
============
rsync -avz wang@192.168.2.a::share /var/www/html/* /backup/  # 使用share虚拟用户同步；
rsync -avz  /backup/  wang@192.168.2.a::share /var/www/html/*  # 上行同步；
```

> 注意事项：1、密码文件权限必须600；2、上行同步时，nobody需要有写入权限；

#### 6、免密码验证

我们希望自动同步，没必要还得输入密码，这是就需要密钥对了（类似ssh免密码登录）。

```sh
# ssh同步源免密码；
ssh-keygen -t rsa
ssh-copy-id yaro@192.168.2.a  # 将公钥上传至服务器的yaro账号家目录，这时ssh连接服务器A，或者同步都不需要么密码了。

# rsync同步源免密码；
echo $RSYNC_PASSWORD  # 自带这个变量，默认为空，只需把密码复制给这个变量即可；
export RSYNC_PASSWORD=123456  # 现在就可以免密码了；
```

#### 7、inotify实现实时同步

Rsync只能实现增量同步，不能实时监控文件变化，实时同步，可以通过inotify实现，具体请google。

#### 8、unsion实现双向同步

场景：服务器A的a目录，客户端B的b目录；我们上面都实现了a到b的同步，或者b到a的同步，如何实现二者双向同步呢？

服务器A的公钥传给B，服务器B的公钥传给A，实现免密码；

具体请google。

