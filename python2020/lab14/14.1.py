# 14.1
# coding=utf-8

from Tri import Tri

class Pyr(Tri):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def __S__(self):
        return self.__Areaoftriangle__()*2 + 2*self.s*self.h


    def __V__(self):
        return self.__Areaoftriangle__()*self.h


pyrism = Pyr(3, 4, 5, 8)
print("三棱柱的表面积为：{}\n体积为{}。".format(pyrism.__S__(), pyrism.__V__()))