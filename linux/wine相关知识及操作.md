# wine相关知识及操作
Tags：wine，winetricks，wine-tim，wine-qq
参考网页：
[Wine-wiki(简体中文)][]
[Wine-wiki(简体中文)]: https://wiki.archlinux.org/index.php/Wine_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\

[TOC]
## 安装
> 声明：wine不是沙箱，可以访问计算机的任何东西，所以windows下的病毒一样可以运行。
wine可以在官方仓库下载，但是前提需要启用pacman.conf里面的multilib仓库（针对32bit软件），然后更新包数据库。
默认的wine是32bit的程序，所以它不能运行64bit的windows程序；其实运行64bit程序正在实验阶段，还不是太成熟；
总结一下，配置WINEARCH=win32后，x86_64平台的Arch和i686平台的Arch完全相同；
## 配置
### 配置Wine的方式通常有：
`winecfg`是Wine的图形界面配置程序。控制台下调用`$ winecfg`（或指定系统目录：`$ WINEPREFIX=~/.系统目录 winecfg`）即可启动
`control.exe`是Windows控制面板的Wine实现，通过`$ wine control`命令启动
`regedit`是Wine的注册表编辑器，比较前两者，该工具能配置更多东西。
### WINEPREFIX：
Wine默认将配置文件和安装的Windows程序保存在`~/.wine`。这样的目录称为一个"`Wine prefix`"或"`Wine bottle`"（保留原文，下文称“系统目录”）。每次运行Windows程序（包括内置程序，如winecfg）时，系统目录会自动创建（如果缺失）或更新。系统目录中存放有相当于Windows下 `C:\`C盘（更确切的说应是系统盘）的文件夹。
通过设置WINEPREFIX环境变量，可以更改Wine系统目录的位置。如果希望让不同的Windows程序使用不同的系统环境或配置，这一变量会非常有用。
> 例如，如果您使用 `env WINEPREFIX=~/.win-a wine A程序.exe`来运行一个程序。另一个使用 `env WINEPREFIX=~/.win-b wine-B程序.exe`，这两个程序将使用独立的C盘和注册表配置。
### WINEARCH
对于64位用户，如果使用`[multilib]`仓库里的Wine，默认创建的系统目录是64位环境的。若想使用纯32位环境，修改WINEARCH 变量win32为即可： `WINEARCH=win32` `winecfg`这样就会生成32位Wine环境。若不设置WINEARCH得到的就是64位环境。
通过WINEPREFIX变量，在不同的系统目录分别创建32位和64位环境：
```sh
$ WINEARCH=win32 WINEPREFIX=~/win32 winecfg  
$ WINEPREFIX=~/win64 winecfg
```
> 提示： 编辑 ~/.bashrc OR .zshrc，使得 WINEPREFIX 和 WINEARCH 永久生效。
```sh
export WINEPREFIX=$HOME/.config/wine32/  
export WINEARCH=win32
```
## 其他相关安装包
wine-mono # 用于运行依赖Microsoft's .NET Framework的程序；
wine_gecko # 用于运行Microsoft's Internet Explorer的程序；
winetricks # 安装 ddl、组件、字体、软件等，国内版的还可以安装国内的软件；

## 常用命令
```sh
wine xxx.exe # 安装软件
msiexec /i path_to_msi # 安装msi文件
wine start xxx.xxx # 安装软件（不是exe结尾）
winecfg # 配置wine环境，～/.wine
winetricks # 打开winetricks
wine uninstaller # 卸载程序
wine-server -k # 终止wine
wine xxx.exe # 运行UI程序默认的wine环境
env LANG=zh_CN.UTF-8 wine ‘C:\Program Files...QQScLauncher.exe’ # 使用中文系统运行wine环境的软件
env WINEPREFFIX=/home/yaro/.../wineprefix/tim wine ‘C:\Program Files...QQScLauncher.exe’ # 使用tim环境下wine运行当前环境下的软件
wineconsole xxx.exe # 运行cmd程序
winedbg xxx.exe # 调试程序
```
## 中文乱码
> 只是部分解决
创建 zh.reg 文件，写入如下内容：
然后运行 regedit zh.reg
```
REGEDIT4
 
[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\FontLink\SystemLink]
"Lucida Sans Unicode"="wqy-microhei.ttc"
"Microsoft Sans Serif"="wqy-microhei.ttc"
"Tahoma"="wqy-microhei.ttc"
"Tahoma Bold"="wqy-microhei.ttc"
"SimSun"="wqy-microhei.ttc"
"Arial"="wqy-microhei.ttc"
"Arial Black"="wqy-microhei.ttc"
```
