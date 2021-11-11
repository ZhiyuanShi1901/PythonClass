# example 2-4
#
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# '''
# tshitrs = [(color, size) for color in colors for size in sizes]
# print(tshitrs)
# '''
# for color in colors:
#      for size in sizes:
#          print((color, size))


# # example 2-6
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
#     print(tshirt)
#
# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
#
# for country, _ in traveler_ids:
#     print(country)


# # example 2-8
# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR, 19.649', 19.3649,  (-23.547778, -46.635833)),
# ]
#
# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     if longitude <= 0:
#         print(fmt.format(name, latitude, longitude))

# # example 2-9
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# print(tokyo.population)
# print( tokyo.coordinates)
#

# example 2-10
# print(City._fields)  #包含这个类所有字段名称的元组
# LatLong = namedtuple('LatLong', 'lat long')
# delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# delhi = City._make(delhi_data)
# print(delhi._asdict())
#
# for key, value in delhi._asdict().items():
#     print(key + ':', value)

# example 2-17
import bisect
import sys
# HAYSTACK = [1, 4, 5, 6, 8, 15, 12, 20, 21, 23, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
#
# ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'
#
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position * '  |'
#         print(ROW_FMT.format(needle, position, offset))
#
# if __name__=='__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#
#     print('DEMO:', bisect_fn.__name__)
#     print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
#     demo(bisect_fn)
#
# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]
#
# print(grade(70))

# # example 2-20
from array import array
from random import random
# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()
# floats2 = array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**7)
# fp.close()
# print(floats2[-1])
# print(floats2==floats)

# example 2-21
# numbers = array('h', [-2, -1, 0, 1, 2])
# memv = memoryview(numbers)
# print(len(memv))
# print(memv[0])
# memv_oct = memv.cast('B')
# print(memv_oct.tolist())
# memv_oct[5]=4
# print(numbers)

import numpy

# example 2-22
a = numpy.arange(12)
print(a)
print(type(a))
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])

print(a[:, 1])
print(a.transpose())
print(a)

from collections import deque