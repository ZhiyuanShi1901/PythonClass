# 4.2
# coding=utf-8
import math as m
x = eval(input("请输入您需要计算的x值(0.2<x<0.9)："))
if x < 0.3 and x > 0.2:
    equation = m.exp(x)*m.log(abs(x))/(m.pi*abs(m.tan(x)))
elif x > 0.4 and x < 0.6:
    equation = (m.cos(20/180*m.pi)+m.sqrt(x))/(m.sin(x)+x)
elif x > 0.7 and x < 0.9:
    equation = -m.pow(x,2)*m.log10(x)/m.sqrt(m.pow(m.sin(x),3)) + m.cos(20/180*m.pi)
else:
    print("请输入0.2<x<0.9范围内的x值。")
print("equation = {:.6}".format(equation))