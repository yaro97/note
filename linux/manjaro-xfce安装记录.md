# manjaro-xfce安装记录

Tags：manjaro，xfce，archlinux，aur，xfce美化

[TOC]

遇到问题请参考**ArchLinux官网**:https://wiki.archlinux.org

刻录U盘（建议windows下使用Rufus刻录软件），安装即可；值得注意的是，在进入U盘的界面可以选择驱动，先尝试闭源驱动（nofree），倘若无法进入系统，再尝试开源驱动即可。

## 分区相关

我的硬盘主分区只能四个（其实是三个，预留一个给逻辑分区）。

双系统分区如下：Windows占用三个主分区（`预留盘 `- `C盘` - `D盘`），Linux只能在逻辑分区中再细分。

boot：500M，swap：4G，/：50G，home：剩余其他

## 修改源，更新系统

```sh
sudo pacman-mirrors -i -c China -m rank  # 这个会对国内的源进行测速排名，然后弹出图形化的设置界面，然后根据上图的访问速度，勾选想要的源，

## 显示pacman/pacaur颜色：启动 /etc/pacman.conf 中的 Color 和 VerbosePkgLists 选项

## 当然除了官方源之外，还可以添加aurlinux源，具体可以google一下，但是不建议这样，以防滚挂。

sudo pacman -Syyu # 更新软件包db并更新所有软件（即系统）；

sudo pacman -Sv yay/pacaur/aurman(aur) # 当然还可以选择yaourt(可以更改为清华源)；
# 貌似aur服务器在德国，不过还能接受；
# 倘若在安装aur时遇到错误（fakeroot等），记得安装base-devel编译包；
```

## 安装搜狗输入法

```sh
sudo pacman -S fcitx-sogoupinyin（aur） fcitx-im fcitx-configtool
# fcitx-sogoupinyin依赖qtwebkit，安装要是出现问题（安装无法完成），建议先单独安装qtwebkit-bin

# .xprofile (如果遇到有些软件不能输入中文，再添加到.bash_profile)是配置窗口打开时运行的命令,写入如下内容：
sudo echo -e "export GTK_IM_MODULE=fcitx\nexport QT_IM_MODULE=fcitx\nexport XMODIFIERS=@im=fcitx" >> ~/.xprofile

#对于jetbrians系列fcitx无法跟随的情况 fcitx输入法配置>附加组件>勾选高级>xim前端>勾选on the spot

## 注销用户重新登录即可使用
```

## 安装zsh

```sh
pacaur -Sv zsh

sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# 安装oh my zsh；

# 设置oh-my-zsh主题为默认的 ys；
# 或者使用spaceship主题；
官网：https://github.com/denysdovhan/spaceship-prompt

# 启用插件：git sudo history autojump zsh-autosuggestions zsh-syntax-highlighting 等；
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

## 注销用户重新登录即可使用
```
## 中文字体

```sh
sudo pacman -S --noconfirm wqy-microhei && fc-cache -fv
# 外观》字体：设置应用程序默认字体。
# qt5设置》字体：设置qt窗体的默认字体

# 其他字体选用
sudo pacman -Sv wqy-microhei-lite wqy-bitmapfont wqy-zenhei
sudo pacman -Sv adobe-source-han-sans-cn-fonts adobe-source-han-serif-cn-fonts noto-fonts-cjk
```

## 卸载软件

```sh
sudo pacman -Rsnv firefox thunderbird gimp hexchat xfburn xfce4-dict catfish pidgin mousepad vlc-nightly audacious xfce4-screenshooter
```

假如因为依赖问题卸载掉系统图片管理器`ristretto`(系统自带图片浏览)，再安装即可。

## 安装常用软件

```sh
# Repo软件：
sudo pacman -Sv gvim base-devel autojump git axel tmux mpv htop mlocate goldendict shadowsocks proxychains-ng  the_silver_searcher(ag) filezilla

# aur软件：
pacaur -Sv unzip-iconv(支持unzip的-O选项) pycharm-professional xmind typora nutstore chromium(google-chrome) deepin-screenshot electronic-wechat vsftpd(ftp服务器) gimp qbittorrent(bt搜索下载) obs-studio chmsee gpick（取色配色） peek（录屏为gif软件） deepin-terminal ieaseMusic(github) sublime-text-dev-imfix2 

# 其他软件
dbeaver:mysql等数据库连接软件
mariadb：务必参考官网：https://wiki.archlinux.org/index.php/MySQL
redis：redis服务器 https://wiki.archlinux.org/index.php/Redis
mongodb mongodb-tools:MongoDB数据库相关软件 https://wiki.archlinux.org/index.php/MongoDB
Anki:https://apps.ankiweb.net/
zeal:离线文档查看软件
字体:ttf-hack ttf-ms-fonts
kid3-qt:音频meta信息编辑

# 下载软件
yay -Sv uget aria2
# 打开uget》编辑》设置》插件》启用aria2
# 分类》属性》默认一般设置》最大连接数>5
```

