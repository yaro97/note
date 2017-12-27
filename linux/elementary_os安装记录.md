- 可以卸载的软件

  ```sh
  Epiphany
  Browser #Browser
  pantheon-mail  
  #mail
  pantheon-*  #其他内置软件
  Maya    #The official elementary
  calendar.
  Noise   #The official elementary music
  player.
  Scratch     #The text editor that
  works.
  simple-scan #Simple Scanning Utility
  ```

- 终端字体修改

  执行如下命令

  ​`gsettingsset org.pantheon.terminal.settings font 'Roboto Mono 11'`

- gvfsd-smb-brows进程CPU占用太高.

  参考[网页](http://www.codesec.net/view/483645.html)

  在`/etc/samba/smb.conf`文件的 [global]下面添加一行`name resolve order = wins lmhosts bcast.` 倘若没有这个文件,可以`sudo apt-get install samba samba-common`安装相关软件.

- PackageKit进程CPU占用太高.

  参考[网页](https://baheyeldin.com/technology/linux/how-avoid-packagekit-consuming-lots-cpu-and-ram-kubuntu-1404.html)

  卸载相关软件`sudo aptitude purge apperpackagekit-backend-aptcc packagekit-backend-apt packagekit-tools packagekit`

  倘若担心不能及时接收安全更新,可以安装`sudo aptitude install apticron`

- 禁用Guest Session 的方法

  在文件`/usr/share/lightdm/lightdm.conf.d/40-pantheon-greeter.conf`中添加一行`allow-guest=false`

- 安装软件和更新

  执行命令`sudo apt install software-properties-gtk`

- 安装软件与更新

  安装软件源管理,以及驱动管理的图形界面

  `sudoapt install software-properties-gtk`