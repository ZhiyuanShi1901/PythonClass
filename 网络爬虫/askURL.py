# askURL
# coding=utf-8
import urllib.request, urllib.error  # 指定url 获取网页数据
import urllib.parse
import urllib.request
# 得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"
    }

    data = {
        "username": "cheshiresnake"
        "password": "WWW.SHIZHIYUAN13"
    }

    request = urllib.request.Request(url, headers=head)  # 封装头部信息，，避免爬虫程序被反爬虫

    html = ""

    try:
        response = urllib.request.urlopen(request)  # 返回头部信息所获取到的数据
        html = response.read().decode("utf-8")    # 读取数据并解码，输出为html
        # print(html)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html