## 字体设置

系统字体：Microsoft YaHei
终端字体：YaHei Monaco Hybird Regular

## Dock

软件：`pacaur -S plank`
主题：transparent（系统自带）
选项：`ctrl+鼠标右键`
有些软件无法添加logo：用`thunar`（文件管理器）打开`/usr/share/application`，直接拖拽即可。
plank阴影解决办法：'`Setting > Window manager Tweaks > Compositor`' and uncheck '`Show shadows under dock windows`'.
开机启动：系统自带软件 `Session and Startup` 添加`plank`开机启动。

## panal设置

左上角：`Whisker Menu`，`Directory Menu`

右上角：`Notification Area`，`PulseAudio Plugin`, `Clock`， `Action Buttons`

## 可选dm软件：lightdm

假如系统软件dm崩溃的话，可以自己安装lightdm。

```sh
pacaur -Sv lightdm-gtk-greeter # 依赖lightdm；
systemctl enable lightdm
systemctl start lightdm
```

## SS启动

在目录`/etc/shadowsocks/`下面，复制`example.json`为`config.json`。

启动：`sudo systemctl start/enable shadowsocks@config`

## 主题设置

gtk主题：`pacaur -S adapta-gtk-theme`

xfwm4窗口标题主题：`pacaur -S gtk-arc-flatabulous-theme-git `

icon主题：`pacaur -S la-capitaine-icon-theme-git`(貌似github下载速度更快)；

xfce4-terminal配色：参考 https://github.com/osheep/Xfce4-terminal-colors   

## 更换grub

`yay -Sv grub2-theme-vimix-git`

修改`/etc/default/grub`：

```sh
GRUB_THEME="/path/to/gfxtheme" 为：
GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"`
```

修改`/boot/grub/themes/Vimix/`中的背景

更新grub配置：`grub-mkconfig -o /boot/grub/grub.cfg`

## 常用快捷键

```sh
Ctrl + Alt + Q： deepin-screenshot
Super + E ： thunar
Super + A ： xfce4-popup-whiskermenu
Super + T ： xfce4-terminal
```

> 记得删除系统设置里自带的快捷键(和pycharm、vscode冲突)：
>
> 1、Settings - Window Manager ;
>
> 2、Settings - Keyboard ;
>
> 3、Settings - Settings Editor.


## 其他事项

开机开启Num Lock：Settings - settings Editor - keyboards ,设置Numlock、RestoreNumlock为True。

系统时间显示不对：时区显示的是上海，但是却是0000时区；解决办法：在sudo vim /etc/profile文件中添加export TZ='CST-8'  。

unzip解压zip压缩文件乱码：`unzip -O CP936 zip_file_name`

## 安装QQ

有两种方式：

> 前提：pacaur -Sv wine winetricks wine-mono wine_gecko

1、使用winetricks-zh安装基本可以使用，遇到问题可以参考下面。

2、参考： https://github.com/askme765cs/Wine-QQ

**请务必查看如下内容：，有必要的话，参考“”**

```sh
# 更改.zshrc，默认安装bit32wine，添加如下内容：
export WINEPREFIX=$HOME/.config/wine/
export WINEARCH=win32

source .zshrc # 使.zshrc生效

pacaur -Sv wine wine-mono wine_gecko winetricks-zh-git
# wine-mono # 用于运行依赖Microsoft's .NET Framework的程序
# wine_gecko # 用于运行Microsoft's Internet Explorer的程序
# winetricks # 安装 ddl、组件、字体等，中文版的是自带一些国内的软件等；
# 参考：https://github.com/hillwoodroc/winetricks-zh

locate -ir "腾讯.*tim.desktop" # 查找快捷图标位置，修改无法输入中文bug。
# 插入如下内容：
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```
