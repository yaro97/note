# win10安装linux子系统（WSL-windows subsystem linux）

## 安装ubuntu子系统

- 系统设置-开发人员-打开开发人员模式；  
- 程序和功能 - 启用或关闭windows功能；  
- 重启电脑；  
- 打开win10应用商店，搜索ubuntu安装; 
- `ubuntu`命令进入ubuntu（默认可以设置为zsh），`bash`命令进入ubuntu的bash；  

> 新版的linux系统已经集成到应用商店中，除了ubuntu还有其他系统，当然推荐安装ubuntu系统；

## 安装Hyper及zsh相关工具

- Hyper [github下载](https://github.com/zeit/hyper),官网的版本太落后，中文无法显示；  
- apt 安装 curl, git, zsh等工具  
- 安装 oh my zsh 及相关插件；  

```sh
# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# 安装插件：zsh-autosuggestions（仿fish自动提示，右方向键补全所有，ctrl+右方向键-补全字符）
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

# 安装插件：zsh-syntax-highlighting（仿fish自动高亮）
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# 启用插件：git sudo history autojump zsh-autosuggestions zsh-syntax-highlighting 等；
vim ~/.zshrc # 修改其中的：plugins=(xxx)
sudo chsh -s /usr/bin/zsh
```

## Hyper技巧

- `explore.exe 目录`可以打开指定目录，当然可以alias；  
- 配置文件`.pyper.js`可以制定启动时执行ubuntu(`shell: 'ubuntu.exe',`和`shellArgs: [],`)；  


## Hyper美化

- `npm install -g hpm-cli`首先安装`hpm`管理工具，使用帮助`hpm help`;  
- 然后使用hpm工具安装相应的插件即可，推荐："hypercwd", "hyper-materialshell", "hyperline"；  

具体查看[awesome-hyper](https://github.com/bnb/awesome-hyper)项目，有很多插件；  

## 禁止Bash声音

- 搜索了下,执行`echo "set bell-style none" >> ~/.inputrc`即可,或者是修改`/etc/inputc`;  
- 上述方法没有效果的话: 右键右下角声音控制 - 选择"声音混合器", 然后打开`bash` - 触发声音 - '声音混合器'会出现对应的声音 - 静音即可;




