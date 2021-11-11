# 9.4
# coding=utf-8
from scipy.misc import derivative

def Newton(x_0):
    def f(x):
        return x**5+3*x**4-5*x**2-6
    condition = True
    i = 0
    while condition:
        x_1 = x_0 - f(x_0)/derivative(f, x_0, dx=1e-6)
        if abs(x_1-x_0) <= 1e-7:
            condition = False
        x_0 = x_1
        i+=1

    return x_0, i
x_0 = eval(input("请输入初值："))
print("迭代次数为：{}，根为：{}".format(Newton(x_0)[1],Newton(x_0)[0]))