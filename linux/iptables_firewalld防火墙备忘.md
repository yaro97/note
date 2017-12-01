# iptables_firewalld防火墙

[TOC]

关键词：iptables firewalld CentOS7 防火墙

参考：
- http://www.firewalld.org/documentation/man-pages/firewall-cmd.html
- http://www.linuxprobe.com/chapter-08.html  
- https://www.ibm.com/developerworks/cn/linux/1507_caojh/index.html  
- http://seanlook.com/2014/02/23/iptables-understand/  

## 概述

Netfilter是由Rusty Russell提出的Linux 2.4内核防火墙框架，该框架既简洁又灵活，可实现安全策略应用中的许多功能，如数据包过滤、数据包处理、地址伪装、透明代理、动态网络地址转换(Network Address Translation，NAT)，以及基于用户及媒体访问控制(Media Access Control，MAC)地址的过滤和基于状态的过滤、包速率限制等。

Netfilter 平台中制定了数据包的五个挂载点（Hook Point，我们可以理解为回调函数点，数据包到达这些位置的时候会主动调用我们的函数，使我们有机会能在数据包路由的时候改变它们的方向、内容），这5个挂载点分别是PRE_ROUTING、INPUT、OUTPUT、FORWARD、POST_ROUTING。

Netfilter 所设置的规则是存放在内核内存中的，而 iptables 和 firewalld 仅仅是一个应用层的应用程序，它通过 Netfilter 放出的接口来对存放在内核内存中的 XXtables（Netfilter的配置表）进行修改。这个XXtables由表tables、链chains、规则rules组成，iptables和firewalld在应用层负责修改这个规则文件。

> 在 Linux 历史上已经使用过的防火墙工具包括：ipfwadm、ipchains、iptables。在 Firewalld 中新引入了区域（Zones）这个概念。

