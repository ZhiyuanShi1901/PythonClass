# di2t
# coding=utf-8

setaarray = ((1, 5, 97, 52), (25, 58, 96, 35), (48, 12, 32, 58), (45, 23, 41, 23))
maxrow, minrow, cols, cols_1 = [], [], [], []
for rows in setaarray:
#最大值循环
    number = max(rows)
    cols.append(rows.index(number))
    maxrow.append(number)
#最小值循环
    number_1 = min(rows)
    cols_1.append(rows.index(number_1))
    minrow.append(number_1)
#最大值求解
maxnumber = max(maxrow)
row = maxrow.index(maxnumber)
col = cols[row]
#最小值求解
minnumber = min(minrow)
row_1 = minrow.index(minnumber)
col_1 = cols_1[row_1]

print("矩阵的最大值为：{},行列值为：({},{})".format(maxnumber, row, col))
print("矩阵的最小值为：{},行列值为：({},{})".format(minnumber, row_1, col_1))
