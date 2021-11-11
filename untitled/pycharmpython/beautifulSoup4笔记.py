#-*- codeing = utf-8 -*-
#@Time : 2021/2/24 10:06
#@Author : 史致远
#@File : testBs4.py
#@Software : PyCharm

from bs4 import BeautifulSoup
import re

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

#1tag 标签以及内容  只能拿到它所找到的第一个内容
#print(bs.title)
# print(bs.a)
# print(bs.head)
#print(type(bs.head))

#2 NavigableString   标签里的内容 字符串
#print(bs.title.string)   #只有内部字符串的内容

#print(bs.a.attrs)   #attrs 以字典形式保存一个标签里面的所有属性

#3 BeautifulSoup  表示整个文档
#print(type(bs))

# print(bs.name)
# print(bs.attrs)
# print(bs)  #bs即整个文档

#4.comment 特殊的NavigableString  输出的内容不包含注释符号

# print(bs.a.string)
# print(type(bs.a.string))  #

#--------------------------------------------------------------------------------------------------------

#文档的遍历

#print(bs.head.contents)   #contents 寻找meta行  获取Tag所有子节点
#print(bs.head.contents[1])
#更多内容搜索文档


#文档的搜索
#(1) find_all()直接查找所有
#字符串过滤  查找与字符串完全匹配的内容
#t_list = bs.find_all("a")


#正则表达式搜索：使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))


#方法 ： 传入一个函数  根据函数的要求搜索
# def name_is_exist(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exist)
#
# for item in t_list:
#     print(item)

#2.kwargs  指定参数进行搜索
#t_list = bs.find_all(id = "head")
# t_list = bs.find_all(href = "http://")
# t_list = bs.find_all(class_=True)
#
# for item in t_list:
#     print(item)

#3.text参数

#t_list = bs.find_all(text = ["hao123","地图","贴吧"])
#t_list = bs.find_all(text = re.compile("\d"))    #应用正则表达式查找包含特定文本的内容  （标签里面的字符串）

#4.limit 参数

# t_list = bs.find_all("a",limit = 3)   #限制需要多少个a的信息
# for item in t_list:
#     print(item)

#print(t_list)


#css选择器

#t_list = bs.select('title')  #通过标签查找

# t_list = bs.select(".mnav")   #通过类名查找  "."

# t_list = bs.select("#u1")   #通过id查找

#t_list = bs.select("a[class='bri']")   #通过属性查找

#t_list = bs.select("head > title")  # 通过子标签查找

t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())

for item in t_list:
    print(item)