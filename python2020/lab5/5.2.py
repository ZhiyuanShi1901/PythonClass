# 5.2
# coding=utf-8
condition = True
i = 1
A, B, C, D, E = 0, 0, 0, 0, 0
sum = 0
sum = float(sum)
while condition:
    score = eval(input(f"请输入第{i}个学生的成绩:"))
    if score <= 100 and score >= 90:
        A += 1
        sum += score
        i += 1
    elif score <= 89 and score >= 80:
        B += 1
        sum += score
        i += 1
    elif score <= 79 and score >= 70:
        C += 1
        sum += score
        i += 1
    elif score <= 69 and score >= 60:
        D += 1
        sum += score
        i += 1
    elif score <= 59 and score >= 0:
        E += 1
        sum += score
        i += 1
    else:
        condition = False
aver = sum/(i-1)
print(f"总人数为：{i-1}")
print("各档次人数：")
print("A:{}\nB:{}\nC:{}\nD:{}\nE:{}".format(A,B,C,D,E))
print("平均成绩为{:.2f}".format(aver))
