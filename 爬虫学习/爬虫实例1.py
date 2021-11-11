#import bs4   # 网页解析，获取数据
import re    #正则表达式 进行文字匹配
import urllib.request,urllib.error   #指定url 获取网页数据
#import xlwt      #进行excel操作
import sqlite3  #进行SQLite数据库操作

import urllib.parse
import urllib.request

def main():
	baseurl = "https://movie.douban.com/top250?start="#输入网址
	#1.爬取网页
	datalist = getData(baseurl)
	savepath = ".\\豆瓣电影top250.xls"
	#保存数据
	saveData(savepath)
	
	askURL("https://movie.douban.com/top250?start=")
	

#爬取网页
def getData(baseurl):
	datalist = []
	#2.逐一解析数据
	# for i in range(0,10):   #调用获取页面信息的函数10次
	# 	url = baseurl + str(i*25)
	# 	html = askURL(url)

	return datalist


#得到指定一个URL的网页内容
def askURL(url):
	head = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 FS"
	}

	request = urllib.request.Request(url , headers = head)
	html = ""

	try:
		response = urllib.request.urlopen(request) 
		html = response.read().decode("utf-8")
		print(html)

	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)

	return html

# #3.保存数据
def saveData(savepath):  #保存数据
	print("save...")

if __name__ == "__main__":   #当程序执行时
# #调用函数
	main()