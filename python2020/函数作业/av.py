# av.py
# coding=utf-8
from math import pi, sqrt


def cylinder_v(r, h):
    return pi * r ** 2 * h


def cylinder_s(r, h):
    return 2 * pi * r ** 2 + 2 * pi * r * h


def cone_v(rander, length):
    return pi * (rander ** 2) * sqrt(length**2-rander**2) / 3


def cone_s(rander, length):
    return pi * rander * (rander + length)
