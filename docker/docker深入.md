# Docker技术从入门到放弃



参考：

[Docker官网docs](https://docs.docker.com/)  
[Docker-从入门到实践](https://www.gitbook.com/book/yeasy/docker_practice/details)  
[Docker常用命令](http://blog.51cto.com/linuxpython/1682219)

## Docker常用命令

此章节仅做命令复习，具体知识点从下一节开始。

推荐使用`zsh`自带命令、选项提示，再不行使用`man docker run`等查看`docker run`子命令manual。不懂的一定记得`man`，多man才会真的man！！

![](https://i.loli.net/2017/11/26/5a1a3dc3bee6e.png)

图0:docker命令图谱-命令关系都在这里了

### 容器相关操作

```sh
docker create # 创建一个容器但是不启动它
docker run # 创建并启动一个容器
docker stop # 停止容器运行，发送信号SIGTERM
docker start # 启动一个停止状态的容器
docker restart # 重启一个容器
docker rm # 删除一个容器
docker kill # 发送信号给容器，默认SIGKILL
docker attach # 连接(进入)到一个正在运行的容器
docker wait # 阻塞到一个容器，直到容器停止运行
docker exec # 在容器里执行一个命令，可以执行bash进入交互式
```

### 获取容器相关信息

```sh
docker ps # 显示状态为运行（Up）的容器
docker ps -a # 显示所有容器,包括运行中（Up）的和退出的(Exited)
docker inspect # 深入容器内部获取容器所有信息
docker logs # 查看容器的日志(stdout/stderr)
docker events # 得到docker服务器的实时的事件
docker port # 显示容器的端口映射
docker top # 显示容器的进程信息
docker diff # 显示容器文件系统的前后变化
```

### 容器启动时端口映射

```sh
docker run -P ...  # 映射所有端口到host的随机端口
docker port cct5 # 查看映射情况
docker run -p 80 ...  # 映射80端口到host的随机端口
docker run -p 90:80 ...  # 映射client80端口到host的90端口
```

### 导出容器

```sh
docker cp # 从容器里向外拷贝文件或目录
docker export # 将容器整个文件系统导出为一个tar包，不带layers、tag等信息
```

### 镜像操作

```sh
docker images # 显示本地所有的镜像列表
docker import # 从一个tar包创建一个镜像，往往和export结合使用
docker build # 使用Dockerfile创建镜像（推荐）
docker commit # 从容器创建镜像
docker rmi # 删除一个镜像
docker load # 从一个tar包创建一个镜像，和save配合使用
docker save # 将一个镜像保存为一个tar包，带layers和tag信息
docker history # 显示生成一个镜像的历史命令
docker tag # 为镜像起一个别名
```

### 镜像仓库(registry)操作

```sh
docker login # 登录到一个registry
docker search # 从registry仓库搜索镜像
docker pull # 从仓库下载镜像到本地
docker push # 将一个镜像push到registry仓库中
```

### 命令杂项

```sh
docker inspect container_id | grep IPAddress | cut -d '"' -f 4
# 获取container IP地址，必须是up状态。
docker exec container_id env
# 获取容器的环境变量
docker kill $(docker ps -q)
# 杀死所有正在运行的容器
docker ps -a | grep 'weeks ago' | awk '{print $1}' | xargs docker rm
# 删除一周前创建的容器
docker rm `docker ps -a -q`
# 删除已停止的容器
docker rmi $(docker images -q)
# 删除所有image（小心！）

```

### Dockerfile

Dockerfile是docker构建镜像的基础，也是docker区别于其他容器的重要特征，正是有了Dockerfile，docker的自动化和可移植性才成为可能。

不论是开发还是运维，学会编写Dockerfile几乎是必备的，这有助于你理解整个容器的运行。

```sh
FROM ubuntu
# FROM , 从一个基础镜像构建新的镜像
MAINTAINER William <wlj@nicescale.com>
# MAINTAINER , 维护者信息
ENV TEST 1
# ENV , 设置环境变量
RUN apt-get -y update 
RUN apt-get -y install nginx
# RUN , 非交互式运行shell命令
ADD http://nicescale.com/  /data/nicescale.tgz
# ADD , 将外部文件拷贝到镜像里,src可以为url
WORKDIR /var/www
# WORKDIR /path/to/workdir, 设置工作目录
USER nginx
# USER , 设置用户ID
VOLUME [‘/data’]
# VULUME <#dir>, 设置volume
EXPOSE 80 443
# EXPOSE , 暴露哪些端口
ENTRYPOINT ["/usr/sbin/nginx"]
# ENTRYPOINT [‘executable’, ‘param1’,’param2’]执行命令
CMD ["start"]
# CMD [“param1”,”param2”]
# docker创建、启动container时执行的命令，如果设置了ENTRYPOINT，则CMD将作为参数

## 尽量将一些常用不变的指令放到前面
## CMD和ENTRYPOINT尽量使用json数组方式

docker build csphere/nginx:1.7 .  
# 通过Dockerfile构建image
```



## Docker概述

registry > repository > images > container

registry（仓库？船籍）是存储镜像的远程库；

repository(仓库)是一系列镜像的集合，如：一个ubuntu可以有很多版本(tags)；

在同一个repository中，不同的镜像以 tag 区分；

一个 repository 和 tag 一起标识一个独立的image，对应唯一ID，如 ubuntu:14.04，默认tag是latest；

可以为同一个iamge（ID）可以标识多个不同的tags

然后，image是什么？container是什么？二者什么关系？具体docker知识点请另行google，这里列出三张图，能看懂这三张图，说明你已经基本掌握了docker。

![](https://i.loli.net/2017/11/26/5a1a3dc02cc39.png)

图1：你需要关注的四点：image|container|network|data_volumes

![](https://i.loli.net/2017/11/26/5a1a3dc3d6416.jpg)

图2：docker总体的概念

![](https://i.loli.net/2017/11/26/5a1a3dc3bee6e.png)

图3：docker命令图谱-命令关系都在这里了

## Image相关

镜像结构：bootfs > rootfs(ubuntu) > add emacs > add apache
镜像是容器的基石，存储在 /var/lib/docker 目录下，可以通过 docker info 命令查看；

### 镜像registry:

```sh
docker search xxx
docker pull ubuntu/ -a --all version
# 修改为国内镜像
docker push xxx/xxx
```

### image 相关命令

```sh
docker images [options]  # 查询镜像
-a 选项 # 可以显示“中间层”image，没有仓库名和tag；
docker inspect [options] container|image [container|image...] # 镜像详细信息
# inspect 命令查看用于container 或 image
docker inspect  ubuntu:14.4/ID # (一个ID可以多个标签)
docker tag 473e79d4d5f test:1.0 # 修改tag
docker rmi  [options] image [image...]  # 移除镜像
docker rmi 473e79d4d5f
# 通过 image id 删除image，-f可以强制移除包含正在运行容器的image；
docker rmi tacaojs1607:1.2
# 移除标签
docker rmi $(docker images -q ubuntu)  # 删除ubuntu repo的所有镜像；
```

### 构建镜像:

构建镜像的优点：

- 保存对容器的修改，再次使用；
- 自定义镜像的能力；
- 以软件的形式打包并分发服务及其运行环境。

#### method 1:docker commit 

通过容器构建镜像；

```sh
docker commit [options] container [repository[:tag]]
docker run -it -p 80 --name commit_test ubuntu /bin/bash  # 启动一个容器commit_test
# apt update  # 修改容器
# apt nginx
# exit
docker commit -a "yaro" -m "nginx" commit_test yaro/commit_test  # 制作名称为yaro/commit_test的镜像
docker run -d --name nginx_web -p 80 yaro/commit_test nginx -g "daemon off;" # 运行刚刚制作的image
docker ps 
```

#### method 2:docker build  

通过Dockerfile构建镜像:创建 Dockerfile -> 使用 `$docker build` 命令

```sh
# First Dockerfile
FROM ubuntu:14.04
MAINTAINER yaro "wyz@163.com"
RUN apt-get update
RUN apt-get install -y nginx
EXPOSE 80  # 暴露80端口
-------
docker build -t=‘yaro/df_test1’ .  # 执行build命令，‘点’表示当前目录
```

## Container相关

假如把image比作程序语言中的class，container就是其实例化，是动态的存在。

这里仅列举一些实例，详细命令请参考第一部分“docker常用命令”及man命令啦。

```sh
# exit 或 ctrl+d 退出后，container会状态会变为“exited”；ctrl+p+q 退出会后台执行；

docker run -it yaro/test bash  # 建立容器启动，交互，tty，执行bash
docker run -it -d yaro/test tail -f /dev/null #使用 daemon 模式建立容器并启动
docker run -it -v ~/Downloads:/data yaro/test bash # 建立容器并启动，且挂载到本机目录（local在前）；
docker ps # 查看已启动 running 的containers
docker ps -a # 查看所有状态的containers
docker stop 容器名/id
docker start 容器名/id

# 前面用了 -d  daemon模式run容器，需要使用attach/exec进入、操作；
docker attach 容器名/id  # 接入container 
docker exec -it 容器名/id bash  # 重新执行bash

docker commit -m "提交信息" -a "作者"  473e79d4d5f tacaojs1607 # 储存现有container状态为image，-m/a可以省略

docker rm 473e79d4d5f
# 移除已经停止的容器，-f 强制移除容器
```

## Docker容器数据管理

### Docker容器的数据卷（Data Volume）

docker=软件及环境的打包，但是数据需要持久化。

数据卷是经过特殊设计的目录，可以绕过联合文件系统（UFS），为一个或多个容器提供访问，docker数据卷存在与宿主机（docker host）。

数据卷设计的目的，在于数据的持久化，它完全独立于容器的生存周期，因此docker不会在删除容器时删除其挂载的数据卷，它更不会存在类似的垃圾收集机制，对容器引用的数据卷进行处理。

```sh
docker run -v ~/container_data:/data -it ubuntu /bin/bash  # 添加数据卷，目录映射前面是host，目录会在自动创建；
# 可以使用 docker inspect 查看是否有容器数据卷挂载；

docker run -v ~/container_data:/data：ro -it ubuntu /bin/bash  # 添加ro权限

# 可以使用Dockerfile构建包含数据卷的镜像，进而开启挂载数据卷的容器；
# Dockerfile指令：
VOLUME ["/data"，“/data2”] # 创建两个数据卷；
# 值得注意的是，这样创建的容器挂载的数据卷在host主机的目录无法自己指定；
```

### Docker的数据卷容器

数据卷容器：命名的容器1挂载数据卷，其它容器通过挂载这个容器实现数据共享，挂载数据卷的容器1，就叫做数据卷容器。

```sh
docker run --volumes-from [CONTAINER NAME]  # 
# 上面使用Dockerfile构建包含数据卷的镜像，无法指定数据卷对应的主机目录，可以通过“数据卷容器”容器之间数据的思想；
# 数据卷容器仅仅是传递挂载的载体，删除数据容器，不会影响后面的容器的数据挂载；
# 只要有容器在使用数据卷，哪怕是 docker rm -v container 也无法删除数据的挂载；
```

### Docker数据卷的备份和还原

```sh
docker run --volumes-from dvt5 -v ~/backup:/backup --name dvt10 ubuntu tar cvf /backup/dvt5.tar /datavolune1
# --volumes-from dvt5  使用dvt5作为数据卷容器；
# -v ~/backup:/backup 挂载local目录；
# --name dvt10 ubuntu 以ubuntu镜像创建名称为dvt10的容器
# tar cvf /backup/dvt5.tar /datavolune1  执行压缩命令，把dvt5中的数据备份到local；

docker run --volumes-from [container name] -v $(pwd):/backup ubuntu tar xvf /backup/backup.tar [container data volume]  # 数据的还原
```

## Docker容器的网络连接

### docker容器的网络基础

- 启动docker deamon之后，在host使用 ifconfig 命令可以看到docker0的网卡，其为docker的容器提供网络服务，docker0其实是linux的虚拟网桥，
- 网桥是OSI七层模型中的数据链路层（第二层）的设备，通过MAC地址对网络进行划分，并在不同的网络之间通讯。
- linux虚拟网桥的特点：可以设置ip地址（通常是第三层-网络层的特点），相当于拥有一个隐藏的虚拟网卡。
- docker0的地址划分：ip：172.17.42.1；子网掩码：255.255.0.0(65534个地址)；MAC：02:42:ac:11:00:00 到 02:42:ac:11:ff:ff.
- 可以使用`brctl show`命令（需要安装bridge-utils）查看网桥设备,启动一个容器后（ctrl+p+q后台运行），可以看到docker0提供的veth...虚拟网络接口。
- 修改docker0地址：`ifonfig docker0 192.168.200.1 netmask 255.255.255.0`，可以修改docker0提供ip网段。

自定义虚拟网桥（不使用docker0）如下：

```sh
# 1、添加虚拟网桥
sudo brctl addbr br0
sudo ifconfig br0 192.168.100.1 netmask 255.255.255.0
# 2、更改docker守护进程的启动配置：
/etc/default/docker 中添加DOCKER_OPS值:  
-b=br0 
```

### docker容器的互联

环境准备：用于测试的Docker镜像的DOckerfile：

```sh
# Container connection test
FROM ubuntu:14.04
RUN apt-get install -y ping
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y curl
EXPOSE 80
CMD /bin/bash  # 默认运行bash

# 构建image
docker build -t yaro/cct .  # 指定tag，当前目录构建
```

1、允许所有容器互联（默认）

Docker daemon的启动选项中添加：`--icc=true`

```bash
docker run -it --name cct1 yaro/cct  # Dockerfile文件中已经声明执行bash；
# nginx # 启动nginx
# ifconfig  # 查看ip地址；
# ctrl+p+q
docker run -it --name cct2 yaro/cct  # 再启动一个容器cct2
# ifconfig  # 查看ip地址；
# ping ip_cct1
# curl http://ip_cct1  # 访问nginx服务
```

重启container可能造成container的ip地址发生改变，如何能固定的访问一个container呢？

```sh
docker run --link=[CONTAINER_NAME]:[ALIAS] [IAMGE] [COMMAND]
# 可以在启动container时起一个代号，方便我们连接。
docker run -it --name cct3 --link=cct1:webtest yaro/cct  # 给cct1起个别名
# ping webtest  # 这时就可以用 webtest 访问 cct1 了
# env  # 查看原理
# cat /etc/hosts  # 查看原理
```

2、拒绝容器间互联

Docker daemon的启动选项中添加：`--icc=false`

```sh
sudo vim /etc/default/docker
# DOCKER_OPTS="--icc=false"
systemctl restart docker 
docker restart cct1 cct2 cct3
docker attach cct3
# ping webtest  # 无法访问
```

3、允许特定容器间的连接

Docker daemon的启动选项中添加：`--icc=false --iptables=true`,且启动container时使用`--link`选项。

```sh
sudo vim /etc/default/docker
# DOCKER_OPTS="--icc=false --iptables=true"
systemctl restart docker 
docker restart cct1 cct2 cct3
docker attach cct1
# nginx  
# ctrl+p+q
docker attach cct3
# curl webtest  # 无法访问
# ctrl+p+q
iptables -L -n  # 会发现FORWARD默认是DROP
iptables -F  # 清空iptables
systemctl restart docker 
iptables -L -n  # 会发现FORWARD已经允许docker的访问
docker restart cct1 cct2 cct3
docker attach cct1
# nginx  
# ctrl+p+q
docker run -it --name cct4 --link=cct1:webtest yaro/cct 
# curl webtest
## 只有cct2不能连接cct1，cct3和cct4都能连接
iptables -L -n  # DOCKER链中的已经有允许的连接。
```

### docker容器的与外部网络的连接

容器与外部网络的连接首先开启`--ip-forward`选项

```sh
sudo sysctl net/ipv4/conf/all/forwarding  # 查看--ip-forward是否开启，默认是开启的；
# docker配置选项中可以指定 --ip-forward=true
```

容器与外部网络的连接需要用到iptables中的filter表中的INPUT/FORWARD/OUTPUT链。

```sh
sudo iptables -t filter -L -n   # 会发现DOCKER 链，其实是FORWARD的子链；
docker run -it -p 80 --name cct5 yaro/cct  # 指定publish容器的80端口；
# nginx  #启动nginx
docker port cct5  # 假设49153，查看container的80端口，映射主机的什么端口；
# 其他主机host_ip2便可以通过 curl host_ip1:49153来访问cct5_ip:80端口；
iptables -L -n  # 查看规则
iptables -I DOCKER -s host_ip2 -d cct5_ip -p TCP --dport 80 j DROP
iptables -L -n  # 查看规则
# 主机 host_ip2 便不能访问 host_ip1:49153 了；
```
