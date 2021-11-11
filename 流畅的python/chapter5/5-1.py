import random
#
# class BingoCage:
#     def __init__(self, items):
#         self._items = list(items)
#         random.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingoCage')
#
#     def __call__(self):
#         return self.pick()
#
# bingo = BingoCage(range(3))
# print(bingo.pick())
# print(bingo())
# print(callable(bingo))

import bobo

def clip(text, max_len=80):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
    if end is None:
        end=len(text)
    return text[:end].rstrip()

# clip.__defaults__


from abc import ABC, abstractmethod
from collections import namedtuple


