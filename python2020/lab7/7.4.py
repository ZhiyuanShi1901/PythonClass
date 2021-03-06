# 7.4
# coding=utf-8

# 浅拷贝： 新列表值改变，原列表值会改变
list__1 = [4, 5, 8, 9.6, 2, 12, 32, 44, 52]
list__2 = list__1

list__1[0] = 5
print(list__1)
print(list__2)

# 深拷贝：新列表值改变，原列表值不改变
list__1 = [4, 5, 8, 9.6, 2, 12, 32, 44, 52]
list__2 = []
for i in range(0, len(list__1)):
    list__2.append(list__1[i])
list__1[0] = 5
print(list__1)
print(list__2)

# 浅拷贝只拷贝了原有列表的存储位置，新列表名实际上指向的存储位置仍然是老列表的位置，因此当新列表改变之后，原有老列表也改变了。
# 深拷贝将每一个原有老列表中的值复制到另一个存储区域内，即新列表所指向的另一个存储区域，因此改变新列表值，原有老列表不会改变。