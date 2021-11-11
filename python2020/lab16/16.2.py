# 16.2
# coding=utf-8

import random
def prime_number(number): # 判断是否为素数的函数

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

sushu = []
while len(sushu) < 10:
    number = random.randint(10, 99)
    if prime_number(number) == 1:
        sushu.append(number)
    else:
        continue
print("随机生成的素数为:", end='')
for number in sushu:
    print("{}".format(number), end=',')