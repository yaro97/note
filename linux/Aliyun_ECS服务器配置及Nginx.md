## Aliyun ECS设置及Nginx入门

### 初步设置

- 阿里客服推广、官网推广时购买，有一定优惠；
- 购买之后，在控制台修改密码 - 需要重启服务器才能生效；
- 连接：ssh root@xxx.xxx.xxx.xxx
- 新建普通用户&设置密码：`useradd xxx`; `pwd xxx`
- 在sudoers文件中添加刚刚添加的用户xxx。默认sudoers文件是只读，需要（`chmod +x xxx` ）

### ssh安全策略

建议修改`/etc/sshd_config` 中的`PermitRootLogin no`，禁止root登录，然后使用普通用户登陆后，切换到root用户操作。

### vim相关配置

默认配色很难受，建议使用：`colorscheme ron`

```sh
# 把.vimrc文件上传只用户目录
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim # 安装plug.vim工具
PlugInstall # 使用plug.vim安装.vimrc中的相关插件
```

### zsh相关配置

```sh
###======
sudo yum install zsh
sudo yum install git
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

# 启用zsh插件：git sudo history autojump zsh-autosuggestions zsh-syntax-highlighting 等；
vim ~/.zshrc
chsh -s /usr/bin/zsh

# 安装插件：zsh-autosuggestions（仿fish自动提示，右方向键补全所有，ctrl+右方向键-补全字符）
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
# 添加到.zshrc插件：plugins=(zsh-autosuggestions)
# 重启teminal

# 安装插件：zsh-syntax-highlighting（仿fish自动高亮）
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# 添加到.zshrc插件：plugins=(zsh-syntax-highlighting)
source ~/.zshrc
```

### ftp、sftp相关

没有必要使用ftp，需要传输文件的话，使用sftp即可

### 其他安装

```sh
sudo yum install mlocate tmux
```

## Nginx

### 推荐环境

系统硬件：cpu>=2core， 内存：>=256

阿里云、虚拟机、docker（迁移方便）

软件：centOS>=7.0 X64

### 环境调试确认

四项确认：

```sh
# 1. 确认系统网络
ping baidu.com
# 2. 确认yum可用
yum list | grep gcc
# 3. 确认关闭iptables规则（初学者）
sudo iptables -L  # 查看所有规则
sudo iptables -F  # Flush 删除所有规则
sudo iptables -t nat -L
sudo iptables -t nat -F
# 4. 确认停用selinux
getenforce  # 查看selinux状态
setenforce 0  # 禁用selinux
```

两项安装：

```sh
sudo yum -y install gcc gcc-c++ autoconf pcre pcre-devel make automake
sudo yum -y install wget httpd-tools vim
```

一次初始化

```sh
cd /opt
mkdir app download logs work backup
```

### 安装nginx

官网：http://nginx.org/

官网-download：

Mainline version：最新版，供开发研究使用；

Stable version：稳定版：商业使用；

Legacy versions：历史版本：。。

Source Code：源代码编译

Pre-Built Packages：Linux相应的Repo源

> pgp:适用于安全校验的（非官网下载时，最好校验一下）

这里选择Pre-Built Packages安装：

 http://nginx.org/en/linux_packages.html#stable

To set up the yum repository for RHEL/CentOS, create the file named `/etc/yum.repos.d/nginx.repo` with the following contents:

> ```
> [nginx]
> name=nginx repo
> baseurl=http://nginx.org/packages/OS/OSRELEASE/$basearch/
> gpgcheck=0
> enabled=1
> ```

Replace “`OS`” with “`rhel`” or “`centos`”, depending on the distribution used, and “`OSRELEASE`” with “`6`” or “`7`”, for 6.x or 7.x versions, respectively.

```sh
yum list | grep nginx # 查看yum源是否添加成功
sudo yum install nginx # 安装
nginx -v # 查看版本
nginx -V # 查看编译参数
```

### nginx基本使用

- 开启相应服务

```sh
systemctrl start nginx # 开启服务
systemctrl enable nginx # 开机启动
# 授予nginx网页目录下文件相应的访问权限：755，否则css、js文件会不能正常加载。
# 即可通过访问ECS外网ip，访问网页
```

- 阿里云控制台相应设置

```sh
# 记得设置阿里云“管理控制台”-ecs实例-安全组规则
# 规则如下：http（80） 优先级1 https（443） 优先级1
```

- 解析php相应设置

```sh
# nginx默认不支持php，需要安装php-fpm。
systemctrl start php-fpm # 开启服务
systemctrl enable php-fpm # 开机启动
# nginx的配置文件也需要针对php作相应的修改
```

