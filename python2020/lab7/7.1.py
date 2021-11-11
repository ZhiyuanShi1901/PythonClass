# 7.1
# coding=utf-8

numbers = []
for i in range(0, 10):
    numbers.append(eval(input(f"请输入第{i+1}个数字：")))

print(f"排序前的数为：{numbers}")

# # 方法1
# for j in range(0, 9):
#     for i in range(0, 9-j):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = (numbers[i+1], numbers[i])
# print(f"排序后的数为：{numbers}")

# 方法2
print(sorted(numbers))

# # 方法3
# for j in range(0, 9):
#     for i in range(0, 9-j):
#         if numbers[i] < numbers[i+1]:
#             numbers[i], numbers[i+1] = (numbers[i+1], numbers[i])
# print(f"排序后的数为：")
# for i in range(9, -1, -1):
#     print(f"{numbers[i]} ", end="")