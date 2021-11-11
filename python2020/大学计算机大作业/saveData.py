# saveData
# coding=utf-8
import xlwt  # 进行excel操作


def saveData(datalist, savepath, sheetname, workexcel):  # 保存数据
    print("save...")
    worksheet = workexcel.add_sheet(sheetname)   #创建工作表
    colname = ['封面链接', '书名', '作者', '评分', '类型', '最后发表时间', '累计字数', '简介']
    for i in range(0, 8):
        worksheet.write(0, i, colname[i])
    row = 1
    for item in datalist:
        if item == '':  # 判定循环结束条件
            break
        for i in range(3):  # 对每一个小说包含的信息内容进行写入
            worksheet.write(row, i, item[i])
        p = 0
        for gegezonghe in item[3]:   #对每一个综合信息列表中的信息进行写入
            worksheet.write(row, 3+p, gegezonghe)
            p += 1
        row += 1  # 行进行循环写
    print(f"{sheetname}已保存")
    workexcel.save(savepath)
