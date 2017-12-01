## Server Location

- 提前查看一下最近比较火的vps厂商,这次入了Vultr的坑
- 服务器建议选择日本、新加坡、美国西部城市（洛杉矶、硅谷、西雅图等）
- 服务器的位置多开几个测试一下ping值，ping要求有三点**：1、本机ping值；2、全国各地ping值；3、路由跟踪；4、掉包率；5、不同时段的ping值。**
- 测试ping工具：Best Trace可视化路由追踪、pingchinaz测试全国的ping。

> **再次声明：选择一个好的IP很重要，有时还的靠运气！！！**

- Linux的分区

分区参考如下：

> boot分区200M，防止磁盘写满无法启动系统
> swap分区内存两倍，上限4G-8G，根据内存酌情设置
> /根分区，剩余的磁盘空间都给`/`分区即可，倘若服务器用于上传下载，可以单独设置home分区

倘若不能界面划分swap分区，需要命令行设置，参考：[Setup swap file on linux](https://www.vultr.com/docs/setup-swap-file-on-linux)



## SSH连接

- Debian安装时记得勾选ssh服务，否则的话安装后需要apt-get install ssh
- 添加源（/etc/apt/sources.list）：

``` sh
deb http://ftp.us.debian.org/debian jessie main non-free contrib
deb-src http://ftp.us.debian.org/debian jessie main non-free contrib
deb http://ftp.us.debian.org/debian jessie-updates main contrib non-free
deb-src http://ftp.us.debian.org/debian jessie-updates main contrib non-free
```
> 将上面URL中的`ftp.debian.org`替换成就近的[mirror](https://www.debian.org/mirror/list)
>

- root用户登录，安装sudo，使用一般用户登录VPS
- 一般用户要想使用sudo，还需要在/etc/sudoers文件中添加当前用户，记得强制保存`w!`，


## 虚拟机网络设置

VPS的网络要是正常的话，不需要设置即可使用。虚拟lnux系统的话，网络设置如下：

- VirtualBox全局设定：1、NAT网络标签无设置；2、 仅主机（Host-Only）网络添加 “VirtualBox Host-Only Ethernet Adapter”，  设置IP地址和网络掩码（关闭DHCP服务器，即动态获取ip服务器）
- 特定虚拟机网络设置：网卡链接方式设置为“桥连网卡Bridged Adapter”
- 进入Debian系统，配置网络为静态ip，按照下面的方式设置IP和DNS。

```sh
#修改网络配置
vi /etc/network/interfaces
auto eth0
iface eth0 inet static
address 192.168.0.120
gateway 192.168.0.1
netmask 255.255.255.0
#修改dns服务器
vi /etc/resolv.conf
nameserver 223.5.5.5
nameserver 223.6.6.6
#重启服务
sudo /etc/init.d/networking restart
#上面的设置，除了IP以外，其他要和主机上的设置保持一致。主机网络配置需要具体去看。
```

## 开启TCP BBR拥塞控制算法

BBR 目的是要尽量跑满带宽, 并且尽量不要有排队的情况, 效果并不比速锐差，Linux kernel 4.9+ 已支持 tcp_bbr。

具体参考：https://github.com/iMeiji/shadowsocks_install/wiki/%E5%BC%80%E5%90%AFTCP-BBR%E6%8B%A5%E5%A1%9E%E6%8E%A7%E5%88%B6%E7%AE%97%E6%B3%95


## 安装常用软件

```sh
#切记修改sources.list源文件
apt-get update #更新源
apt-get upgrade #更新软件
vim sudo lrzsz mlocate tmux curl | 可选：tree 
```

- 在安装过程中提示`dpkg-reconfigure tzdata`更新当前时区。

配置vim，

```sh
vim .vimrc
syntax on                                                                                  
set showmatch #匹配括号
set cursorline #高亮行
set nu
```



## 查看系统信息

```sh
#系统
uname -a               # 查看内核/操作系统/CPU信息
cat /proc/version	   # 查看内核/操作系统/CPU信息
lsb_release -a		   #查看linux版本
cat /proc/cpuinfo      # 查看CPU信息
hostname               # 查看计算机名
env                    # 查看环境变量
#硬盘/资源
free -h                # 查看内存使用量和交换区使用量
df -h                  # 查看各分区使用情况（disk file system）
#网络服务
ifconfig               # 查看所有网络接口的属性
iptables -L            # 查看防火墙设置
netstat -lntp          # 查看所有监听端口
netstat -antp          # 查看所有已经建立的连接
```

## 配置Shadowsocks服务

- SS需要同时进行服务器和客户端配置


- 服务器端有很多版本，这里使用libev版本，据说省资源。

  具体安装参考：https://github.com/shadowsocks/shadowsocks/wiki/Ports-and-Clients

- ```json
  {
  "server":"my_server_ip",
  "server_port":8388,
  "local_address": "127.0.0.1",
  "local_port":1080,
  "password":"mypassword",
  "timeout":300,
  "method":"aes-256-cfb",
  }
  ```
  }

- 切记别忘了网站防火墙iptables

  ```sh
  iptables -L #查看防火墙规则列表
  vim /etc/iptables.test.rules #编辑防火墙列表，查看8388端口是否开启
  # 重启vps是防火墙列表生效
  ```

- 优化SS：参考官方说明https://github.com/shadowsocks/shadowsocks/wiki

## LEMP的安装与配置

这里暂时使用一键安装包，等待熟悉后在考虑自己配置（能力暂时不够啊）；

参考文章：
https://oneinstack.com
https://serversforhackers.com/video/lemp-on-debian

### 安装网站CMS

下载cms之后记得**修改网站根目录所有者**（如：`chown www -R /data/wwwroot`），或者是修改权限；不然安装以及使用过程中会因为**读写权限**而出错。



### mysql 基本使用

作为 MySQL 的简单替代品，MariaDB 保证了与 MySQL 的 API 和命令行用法方面最大的兼容性。

查看mysql现在已提供什么存储引擎，及当前默认的存储引擎，MyISAM或者innodb

```mariadb
mysql> show engines;
```

查看performance schema是否开启，及其默认系统变量

```mariadb
SHOW VARIABLES LIKE 'perf%';
SHOW STATUS LIKE ‘perf%’;		#查看performance schema 状态，倘若为0，也标识没有启动；
```



mysql优化参考：https://www.teakki.com/p/57e2285ba16367940da62840

### 添加虚拟机-选项 vhost

直接使用OneStack添加虚拟主机？

```sh
./vhost.sh #添加虚拟机
#Do you want to setup SSL under Nginx? [y/n]: n
#Do you want to add hotlink protection? [y/n]: n
#Allow Rewrite rule? [y/n]:y zblog
./vhost.sh del #删除虚拟机
```

## 网站数据备份及恢复

### 数据备份

- 可以直接使用OneStack的`./backup_set.sh`、`./backup.sh`。

- 也可以手动备份

  - 1、网站备份：打包即可。

  - 2、数据库备份（导出）：`mysqldump -u root -p abc > abc.sql`

    > mysqldump命令是mysql数据库中备份工具，用于将MySQL服务器中的数据库以标准的sql语言的方式导出，并保存到文件中。
    >
    > 来自: [http://man.linuxde.net/mysqldump](http://man.linuxde.net/mysqldump)

### 数据恢复

提前建立好虚拟机（文件夹）及数据库，名字最好一致哈。

- 网站恢复：解压

- 数据库恢复：

  首先创建数据库

  ```sh
  mysql> create database XXX;
  ```

  导入数据库

  ```sh
  mysql -u root -p XXX < xxx.sql #最后为sql文件路径
  ```

### Linux文件传输

- (S)FTP：首先要安装并开启ftp服务，然后通过ftp工具或者命令传输。

- wget/curl：前提是目标主机搭建好LEMP服务器，将目标文件**放在网站目录下**即可。

- scp：scp是secure copy的简写，是linux系统下基于ssh登陆进行安全的远程文件拷贝命令。

  > 当两台LINUX主机之间要互传文件时可使用SCP命令来实现，建立信任关系之后可不输入密码。

  ```sh
  #1、将本地服务器的文件传送到远程服务器。
  scp local_file remote_username@remote_ip:remote_folder # 需要密码
  scp local_file remote_ip:remote_folder  #需要用户名+密码

  #2、将本地服务器的目录传送到远程服务器。
  命令格式：  
  scp -r local_folder remote_username@remote_ip:remote_folder  
  scp -r local_folder remote_ip:remote_folder  

  #3、从远程服务器的文件或目录拷贝到本地服务器。与从本地传送到远程服务器相类似，只是将参数位置互换一下。
  ```



## 服务管理

```sh
# 列出所有配置文件
$ systemctl list-unit-files
# 列出指定类型的配置文件
$ systemctl list-unit-files --type=service
# 查看开机启动的服务
$ systemctl list-unit-files --type=service | grep enabled
#设置开机启动
systemctl disable nginx.service
# 列出所有正在运行的、类型为 service 的 Unit
$ systemctl list-units --type=service
```

service --status-all 可以查看所有的服务状态，service是管理服务状态的，CentOS中chkconfig是管理服务开机启动的，而systemctl的功能包括两者，其实还有更多功能。

**service 命令是调用/etc/init.d/目录下的服务**

**systemctl命令是调用/lib/systemd/system目录下的单元**

