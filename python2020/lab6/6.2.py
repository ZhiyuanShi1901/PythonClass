# 6.2
# coding=utf-8
primnum = [] #设定一个素数列表
for i in range(1, 301):
    condition = 0  #设置判断条件，如果其不是素数，则条件为1
    for j in range(2, i):
        if i%j == 0:
            condition = 1
            break
        else:
            continue

    if condition == 0:
        primnum.append(i)

print(f"一共有{len(primnum)}个素数")
print(f"300以内的素数为：{primnum}")
