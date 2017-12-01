# cURL工具介绍

参考：[用法参考](http://stackeye.com/categories/curl/)  
测试工具：[http://httpbin.org/](http://httpbin.org/)

curl = "see url" OR "Client for URLs"

curl wget 对比：wget主要用于下载文件，curl主要来REST API交互调试；当然二者功能有交叉。

REST：全称是 Resource Representational State Transfer：通俗来讲就是：资源在网络中以某种表现形式进行状态转移。分解开来：Resource：资源，即数据（前面说过网络的核心）。比如 newsfeed，friends等；Representational：某种表现形式，比如用JSON，XML，JPEG等；State Transfer：状态变化。通过HTTP动词实现。

简单的说：用URL定位资源，用HTTP描述操作；看URL就知道要什么，看HTTP METHOD就知道要干什么，看HTTP STATE CODE就知道结果如何。

首先为什么要用RESTful结构呢？：大家都知道"古代"网页是前端后端融在一起的，比如之前的PHP，JSP等。在之前的桌面时代问题不大，但是近年来移动互联网的发展，各种类型的Client层出不穷，RESTful可以通过一套统一的接口为 Web，iOS和Android提供服务。另外对于广大平台来说，比如Facebook platform，微博开放平台，微信公共平台等，它们不需要有显式的前端，只需要一套提供服务的接口，于是RESTful更是它们最好的选择。

[参考链接](https://www.zhihu.com/question/28557115/answer/48094438)

**用法实例：**

```sh
curl http://www.baidu.com
curl http://localhost:5000/methods
curl http://localhost:5000/json-test
curl -i http://localhost:5000/json-test # --include 包含protocol response headers；
curl -I  http://httpbin.org/ip #--head Show document info only
curl -d "first=Yaro&last=Seth" http://localhost:5000/methods  # --data
curl -X PUT -d "first=Yaro&last=Smith" http://localhost:5000/methods
curl -X DELETE http://localhost:5000/methods
curl http://localhost:5000/secrets
curl -u yaro:pass http://localhost:5000/secrets
curl -o/--output index.html http://www.baidu.com
curl -C -  http://xxx.QProtect2.8.exe  # -C/--continue-at <offset>，上次ctrl+c结束后，自动检测断点续传；
curl -u ftpuser:ftppass -O ftp://ftp_server/index.php  # ftp下载需要登录；
curl -s/--silent -o/--output index.html http://www.baidu.com  # 静默执行；
curl -v/–verbose http://www.baidu.com  # 查看通讯过程、调试；所有命令都可以 -v ；
curl --trace-ascii debug.txt http://www.baidu.com  # 更详细的调试信息；
curl -A/–user-agent  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" http://www.stackeye.com
curl -A  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" -e/–referer http://www.baidu.com http://www.stackeye.com
# http://www.stackeye.com将检测到来源网站为http://www.baidu.com,有些网站防止图片盗链（防止站外引用）。
curl -A  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" -e http://www.baidu.com -D/--dump-header stackeyecookie.txt http://www.stackeye.com
# 保存头部信息，头部信息中包含最常使用的cookie信息；
curl -A  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" -b "user=Adeploy;pass=password" http://www.stackeye.com  # 或者加载cookie文件；
curl -A  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" -e http://www.baidu.com -b/--cookie stackeyecookie.txt http://www.stackeye.com
# -b后可直接加-D保存的文件，curl会自动从中读取出cookie值，而且-b选项不会修改此文件。
-L/--location  # 可以跟踪重定向，有些网站迁移，会redirect网页；
```
