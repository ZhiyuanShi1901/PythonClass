# 5.3
# coding=utf-8
import math as m
from math import pi
print("x\t\t\tsin(x)\t\t\tcos(x)")
for i in range(0, 181, 10):
    x = i
    x = int(i)/180*pi
    print("{:8.0f}\t{:8.4f}\t{:8.4f}".format(i, m.sin(x), m.cos(x)))