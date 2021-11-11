# 15.2
# coding=utf-8

grades = []
number = 1  # 进行有效学生成绩个数的记录
while True:
    grade = eval(input(f"请输入第{number}个学生的英语成绩："))
    try:
        assert 0 <= grade <= 100  # 如果成绩不在这个区间之内，抛出AssertionError。
    except AssertionError:
        print("成绩应为0-100之间，请输入正确的成绩。该成绩无效")
    else:
        grades.append(grade)
        number += 1  # 保证有效成绩个数不受到其他干扰
    finally:
        aver = sum(grades) / len(grades)  # 每一次输入均进行一次平均成绩计算
        print("平均成绩为：{:.2f}".format(aver))
        print(f"已输入{len(grades)}个学生的有效成绩。")  # 输出已有的有效成绩个数
        if len(grades) == 10:
            print("小组成绩输入结束。")
            break
