# 13.2
# coding=utf-8

from math import pi, sqrt
class Cir:
    def __init__(self,r):
        self.r = r


    def __Display__(self):
        print("圆半径为：{}".format(self.r))

    def __S__(self):
        return pi*self.r**2


    def __Sum__(self):
        return pi*self.r*2


circle = Cir(5)
print("圆的面积为：{}，周长为：{}。".format(circle.__S__(), circle.__Sum__()))
