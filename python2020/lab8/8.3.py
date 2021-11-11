# 8.3
# coding=utf-8

setA = {1,52,63,58,85,41,23}
setB = {2,36,58,92,12,14,52,41}
intersection = []
unionset = []
differenceset = []
for value in setA:
    unionset.append(value)
    if value in setB:
        intersection.append(value)
    if value not in setB:
        differenceset.append(value)
for value in setB:
    unionset.append(value)
set(unionset)

print("交集：{}\n并集：{}\n差集：{}".format(intersection, unionset, differenceset))
