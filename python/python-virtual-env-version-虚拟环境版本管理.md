# python虚拟环境管理

Tags：python虚拟环境，pyenv,virtualenv,virtualenvwrapper,conda,anaconda

> 参考：
https://github.com/pyenv/pyenv
https://github.com/pyenv/pyenv-virtualenv

[TOC]

## pyenv工具

pyenv可以用来管理和切换不同的python版本，相比用virtualenv和anacondo来创建虚拟python环境，pyenv的使用更简易轻便。

**安装：**

方法1、使用github官网安装；

方法2、使用pacaur等linux包管理工具安装；

> 下面使用git官网安装，记得把下面的`zsh`根据情况更改为`bash`。

### 安装pyenv

```sh
git clone https://github.com/pyenv/pyenv.git ~/.pyenv # clone到～/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc # 声明PYENV_ROOT变量为pyenv路径
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc # 把pyenv变量写入环境变量PATH
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc # 写入shims等
#上一句命令也可使用：echo 'eval "$(pyenv init -)"' >> ~/.bashrc

exec "$SHELL" # 重启zsh，使path失效

cd $(pyenv root)
git pull # 更新pyenv

rm -rf $(pyenv root)

注释 `.zshrc` 的 `pyenv init` 一行 # 禁用pyenv；
```

### 安装virtualenv插件

```sh
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv # 下载virtualenv插件
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

exec "$SHELL"
```

### 使用pyenv

和git命令类似，pyenv也是以第二个参数为子命令。常用命令如下：

```sh
pyenv commands # 列举所有可用的命令；

pyenv local 2.7.6 # 设置当前文件夹局部python版本 application-specific Python version；
pyenv local # 查看python版本
pyenv local unset # 重置

pyenv global 2.7.6 # 设置全局python版本used in all shells
pyenv global
pyenv global unset

pyenv shell pypy-2.2.1 # shell-specific Python version
pyenv shell
pyenv shell unset

pyenv install --list/-l # 查看所有可以安装的python版本
pyenv install 2.7.6 # 安装2.7.6版本
pyenv uninstall [-f|--force] <version> # 卸载特定版本

pyenv version # 查看当前版本
pyenv versions # 查看所有版本

pyenv rehash # 重新安装shims，当新安装python时运行
pyenv which python3.3 # 查看python3.3命令的位置
pyenv whence 2to3 # Lists all Python versions with the given command installed
```

### 使用virtualenv插件(虚拟环境ENV)

```sh
pyenv version # 查看现有python版本，假设是3.6.2
pyenv virtualenv venv3.6.2 # 根据现有版本创建虚拟环境
pyenv virtualenv 2.7.10 my-virtual-env-2.7.10 # 创建2.7.10版本的虚拟环境
pyenv virtualenvs # 查看所有已创建的虚拟环境
pyenv activate <name> # 激活
pyenv deactivate # 退出
pyenv uninstall my-virtual-env # 删除虚拟环境
```

### virtualenv插件和virtualenv/venv

There is a venv module available for CPython 3.3 and newer. It provides an executable module `venv` which is the successor of `virtualenv` and distributed by default.

`pyenv-virtualenv` uses `python -m venv` if it is available and the `virtualenv` command is not available.

### virtualenv插件和Anaconda/Miniconda

You can manage `conda` environments by `conda` create as same manner as standard Anaconda/Miniconda installations. To use those environments, you can use `pyenv activate` and `pyenv deactivate`.

If `conda` is available, `pyenv virtualenv` will use it to create environment by `conda create`.

##　virtualenv工具

安装：`pip install virtualenv`

使用：

```sh
cd my_project_folder # 进入项目目录
virtualenv venv # 创建虚拟环境（在项目目录中生成虚拟环境文件夹）；
virtualenv -p /usr/local/bin/python3 venv # 可以制定python版本；
virtualenv --no-site-packages [虚拟环境名称] # 默认会复制环境中已安装的包，此命令可以去除；
source my_project_folder/bin/activate # 进入虚拟环境
deactivate # 退出虚拟环境
rm -rf venv/ # 删除虚拟环境
```

## Virtaulenvwrapper

Virtaulenvwrapper是virtualenv的扩展包，用于更方便管理虚拟环境。

安装

```sh
pip install virtualenvwrapper # 安装

#此时还不能使用virtualenvwrapper，默认virtualenvwrapper安装在/usr/local/bin下面，实际上你需要运行virtualenvwrapper.sh文件才行，打开这个文件看看,里面有安装步骤，我们照着操作把环境设置好。

# 创建目录用来存放虚拟环境
mkdir $HOME/Envs

# 编辑~/.zshrc或~/.bashrc（根据你使用shell类型决定）
export WORKON_HOME=$HOME/Envs
source /usr/local/bin/virtualenvwrapper.sh

source ~/.zshrc
```

基本使用

```sh
workon 或者 lsvirtualenv # 列出所有虚拟环境
mkvirtualenv [虚拟环境] # 新建虚拟环境
workon [虚拟环境] # 激活虚拟环境
deactivate # 退出虚拟环境
rmvirtualenv [虚拟环境名称] # 删除虚拟环境
```