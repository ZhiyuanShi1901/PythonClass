# wenjian.1
# coding=utf-8
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

sushu = open("sushuin1000.txt", 'a+')
sushu.write("1000以内的素数为：\n")
for number in range(1, 1001):
    if prime_number(number) == 1:
        sushu.write(str(number)+"  ")
sushu.seek(0, 0)  # 将光标设置为文件开头处

print(sushu.read())

sushu.close()