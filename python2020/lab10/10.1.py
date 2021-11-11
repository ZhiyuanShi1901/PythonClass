# 10.1
# coding=utf-8

from judge import if_nar_num, if_prime_num
number = eval(input("请输入一个三位数，来判断它是否是素数或水仙花数："))
if if_nar_num(number) == True:
    print("这个数是水仙花数。")
else:
    print("这个数不是水仙花数。")
if if_prime_num(number) == True:
    print("这个数是素数。")
else:
    print("这个数不是素数。")