# 7.2
# coding=utf-8
from numpy import array
matrix = []
for i in range(0, 5):
    matrix.append([])
for i in range(0, 5):
    for j in range(0, 5):
        if i == j:
            matrix[i].append(1)
        else:
            matrix[i].append(0)
print("方阵：")
for i in range(0, 5):
    for j in range(0, 5):
        print("{:2}".format(matrix[i][j]), end='')
    print()

print(f"矩阵：\n{array(matrix)}")
