## Aliyun ECS设置及Nginx入门

### 初步设置

- 阿里客服推广、官网推广时购买，有一定优惠；
- 购买之后，在控制台修改密码 - 需要重启服务器才能生效；
- 连接：ssh root@xxx.xxx.xxx.xxx
- 新建普通用户&设置密码：`useradd xxx`; `pwd xxx`
- 在sudoers文件中添加刚刚添加的用户xxx。默认sudoers文件是只读，需要（`chmod +x xxx` ）

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

### 安装

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

### 基本使用

```sh
sudo systemctrl start nginx # 开启服务
# 记得设置阿里云“管理控制台”-ecs实例-安全组规则
# 规则如下：http（80） 优先级1 https（443） 优先级1

# 访问ECS外网ip即可访问
```

### 基本参数使用

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

- nginx.conf

```sh
/etc/nginx/nginx.conf
# 含有events和http
# http 包含所有 /etc/nginx/conf.d/*.conf

/etc/nginx/conf.d/default.conf
# 包含一个server {...}
# 一个server里面有很多location

# 各单元包含关系：http > server > location
```

### 常用模块

nginx有很多自带模块、第三方模块。模块生效的区域可以是http、server、location中某个级别。

**待完善.....**

## nginx常见问题解决

- 很多css js文件无法加载

```sh
# 如果发现很多文件无法加载（css　js 等），是因为这些文件nginx用户没有读取权限。
# 索性直接以root用户读取，哈哈
vim /etc/nginx/nginx.conf
# 修改为如下：
user  root;  
worker_processes  8;  
```