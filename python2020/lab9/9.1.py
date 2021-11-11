# 9.1
# coding=utf-8
from math import pow

def if_nar_num(number):   #判断是否为水仙花数
    s = str(number)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == int(s[0]) * 100 + int(s[1]) * 10 + int(s[2]):
        return True
    else:
        return False

narnum = []
for i in range(100, 300):
    if if_nar_num(i) == True:
        narnum.append(i)

print(f"100-300之间的水仙花数：{narnum}")