> 具体的nginx位置文件请参考备份（百度网盘-其他-备份-paotime_nginx配置备份）

### 基本参数介绍

- 安装目录

```sh
rpm -ql nginx # 列出nginx的安装目录
/etc/logrotate.d/nginx # 配置文件：nginx日志轮转，用于logrotate服务的日志切割

/etc/nginx
/etc/nginx/conf.d 
/etc/nginx/nginx.conf # 1 日志、配置文件：Nginx主配置文件
/etc/nginx/conf.d/default.conf # 2 

/etc/nginx/fastcgi_params
/etc/nginx/scgi_params
/etc/nginx/uwsgi_params # 配置文件：cgi配置文件fastcgi配置文件

/etc/nginx/koi-utf
/etc/nginx/koi-win
/etc/nginx/win-utf # 配置文件：编码转换映射转化文件

/etc/nginx/mime.types # 配置文件：设置http协议的Content-Type与扩展名对应关系

/usr/lib/systemd/system/nginx-debug.service
/usr/lib/systemd/system/nginx.service
/etc/sysconfig/nginx
/etc/sysconfig/nginx-debug # 配置文件：用于配置出系统守护进程管理器管理方式

/usr/lib64/nginx/modules
/etc/nginx/modules # 目录：Nignx模块目录

/usr/sbin/nginx
/usr/sbin/nginx-debug # 命令：Nginx服务的启动管理的终端命令。

/usr/share/doc/nginx-1.14.0
/usr/share/doc/nginx-1.14.0/COPYRIGHT
/usr/share/man/man8/nginx.8.gz # 文件、目录：nginx的手册和帮助文件

/var/cache/nginx # 目录：nginx缓存目录

/var/log/nginx # 目录：nginx日志目录
```

- 编译参数

```sh
nginx -V #查看编译参数

--prefix=/etc/nginx 
--sbin-path=/usr/sbin/nginx 
--modules-path=/usr/lib64/nginx/modules 
--conf-path=/etc/nginx/nginx.conf 
--error-log-path=/var/log/nginx/error.log 
--http-log-path=/var/log/nginx/access.log 
--pid-path=/var/run/nginx.pid 
--lock-path=/var/run/nginx.lock  # 安装目的目录或路径

--http-client-body-temp-path=/var/cache/nginx/client_temp 
--http-proxy-temp-path=/var/cache/nginx/proxy_temp 
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp 
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp 
--http-scgi-temp-path=/var/cache/nginx/scgi_temp # 执行对应模块时，nginx所保留的临时性文件

--user=nginx 
--group=nginx # 设定nginx进程启动的用户和组

--with-compat 
--with-file-aio 
--with-threads 
--with-http_addition_module 
--with-http_auth_request_module 
--with-http_dav_module 
--with-http_flv_module 
--with-http_gunzip_module 
--with-http_gzip_static_module 
--with-http_mp4_module 
--with-http_random_index_module 
--with-http_realip_module 
--with-http_secure_link_module 
--with-http_slice_module 
--with-http_ssl_module 
--with-http_stub_status_module 
--with-http_sub_module 
--with-http_v2_module 
--with-mail 
--with-mail_ssl_module 
--with-stream 
--with-stream_realip_module 
--with-stream_ssl_module 
--with-stream_ssl_preread_module 
--with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' # 设置额外的参数将被添加到CFLANGS变量
--with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie' # 设置附加的参数，链接系统库
```

### nginx配置文件

nginx的配置文件nginx.conf位于安装目录的conf目录下，是由多个块嵌套而成。

- 主要结构如下：

