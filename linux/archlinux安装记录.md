# archlinux安装记录
Tags：archlinux，gnome，xfce4
参考：
https://wiki.archlinux.org/index.php/Installation_guide
https://blog.ikke.moe/posts/archlinux-installation-notes/
https://blog.ikke.moe/posts/continuation-of-archlinux-installation-notes/
[TOC]
## 基础安装
### 为何安装arch
更深层次理解linux，系统内核、软件都是最新。还有，就是闲的蛋疼。
### 安装介质
U盘首选，本例使用MBR，UEFI请另行搜索。
### 制作U盘启动
- linux上
```sh
dd if=archlinux-2015.11.01-dual.iso of=/dev/sdb
```
- Windows上
建议使用[rufus](https://rufus.akeo.ie/)软件
- ISO文件下载
官网，国内镜像，qbittorrent等等
### 开始安装
插入电脑，设置BIOS启动方式。
### 链接网络
由于arch安装全过程需要联网下载各种软件包，没有网络就洗洗睡吧。
- 有线网络：用`ip addr`查看网卡接口型号，比如`enp2s0`，然后直接启动网卡的DHCP功能即可。
```sh
systemctl enable dhcpcd@enp2s0.service
ping baidu.com
```
- 无线网络：使用`wifi-menu`查看现有无线列表，然后输入密码，OK。
### 分区
我是整块硬盘安装一个系统的，有多块硬盘的话具体用 lsblk 查看一下，我因为只有一块硬盘所以可以看到 /dev/sda。
分区工具比较多，推荐 `parted` 或者 `fdisk`，后者有个类似图形化一样的界面很方便。`parted`如下：
```sh
parted /dev/sda
(parted) mklabel msdos
(parted) mkpart primary ext4 1M 500M
(parted) set 1 boot on
(parted) mkpart primary ext4 500M 50G
(parted) mkpart primary linux-swap 50G 54G
(parted) mkpart primary ext4 54G 100%
## 语法
(parted) mkpart part-type fs-type start end
## 进入 parted 交互界面后使用 mkpart 创建，后面跟上 4 个参数，分别是 分区类型、文件系统类型、起始点、结束点，分区类型就主分区还是逻辑分区，起始结束点使用 MB、GB 方便计算你懂的。
```
使用 parted 对 /dev/sda 设备进行分区，分区表 为 MS-DOS 即 MBR 分区结构。共分了4个区，个人习惯～
```
挂载点 大小 说明
------------------------------------------------------------------
/boot 1-500M 用于挂载 /boot 分区，设置为 Bootable。
/ 500M-50G 用于挂载 / 分区
swap 50G-54G 用于交换分区(Swap)
/home 54G-100% 剩余空间用于挂载 /home分区
```
分完区后进行格式化
```sh
mkfs.ext4 /dev/sda1
mkfs.ext4 /dev/sda2
mkfs.ext4 /dev/sda4
mkswap /dev/sda3
```
挂载分区
```sh
mount /dev/sda2 /mnt
mkdir /mnt/{boot,home}
mount /dev/sda1 /mnt/boot
mount /dev/sda4 /mnt/home
swapon /dev/sda3
```
### 安装基本系统
使用 `pacstrap` 命令
```sh
pacstrap /mnt base base-devel
## base-devel 提供aur软件源支持
```
### 生成 fstab
```sh
genfstab -U -p /mnt > /mnt/etc/fstab
# 这里使用的是UUID，如果不加-U，那么在fstab中记录的就是/dev/sdX之类的地址了，UUID的方式更加好
```
接下来的操作就要全部切换到这个基本系统上去了。
```sh
arch-chroot /mnt /bin/bash
# 切换根目录为/mnt，并使用/bin/bash终端
```
### 时区
设置 [时区](https://wiki.archlinux.org/index.php/Time_zone):
```
# ln -sf /usr/share/zoneinfo/zone/subzone /etc/localtime
```
例如：
```
# ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```
建议设置[时间标准](https://wiki.archlinux.org/index.php/Time_standard) 为 UTC，并调整 [时间漂移](https://wiki.archlinux.org/index.php/Time_skew):
```
# hwclock --systohc --utc
```
### 设置Locale
```sh
nano /etc/locale.gen # 
# 务必开启en_US.UTF-8，否则有些软件不支持中文就尴尬了
# 选择开启zh_CN.UTF-8，中文界面。
locale-gen # 生成本地化文件
echo LANG=zh_CN.UTF-8 >> /etc/locale.conf # 设置当前语言
```
这里由于console字体的原因，中文会变成方框，如果你不安装桌面环境，请使用en_US.UTF-8。
### 主机名
要设置 [hostname](https://wiki.archlinux.org/index.php/Hostname)，将其[添加](https://wiki.archlinux.org/index.php/Add) 到 `/etc/hostname`, *myhostname* 是需要的主机名:
```sh
echo myhostname > /etc/hostname
```
建议添加[对应的信息](https://wiki.archlinux.org/index.php/Network_configuration#Local_network_hostname_resolution)到[hosts(5)](http://jlk.fjfi.cvut.cz/arch/manpages/man/hosts.5):
```sh
/etc/hosts
127.0.0.1 localhost.localdomain localhost
::1 localhost.localdomain localhost
127.0.1.1 myhostname.localdomain myhostname
```
### 创建 ramdisk
```sh
mkinitcpio -p linux # 系统最先启动的东东
```
### 设置 root 用户密码
```sh
passwd root
```
### 安装 bootloader
一般都是用 grub，因为本人笔记本并不支持 UEFI，所以使用 UEFI 板子的同学得自己查找一下相关的 Wiki 了。
```sh
pacman -S grub
grub-install /dev/sda # 这里是安装到硬盘ada，而不是分区
grub-mkconfig -o /boot/grub/grub.cfg # 写入配置文件
```
### 网络配置
基本上跟开始安装的时候一样。
有线：
```sh
systemctl enable dhcpcd@enp2s0.service
```
无线的话注意了，需要安装几个包不然无法使用。
```sh
pacman -S wpa_supplicant dialog
```
### 添加用户
虽然你也可以直接用 root 用户，但是毕竟不安全，貌似有些软件还不能直接用 root ？
```sh
useradd -m -g users -G wheel -s /bin/bash ikke
# -m 生成home文件夹
# -g 指明所属主组
# -G 指明所属追加组
passwd ikke
```
### 安装 sudo
要使用 `sudo` 命令提权的话需要安装 sudo 并且做相应配置
```sh
pacman -S sudo
```
打开 `/etc/sudoers` 文件，找到 `root ALL=(ALL) ALL` 并依葫芦画瓢添加 `ikke ALL=(ALL) ALL` 即可。
### 卸载分区并重启。
到此系统就安装结束，可以退出安装程序并重启系统了。
```sh
exit
umount -R /mnt
reboot
```
## 安装桌面环境
### 驱动安装
相关驱动的安装参考arch wiki官网
### 安装 Xorg
原本以为需要安装整个 Xorg 事实上根本不用～
```sh
sudo pacman -Syu
sudo pacman -S xorg-xinit xorg-server
```
桌面环境可根据需要安装 GNOME 或者 KDE。
### 安装 GNOME
```sh
sudo pacman -S gnome
# 里面默认集成了GDM（系统登录界面）
```
如果你还需要 GNOME 自带的软件的话
```sh
sudo pacman -S gnome-extra
```
顺便安装一下 GNOME 优化工具 GNOME Tweak Tool
```sh
sudo pacman -S gnome-tweak-tool
```
显示管理器 GNOME 默认是用的是 GDM。
```sh
sudo systemctl enable gdm.service
```
装完 GNOME 进系统过后你会发现没地方设置网络，到 Settings 里面找到 Network 点开会提示你 NetworkManager 没有运行。
```sh
sudo systemctl start NetworkManager.service
sudo systemctl enable NetworkManager.service
```
然后重启电脑应该就能进入 GDM 了，选择用户名密码登录即可。
> 倘若不能进入界面，可以`sudo pacman -Rnv gdm`卸载登录界面软件，替换成`slim`即可，记得在用户主目录下面创建`.xinitrc`文件，写入`exec gnome-session`。
### 安装xfce4桌面
倘若不喜欢gnome桌面的话，安装xfce也挺不错。
```sh
pacman -Syu xorg-server xorg-xinit
pacman -S xfce4 xfce4-goodies # 扩充包，类似于gnome-extra
# 当前目录下创建 .xinitrc 文件写入如下内容： exec startxfce4
startx # 启动桌面
sudo pacman -Sv slim # SLiM是Simple Login Manager（简单登录管理器）；
systemctl enable slim
```
### 更新系统
因为我们在大天朝，所以软件源建议设置为国内的，例如清华大学 TUNA 或者中科大 USTC。
注意备份已有的 mirrorlist 文件。
```sh
sudo mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo echo Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch > /etc/pacman.d/mirrorlist
sudo pacman -Syy
sudo pacman -Syu
```
### 安装 Yaourt
同样使用 TUNA 的镜像，编辑 `/etc/pacman.conf` 文件，加入
```sh
[archlinuxcn]
SigLevel = Optional TrustedOnly
Server = http://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```
导入 GPG Key。
```sh
sudo pacman -S archlinuxcn-keyring
```
然后执行 以下命令安装 Yaourt
```sh
sudo pacman -Syu
sudo pacman -S yaourt
```
## 其他补充项
由于本人习惯使用简体中文，所以自然要切回简体中文。
### 设置 Locale
编辑 `/etc/locale.gen` 文件，去掉 `zh_CN.UTF-8` 前面的注释，然后执行 `sudo locale-gen`。
### 设置系统语言
到系统设置地域语言中，把语言改成 **汉语(中国)**，然后注销用户重新登录即可。
### 优化中文显示
重启后你会发现中文显示很难看还锯齿严重，因为系统并没有安装合适的中文字体以及开启抗锯齿。
中文字体推荐[思源黑体（Source Han Sans）](https://github.com/adobe-fonts/source-han-sans)，我真的是非常喜欢哈哈～
```sh
sudo pacman -S adobe-source-han-sans-cn-fonts
```
装完中文字体后打开 GNOME Tweak Tool，中文名叫做优化工具，切换到字体一栏，将窗口、界面、文档的字体改为 `Source Han Sans Normal`，中文叫做 **思源黑体**，重口味的需要窗口用粗体的话也自行更改，然后别忘了将下方的抗锯齿选择为 `Grayscale` 或者 `Rgba`，到此中文化就完整了，看着界面真是舒服。
另外还有个等宽字体的设置，个人用的是 [Source Code Pro](https://github.com/adobe-fonts/source-code-pro/)，`hack`字体也是极好的，另外再推荐一个 Mac 用户必定知道的字体 [Monaco](https://github.com/cstrap/monaco-font)。
### 安装常用软件
常用一：
google-chrome，sogoupinyin， wine-qqintl， ntfs-3g（写入ntfs格式），
解压缩软件：
sudo pacman -S file-roller unrar unzip p7zip 
ssh、git软件：
sudo pacman -S git openssh
