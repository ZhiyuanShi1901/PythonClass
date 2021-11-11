# spider
# coding=utf-8

import requests as re
import bs4
from bs4 import BeautifulSoup

douban = open("doubanreadinglist", 'a+', encoding='utf-8')



def get_data(url):
    head = {

    }
    try:
        data = re.get(url, timeout = 20)
        data.raise_for_status()
        data.encoding = data.apparent_encoding
        return data.text
    except:
        data = "fail"
        return data


def find_table(html):
    soup = BeautifulSoup(html, "html.parser")
    tbodies = []
    urllists = []
    tobdies = soup.find('tbody')#.children
        for body in tobdies:
            trs = re.findall(r'<tr>(.*?)<tr>',body)
            urllists.append(trs)
            #urllists.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string, tds[5].string])
        else:
            continue
    return urllists



url = 'https://www.kuaiyilicai.com/stats/global/yearly_overview/g_gdp.html'
data = get_data(url)
urls = find_table(data)
print(urls)
# get_data(url)
# books = BeautifulSoup(data, 'html.parser')
# find_title(books)

douban.close()