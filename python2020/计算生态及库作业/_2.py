# _2
# coding=utf-8
import random
def countchar(letter, list):
    number = 0
    for le in list:
        if le == letter:
            number+=1
        else:
            continue
    return number

n = input("请输入随机生成的英文字符个数：")
list = ''
for i in range(0, eval(n)):
    letter = random.randint(1, 27)
    list += chr (letter+96)

for number in range(97, 97+26):
    print('{:<5}{:>4}'.format(chr(number), countchar(chr(number), list)))
print('{:' '<5}{:>4}'.format('总数', len(list)))



