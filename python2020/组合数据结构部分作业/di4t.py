# di4t
# coding=utf-8

studnumber = 20
grades = []
grades_upper = []
sum = 0
for i in range(0, studnumber):
    grades.append(input(f"请输入第{i+1}名学生的成绩："))
    sum += eval(grades[i])
aver = sum/studnumber

for grade in grades:
    if eval(grade) >= aver:
        grades_upper.append(grade)
print("平均成绩为：{}\n不低于平均成绩的人数为：{}".format(aver, len(grades_upper)))