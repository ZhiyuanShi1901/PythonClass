# 4.1
# coding=utf-8
a,b = input("请键入一对坐标值（中间用空格隔开）：").split()
a=int(a)
b=int(b)
if a > 0 and b > 0:
    print("这是第一象限坐标。")
elif a > 0 and b < 0:
    print("这是第二象限坐标。")
elif a < 0 and b < 0:
    print("这是第三象限坐标。")
elif a < 0 and b > 0:
    print("这是第四象限坐标。")
elif a == 0 and b == 0:
    print("它是原点。")
elif a == 0 and b != 0:
    print("它在y轴上。")
elif  b == 0 and a != 0:
    print("它在x轴上。")

