# 9.2
# coding=utf-8
import math as m
def triangle_area(a,b,c):
    s = (a + b + c) / 2
    return m.sqrt(s * (s - a) * (s - b) * (s - c))

def incircle_area(a,b,c):
    s = (a + b + c) / 2
    incircle_r = m.sqrt((s - a) * (s - b) * (s - c) / s)
    return m.pi * (incircle_r ** 2)

def outcircle_area(a, b, c):
    s = (a + b + c) / 2
    outcircle_r = a * b * c / (4 * m.sqrt(s * (s - a) * (s - b) * (s - c)))
    return m.pi * (outcircle_r ** 2)

print("请输入需要计算的三角形的三个边长：")
a = eval(input("第一个边长："))
b = eval(input("第二个边长："))
c = eval(input("第三个边长："))

print("三角形的面积为：{0:.5}\n它的内接圆面积为：{1:.5}\n外接圆面积为：{2:.5}".format(triangle_area(a, b, c), incircle_area(a, b, c), outcircle_area(a, b, c)))
