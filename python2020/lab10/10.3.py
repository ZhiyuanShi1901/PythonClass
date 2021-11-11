# 10.3
# coding=utf-8

from jfroot import intecom, Newton

left_margin, right_margin = input("请输入积分区间,用逗号隔开:").split(",")
left_margin, right_margin = eval(left_margin), eval(right_margin)
n = eval(input("请输入梯形法求积分的区间数（区间越小精确度越高）："))  #区间数

x_0 = eval(input("请输入初值："))
print("梯形法计算得到积分值为{:}\n矩形法计算得到积分值为{:}".format(intecom(left_margin, right_margin, n)[0], intecom(left_margin, right_margin, n)[1]))

print("迭代次数为：{}，根为：{}".format(Newton(x_0)[1], Newton(x_0)[0]))