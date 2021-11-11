# 12.2
# coding=utf-8

import pickle
with open('bin.pkl', 'wb+') as bin:
    with open('C:/Users/Muadibu/PythonClass/lab11/shuixianin1000.txt','r') as shuixian:
        shuju = shuixian.readlines()
    pickle.dump(shuju, bin)
    bin.seek(0)
    print(pickle.load(bin))
