# 4
# coding=utf-8
from math import pow

n = 100  #区间数
x, integral, integral_juxing = 0, 0, 0
while x + 2/n <= 2:
    x = x + 2/n
    # 梯形法
    integral += ((pow(x, 2) + 2*x + 1) +(pow(x - 2/n, 2) + 2 * (x - 2/n) + 1))*(2/n)/2
    # 矩形法
    integral_juxing += (pow(x, 2) + 2*x + 1)*2/n

print("梯形法计算得到积分值为{:}".format(integral))
print("矩形法计算得到积分值为{:}".format(integral_juxing))




