# di1t
# coding=utf-8

setaarray = ((1, 5, 97, 52), (25, 58, 96, 35), (48, 12, 32, 58), (45, 23, 41, 23))
sum_diagonals, sum_diagonal_lines = 0, 0
width=len(setaarray)
for i in range(0, width):
    sum_diagonals += setaarray[i][i]
    sum_diagonal_lines += setaarray[i][width-1-i]   #斜对角线上坐标之和为矩阵的宽度（长度）-1

print(f"矩阵的对角线元素之和为：{sum_diagonals},斜对角线元素之和为：{sum_diagonal_lines}")
