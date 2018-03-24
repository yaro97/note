# WireShark使用备忘

参考：

WireShark自带的本地参考文件

http://www.zhoulujun.cn/zhoulujun/html/theory/network/2016_1130_7908.html

http://www.vuln.cn/2267

## 需要说明的点

- WireShark监控某个网卡的流量。
- OSI模型：物理层/数据链路层/网络层/传输层/（会话层/表示层/）应用层。
- TCP/IP五层模型：物理层/链路层/网络层/传输层/应用层。
- WireShark可以监控某个连接的各层的数据，so，（ARP/IP）、（TCP/UDP）、Http等都可以监控。
- WireShark只能抓取数据，不能解析/伪造/篡改。

## 善用统计功能

善用其统计功能，图形显示很直观/强大。

## 抓包过滤

抓取前先设定好过滤，只抓取某些数据。

`Capture - Option` 可以选择对应的 Interface； 同时也可以输入/选择对应的过滤条件。

## 数据过滤

对抓取的数据进行进一步的过滤。

## Follow TCP Stream

对于Tcp协议，可以对某帧TCP数据进行 `Follow TCP Stream` 。

## 过滤规则技巧

- 输入相应规则时会有颜色提示：绿色表示正确，其他表示错误。
- 可以在对应的规则上面 `右键` - `应用过滤`。（很方便！！）

## 过滤语法

更多内容请参考：WireShark本地帮助文件。

- 比较运算符

```
    eq, ==    Equal
    ne, !=    Not Equal
    gt, >     Greater Than
    lt, <     Less Than
    ge, >=    Greater than or Equal to
    le, <=    Less than or Equal to
```

- 布尔运算符

```
    and, &&   Logical AND
    or,  ||   Logical OR
    not, !    Logical NOT
```

- Search and Match运算符

- Protocol field types

- The slice operator

- The membership operator

- Type conversions


## 常用过滤规则

```
ip.addr == xx.xx.xx.xx  
ip.src ==  #本地ip 
ip.dst ==  #目标ip
===
arp/dns/http/tcp/udp  # 各协议  
dns and http  
dns or http  
===
tcp.port == 443
===
tcp.analysis.flags  所有有问题的tcp
# 可以再分析中查看
===
!(arp or dns or icmp)  # 排除
===
TCP协议的记录上右键- follow stream，可以查看tcp对话。
==
tcp contains facebook  # 查看tcp协议的传输内容中包含 facebook 的
udp contains facebook
dns contains facebook
===
http.request
http.response
http.response.code == 200
===
tcp.flags.syn == 1  # 可用于查看是否被攻击
tcp.flags.reset == 1
===
sip && rtp && rtsp  # 流媒体
```