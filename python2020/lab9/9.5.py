# 9.5
# coding=utf-8

def sums(n):
    if n == 1:
        return 1
    else:
        n += sums(n-1)
    return n
n = eval(input("请输入一个数，我们将从1加到它："))
print(f"他们的和为：{sums(n)}")