# 11.3
# coding=utf-8
import shutil
shutil.copy('shuixianin1000.txt', 'D:\doc\shuixian1.txt')  #拷贝到D盘 方法1

shutil.copy('../lab15/poem.txt', 'poem_mao.txt')  # 拷贝到本路径
shutil.move('poem_mao.txt', 'D:\doc')  # 拷贝到D盘

with open("shuixianin1000.txt", 'r') as shuixian:  #方法2
    shuixian2 = open('D:\doc\shuixian2.txt','w')
    while True:
        line = shuixian.readline()
        if line == '':
            break
            close(shuixian2)
        else:
            shuixian2.write(line)
