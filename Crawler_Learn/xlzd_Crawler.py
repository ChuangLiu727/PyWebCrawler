# coding=UTF-8
import requests

resp = requests.get('http://xlzd.me')
resp.status_code

#发送一个完整的http请求

r = requests.post("http://xlzd.me/login", data = {"user":"xlzd", "pass": "mypassword"})
r = requests.put("http://xlzd.me/post", data = {"title":"article"})
r = requests.delete("http://xlzd.me/foo")
r = requests.head("http://xlzd.me/bar")
r = requests.options("http://xlzd.me/abc")

# ## 解析URL中的参数

r = requests.get("http://xlzd.me/query", params={"name":"xlzd", "lang": "python"})
print(r.url)
#字典中的参数会被requests自动解析并且正确连接到URL中。

# ## 响应内容 HTTP response

r = requests.get('http://xlzd.me')

r.encoding

r.headers

r.cookies

#r.text
#响应内容（文件、图片、...）
#r.content

#json内容
#r.json

# ## 自定义Headers

#模拟浏览器是发请求
url = 'http://xlzd.me'
headers = {'User-Agent': 'my custom user agent', 'Cookie': 'haha'}
requests.get(url, headers=headers)

# ## 重定向和超时

r = requests.get('http://xlzd.me', allow_redirects=False)
#allow_redirects参数为False则表示不会主动重定向

r = requests.get('http://xlzd.me', timeout＝3)
#timeout表示这次请求最长我最长只等待多少秒