# 5.1
# coding=utf-8
year = int(input("请输入一个年份，我们将判断它是否为闰年："))
if year % 4 == 0 and year % 100 != 0 :
    print("这一年份是闰年。")
elif year % 100 == 0:
    print("这一年份是闰年。")
elif year % 400 == 0:
    print("这一年份是闰年。")
else:
    print("这一年份不是闰年。")