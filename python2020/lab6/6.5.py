# 6.5
# coding=utf-8

n = eval(input("请输入一个n以计算e的近似值（n越大，e的近似度越高）："))
e = 0
for i in range(1, n+1):
    series = 1
    for j in range(1, i):
        series *= j
    if series >= 100000:
        break
    e += 1/series
print("e≈{}".format(e))
