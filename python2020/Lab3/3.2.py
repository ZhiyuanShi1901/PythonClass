# coding=utf-8
from math import sin, cos, tan, pi
from numpy import log, log10, exp
# 方程1
print("下面是第一个方程式的计算：")
x = eval(input("请输入x的值："))/180*pi
y = eval(input("请输入y的值："))
equation_1 = (sin(x)+tan(x)-5*exp(10+y))/(1+cos(x)*log10(y))
print("{:}".format(round(equation_1, 4)))

# 方程2
print("下面是第二个方程式的计算：")
x = eval(input("请输入x的值："))
y = eval(input("请输入y的值："))
equation_2 = (cos(x)+1/tan(x)-10**(5+y))/(1-sin(x)*log(y))
print("{:}".format(round(equation_2, 4)))
