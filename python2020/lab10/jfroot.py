# jfroot
# coding=utf-8
from math import pow
from scipy.misc import derivative

def intecom(left_margin, right_margin, n):
    x, integral, integral_juxing = left_margin, 0, 0
    while x <= right_margin:
        x = x + (right_margin - left_margin) / n
        # 梯形法
        integral += ((pow(x, 4) + 3 * x ** 3 - 1) + (pow(x - (right_margin - left_margin) / n, 4) + 3 * (x - (right_margin - left_margin) / n) ** 3 - 1)) * ((right_margin - left_margin) / n) / 2
        # 矩形法
        integral_juxing += (pow(x, 4) + 3*x**3 - 1)*(right_margin - left_margin)/n
    return integral, integral_juxing

def Newton(x_0):
    def f(x):
        return x**4+3*x**3-1
    condition = True
    i = 0
    while condition:
        x_1 = x_0 - f(x_0)/derivative(f, x_0, dx=1e-6)
        if abs(x_1-x_0) <= 1e-7:
            condition = False
        x_0 = x_1
        i+=1

    return x_0, i

