# duomei
# coding=utf-8

# spider
# coding=utf-8

import requests as req
import bs4
from bs4 import BeautifulSoup
import re
douban = open("doubanreadinglist", 'a+', encoding='utf-8')

def get_data(url):

    try:
        data = req.get(url, timeout = 20)
        data.raise_for_status()
        data.encoding = data.apparent_encoding
        return data.text
    except:
        data = "fail"
        return data

def find_title(data):
    title = str(data.find_all('h1', {"class":{"ts"}}))
    title0 = re.findall(r'id="thread_subject">(.*)</span>', title)
    return title0

def find_baidupan(data):
    baidupan = data.find_all('div', {"class" : "quote"})
    return baidupan

def find_wangzhi(baidupans,wangzhis):
    wangzhi = re.search('(?<=href=")', baidupans)

    wangzhis.append(baidupans.find('a herf'))

def find_mima(baidupans,mimas):
    mimas.append(baidupans.find_all('br'))


url = 'http://www.skyb7538.xyz/forum.php?mod=viewthread&tid=7355&extra=page%3D1%26filter%3Dauthor%26orderby%3Ddateline'
data = get_data(url)
get_data(url)
books = BeautifulSoup(data, 'html.parser')
titles = []
titles.append(find_title(books))
print(find_baidupan(books))

# wangzhis = []
# mimas = []
# wangzhis.append(find_wangzhi(find_baidupan(books), wangzhis))
# mimas.append(find_mima(find_baidupan(books), mimas))
# print(mimas)
# print(wangzhis)
douban.close()