# piemark
# coding=utf-8

import matplotlib.pyplot as py
import matplotlib.font_manager as fm

def piemake(novelnumber, leixing):
    py.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    py.rcParams['axes.unicode_minus'] = False   # 正确显示正负号

    size = []
    sum = 0
    for i in range(0, 5):
        sum += novelnumber[i]

    for i in range(0, 5):
        bili = novelnumber[i]*100/sum
        size.append(bili)

    py.title(f'{leixing}小说评分分段统计饼图')
    labels = ['0-6.0', '6.1-7.0', '7.1-8.0', '8.1-9.0', '9.1-10.0']
    colors = ('r', 'g', 'b', 'orange', 'purple')
    py.pie(x=size, labels=labels, explode=[0.1, 0, 0, 0, 0.1], startangle=0, colors=colors, shadow=False, autopct='% 1.1f%%', labeldistance=1.3, pctdistance=0.8)
    py.legend()  # 展示图例
    savepath = f'.\\{leixing}小说评分分段统计饼图.jpg'
    py.savefig(savepath)
    py.close() # 关闭避免图片重叠
    print(f'{leixing}制图完成')

    return 0
