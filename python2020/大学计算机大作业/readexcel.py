# readexcel
# coding=utf-8

import xlwt


def read_excel_sheet(workbook, sheetname):  # 特定类型小说的评分统计
    # 获取所有的sheet内容
    # sheetnames = workbook.sheet_names()

    sheet = workbook.sheet_by_name(sheetname)
    pingfen = []
    for item in sheet.col_values(3):
        if item == '评分':
            continue
        else:
            fenshu = item.split('分')[0]
            pingfen.append(eval(fenshu))

    return pingfen

def pingfentongji(pingfens, leixing):  # 对每一个类型小说的评分区间，其中每个评分区间的小说数目进行统计
    smth6 = 0
    s6_7 = 0
    s7_8 = 0
    s8_9 = 0
    s9_10 = 0
    for pingfen in pingfens[leixing]:
        if pingfen <= 6.0:
            smth6 += 1
        elif pingfen <= 7.0:
            s6_7 += 1
        elif pingfen <= 8.0:
            s7_8 += 1
        elif pingfen <= 9.0:
            s8_9 += 1
        else:
            s9_10 += 1
    pingfenshu = []
    pingfenshu.extend([smth6, s6_7, s7_8, s8_9, s9_10])

    return pingfenshu   # 返回一个列表，包含各个评分段该类型小说数目
