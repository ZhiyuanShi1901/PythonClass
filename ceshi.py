# coding=utf-8
a=eval(input("请输入一个正整数:"))
print('它的二进制为',bin(a),'\n它的八进制为',oct(a),'\n它的十六进制为',hex(a))
s=input('请输入一个字符串：')
print('{:*<30}'.format(s))
from math import *
x=40/180*pi
y=5.0
c=(sin(x)+tan(x)-5*e**(10+y))/(1+cos(x)*log(y,10))
x=pi/5
y=0.5
d=(cos(x)+tan(pi/2-x)-10**(5+y))/(1-sin(x)*log(y,e))
print('(1)的结果为',round(c,2),'\n(2)的结果为',round(d,2))