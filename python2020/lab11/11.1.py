# 11.1
# coding=utf-8

def if_nar_num(number):   #判断是否为水仙花数
    s = str(number)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == int(s[0]) * 100 + int(s[1]) * 10 + int(s[2]):
        return True
    else:
        return False

with open("shuixianin1000.txt", 'a+') as shuixian:
    shuixian.write("100-999的水仙花数为：\n")
    for number in range(100, 1000):
        if if_nar_num(number) == True:
            shuixian.write(str(number)+"  ")
    shuixian.seek(0, 0)  # 将光标设置为文件开头处
    print(shuixian.read())
