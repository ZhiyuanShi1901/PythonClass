# spiconsumer
# coding=utf-8
import xlwt
import xlrd
from spider import spider
from piemark import piemake
from readexcel import *
# 类别整理
leibie = {'魔幻': str(21), '玄幻': str(22), '古风': str(23), '科幻': str(24), '校园': str(25), '都市': str(26), '游戏': str(27),
          '同人': str(28), '悬疑': str(29)}
url_base = 'https://book.sfacg.com/List/default.aspx?tid='  # 基础url
index = '&PageIndex='   # 页码url

# 需要爬取的页面总基础url整理
baseurls = []
mohuan = url_base+leibie['魔幻']+index
xuanhuan = url_base+leibie['玄幻']+index
gufeng = url_base+leibie['古风']+index
kehuan = url_base+leibie['科幻']+index
xiaoyuan = url_base+leibie['校园']+index
dushi = url_base+leibie['都市']+index
youxi = url_base+leibie['游戏']+index
tongren = url_base+leibie['同人']+index
xuanyi = url_base+leibie['悬疑']+index
baseurls.extend([mohuan, xuanhuan, gufeng, kehuan, xiaoyuan, dushi, youxi, tongren, xuanyi])

# 类型名称整理
leixings = ['魔幻', '玄幻', '古风', '科幻', '校园', '都市', '游戏', '同人', '悬疑']
workexcel = xlwt.Workbook(encoding='utf-8')  # 创建一个wookexcel对象，

for num in range(0, 9):
    savepath = ".\\SF轻小说.xls"
    spider(baseurls[num], savepath, leixings[num], workexcel)


# 打开excel文件
workbook = xlrd.open_workbook('SF轻小说.xls')
Pingfens={}  #创建容纳所有类型评分总统计的字典
for leixing in leixings:
    pingfen = read_excel_sheet(workbook, sheetname=leixing)  # 对该类型的评分进行汇总
    Pingfens[leixing]=pingfen  # 该类型的评分记入统计


for leixing in leixings:
    novelnumber = pingfentongji(Pingfens, leixing)  # 返回该类型小说各个评分段小说数目
    print(novelnumber)
    piemake(novelnumber, leixing)
