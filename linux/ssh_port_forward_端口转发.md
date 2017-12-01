# ssh端口转发

[TOC]

关键词：ssh 端口转发 port forward

参考：
- https://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/index.html  
- https://gist.github.com/suziewong/4413491  
- http://z-rui.github.io//post/2015/10/x11forward/  

## 概述

所谓ssh端口转发，即让本地ssh client的1111端口通过（本地ssh的`随机端口`和远程ssh服务的22端口建立的）`隧道`映射（转发）到远程ssh server的的2222端口；进而实现访问本地的1111端口就可以访问远程的2222端口。当然，这里说的本地和远程，你可以替换为主机A和主机B。

> 连接的服务器目标端口是固定的80/22等，但是发起端口是1024以上随机的，可以通过本地`netstat -an`查看！

**In a word,只要是你连接的ssh服务器能实现的东西，你都可以实现，而且是加密的！**

## 本地端口转发

使用场景：服务器上的某个端口只能服务器端（localhost）才能访问，远程如何访问它？如何让非加密的协议通过ssh隧道传输？等等

本地端口转发命令格式：

```sh
ssh -L <local port>:<remote host>:<remote port> <SSH hostname>
```

本地（ssh client）想在远程（ssh server）进行一些操作，但是远程不允许（ssh client），比如：远程的数据库设置的只能localhost（ssh server）操作OR远程开启了`netdata`的port：`19999`，但是防火墙并没有开启`19999`端口，ssh client也不能访问19999端口。so如何才能操作远程的数据库呢？可以这样操作：

```sh
ssh -L 7001:localhost:19999 yaro@ssh_Server  
# 7001是ssh_client端口，
# localhost:19999这是是指ssh_server的localhost及端口，即ssh_server本身
```

**如此，我们便可以访问`ssh_client`的`localhost:7001`来访问`ssh_Server`或`B host`的19999端口了。**

解释：我们通过ssh连接，把ssh client的7001端口，通过ssh这条隧道映射到ssh server本机的19999端口；

延伸：我们除了映射到ssh server的19999端口外，能否映射到另一台主机呢？答案是肯定的，如：

```sh
ssh -L 7001:B_host:19999 yaro@ssh_Server  
```

这样我们可以通过`ssh client`的7001端口来控制`B host`的19999端口，当然前提是`ssh_Server`能控制`B host`；值得说明的是，`ssh_Server`和`B host`之间的连接没有使用ssh加密。

再次延伸：假如我们有台主机`A host`能访问`ssh client`主机的7001端口，那么我们能否通过上面的本地端口转发实现`A host`通过`ssh client`的7001端口控制`ssh_Server`或`B host`的19999端口呢？当然可以，但是需要加上`-g`选项，即：、

```sh
ssh -L -g 7001:localhost:19999 yaro@ssh_Server  
# -g  --allow remote hosts to connect to local forwarded ports
```

需要注意的事项：

- SSH 端口转发是通过 SSH 连接建立起来的，我们必须保持这个 SSH 连接以使端口转发保持生效。一旦关闭了此连接，相应的端口转发也会随之关闭。  
- 我们只能在建立 SSH 连接的同时创建端口转发，而不能给一个已经存在的 SSH 连接增加端口转发。  
- 你可能会疑惑上面命令中的 <remote host> 为什么用 localhost，它指向的是哪台机器呢？在本例中，它指向 LdapServertHost 。我们为什么用 localhost 而不是 IP 地址或者主机名呢？其实这个取决于我们之前是如何限制 LDAP 只有本机才能访问。如果只允许 lookback 接口访问的话，那么自然就只有 localhost 或者 IP 为 127.0.0.1 才能访问了，而不能用真实 IP 或者主机名。  

## 远程端口转发

