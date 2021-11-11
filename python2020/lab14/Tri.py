# 13.1
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

    def __Sumoftri__(self):
        return 2*self.s

