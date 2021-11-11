# coding=utf-8
i = 1
unpassed, excellent= int(0), int(0)
while i <= 20:
    score = eval(input(f"请输入第{i}名同学的成绩："))
    if score > 90:
        excellent += 1
        i+=1
    elif score < 60:
        unpassed += 1
        i+=1
    else:
        i+=1
print(f"不及格的人数：{unpassed}\n90分以上的人数为：{excellent}")
