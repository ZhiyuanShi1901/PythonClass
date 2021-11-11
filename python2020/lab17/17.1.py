# 17.1
# coding=utf-8

import jieba


def chinesenum(poem):
    sum=0
    for line in poem:
        for city in line:
            if city != '/' and city != '\n':
                sum += 1
    return sum

def jingque(poem):
    cihui = []
    number = 0
    for line in poem:
        cihuiinline=jieba.lcut(line)
        for ci in cihuiinline:
            if ci != '\n' and ci!='，' and ci!='。' and ci!='？' and ci != '！'and ci != '·':
                cihui.append(ci)
                number+=1
    return cihui, number

def sousuo(poem):
    cihui = []
    number = 0
    for line in poem:
        cihuiinline=jieba.lcut_for_search(line)
        for ci in cihuiinline:
            if ci != '\n' and ci!='，' and ci!='。' and ci!='？' and ci != '！' and ci != '·':
                cihui.append(ci)
                number+=1

    return cihui, number

with open('poem.txt', 'r', encoding='utf-8') as poem:
    poemlines = poem.readlines()
    print(f"中文字符数为：{chinesenum(poemlines)}。")

    print("精准模式：")
    print("输出的词汇为：\n{}\n词语数量为：{}".format(jingque(poemlines)[0], jingque(poemlines)[1]))

    print("搜索模式：")
    print("输出的词汇为：\n{}\n词语数量为：{}".format(sousuo(poemlines)[0], sousuo(poemlines)[1]))
