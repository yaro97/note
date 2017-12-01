---
title: Hexo-Github建博客教程
tags:
- hexo
- github page
- 搭建博客
---
本人=一名小白,而且我对网站开发以及前端的知识几乎是零基础,所以在自己刚接触这个东西的时候,我像很多人一样,都是上网找教程,但是要知道,那都是程序员的教程.一路摸爬滚打,终于搞定了,这篇文章算是自己的操作记录,为以后的重新搭建留个备忘...

参考官网:https://hexo.io/docs  
参考网站1:http://jiji262.github.io  
参考网站2:http://sufaith.com/2016/02/27/Hexo%E8%BF%81%E7%A7%BB/

## 安装Hexo

Hexo需要安装`Node.js`和`Git`.二者的安装可以到相应的官网下载安装即可.注意`apt-get`安装的`Node.js`不是最新版本. 具体参考[hexo官网](https://hexo.io/docs  ).  

在任意目录下(如`E\hexo`)文件夹中运行

```bash
npm install hexo-cli -g 
```

注:卸载hexo可尝试`npm uninstall hexo-cli`.

## 初始化Hexo

在相应目录下(如`E\hexo`)文件夹中运行

```bash
hexo init blog #建立文件夹`blog`,并在其中初始化hexo
cd blog #进入`blog`目录
npm install #npm安装package.json中的依赖包
npm install hexo-deployer-git --save #安装deploy插件,后续部署github需要.
```

<!--more-->

初始化完成后,可以`hexo generate`,`hexo server`查看是否能正常访问本地博客`http://localhost:4000`.  
安装成功后可以使用`hexo -v`查看本地配置环境

## Hexo主题

### 下载主题

- 可以直接下载相关zip文件,解压缩到`.../hexo/themes`文件夹下

- 可以在`blog`目录下运行`git clone https://github.com/iissnan/hexo-theme-next themes/next`将next主题下载到themes文件夹下(推荐,可以使用`git pull`更新主题).

### 启用主题

编辑配置文件`_config.xml`中的主题名为`themes`文件夹下对应的文件夹名.然后运行如下命令.

```bash
hexo clean #清理hexo缓存
hexo s #重新启动本地web服务器
```

主题的其他设置见next主题[官网](http://theme-next.iissnan.com/).

## 创建Github pages

- 在线创建库并起名`yaro97.github.io`,在设置中通过` Launch automatic page generator`生成github page即可  
**注意:**`name`要是唯一的话,生成的网址为`name.github.io`,若不唯一,网址为`yaro97.github.com/name.github.io`

## 部署本地Hexo到Github pages

- 注意部署前一定要安装插件`hexo-deployer-git`.前面已经安装

- 修改`_config.xml`文件

    ```bash
    deploy:
        type: git
        repo: https://github.com/yaro97/yaro97.github.io.git
        branch: master
        name: yaro
        email: wyzh97@gmail.com
    # 具体设置可以参考hexo官网.
    ```

- 执行命令`hexo d`完成部署,过程中需要github账号/密码,账号为`yaro97`.

## 自定义域名

### 绑定主域名

- 在新建的`repository`中新建文件`CNAME`,内容填写:
    
    ```bash
    www.paotime.com
    paotimecom
    ```

- 在阿里云中,添加域名解析,内容如下:

    ```bash
    记录类型:A; 主机记录:@; 记录值:192.30.252.153.
    记录类型:A; 主机记录:www; 记录值:192.30.252.153.
    ```

### 绑定二级域名

- 在新建的`repository`中新建文件`CNAME`,内容填写:

    ```bash
    blog.paotime.com
    ```

- 在阿里云中,添加域名解析,内容如下:

    ```bash
    记录类型:CNAME; 主机记录:blog 记录值:paotime.github.io. #注意这个点`.`
    ```

## 在两个台电脑同时更新

### 对A电脑的操作如下

1. 在github新建仓库名为blog
2. 上传A电脑本地Hexo博客的源文件夹至github的blog仓库，流程如下：

    - 删除根目录和主题目录下的.git文件夹
    - 修改根目录下的.gitignore文件为：

        ```bash
        /.deploy_git
        /public
        ```

    - 依次执行以下指令，同步源文件至github

        ```bash
        git init 
        git add .
        # 若出现`warning: LF will be replaced by CRLF in`
        # 执行:
        # git config --global core.autocrlf  false
        git commit -m "first commit"
        git remote add origin git@github.com:yaro97/blog.git
        git push -u origin master
        # 此时可能会出错failed to push some refs to git  出现错误的主要原因是github中的README.md文件不在本地代码目录中，可以通过如下命令进行代码合并
        # git pull --rebase origin master
        # 此时再执行语句 
        # git push -u origin master
        ```

### 对B电脑的操作如下：

1. 安装Git，并配置github账号下的B电脑的.ssh
2. 安装Node.js
3. 使用npm指令安装Hexo  

    ```bash
    npm install -g hexo-cli
    ```

4. 使用Git bash随便选择一个文件夹,执行git clone

    ```bash
    git clone git@github.com:yaro97/blog.git
    ```

至此，两个电脑的hexo环境一致，Hexo博客源文件一致.倘若还有C电脑,重复B电脑的操作即可.  
这里需要说明的是:在blog

## 关于日常的改动流程（A，B两台电脑均使用的情况下）

1. 建议先检查更新git pull，将本地博客源文件更新至最新版本

    ```bash
    git pull
    ```

2. 然后可以新建或修改博客内容，进行预览等操作

    ```bash
    hexo new <新的博客名称>
    hexo server
    ```

3. 新建博客后，先同步Hexo源文件，将修改后的源文件同步至github

    ```bash
    git add . #不添加被删除的文件,`git add -A`会添加所有修改.
    git commit -m "更新描述"
    git push origin master
    ```

4. 然后再执行Hexo的生成文件和部署指令

    ```bash
    hexo g -d #hexo generate && hexo deploy
    ```