![图片描述](https://segmentfault.com/img/bVFbmP?w=417&h=634)

- 配置文件形式如下：

```sh
user www www;
#其他全局配置项
events{
}
http{
      upstream{
      }
      server{
            location {
            }
      }
}
```

外层的main是全局配置，不需要标明“main”

- 每个块的含义如下：

| 模块     | 含义                          |
| -------- | ----------------------------- |
| main     | Nginx的全局属性配置           |
| event    | Nginx的工作模式以及连接数上线 |
| http     | http服务器相关属性配置        |
| upstream | 负载均衡配置                  |
| server   | 虚拟主机的配置                |
| location | location配置                  |

- 配置实例

```sh
#运行用户
user nobody;
#启动进程,通常设置成和cpu的数量相等
worker_processes  1;

#全局错误日志及PID文件
#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;

#工作模式及连接数上限
events {
    #epoll是多路复用IO(I/O Multiplexing)中的一种方式,
    #仅用于linux2.6以上内核,可以大大提高nginx的性能
    use   epoll;

    #单个后台worker process进程的最大并发链接数
    worker_connections  1024;

    # 并发总数是 worker_processes 和 worker_connections 的乘积
    # 即 max_clients = worker_processes * worker_connections
    # 在设置了反向代理的情况下，max_clients = worker_processes * worker_connections / 4  为什么
    # 为什么上面反向代理要除以4，应该说是一个经验值
    # 根据以上条件，正常情况下的Nginx Server可以应付的最大连接数为：4 * 8000 = 32000
    # worker_connections 值的设置跟物理内存大小有关
    # 因为并发受IO约束，max_clients的值须小于系统可以打开的最大文件数
    # 而系统可以打开的最大文件数和内存大小成正比，一般1GB内存的机器上可以打开的文件数大约是10万左右
    # 我们来看看360M内存的VPS可以打开的文件句柄数是多少：
    # $ cat /proc/sys/fs/file-max
    # 输出 34336
    # 32000 < 34336，即并发连接总数小于系统可以打开的文件句柄总数，这样就在操作系统可以承受的范围之内
    # 所以，worker_connections 的值需根据 worker_processes 进程数目和系统可以打开的最大文件总数进行适当地进行设置
    # 使得并发总数小于操作系统可以打开的最大文件数目
    # 其实质也就是根据主机的物理CPU和内存进行配置
    # 当然，理论上的并发总数可能会和实际有所偏差，因为主机还有其他的工作进程需要消耗系统资源。
    # ulimit -SHn 65535

}


http {
    #设定mime类型,类型由mime.type文件定义
    include    mime.types;
    default_type  application/octet-stream;
    #设定日志格式
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    '$status $body_bytes_sent "$http_referer" '
    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  logs/access.log  main;

    #sendfile 指令指定 nginx 是否调用 sendfile 函数（zero copy 方式）来输出文件，
    #对于普通应用，必须设为 on,
    #如果用来进行下载等应用磁盘IO重负载应用，可设置为 off，
    #以平衡磁盘与网络I/O处理速度，降低系统的uptime.
    sendfile     on;
    #tcp_nopush     on;

    #连接超时时间
    #keepalive_timeout  0;
    keepalive_timeout  65;
    tcp_nodelay     on;

    #开启gzip压缩
    gzip  on;
    gzip_disable "MSIE [1-6].";

    #设定请求缓冲
    client_header_buffer_size    128k;
    large_client_header_buffers  4 128k;


    #设定虚拟主机配置
    server {
        #侦听80端口
        listen    80;
        #定义使用 www.nginx.cn访问
        server_name  www.nginx.cn;

        #定义服务器的默认网站根目录位置
        root html;

        #设定本虚拟主机的访问日志
        access_log  logs/nginx.access.log  main;

        #默认请求,优先级最低的匹配
        location / {
            # 匹配任何请求，因为所有请求都是以"/"开始
            # 但是更长字符匹配或者正则表达式匹配会优先匹配
            #定义首页索引文件的名称
            index index.php index.html index.htm;

        }

        #1. = 精确匹配会第一个被处理。如果发现精确匹配，nginx停止搜索其他匹配。
        location  = / {
            # 只匹配"/".
        }

        # 定义错误提示页面
        error_page   500 502 503 504 /50x.html;
        location = /50x.html {
        }

        #静态文件，nginx自己处理
        #2.波浪线表示执行一个正则匹配，区分大小写
        location ~ ^/(images|javascript|js|css|flash|media|static)/ {

            #过期30天，静态文件不怎么更新，过期可以设大一点，
            #如果频繁更新，则可以设置得小一点。
            expires 30d;
        }

        #PHP 脚本请求全部转发到 FastCGI处理. 使用FastCGI默认配置.
        location ~ .php$ {
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include fastcgi_params;
        }

        #禁止访问 .htxxx 文件
        location ~ /.ht {
            deny all;
        }

        #3.^~ 则只匹配该规则，nginx停止搜索其他匹配，否则nginx会继续处理其他location指令。
        location ^~ /images/ {
            # 匹配任何以 /images/ 开始的请求，并停止匹配 其它location
            #[Configuration C]
        }

        #4.~*    #表示执行一个正则匹配，不区分大小写
        location ~* .(gif|jpg|jpeg)$ {
            # 匹配以 gif, jpg, or jpeg结尾的请求.
            # 但是所有 /images/ 目录的请求将由 [Configuration C]处理.
        }
    }
}
```

- 常用模块

nginx有很多自带模块、第三方模块。模块生效的区域可以是http、server、location中某个级别。

**待完善.....**

