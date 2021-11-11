# 16.4
# coding=utf-8
import turtle as ttl
ttl.setup(1920, 1080, startx=0, starty=-20)
r=20
ttl.speed(200)
ttl.pendown()
ttl.pensize(1) #设置笔的宽度为1
ttl.pencolor('green')#设置笔的颜色为绿色
for i in range(0, 20):  #循环进行20个圆形的绘图
    ttl.circle((i+1)*r)  #设置画圆，半径为r的倍数
    ttl.penup()
    ttl.setheading(-90) #设置朝向为y轴负方向
    ttl.forward(r)   # 向下移动一个半径的大小
    ttl.setheading(0)  # 回到初始转向方向
    ttl.pendown()


ttl.exitonclick()