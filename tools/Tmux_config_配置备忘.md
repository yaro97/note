# Tmux 教程

> tmux是实现在一个bash屏幕，多开bash进程的工具。

Tips: **服务server》会话session》窗口window》面板pane**

## 1 默认tmux快捷键：

### 1.0 常用命令

```sh
tmux #新开tmux
tmux a #从bash进入tmux
tmux new-session -s name  #新开一个名为name进程
tmux ls #列举当前所有tmux（list-session）
exit #退出当前tmux
tmux kill-server #关闭所有tmux终端
C-b ? #显示快捷键帮助
```

### 1.1 Sessions

```sh
:new<CR>  new session
C+c   new session
s  list sessions
$  name session
```

### 1.2 Windows (tabs)

```sh
c  create window
w  list windows
n  next window
p  previous window
f  find window
,  name window
&  kill window
```

### 1.3 Panes (splits)

```sh
%  vertical split
# "  horizontal split
o < >  swap panes
q  show pane numbers
x  kill pane
+  break pane into window (e.g. to select text by mouse to copy)
-  restore pane from window
⍽  space - toggle between layouts
<prefix> q (Show pane numbers, when the numbers show up type the key to goto that pane)
<prefix> { (Move the current pane left)
<prefix> } (Move the current pane right)
<prefix> z toggle pane zoom
```

### 1.4 Misc

```sh
d  detach #退出并保存当前会话，tmux仍在后台运行，可以通过tmux a进入
t  big clock
?  list shortcuts
:  prompt
```

## 2 使用Oh my tmux

详见 : https://github.com/gpakosz/.tmux

```sh
cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```

Oh my tmux的快捷键如下：

```sh
<prefix> C-c  # creates a new session
<prefix> e  # opens ~/.tmux.conf.local with the editor defined by the $EDITOR environment variable (defaults to vim when empty)
<prefix> r  # reloads the configuration
<prefix> C-f  # lets you switch to another session by name
<prefix> C-h and <prefix> C-l  # let you navigate windows (default <prefix> n and <prefix> p are unbound)
<prefix> Tab brings you to the last active window
<prefix> h, <prefix> j, <prefix> k and <prefix> l let you navigate panes ala Vim
<prefix> H, <prefix> J, <prefix> K, <prefix> L let you resize panes
<prefix> < and <prefix> > let you swap panes
<prefix> +  # maximizes the current pane to a new window
<prefix> m toggles mouse mode on or off
<prefix> U launches Urlview (if available)
<prefix> F launches Facebook PathPicker (if available)
<prefix> Enter enters copy-mode
<prefix> b lists the paste-buffers
<prefix> p pastes from the top paste-buffer
<prefix> P lets you choose the paste-buffer to paste from
C-l clears both the screen and the history
```

## 3 个性化设置

不需要修改`.tmux.conf`,相应个性化在`.tmux.conf.local`文件中即可完成。

### 3.1 调整默认`.tmux.conf.local`文件

increase history size

start with mouse mode enabled

force Vi mode

replace C-b by C-a instead of using both prefixes（M-b 表示设置为alt+b）

### 3.2 启动shell时自动启动tmux：

> 参考：https://wiki.archlinux.org/index.php/Tmux

在`.zshrc`文件中添加如下内容：

```sh
# TMUX
if which tmux >/dev/null 2>&1; then
    #if not inside a tmux session, and if no session is started, start a new session
    test -z "$TMUX" && (tmux attach || tmux new-session)
fi
```

### 3.3 快捷键划分pane

创建文件`/home/yaro/.yaro/my_tmux_default_layout`，写入如下内容：

```sh
selectp -t 1    #选中第1个窗格
splitw -h -p 50  #将其分成左右两个
selectp -t 1     #选中第1个，也就是左边那个
splitw -v -p 50  #将其分成上下两个，这样就变成了图中的布局了
selectp -t 3     #选回第3个
```

在`.tmux.conf.local`中添加如下内容：

```sh
bind D source-file /home/yaro/.yaro/my_tmux_default_layout \; display "Splited ^_^ !"
```
