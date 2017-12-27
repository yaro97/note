1、 docker pull xxx

2、 docker images 

3、 创建（run）容器

```sh
- docker run -it chusiang/takaojs1607 bash
# 建立容器并启动，并绑定到标准输入上，exit退出
- docker run -it -d chusiang/takaojs1607 tail -f /dev/null
# 使用 daemon 模式建立容器并启动
- docker run -it -v ~/Downloads:/data chusiang/takaojs1607 bash
# 建立容器并启动，且挂载到本机目录（local 在前 container 在后），exit退出；
```

4、 docker ps [OPTIONS]

```sh
docker ps 
# 查看已启动 running 的containers
docker ps -a, --all
# 查看所有状态的containers
```

5、 docker stop 容器名/id

6、 docker start 容器名/id

7、 进入容器（exec）

```sh
# 前面用了 -d  daemon模式run容器，需要使用exec进入、操作；
# run是直接就进去了，exec 是先开启，需要时再进去；
docker ps
docker exec -it 容器名/id bash
```

8、 提交image（commit），储存现有container状态

```sh
docker ps
docker commit 473e79d4d5f tacaojs1607
docker commit -m "提交信息" -a "作者"  473e79d4d5f tacaojs1607
```

9、 修改标签（tag）

```sh
docker tag IMAGE[:TAG] [REGISTRYHOST/] [USERNAME/]NAME[:TAG]

docker images
docker tag 473e79d4d5f tacaojs1607:1.0
# 通过IMAGE ID 修改TAG

docker tag tacaojs1607 tacaojs1607:1.1
# 通过 REPOSITORY 名称修改TAG

docker tag tacaojs1607:latest tacaojs1607:1.2
```

10、 移除 iamge 和 tag （rmi）

```sh
docker rmi [OPTIONS] IMAGE [IMAGE...]

docker images
docker rmi 473e79d4d5f
# 通过 image id 删除image

docker rmi tacaojs1607:1.2
# 移除标签

docker run hello-world
docker rmi -f hello-world
# 强制移除（包含正在运行的容器）
```

11、 移除容器（rm）

```sh
docker rm [OPTIONS] CONTAINER [CONTAINER ...]

docker ps -a
docker rm 473e79d4d5f
# 移除已经停止的容器

docker rm -f 473e79d4d5f
# 强制移除容器
```

12、 上传iamge（push）

```sh
docker push NAME[:TAG] [OPTIONS]

# 需要登录Docker Registry才可使用:docker login .. 。
# Docker Hub: <USERNAME>/<REPO_NAME>
# Private Docker Registyr: <SERVER_NAME>/<REPO_NAME>

docker images

docker tag 473e79d4d5f <USERNAME>/foo
docker tag 473e79d4d5f <SERVER_NAME>/foo

docker push <USERNAME>/foo
docker push <SERVER_NAME>/foo
# 上传 image
```

使用案例

```sh
docker pull chusiang/takaojs1607 # Get docker image.

docker port $(docker run --name e2e -d -P chusiang/takaojs1607) 5900
 0.0.0.0:32820
# Get vnc port (5900 port on guest os).

open vnc://:secret@127.0.0.1:32820
# Remote with VNC client.on macOS.

##  e2e test with angular-seed

docker exec -it e2e bash  # Enter e2e container.
root@9ecd32e05262:/# su - seluser # Switch user.
seluser@9ecd32e05262:~$ git clone https://github.com/angular/angular-seed.git && cd angular-seed
#Get angular-seed repo with git.
npm install # Install npm packages
npm run start &   
# Start server

npm run protractor  # Run e2e test.



```

