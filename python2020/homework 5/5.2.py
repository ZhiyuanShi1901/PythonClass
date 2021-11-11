# coding=utf-8
a, b = input("请输入两个整数，中间用空格隔开：").split()
a, b = int(a), int(b)
if a % 2 != 0:
    print("结果为：{}".format(a-b))
elif a%2 == 0:
    print("结果为：{}".format(a+b))
else:
    print("请输入整数。")