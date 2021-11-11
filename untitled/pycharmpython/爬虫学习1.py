from bs4 import BeautifulSoup # 网页解析，获取数据
import re  # 正则表达式 进行文字匹配
import urllib.request,urllib.error  # 指定url 获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

import urllib.parse
import urllib.request


def main():
    baseurl = "https://movie.douban.com/top250?start="  # 输入网址
    # 1.爬取网页
    datalist = getData(baseurl)
    #savepath = "豆瓣电影top250.xls"
    dbpath = "movie.db"
    # 保存数据
    #saveData(datalist,savepath)
    saveData2DB(datalist, dbpath)

    #askURL("https://movie.douban.com/top250?start=")

findLink = re.compile(r'<a href="(.*?)">')   #创建正则表达式对象，表示规则（字符串的模式）
#影片图片链接
findImgSrc = re.compile(r'<img alt=.*src="(.*?)"', re.S)   # .*若干字符   你需要的(.*?)   re.S 让换行符包含在字符中

findTitle = re.compile(r'<span class="title">(.*?)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):   #调用获取页面信息的函数10次
        url = baseurl + str(i*25)
        html = askURL(url)
    # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):   #查找符合要求的字符串，形成列表   class类别需要加_，表示属性值为item
            #print(item)  #测试查看电影item全部信息
            data = []  #存储一部电影的最终所有信息
            item = str(item)

            link = re.findall(findLink, item)[0]   #re库用来通过正则表达式查找指定的字符串  [0]指拿取第一个
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)         #添加图片

            titles = re.findall(findTitle,item)     #片名可能只有一个中文名，没有外语
            if len(titles) == 2:
                data.append(titles[0] ) #添加中文名
                data.append(titles[1].replace("/",""))#去掉外语名无关符号
            else:
                data.append(titles[0])
                data.append(' ')  #外国名空出来，以免格式错误

            rating = re.findall(findRating,item)[0]   #添加评分
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]  #添加评价人数
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")       #去掉句号
                data.append(inq)    #添加概述
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub("/...<br(\s+)?/>(\s+)?"," ",bd)   #去掉<br/>
            bd = re.sub('/'," ",bd)   #替换/
            data.append(bd.strip())

            datalist.append(data)
    print(datalist)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 FS"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# #3.保存数据
def saveData(datalist,savepath):  # 保存数据
    print("save...")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250.xls',cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接',"图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])    #数据保存

    book.save(savepath)  # 保存

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 5 or index == 4:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250 (
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s)''' %",".join(data)   #data列表中元素用，连接起来

        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()



def init_db(dbpath):
    sql = '''
    create table movie250 
    (
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar,
    ename varchar,
    score numeric,
    rated numeric ,
    instroduction text,
    info text
    )
    ''' #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":  # 当程序执行时
    # #调用函数
    main()
    print("爬取完毕")