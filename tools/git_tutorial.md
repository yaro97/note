# Git Tutorial 教程

参考：  
https://www.atlassian.com/git/tutorials  
https://ndpsoftware.com/git-cheatsheet.html  
http://rogerdudler.github.io/git-guide/

![git简单示意图](http://image.beekka.com/blog/2014/bg2014061202.jpg)

## 基本命令

git三层结构：working directory, staging index, git directory(repository)
git四种状态：untracked, modified, staged, committed.

```sh
git init  # 初始化
git config --global user.name yaro
git config --global user.email yaro@demo.com
git config --list

git status
git add .
git commit -m "massage"
git commit -am "msg"  # 直接将工作区所有tracked文件提交到repo，不经过staged；
git log
git log --oneline
git log -5 # 只看最近5次；
git log --graph --oneline --decorate
git blame fiel_name
git shortlog -sn  # 看每个人提交了多少次；
```

## 撤销操作

```sh
git commit --amend # Modify the last commit with the current index changes(将index文件重新提交-修改上一次commit），可以用作修改上一次commit的msg；
git checkout -- file_name  # 从repo里面恢复到working；
git reset HEAD file_name  # 从repo里面恢复到staging，HEAD可以是任何一次提交的ID；
# --hard                    -- match the working tree and index to the given tree   
# --mixed                   -- reset the index but not the working tree (default)  
# --soft                    -- do not touch the index file nor the working tree  
```

## 删除操作

```sh
删除文件后使用 git add .  # 先删除文件，在提交到staging；
git rm file_name  # 直接删除working和staging里面的文件，前提是二者一致；
git rm -f file_name  # 当working和staging不同时，强行都删除。
git rm --cached file_name  # 只删除staging里面的文件，working保留；
mv重命名，git add. # 常规提交，先删除原文件，再新建新文件；
git mv file1 file2  # 在修改working的同时，也修改staging；
```

## 分支

```sh
git branch dev # 创建dev分支
git branch # 查看所有分支；
git checkout dev  # 切换到dev分支；
git checkout -b dev1 # 创建dev1分支，并且换到dev1；
git branch -d dev  # 删除dev分支；
git branch -m dev1 fix # 修改分支名称为fix；

HEAD指针执行当前branch的最新版本；

git merge dev  # 把dev分支，合并到当前分支；

git diff  # 默认比较working和staging的不同；
git diff --staged  # 比较staging和repo的不同；
git diff xxxx xxxx # 比较两个repo版本号，hash值最少4个，推荐6-8；
git diff fix  # 比较当前分支和fix分支的区别；

git stash  # 当一个分支没有commit处理干净，需要先存储当前状态在切换到另一个分支；
git stash list  # 列出所有stash；
git stash apply stash_name # 读取stash
git stash drop  stash_name  # 删除stash
git stash pop stash_name  # 读取的同时并删除；
```

# 远程仓库

```sh
git push xxx
git clone xxx
git pull xxx

ssh-keygen -t rsa # 其实默认就是rsa‘

git remote add name github_url  # 可以为github_url地址起名字；
git remote -v  # 查看起的名字；
```

## 自己搭建远程repo

```sh
ssh yaro@....  # 登录远程vps；
mkdir paotime.com.git  # 通常带有.git
git init --bare  # 初始化一个裸仓库；
# 之所以叫裸仓库是因为这个仓库只保存git历史提交的版本信息，而不允许用户在上面进行各种git操作，如果你硬要操作的话，只会得到下面的错误（”This operation must be run in a work tree”）。这个就是最好把远端仓库初始化成bare仓库的原因。

git push ssh://root@x.x.x.x/var/paotime.com/git master  # 推送本地到vps

ssh-copy-id root@x.x.x.x  # 免密码登录；
```

## 其他

```sh
.gitignore 文件 # 可以使用通配符，文件使用“file_name”,文件夹使用"folder_name/" 
git rm xxx --cached  # 写入.gitignore文件可以是新建文件生效，但是修改这个文件需要执行这个命令才生效；

git help help # 查看帮助文档的用法；
```

## 关于 reset checkout revert

参考：https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting

**1 Commit-level**

```sh
git reset HEAD~2  # HEAD退后两个commit，这两个commit记录作废；
--soft repo还原；
--mixed repo、index还原(默认)；
--hard repo、index、workspace还原；

git checkout hotfix  # 切换到hotfix分支，会rewrite workspace，切换前记得commit OR stash。
git checkout HEAD~2  # 也可以退后两个commit，可以查看之前的状态；但是再次commit之前，记得新建分支。

git revert HEAD~2  # HEAD根据 2nd to last commit，在最新的commit后面，创建一个新的commit；会rewrite workspace，记得commit OR stash。
```

**2 File-level**

```sh
git reset HEAD~2 foo.py  # commit->index;还原index为2nd-to-last commit的状态，没有soft mixed hard 等选项。

git checkout HEAD~2 foo.py  # commit->workspace;还原workspace为2nd-to-last commit的状态。
# 文件 foo.py 前面最好使用 -- ;
# 在Git中，默认git checkout 命令后面跟的是branch，但是没有这个branch的话，会自动搜索对应的文件；git checkout -- 命令后面跟文件/夹；
# git checkout -- --mydirectory 可以还原名称--mydirectory的文件;
# touch -- -testfile ，-- 后面表示跟的是文件，说不出参数。

git revert 不能接受file参数；
```