上面介绍了本地端口转发，再次强调：既然能控制ssh server，ssh server能做什么，本地（ssh client）就能通过ssh实现什么！不难发现：本地端口转发中，`ssh的访问`和`特定服务访问`是同向的(你登录ssh server，你操作ssh server的特定端口),但是当二者的方向相反时，便是远程端口转发。

远程转发命令格式：

```sh
ssh -R <local port>:<remote host>:<remote port> <SSH hostname>
```

使用场景：一般人的PC在家庭局域网（路由器），你可以访问远程的VPS；但是如何能实现远程的VPS访问你的家庭局域网中的PC(开启ssh服务)呢？

当然，你可以通过路由器端口转发等方式实现，这里使用远程端口转发实现。再次重复上面的话：“你可以实现任何你控制的VPS能实现的功能”，虽然他不能连接你局域网的PC，但是PC是你能控制的，你让VPS连接你的PC，当然应该也能实现！好拗口！！

```sh
ssh -R 2022:localhost:22 yaro@VPS_Server
# 2022端口是VPS_Server的端口；
# localhost:22指的是你的家庭局域网中PC及其端口，当然这个端口可以是1999等等；
```

估计聪明的你一定有点晕了！总结一下：

- 本地端口转发是：通过ssh隧道，让你通过访问本地ssh client的特定端口，来变向的访问远程ssh server的特定端口。  
- 远程端口转发是：通过ssh隧道，让远程的ssh server通过访问它的特定端口，实现访问本地ssh client的特定端口。

好好理理吧，上面的本地和远程只是为了方便理解，你可以让他想象成A主机和B主机，可以相互是client或server。

## 动态端口转发

上面讲述的本地和远程端口转发，实现的是特定端口7001转发到另一端的1999端口，都是一对一的；那么能否处理多个端口呢？你可能会问什么服务需要这么多端口呢？WEB服务啦，http-80，https-443,ftp-21 等等。

动态端口转发格式

```sh
ssh -D <local port> <SSH Server>
```

使用场景：由于防火网的问题，你无法访问很多网站，但是，你有个VPS可以访问这些网站，你可以把这些网络服务的端口(80/443/21)全部交给本地的1080端口转发，然后让1080端口经过SSH隧道传送到VPS上再还原成原本的网络端口(80/443/21),通过VPS访问这些网站，最后在把数据通过ssh传送回来，呃，也挺拗口，看看man说明吧：


>  This works by allocating a socket to listen to port on the local side, and whenever a connection is made to this port, the con-nection is forwarded over the secure channel, and the applica-tion protocol is then used to determine where to connect to from the remote machine.  Currently the SOCKS4 and SOCKS5 protocols are supported, and ssh will act as a SOCKS server.  Only root can forward privileged ports.  Dynamic port forwardings can also be specified in the configuration file.

```sh
ssh -D 1080 yaro@VPS_Server
# SSH会建立一个socket，去监听本地的1080端口。一旦有数据传向那个端口，就自动把它转移到SSH连接上面，发往远程主机。
```

## X协议转发

使用场景：你可能想把服务端的 X11 应用程序显示到客户端计算机上，咋整？两种解决办法：1、VNC；2、 X-Widndow，这里讲解X-windows。

前提：本地ssh client有 X-Server，远程VPS（ssh server）有X-Client，记得打开远程ssh-server的sshd配置文件启动`X11 forward`，其实此时，只在用本地ssh-client登录远程ssh-server，直接执行X应用命令（如：`subl`代表sublime），即可在本地打开远程的X应用，但是假设远程防火墙不允许X协议的端口呢？或者，你想加密传输呢？

```sh
ssh -X <SSH Server>
```

> 命令启动GUI软件的时候，注意DISPLAY环境变量要设置好，它代表启动哪个显示器？。

就是这么简单，不过平时谁把服务器安装成图形界面呢？(⊙o⊙)…，好吧！你要是控制自己的电脑还是不错的。

windows上可以选择XMing作为XServer，ssh-client就PuTTY\Xshell\Cygwin等等，随意啦