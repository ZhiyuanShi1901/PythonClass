# 9.3
# coding=utf-8
from math import pow
def integral(left_margin, right_margin, n):
    x, integral = left_margin, 0
    while x <= right_margin:
        x = x + (right_margin - left_margin) / n
        # 梯形法
        integral += ((pow(x, 4) + 3 * x ** 2 - 1) + (pow(x - (right_margin - left_margin) / n, 4) + 3 * (x - (right_margin - left_margin) / n) ** 2 - 1)) * ((right_margin - left_margin) / n) / 2
    return integral
left_margin, right_margin = input("请输入积分区间,用逗号隔开:").split(",")
left_margin, right_margin = eval(left_margin), eval(right_margin)
n = eval(input("请输入梯形法求积分的区间数（区间越小精确度越高）："))  #区间数

print("梯形法计算得到积分值为{:}\n".format(integral(left_margin, right_margin, n)))
