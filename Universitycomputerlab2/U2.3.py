# U2.3
# coding=utf-8
weight, increase = input("请输入你今年的体重和你每年增长的体重:").split(",")
weight, increase = eval(weight), eval(increase)
year = 15
weight += year*increase
print("{}年后你在月球的体重为：{:.5}。".format(year, weight*0.165))