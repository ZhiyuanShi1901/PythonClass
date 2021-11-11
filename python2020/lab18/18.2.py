# 18.2
# coding=utf-8

import matplotlib.pyplot as py
py.rcParams['font.sans-serif']=['SimHei']  #显示中文标签
py.rcParams['axes.unicode_minus']=False

sizes = (19, 24, 21, 14, 12, 10)
explode=(0, 0, 0.1, 0, 0, 0)
labels=('语文','数学','英语','生物','化学','物理')
colors=('r', 'g','b','purple','gray', 'orange')
autopct=('19%', '24%', '21%','14%','12%','10%')
py.pie( x=sizes, explode=explode, labels=labels, startangle=0,  colors=colors, shadow=False, autopct='% 1.1f%%')
py.legend()  # 展示图例
py.show()  # 展示表格
