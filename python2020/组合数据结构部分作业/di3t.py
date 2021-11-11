# di3t
# coding=utf-8
from numpy import array, dot
setarray_1 = ((1, 5, 97, 52), (25, 58, 96, 35), (48, 12, 32, 58), (45, 23, 41, 23))
setarray_2 = ((15, 85, 25, 32), (2, 8, 9, 5), (45, 42, 22, 8), (4, 3, 1, 3))
print("原矩阵为：{}\n{}\n乘积为:{}".format(setarray_1, setarray_2, tuple(dot(array(setarray_1), array(setarray_2)))))


# 7.3
# coding=utf-8
# from numpy import array
# A = ((2, 1, 4, 3, 2), (5, 6, 1, 4, 0), (3, 5, 2, 4, 1))
# B = ((1, 2, 3, 4), (4, 3, 2, 1), (0, 2, 6, 7), (3, 5, 2, 6), (1, 8, 5, 4))
#
# product = []
# for i in range(0, len(A)):  #创建一个与A行数相同的数组
#     product.append([])
# for k in range(0, len(A)): #需要计算三行数据
#     for i in range(0, len(B[0])): #每行需要计算四次
#         number = 0
#         for j in range(0, len(B)): #每次需要计算五组
#             number += A[k][j]*B[j][i]
#         product[k].append(number)
#
# print(f"{array(A)}*\n{array(B)}=\n{array(product)}")
