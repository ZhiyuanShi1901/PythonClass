# 8.4
# coding=utf-8
import copy
# dictionary_1 = {'Huawei': 10000,'Samsung': 50000, 'Apple': 70000, 'Sony': 5000, 'Xiaomi': 65000, 'Vivo': 60000, 'Oneplus': 40000}
# dictionary_2 = dictionary_1
# del dictionary_1['Sony']
# print(dictionary_1)
# print(dictionary_2)
#
# dictionary_1 = {'Huawei': 10000,'Samsung': 50000, 'Apple': 70000, 'Sony': 5000, 'Xiaomi': 65000, 'Vivo': 60000, 'Oneplus': 40000}
# dictionary_2 = {}
# for key, value in dictionary_1.items():
#     dictionary_2[key] = value
#
# del dictionary_1['Huawei']
# print(dictionary_1)
# print(dictionary_2)

#浅拷贝
dictionary_1 = {'Huawei': 10000, 'Samsung': 50000, 'Apple': 70000, 'Sony': 5000, 'Xiaomi': 65000, 'Vivo': 60000, 'Oneplus': 40000}
dictionary_2 = copy.copy(dictionary_1)
print("dictionary_1的id：", id(dictionary_1))
print("dictionary_2的id：", id(dictionary_2))
dictionary_1['Sony'] = 80000
print(dictionary_1)
print(dictionary_2)

#深拷贝
dictionary_1 = {'Huawei': 10000, 'Samsung': 50000, 'Apple': 70000, 'Sony': 5000, 'Xiaomi': 65000, 'Vivo': 60000, 'Oneplus': 40000}
dictionary_2 = copy.deepcopy(dictionary_1)
print("dictionary_1的id：", id(dictionary_1))
print("dictionary_2的id：", id(dictionary_2))
dictionary_1['Sony'] = 80000
print(dictionary_1)
print(dictionary_2)


#浅拷贝3（二维）
dictionary_1 = {'Huawei': 10000, 'Samsung': [50000, 6000, 7000], 'Apple': 70000, 'Sony': 5000, 'Xiaomi': 65000, 'Vivo': 60000, 'Oneplus': 40000}
dictionary_2 = copy.copy(dictionary_1)
print("dictionary_1的id：", id(dictionary_1))
print("dictionary_2的id：", id(dictionary_2))
dictionary_1['Sony'] = 80000
dictionary_1['Samsung'][2] = 8000
print(dictionary_1)
print(dictionary_2)

#深拷贝3（二维）
dictionary_1 = {'Huawei': 10000,'Samsung': [50000, 6000, 7000], 'Apple': 70000, 'Sony': 5000, 'Xiaomi': 65000, 'Vivo': 60000, 'Oneplus': 40000}
dictionary_2 = copy.deepcopy(dictionary_1)
print("dictionary_1的id：", id(dictionary_1))
print("dictionary_2的id：", id(dictionary_2))
dictionary_1['Sony'] = 80000
dictionary_1['Samsung'][2] = 8000
print(dictionary_1)
print(dictionary_2)