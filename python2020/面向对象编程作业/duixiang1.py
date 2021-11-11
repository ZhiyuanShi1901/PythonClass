# duixiang1
# coding=utf-8
import math as m
class Tri:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.s = (self.a + self.b + self.c) / 2


    def __Display__(self):
        print("三角形的三边长为：{},{},{}。".format(self.a, self.b, self.c))

    def __Areaoftriangle__(self):
        return m.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))

    def __Areaofincircle__(self):
        incircle_r = m.sqrt((self.s - self.a) * (self.s - self.b) * (self.s - self.c) / self.s)
        return m.pi * (incircle_r ** 2)


    def __Areaofoutcircle__(self):
        outcircle_r = self.a * self.b * self.c / (4 * m.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * //
                                                             (self.s - self.c)))
        return m.pi * (outcircle_r ** 2)

triangle = Tri(3, 4, 5)
print("三角形的面积为：{}\n内切圆面积为：{:}\n外接圆面积为：{:}。".format(triangle.__Areaoftriangle__(), triangle.__Areaofincircle__(), triangle.__Areaofoutcircle__()))