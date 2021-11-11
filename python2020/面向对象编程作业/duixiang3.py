# duixiang3
# coding=utf-8

class Stu:
    def __init__(self, stunumber, grade_1, grade_2):
        self.stunumber = stunumber
        self.grade_1 = grade_1
        self.grade_2 = grade_2


    def __Display__(self):
        print("学生学号：{}\n成绩1：{}\n成绩2：{}".format(self.stunumber, self.grade_1, self.grade_2))


    def __Aver__(self):
        return (self.grade_1 + self.grade_2)/2


    def __Change__(self, newgrade_1, newgrade_2):
        self.grade_1 = newgrade_1
        self.grade_2 = newgrade_2


student1 = Stu(1908525412, 98, 20)
print("学号{}的平均成绩为：{}。".format(student1.stunumber, student1.__Aver__()))
