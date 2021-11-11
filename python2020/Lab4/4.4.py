# 4.4
# coding=utf-8
x, y, z = input("请输入三个数，中间用空格隔开，我们将对其进行由小到大的排序：").split()
x = eval(x)
y = eval(y)
z = eval(z)

#方法1 冒泡排序
if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > z:
    x, z = z, x
print("从小到大的排序为：{},{},{}。".format(x,y,z))
'''
#方法二：数组排序
number = []
number.append(x)
number.append(y)
number.append(z)
number.sort()
print(number)
'''