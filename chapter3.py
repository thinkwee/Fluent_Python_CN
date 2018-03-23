import re
import sys
import collections
from types import MappingProxyType
from unicodedata import name

'''
    introduce:
        dictcomp
        default in dict
        userdict
        MappingProxyType
        sets
        setcomp        
'''

# dictcomp
dial_code = [(86, 'China'), (91, 'India'), (1, 'US')]
country_code = {country: code for code, country in dial_code}
print(country_code)


# set default in dict
# use defaultdict
# use special method __missing__

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


testdict0 = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(testdict0['2'])
print(testdict0[4])
# print(testdict0[1])
print(testdict0.get('2'))
print(testdict0.get(4))
print(testdict0.get(1, 'default value'))
print(2 in testdict0)
print(1 in testdict0)


# other dict in collections
# collections.OrderedDict
# collections.ChainMap
# collections.Counter

# use userdict
class StrKetDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    # some other useful method:Mapping.update,Mapping.get


# immutable dict
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
# d_proxy[2] = 'x'
d[2] = 'B'
print(d_proxy)

# use sets to delete repetition
l = ['spam', 'spam', 'egg', 'spam']
print(set(l))

# support sets operation like a|b,a&b,a-b,a in b,a<=b,a<b,a>=b,a>b

# use set() to create a empty sets otherwise you will get a empty dict
# but you can use literal to create a non-empty set
s = {1}
print(s)
s.pop()
print(s)

# frozen set can not be created using literal
print(frozenset(range(10)))

# setcomps
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
