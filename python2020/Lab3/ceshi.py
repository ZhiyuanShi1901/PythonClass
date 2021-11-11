import scipy
import numpy
import pandas
import math
scipylists = []
numpylists = []
pandaslists = []
mathlists = []

scipylists = dir(scipy)
numpylists = dir(numpy)
pandaslists = dir(pandas)
mathlists = dir(math)

list = []
for sp in mathlists:
    if sp in scipylists:
        print("{}".format(sp))
        list.append(sp)
print("{}".format(len(list)))
