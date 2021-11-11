#example3-1
from collections import abc
import re
import sys
import collections

# example 3-4
# WORD_RE = re.compile(r'\w+')
# index = {}
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start(+1)
#             location = (line_no, column_no)
#             index.setdefault(word, []).append(location)
#
# for word in sorted(index, key=str.upper):
#     print(word, index[word])

# example 3-5

# ct=collections.Counter('hiuahguhughadfghuiy8s')
# print(ct)
# print(ct.most_common(5))

from types import MappingProxyType
# d={1:'A'}
# d_proxy = MappingProxyType(d)  # 创建了一个不能更改的字典，这个字典所显示的是d的内容
# # print(d_proxy)
# print(d_proxy[1])
# # d_proxy[2]='s'
# d[2]='B'
# print(d_proxy)


# s={1,1,2,3}
# print(s)
from dis import dis
dis('{1}')
dis('set([1])')

from unicodedata import name
