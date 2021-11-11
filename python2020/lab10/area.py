# area
# coding=utf-8
import math as m
def triangle_area(a,b,c):
    s = (a + b + c) / 2
    return m.sqrt(s * (s - a) * (s - b) * (s - c))

def incircle_area(a,b,c):
    s = (a + b + c) / 2
    incircle_r = m.sqrt((s - a) * (s - b) * (s - c) / s)
    return m.pi * (incircle_r ** 2)

def outcircle_area(a, b, c):
    s = (a + b + c) / 2
    outcircle_r = a * b * c / (4 * m.sqrt(s * (s - a) * (s - b) * (s - c)))
    return m.pi * (outcircle_r ** 2)
