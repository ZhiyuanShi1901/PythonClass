# judge
# coding=utf-8

def if_nar_num(number):   #判断是否为水仙花数
    s = str(number)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3 == int(s[0]) * 100 + int(s[1]) * 10 + int(s[2]):
        return True
    else:
        return False

def if_prime_num(number):
        condition = 0  # 设置判断条件，如果其不是素数，则条件为1
        for j in range(2, number):
            if number % j == 0:
                condition = 1
                break
            else:
                continue
        if condition == 0:
            return True
        else:
            return False