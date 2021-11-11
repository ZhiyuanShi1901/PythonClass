from selenium import webdriver
from time import sleep
import re

with open('C:\\Users\\14433\\OneDrive\\Documents\\PythonClass\\网络爬虫\\savedurlandpath.txt', 'r', encoding='utf-8') as savedurl:
    lines = savedurl.readlines()
    url = lines[1]
    path = lines[3]
    chromepath = lines[5]
    print(lines)
    print(url)
    print(path)
    print(chromepath)

url = "http://www.dmsy67.com/index.php"

option = webdriver.ChromeOptions()
option.add_argument(r''+chromepath)

bro = webdriver.Chrome(executable_path=r''+path, options=option)  # 此处填driver的地址
bro.get(url=url) # 打开页面