# ceshi
# coding=utf-8
import xlwt  # 进行excel操作

leixings = ['魔幻', '玄幻', '古风', '科幻', '校园', '都市', '游戏', '同人', '悬疑']

workexcel = xlwt.Workbook(encoding='utf-8')  # 创建一个wookexcel对象，
for leixing in leixings:
    worksheet = workexcel.add_sheet(leixing)   #创建工作表
    worksheet.write(0, 0,'heihei')
    workexcel.save(".\\SF轻小说.xls")