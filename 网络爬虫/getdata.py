# getdata
# coding=utf-8
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式 进行文字匹配
from askURL import askURL
# 爬取网页

findImgSrc = re.compile(r'src="(.*?)"')  # 生成查找小说封面链接的正则表达式规则，当字符串中含有该规则，即寻找到,使用r忽视掉所有特殊符号 re.S使换行符也在其中
findtitle = re.compile(r'alt="(.*?)"', re.S)
findarticle = re.compile(r'id="ContentMain_rnlv___NovelList_AuthorLink_(.*?)</a', re.S)
findzonghexinxi = re.compile(r'<span class="font_red">(.*?)</li>',re.S)

def getData(baseurl):  # 使用最开始的url获取网页内容
    datalists = []
    i=1
    while True:   #调用获取页面信息的函数n次，具体次数与网页有关
        datalist = []
        url = baseurl + str(i)  # 发现该页面链接最后一个数字为页面页码，只要对数字进行迭代，就能获得这些页面的url
        html = askURL(url)    # 获取每一页网页中的内容，每一页里拥有需要的数据

    # 2.逐一解析数据， 每一页网页都需要进行对其中的数据解析
        soup = BeautifulSoup(html, "html.parser")   # 对获取到的网页所有内容进行解析
        for item in soup.find_all('ul', class_="Comic_Pic_List"):   # 找到每一个小说所包含的全部内容 ,同时具有ul和class属性的内容
            data = []  # 存储其中需要的内容信息
            item = str(item)  # 将其转化为字符串

            # 小说封面链接
            image = re.findall(findImgSrc, item)[0]   # re正则表达式查找特定的字符串
            data.append(image)
            # 小说题目
            title = re.findall(findtitle, item)[0]  # 寻找到第一个符合要求的值
            data.append(title)
            # 小说作者
            article = re.findall(findarticle, item)[0]
            article = article.split('>')[1].split('<')[0]
            data.append(article)
            # 小说综合信息
            zonghexinxi = re.findall(findzonghexinxi, item)[0]
            from Zonghexinxi import zonghe  # 引入自定义的对综合信息进行整理的函数
            realzonghexinxi = zonghe(zonghexinxi)
            data.append(realzonghexinxi)
            datalist.append(data)
        if datalist == []:
            print("该类型爬取结束")
            break
        else:
            datalists.extend(datalist)
            i += 1

    return datalists
