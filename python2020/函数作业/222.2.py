# 222.2
# coding=utf-8
from math import sqrt
def triangle(x, y, k):
    condition = True
    if x+y>k :
        if x > y:
            if x-y<k:
                condition = False
        if x < y:
            if y-x<k:
                condition = False
    if condition == False:
        print("这三边能构成三角形。")
        a = (x+y+k)/2
        print("三角形的面积为：", sqrt(a*(a-x)*(a-y)*(a-k)))
    else:
        print("这三边不能构成三角形。")
        return 0

x, y, k = input("请输入三个边长，以判断是否为三角形且求出其面积：").split(",")
x, y, k = eval(x), eval(y), eval(k)
triangle(x, y, k)
