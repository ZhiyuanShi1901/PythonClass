# duixiang2
# coding=utf-8
from math import pi, sqrt
class Cyl:
    def __init__(self,r,h):
        self.r = r
        self.h = h


    def __Display__(self):
        print("圆柱体的底面半径为：{}\n高为：{}".format(self.r, self.h))

    def __S__(self):
        return 2*pi*self.r*self.h + 2*pi*self.r**2


    def __V__(self):
        return pi*self.h*self.r**2


    def __change__(self, newr, newh):
        self.r = newr
        self.h = newh

cylinder = Cyl(2,5)
print("圆柱体的表面积为：{}，体积为：{}。".format(cylinder.__S__(), cylinder.__V__()))
cylinder.__change__(3, 10)
print("圆柱体的表面积为：{}，体积为：{}。".format(cylinder.__S__(), cylinder.__V__()))