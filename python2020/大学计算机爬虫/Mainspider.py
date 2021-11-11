# Mainspider
# coding=utf-8

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式 进行文字匹配
import urllib.request, urllib.error  # 指定url 获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

import urllib.parse
import urllib.request



# 对sf轻小说科幻界面的小说名称及各种内容进行爬取
def main():
    baseurl = "https://book.sfacg.com/List/default.aspx?tid=21&PageIndex="  # 输入网址,但不包含index，在后续添加
    # 1.爬取网页
    datalist = getData(baseurl)
    #print(datalist)  # 测试爬取的网页信息是否正常
    # 保存数据
    saveData(datalist)

    #askURL("https://movie.douban.com/top250?start=")

findImgSrc = re.compile(r'src="(.*?)"')  # 生成查找小说封面链接的正则表达式规则，当字符串中含有该规则，即寻找到,使用r忽视掉所有特殊符号 re.S使换行符也在其中
findtitle = re.compile(r'alt="(.*?)"', re.S)
findarticle = re.compile(r'id="ContentMain_rnlv___NovelList_AuthorLink_(.*?)</a', re.S)
findzonghexinxi = re.compile(r'<span class="font_red">(.*?)</li>',re.S)


# 爬取网页
def getData(baseurl):  # 使用最开始的url获取网页内容
    datalists = []
    for i in range(2580, 3001):   #调用获取页面信息的函数499次
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
    return datalists


# 得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 FS"
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


# #3.保存数据
def saveData(datalist):  # 保存数据
    print("save...")
    workexcel = xlwt.Workbook(encoding='utf-8')  # 创建一个wookexcel对象，
    worksheet = workexcel.add_sheet('sheet1')   #创建工作表
    colname = ['封面链接', '书名', '作者', '评分', '类型', '最后发表时间', '累计字数', '简介']
    for i in range(0, 8):
        worksheet.write(0, i, colname[i])
    row = 1
    for item in datalist:
        if item == '':  # 判定循环结束条件
            break
        for i in range(3):  # 对每一个小说包含的信息内容进行写入
            worksheet.write(row, i, item[i])
        p = 0
        for gegezonghe in item[3]:   #对每一个综合信息列表中的信息进行写入
            worksheet.write(row, 3+p, gegezonghe)
            p+=1
        row+=1 # 行进行循环写

    workexcel.save('SF科幻小说合集.xls')

if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
