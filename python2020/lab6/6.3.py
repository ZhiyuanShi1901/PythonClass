# 6.3
# coding=utf-8
from math import pow
narnum = []
# 1字符表征
for i in range(100, 1000):
    s = str(i)
    if int(s[0])**3+int(s[1])**3+int(s[2])**3 == int(s[0])*100+int(s[1])*10+int(s[2]):
        narnum.append(int(s[0])*100+int(s[1])*10+int(s[2]))
print(f"100-999之间的水仙花数：{narnum}")

# 2循环嵌套
narnum = []
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if pow(i, 3)+pow(j, 3)+pow(k, 3) == i*100+j*10+k:
                narnum.append(i*100+j*10+k)
print(f"100-999之间的水仙花数：{narnum}")
'''
# 法3
narnum = []
for i in range(100, 1000):
    a = i % 10
    b = int(int(i/10) % 10)
    c = int(i/100)
    if pow(a, 3)+pow(b, 3)+pow(c, 3) == i:
        narnum.append(i)
print(f"100-999之间的水仙花数：{narnum}")
'''