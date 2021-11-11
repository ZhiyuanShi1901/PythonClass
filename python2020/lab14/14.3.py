# 14.3
# coding=utf-8

class Student:
    def __init__(self, stunumber, name, age, grades):
        self.stunumber = stunumber
        self.grade_1 = int(grades[0])
        self.grade_2 = int(grades[1])
        self.grade_3 = int(grades[2])
        self.name = name
        self.age = age

    def __Display__(self):
        print("学号：{}\n姓名：{}\n年龄：{}\n成绩1：{}\n成绩2:{}\n成绩3：{}".format(self.stunumber, self.name, self.age, self.grade_1, self.grade_2, self.grade_3))

    def __Aver__(self):
        return (self.grade_1 + self.grade_2 +self.grade_3)/3

    def __Best__(self):
        return max(self.grade_1, self.grade_2, self.grade_3)

    def __ADD__(self, other_1, other_2):
        self.stunumber = other_1.stunumber
        self.name = other_1.name
        self.age = other_1.age
        self.grade_1 = other_1.grade_1 + other_2.grade_1
        self.grade_2 = other_1.grade_2 + other_2.grade_2
        self.grade_3 = other_1.grade_3 + other_2.grade_3


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

addstudent = Student('', '', '', [0, 0, 0])
addstudent.__ADD__(students[0], students[1])
addstudent.__Display__()


