# 3.1
# coding=utf-8
import math
import scipy
import pandas
import numpy
lists = []

print("查看标准库函数：")
lists = dir()
for list in lists:
    print(list)

print("查看math函数：")
lists = dir(math)
for list in lists:
    print(list)

print("查看scipy函数：")
lists = dir(scipy)
for list in lists:
    print(list)

print("查看pandas函数：")
lists = dir(pandas)
for list in lists:
    print(list)

print("查看标准库函数分析：")
help(__builtins__)
help(__doc__)

print("查看math函数库分析：")
help(math.copysign)
help(math.degrees)

print("查看scipy函数库分析：")
help(scipy.AxisError)
help(scipy.DataSource)

print("查看pandas函数库分析：")
help(pandas.Flags)
help(pandas.Int32Dtype)

# 计算三角形的面积
print("请输入需要计算的三角形的三个边长：")
a = eval(input("第一个边长："))
b = eval(input("第二个边长："))
c = eval(input("第三个边长："))
s = (a+b+c)/2
triangle_area = numpy.sqrt(s*numpy.add(s, -a)*numpy.add(s, -b)*numpy.add(s, -c))
print("三角形的面积为：{:.2}".format(triangle_area))
