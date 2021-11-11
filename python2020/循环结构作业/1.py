# 1
# coding=utf-8

n = int(input("请输入想要得到的斐波那契数列某项的项数："))
FibonSequence = [1, 1]
for i in range(3, n+1):
    FibonSequence.append(FibonSequence[i-3] + FibonSequence[i-2])
print(FibonSequence[n-1])
