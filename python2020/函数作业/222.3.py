# 222.3
# coding=utf-8
from math import sqrt
def prime_number(number):

    if number == 1:
        return 0
    condition = 0
    for j in range(2, number):
        if number % j == 0:
            condition = 1
            break
        else:
            continue
    if condition == 0:
        return 1   # 返回1时为素数
    else:
        return 0

number = int(input("请输入一个正整数，以判断其是否为素数："))
if prime_number(number) == 1:
    print("这个数为素数。")
else:
    print("这个数不是素数。")