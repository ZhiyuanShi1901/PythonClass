# _4
# coding=utf-8
import jieba

def num_all(sentence):
    num_cihui = 0
    for ll in sentence:
        if ll == '，' or ll == '。' or ll == '？' or ll == '……' or ll == '！' or ll == '、':
            continue
        elif ll != '\n' and ll != ' ':
            num_cihui += 1
        else:
            continue
    return num_cihui

s = input("请输入一段文字：")
LCUT = jieba.lcut(s)  # 精确模式
LCUTALL = jieba.lcut(s, cut_all=True)  # 全模式
LCUTSEARCH = jieba.lcut_for_search(s)  # 搜索模式

print("中文字符个数：{}".format(len(s)))
print("精确模式输出词汇为：")
print(LCUT)
print("中文词汇个数为；{}。".format(num_all(LCUT)))
print("全模式输出词汇为：")
print(LCUTALL)
print(" 中文词汇个数为；{}。".format(num_all(LCUTALL)))
print("搜索模式输出词汇为：")
print(LCUTSEARCH)
print("中文词汇个数为；{}。".format(num_all(LCUTSEARCH)))
# 精确模式输出，每个字只组一次词汇，全模式和搜索模式会将相邻几个字所有可能组成的词汇全部输出。而搜索模式相比全模式，其出现无意义词汇的可能更小。