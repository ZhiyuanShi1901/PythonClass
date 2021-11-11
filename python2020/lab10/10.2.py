# 10.2
# coding=utf-8

from area import triangle_area, incircle_area, outcircle_area
print("请输入需要计算的三角形的三个边长：")
a = eval(input("第一个边长："))
b = eval(input("第二个边长："))
c = eval(input("第三个边长："))

print("三角形的面积为：{0:.5}\n它的内接圆面积为：{1:.5}\n外接圆面积为：{2:.5}".format(triangle_area(a, b, c), incircle_area(a, b, c), outcircle_area(a, b, c)))

