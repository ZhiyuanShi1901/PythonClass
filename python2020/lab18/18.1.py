# 18.1
# coding=utf-8

import requests
import re

baseurl = 'http://www.upc.edu.cn/'

r = requests.get(baseurl)  # 获取石油大学首页
r.raise_for_status()      # 对获取的url进行解析
r.encoding = r.apparent_encoding

shouye = r.text   # 返回出来字符串

https = re.findall(r'href="(http.*?)"', shouye)   # 对前面具有href和句中具有http的链接进行搜索取出，返回一个列表
print(https)

with open('https.txt', 'w') as hrp:
    for item in https:
        hrp.write(item)
        hrp.write('\n')