![Netfilter和iptables/firewalld的关系](http://sean-images.qiniudn.com/iptables-netfilter.png)

## iptables

### iptables简介

Iptable 的前身 ipchains 增加规则链的概念；iptable 则将概念扩展为表。所以 iptable 的结构是：iptables > tables > chains > rules。

iptable 具有四个内置表：

- Filter 表：默认表，具有如下链：
    - INPUT 用于传到本地服务器的包。
    - OUTPUT 用于本地生成以及传出本地服务器的包。
    - FORWARD 用于通过本地服务器路由的包。
- NAT 表（网络地址转换）：
    - PREROUTING：用于目的 NAT，它在路由前更改包 IP 地址。
    - POSTROUTING：用于源 NAT，它在路由前更改包 IP 地址。
    - OUTPUT：用于防火墙上本地生成包的 NAT。
- Mangle 表：用于特定包的更改：
    - PREROUTING
    - OUTPUT
    - FORWARD
    - INPUT
    - POSTROUTING
- Raw 表：用于配置免除：
    - PREROUTING
    - OUTPUT

好吧，我承认有点复杂，有个概念即可，我们平时使用最多的就是Filter表（控制流量），然后Filter里面的三个链我们这最关心的当然是INPUT链了（防火墙主要是控制别人的入侵，即input流量）。如此，我们主要讨论Filter表的INPUT链。

### iptable编写规则

![iptable命令格式](http://sean-images.qiniudn.com/iptables-cli.png)

```sh
[-t 表名]：该规则所操作的哪个表，可以使用filter、nat等，如果没有指定则默认为filter

-A：新增一条规则，到该规则链列表的最后一行
-I：插入一条规则，原本该位置上的规则会往后顺序移动，没有指定编号则为1
-D：从规则链中删除一条规则，要么输入完整的规则，或者指定规则编号加以删除
-R：替换某条规则，规则替换不会改变顺序，而且必须指定编号。
-P：设置某条规则链的默认动作
-nL：-L、-n，查看当前运行的防火墙规则列表

chain名：指定规则表的哪个链，如INPUT、OUPUT、FORWARD、PREROUTING等

[规则编号]：插入、删除、替换规则时用，--line-numbers显示号码

[-i|o 网卡名称]：i是指定数据包从哪块网卡进入，o是指定数据包从哪块网卡输出
[-p 协议类型]：可以指定规则应用的协议，包含tcp、udp和icmp等
[-s 源IP地址]：源主机的IP地址或子网地址
[--sport 源端口号]：数据包的IP的源端口号
[-d目标IP地址]：目标主机的IP地址或子网地址
[--dport目标端口号]：数据包的IP的目标端口号
-m：extend matches，这个选项用于提供更多的匹配参数，如：
-m state –state ESTABLISHED,RELATED
-m tcp –dport 22
-m multiport –dports 80,8080
-m icmp –icmp-type 8

<-j 动作>：处理数据包的动作，包括ACCEPT、DROP、REJECT等
```

### iptable实例

注意事项：

- iptables自上而下执行，遇到规则即执行，忽略后续的规则；没有匹配到规则，便会执行默认规则（策略）；so，记得把允许的规则插入(I)到上面，禁止的附加(A)到后面，否则可能造成后面的规则失效；  
- 在设置之前一定要想好，千万别把自己的封了，然后你就没法操作服务器了，OMG！  

a、查看、添加、删除规则

```sh
iptables -nL
# 查看规则列表，默认是：-t filter

iptables -FORWARD
# 清空规则；

service iptables save
# 以下命令临时生效，重启清零，执行此命令永久生效；

iptables -P INPUT DROP
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
# 设置默认的策略（Policy） ，默认是允许，这里把INPUT链设置为默认拒绝；

iptables -I INPUT 1 -m state --state RELATED,ESTABLISHED -j ACCEPT
# 在INPUT链第一天插入，-m state 扩展匹配state，状态为RELATED,ESTABLISHED的放行，在默认DROP的情况下，可以保命；

iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
# 在input链最后追加，所有新建连接，tcp协议，目标端口为22，允许，不安全，默认。

iptables -A INPUT -s 192.168.1.100 -j ACCEPT
# 接受来自指定IP地址的流入数据包：

iptables -A INPUT --dport 80 -j ACCEPT
# 只接收来自指定端口（服务）的数据包

iptables -A FORWARD -p tcp -d 192.168.1.100-dport smtp -i eth0 -j ACCEPT
# 允许转发所有到本地SMTP服务器的数据包

iptables -A FORWARD -p tcp -d 192.168.1.100-dport www -I eth0 -j REJECT
# 拒绝法网www服务器的请求包

iptables -A INPUT -p tcp -m multiport -dport 21,53,80,25,110 -j ACCEPT
# 允许目的地为指定端口的TCP数据包进入

iptables -A INPUT -p tcp -m multiport -sport 21,53,80,25,110 -j ACCEPT
# 允许来源为指定端口的TCP数据包进入：

iptables -A INPUT -s 172.29.73.0/24 -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
# 访问source为172.29.73.0/24的访问，允许；限制指定IP范围能SSH，可取；

iptables -A INPUT -s 10.30.0.0/16 -p tcp -m tcp -m multiport --dports 80,443 -j ACCEPT
# 允许一个ip段访问多个端口；

iptables -A INPUT -s 10.30.26.0/24 -p tcp -m tcp --dport 80 -j DROP
# 禁止某IP段访问80端口，将-j DROP改成 -j REJECT --reject-with icmp-host-prohibited作用相同。
# reject是拒绝并返回拒绝信息；drop是直接放弃，无视。

iptables -I INPUT 3 -s 172.29.73.23 -j ACCEPT
# 第三行插入，完全信任一台主机，尽量不要使用；

iptables -I INPUT 2 -i lo -j ACCEPT
# interface允许loopback。回环接口是一个主机内部发送和接收数据的虚拟设备接口，应该放行所有数据包。

iptables -A INPUT -p icmp -j ACCEPT
接受icmp数据包，可以ping。也可以设置只允许某个特定的IP。

iptables -A INPUT -j DROP
# 这条规则放在最后，当INPUT链默认没有拒绝，前面所有的规则都没匹配时，自然落到这个DROP上；

iptables -nL --line-number
# 显示每条规则链的编号

iptables -D FORWARD 2
# 删除FORWARD链的第2条规则，编号由上一条得知，默认是-t Filter。如果删除的是nat表中的链，记得带上-t nat；

iptables -D INPUT -j REJECT --reject-with icmp-host-prohibited
# 删除规则的第二种方法，所有选项要与要删除的规则都相同才能删除，否则提示错误；

iptables -A INPUT -m state –state INVALID -j DROP
iptables -A OUTPUT -m state –state INVALID -j DROP
iptables-A FORWARD -m state –state INVALID -j DROP
# 丢弃非法连接

iptables -A INPUT -p tcp -m limit --limit 200/second
iptables -A INPUT -p tcp -m limit --limit 10000/minute
iptables -A INPUT -p tcp -m limit --limit-burst200
# 流量限制

iptables -A INPUT -p icmp --icmp-type 8 -s 0/0 -d 192.168.1.132 -m state --state NEW,ESTABLISHED,RELATED -j DROP
iptables -A INPUT --protocol icmp --in-interface enp0s8 -j DROP
# 禁止ping，两条命令效果类似， Zero (0) is for echo-reply，Eight (8) is for echo-request；

```

b、端口转发

首先要开启端口转发器必须先修改内核运行参数ip_forward,打开转发:

```sh
# echo 1 > /proc/sys/net/ipv4/ip_forward   //此方法临时生效
或
# vi /ect/sysctl.conf                      //此方法永久生效
# sysctl -p
```

```sh
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 8080
# 把本地80端口转发到8080端口，放行时，应该放行8080端口；
```

其他情况，请google。

## firewalld

### firewalld简介

RHEL7已经默认使用firewalld了，firewalld 提供了支持网络 / 防火墙区域 (zone) 定义网络链接以及接口安全等级的动态防火墙管理工具。它支持 IPv4, IPv6 防火墙设置以及以太网桥接，并且拥有运行时配置和永久配置选项。它也支持允许服务或者应用程序直接添加防火墙规则的接口。以前的 iptables 防火墙是静态的，每次修改都要求防火墙完全重启。这个过程包括内核 netfilter 防火墙模块的卸载和新配置所需模块的装载等。而模块的卸载将会破坏状态防火墙和确立的连接。

firewalld可以使用命令行工具firewall-cmd 或 GUI工具firewall-config来管理，这里只介绍cli命令行工具；

iptables 服务在 /etc/sysconfig/iptables 中储存配置，而 firewalld 将配置储存在 /usr/lib/firewalld/（系统） 和 /etc/firewalld/（用户） 中的各种 XML 文件里，如果需要，建议只更改/etc/firewalld/里面的内容； 

firewalld的zone概念通俗来说：你在home的时候，可以放宽流量限制；在public的时候，应该严格控制流量。。。

### firewalld默认区域：

```sh
trusted     允许所有的数据包。
home        拒绝流入的数据包，除非与输出流量数据包相关或是ssh,mdns,ipp-client,samba-client与dhcpv6-client服务则允许。
internal   等同于home区域
work        拒绝流入的数据包，除非与输出流量数据包相关或是ssh,ipp-client与dhcpv6-client服务则允许。
public      拒绝流入的数据包，除非与输出流量数据包相关或是ssh,dhcpv6-client服务则允许。
external    拒绝流入的数据包，除非与输出流量数据包相关或是ssh服务则允许。
dmz          （Demilitarized Zone非军事区、隔离区、对外网络、边界网络）拒绝流入的数据包，除非与输出流量数据包相关或是ssh服务则允许。
block       拒绝流入的数据包，除非与输出流量数据包相关。
drop        拒绝流入的数据包，除非与输出流量数据包相关。
```

当然我们还可以自定义区域，具体用法请google。

### firewall-cmd命令常用参数：

```sh
--get-default-zone  查询默认的区域名称。  
--set-default-zone=<区域名称>   设置默认的区域，永久生效。  
--get-zones 显示可用的区域。  
--get-services  显示预先定义的服务。  
--get-active-zones  显示当前正在使用的区域与网卡名称。  
--add-source=   将来源于此IP或子网的流量导向指定的区域。  
--remove-source=    不再将此IP或子网的流量导向某个指定区域。  
--add-interface=<网卡名称>  将来自于该网卡的所有流量都导向某个指定区域。  
--change-interface=<网卡名称>   将某个网卡与区域做关联。  
--list-all  显示当前区域的网卡配置参数，资源，端口以及服务等信息。  
--list-all-zones    显示所有区域的网卡配置参数，资源，端口以及服务等信息。  
--add-service=<服务名> 设置默认区域允许该服务的流量。  
--add-port=<端口号/协议> 允许默认区域允许该端口的流量。  
--remove-service=<服务名>  设置默认区域不再允许该服务的流量。  
--remove-port=<端口号/协议>  允许默认区域不再允许该端口的流量。  
--permanent 以上设置只是立即（临时）生效，重启失效，使用此参数，代表永久生效（写入配置文件），临时不生效；
--reload    让“永久生效”的配置规则立即生效，覆盖当前的。  
```

### firewall-cmd实例：

```sh
firewall-cmd --get-target --permanent
# 查看当前区域（默认public）的默认target， target is one of: default, ACCEPT, DROP, REJECT。默认是default，及默认区域预先介绍的相关内容。

firewall-cmd --get-zones
# 查看支持的zones；

firewall-cmd --get-default-zone
# 查看默认zone

firewall-cmd --set-default-zone=home
# 设置默认zone

firewall-cmd --get-active-zones
# 查看当前的区域

firewall-cmd --get-zone-of-interface=enp03s
# 设置当前的区域的接口

firewall-cmd --zone=public --list-all
# 显示所有公共区域（public）

firewall-cmd --zone=internal --change-interface=enp03s
firewall-cmd --permanent --zone=internal --change-interface=enp03s
firewall-cmd --reload
# 临时/永久修改网络接口 enp0s3 为  内部区域（internal），使用--permanent选项后，若想立即生效记得--reload；


firewall-cmd --enable service=ssh
# 允许 ssh 服务通过

firewall-cmd --disable service=samba --timeout=600
# 临时禁止 samba 服务 600 秒

firewall-cmd --list-services 
# 显示当前允许的服务

firewall-cmd --zone=public --query-service=ssh
# 查看服务是否被允许；

irewall-cmd --permanent --zone=internal --add-service=http 
# 添加 http 服务到内部区域（internal），需要--reload才能立即生效；

firewall-cmd --zone=work --add-service=smtp 
# 允许 SMTP 接入工作区，--remove移除；

firewall-cmd --zone=internal --add-port=443/tcp 
firewall-cmd --zone=internal --add-port=8080-8081/tcp
firewall-cmd --zone=internal --list-ports 
# 打开 443/tcp 端口在内部区域（internal）:

firewall-cmd --zone=external --add-masquerade
firewall-cmd --zone=external --add-forward-port=port=22:proto=tcp:toport=3777
# 首先启用伪装（masquerade），然后把外部区域（external）的 22 端口转发到 3777。

firewall-cmd --get-icmptypes
firewall-cmd --zone=public --query-icmp-block=echo-reply
firewall-cmd --zone=public --add-icmp-block=echo-reply
# 禁止ping（ICMP）

firewall-cmd --panic-on
# 启用紧急模式，所有东东都禁用，远程vps请不要使用，off关闭；
```

富规则（Rich Language）

```sh
firewall-cmd --permanent --zone=public --add-rich-rule="rule family="ipv4" source address="192.168.10.0/24" service name="ssh" reject"
# 拒绝所有来自于192.168.10.0/24网段的用户访问本机ssh服务（22端口）

firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="http" accept' 
firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="http" accept' --permanent  
# 允许某个服务

firewall-cmd --reload
```

> 貌似firewall-cmd的富规则可以兼容iptables的语法，so，倘若你不能忘记iptables的话，有福啦！