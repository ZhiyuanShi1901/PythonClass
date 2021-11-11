# 222.1
# coding=utf-8

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return("这一年份是闰年。")
    elif year % 100 == 0:
        return("这一年份是闰年。")
    elif year % 400 == 0:
        return("这一年份是闰年。")
    else:
        return("这一年份不是闰年。")

year = int(input("请输入一个年份，我们将判断它是否为闰年："))
print(leap_year(year))

