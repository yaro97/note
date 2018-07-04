# requests模块

我们已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。

更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

## 1 安装requests

如果安装了Anaconda，requests就已经可用了。否则，需要在命令行下通过pip安装：

```sh
$ pip install requests
```

如果遇到Permission denied安装失败，请加上sudo重试。

## 2 使用requests

项目参考：[JiePai_ajax_re](https://github.com/yaro97/spider_projects/blob/master/JiePai_ajax_re/main.py)

```python
import requests
response = requests.get('http://www.baidu.com') # post/put/delete/head/options
# 记得使用 http://httpbin.org 网站测试
data = {
'name':'bob',
'age':22
}
response = requests.get('http://httpbin.org/get', params=data)
response.status_code
response.text  # html内容（字符串）
response.content  # 返回二进制的数据（bytes）,图片/多媒体等
response.cookies  # 还有url/history/属性
r.encoding  # 'utf-8' 当前网页编码
r.headers  # 获取响应头

#对于特定类型的响应，例如JSON，可以直接获取：
response.json() # 如果返回的是json格式字符串,可以直接转变成dict;等同于josn库里面的json.loads(response.text)


# 添加headers
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
response = requests.get('https://www.zhihu.com/explore', headers = headers)

# post请求
data = {'name':'bob', 'age': '22'}
headers = {........}
response = requests.post('http://httpbin.org', data = data, headers = headers)

#requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON
# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。


# 文件上传
files = {'file':open('test.jpg', 'rb')}
response = requests.post('http://httpbin.org',file=files)

# 获取cookies
response = requests.get('http://www.baidu.com')
for key, value in response.cookies.items():
print(key + '=' + value)

# 会话维持
# 证书验证
# 代理设置
proxies = {'http':'http://127.0.0.1:9743', 'https':'https://127.0.0.1:9744'}
response = requests.get('http://www.taobao.com', proxies = proxies)

# 要指定超时，传入以秒为单位的timeout参数：
r = requests.get(url, timeout=2.5) # 2.5秒后超时

# 写入多媒体文件
with open('test.jpg', 'wb') as f:
f.write(response.content)

# 认证设置
# 异常处理
```

## 小结

用requests获取URL资源，就是这么简单！