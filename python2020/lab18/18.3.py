# 18.3
# coding=utf-8

import matplotlib.pyplot as py
import random
time = 10000
times = 0
shujudian = []
for i in range(0, time):  # 生成数据点
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    shujudian.append([x,y])

py.xlim((0,2)) # x轴限定范围
py.ylim((0,2)) # y轴限定范围
py.rcParams['font.sans-serif']=['SimHei']  #显示中文标签
py.rcParams['axes.unicode_minus']=False
py.title('蒙特卡罗图像')

for item in shujudian:
    x=item[0]
    y=item[1]
    if x**2+y**2 <= 1:
        color = 'black'
    else:
        color = 'red'
    py.scatter(x, y, color=color)

py.show()