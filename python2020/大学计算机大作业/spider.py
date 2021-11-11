# spider
# coding=utf-8

from saveData import saveData
from askURL import askURL
from getdata import getData

def spider(baseurl, savepath, sheetname, workexcel): # 输入网址,但不包含index，在后续添加
    # 1.爬取网页
    datalist = getData(baseurl)
    #print(datalist)  # 测试爬取的网页信息是否正常
    # 保存数据
    saveData(datalist, savepath, sheetname, workexcel)


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    spider(baseurl='https://book.sfacg.com/List/default.aspx?tid=24&PageIndex=')
