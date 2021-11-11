import matplotlib.pyplot as plt
from math import pi, sqrt, exp, pow
# 二层模型表面电测深曲线的计算
line = []
dx = 0.1
xpart = -5 + dx  # x坐标对应的值
ypart = []  # y坐标对应的值

n0 = eval(input('请输入层数：'))
m0 = n0 - 1
p, h = [], []

for i in range(0, n0):  # 输入每一层的电阻率p
    p.append(eval(input(f"请输入p{i+1}:")))
for i in range(0, n0-1):  # 输入每一层的层高（厚度）h
    h.append(eval(input(f"请输入h{i+1}:")))
T = eval(input('请输入频点周期：'))
R0 = eval(input(f'请输入R{n0},{n0}：'))
m = m0
R = R0
while( m != 1 ):
    L = (1 - sqrt(p[m] / p[m-1])*R)/(1 + sqrt(p[m] / p[m-1])*R)
    k = 2 * pi * (1-1j)/sqrt(10 * p[m-1] * T)
    R = (1 - L * exp(-2 * k * h[m-1]))/(1 + L * exp(-2 * k * h[m-1]))
    m = m-1
pT = p[0] * pow(R, 2)
