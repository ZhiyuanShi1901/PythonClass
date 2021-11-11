# 14.2
# coding=utf-8
from math import sqrt, pi
from Cir import Cir
class Cyl(Cir):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h
        self.l = sqrt(self.h**2 + self.r**2)

    def __Sum__(self):
        return self.__S__() + self.r * pi * self.l


    def __V__(self):
        return self.__S__() * self.h/3

cone = Cyl(5, 8)
print("圆锥体的表面积为：{:.3f}，体积为：{:.3f}。".format(cone.__Sum__(), cone.__V__()))