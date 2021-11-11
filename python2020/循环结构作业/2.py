# 2
# coding=utf-8
numbers = []
for i in range(1, 5):
    for j in range(1, 5):
        if j != i:
            for k in range (1, 5):
                if k != i and k != j:
                    numbers.append(int(str(i)+str(j)+str(k)))

print(f"可以组成{len(numbers)}个不同且没有重复数字的数。这些数为：")
print(numbers)