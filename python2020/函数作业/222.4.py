# 222.4
# coding=utf-8
from av import cylinder_v, cylinder_s, cone_v, cone_s
print("下面的程序执行计算圆柱体和圆锥体的体积和表面积。请输入所需要的参数：")
r = eval(input("请输入圆柱体的半径："))
h = eval(input("请输入圆柱体的高："))
rander = eval(input('请输入圆锥体的底面半径：'))
length = eval(input('请输入圆锥体的侧边长：'))

print('圆柱体的体积为：{0:.4}表面积为：{1:.4}'.format(cylinder_v(r, h), cylinder_s(r, h)))
print('圆锥体的体积为：{0:.4}表面积为：{1:.4}'.format(cone_v(rander, length), cone_s(rander, length)))

