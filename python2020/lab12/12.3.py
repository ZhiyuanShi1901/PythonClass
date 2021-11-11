# 12.3
# coding=utf-8
import re
import string
with open('singPRC.txt', 'r', encoding='utf-8') as song:
    with open('singPRC2.txt', 'w', encoding='utf-8') as song2:
        while True:
            line = song.readline()
            if line == '':
                break
            else:
                line = line.replace('祖国', '中国')
                song2.write(line)

