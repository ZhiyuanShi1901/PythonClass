# 12.1
# coding=utf-8
import os
import shutil
print(os.listdir())  #输出当前目录下文件列表
map = os.getcwd()   #记录当前文件目录
os.mkdir('py')   #新建py文件夹
os.mkdir('py2')   # 新建py2文件夹
shutil.copy('/lab15/poem.txt', 'py')  #将poem复制到py文件夹
shutil.copy('/lab15/poem.txt', 'py2')    #将poem复制到py2文件夹

os.remove('py2/poem.txt')  # 删除py2文件夹的py文件
os.rmdir('py2')  #删除py2文件夹
os.chdir(map+'/py')  #进入文件夹py
os.listdir()  # 显示文件夹
os.chdir(map)  # 退回到原默认目录
for item in os.walk(map):
    print(item, end='\t')
