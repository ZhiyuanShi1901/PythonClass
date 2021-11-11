# 6.4
# coding=utf-8

from math import pow

n = 1000  #区间数
x, integral, integral_juxing = 0, 0, 0
while x + 4/n <= 4:
    x = x + 4/n
    # 梯形法
    integral += ((pow(x, 3) + 3*x - 1) +(pow(x - 4/n, 3) + 3 * (x - 4/n) - 1))*(4/n)/2
    # 矩形法
    # integral_juxing += (pow(x, 3) + 3*x - 1)*4/n

print("梯形法计算得到积分值为{:}".format(integral))
# print("矩形法计算得到积分值为{:}".format(integral_juxing))




