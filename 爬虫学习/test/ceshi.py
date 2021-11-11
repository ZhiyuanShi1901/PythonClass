#测试urllib

# import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #使用decode(utf-8)解析之后能够解析成合理的网页形式


#获取一个post请求

import urllib.parse
import urllib.request
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding = "utf-8")   #转化二进制数据包，内部可以放键值对
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
# 	response = urllib.request.urlopen("http://httpbin.org/get",timeout=3)
# 	print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
# 	print("time out!")

# response = urllib.request.urlopen("http://www.baidu.com",timeout=3)
# print(response.getheader("Server"))


#伪装浏览器
url = "http://httpbin.org/post" #重新包装
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 FS"
}
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

