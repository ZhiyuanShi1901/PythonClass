# 8.1
# coding=utf-8

n = eval(input("请问你需要统计多少个学生的成绩，输入个数:"))
grades = {'student_number' : [value for value in range(1, n+1)], 'Math': [], 'English': [], 'Chinese': [], 'Physics': [], 'Geophysics': [],
                'Chemistry': [], 'Biology': [], 'Politics': [], 'Sums': [], 'Aver': []}

for i in range(0, n):
    grades['Math'].append(eval(input(f"第{i+1}名学生的Math成绩为：")))
    grades['English'].append(eval(input(f"第{i+1}名学生的English成绩为：")))
    grades['Chinese'].append(eval(input(f"第{i+1}名学生的Chinese成绩为：")))
    grades['Physics'].append(eval(input(f"第{i+1}名学生的Physics成绩为：")))
    grades['Geophysics'].append(eval(input(f"第{i+1}名学生的Geophysics成绩为：")))
    grades['Chemistry'].append(eval(input(f"第{i+1}名学生的Chemistry成绩为：")))
    grades['Biology'].append(eval(input(f"第{i+1}名学生的Biology成绩为：")))
    grades['Politics'].append(eval(input(f"第{i+1}名学生的Politics成绩为：")))

for i in range(0, n):
    grades['Sums'].append(grades['Math'][i]+grades['English'][i]+grades['Chinese'][i]+grades['Physics'][i]+grades['Geophysics'][i]+grades['Chemistry'][i]+grades['Biology'][i]+grades['Politics'][i])
    grades['Aver'].append(grades['Sums'][i]/8)

print("序号\t总成绩\t平均成绩")
for i in range(0, n):
    print("{:>2}\t{:>5}\t{:>}".format(grades['student_number'][i], grades['Sums'][i], round(grades['Aver'][i], 2)))