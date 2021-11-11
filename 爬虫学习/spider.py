import bs4   # 网页解析，获取数据
import re    #正则表达式 进行文字匹配
import urllib.request,urllib.error   #指定url 获取网页数据
import xlwt      #进行excel操作
import sqlite3  #进行SQLite数据库操作

import urllib.parse
import urllib.request
def main():
	baseurl = ""#输入网址
	#1.爬取网页
	datalist = getData(baseurl)
	savepath = ".\\豆瓣电影top250.xls"
	saveData(savepath)
	
	

#爬取网页
def getData(baseurl):
	datalist = []
	#2.逐一解析数据
	return datalist

#3.保存数据
def saveData(savepath):  #保存数据
	


if __name__ == "__main__":   #当程序执行时
#调用函数
	main()