# 15.1
# coding=utf-8

try:
    poem = open("poem.txt", 'r', encoding='utf-8')
except FileNotFoundError:  # 如果文件未找到，则输出如下：
    print("文件未找到。")
else:
    poems = poem.read()
    print(poems)
    poem.close()
finally:
    print("文件打开程序运行结束。")