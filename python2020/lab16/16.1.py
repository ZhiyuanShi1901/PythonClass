# 16.1
# coding=utf-8

import random
time = eval(input("请输入投掷次数："))
times = 0
for i in range(0, time):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2+y**2 <= 1:
        times += 1
    else:
        continue

print("圆周率的近似值为：{}".format(times/time*4))