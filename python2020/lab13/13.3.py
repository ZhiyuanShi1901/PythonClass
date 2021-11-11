# 13.3
# coding=utf-8

class Student:
    def __init__(self, stunumber, name, age, grades):
        self.stunumber = stunumber
        self.grade_1 = float(grades[0])
        self.grade_2 = float(grades[1])
        self.grade_3 = float(grades[2])
        self.name = name
        self.age = age


    def __Aver__(self):
        return (self.grade_1 + self.grade_2 +self.grade_3)/3

    def __Best__(self):
        return max(self.grade_1, self.grade_2, self.grade_3)



students = []
i = 1
while True:
    stunumber = input(f"请输入第{i}个学生的学号：")
    if stunumber == '':  # 当输入为空时，解除循环。
        break
    name, age = input("请输入他/她的姓名和年龄，用','隔开：").split(',')
    grades = []
    for j in range(1, 4):
        grade = input(f"第{j}门科目的成绩为：")
        grades.append(grade)
    student = Student(stunumber, name, age, grades)
    students.append(student)
    i += 1

for student in students:
    print("{}的平均成绩为：{:4.2f}\n最高分为：{:4.2f}。".format(student.name, student.__Aver__(), student.__Best__()))



