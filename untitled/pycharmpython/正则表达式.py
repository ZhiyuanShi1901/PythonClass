#-*- codeing = utf-8 -*-
#@Time : 2021/2/24 17:41
#@Author : 史致远
#@File : 正则表达式.py
#@Software : PyCharm


#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
#创建模式对象
#写法1
# pat = re.compile("AA")   #此处的AA是正则表达式，用来验证其他的字符串
# m = pat.search("ABCAADFFTYGYAA")   #search字符串被校验的内容
#写法2
# m = re.search("asd","Aasd")  #  前面的是规则，后面的是需要检查的字符串
#
# print(m)
# #返回值为<re.Match object; span=(3, 5), match='AA'>

# print(re.findall("a","ASDaDFGAa"))
#
# print(re.findall("[A-Z]","ASDaDFGAa"))   #找到A-Z之间的大写字母
# print(re.findall("[A-Z]+","ASDaDFGAa"))   #符合的一次性输出

#sub替换

print(re.sub("a","A","abcdcasd"))   #在第三个字符串中找到a 用A替换
#建议在正则表达式中，被比较的字符串前面加上r  （r 防止转义字符生效）
a = r"\aabd-\'"
print(a)

