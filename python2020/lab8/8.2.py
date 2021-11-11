# 8.2
# coding=utf-8

students = []
for i in range(0, 10):
    students.append({})
for i in range(0, 10):
    condition = True
    students[i]['name'] = input(f"输入第{i+1}名学生的姓名：")
    print(f"请输入{students[i]['name']}的所修科目和成绩（输入‘q’结束输入）：")
    j = 1
    while condition:
        subject = input(f"第{j}个科目:")
        if subject == 'q':
            condition = False
        else:
            grade = input("科目成绩:")
            students[i][subject] = eval(grade)
            j += 1

print("成绩导入完成。")
name = input("请输入学生的姓名：").lower() # 将学生姓名转化为全小写以便于寻找。

for student in students:
    if student['name'].lower() == name:
        for key, keynote in student.items():
            print(f"{key.title()}的成绩为: {keynote}")
