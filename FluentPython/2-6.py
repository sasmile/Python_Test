# color = ['black','white']
# size = ['s','m','l']
# for shirt in ('%s %s' % (c,s) for c in color for s in size):
#     print(shirt)

import os
from collections import namedtuple
City = namedtuple('city','name country populations coordinates')
tokyo = City('tokyo','JP',36.33,(123455.34,9294858,987))
print(tokyo)