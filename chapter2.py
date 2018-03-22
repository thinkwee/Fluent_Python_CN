from collections import namedtuple
import bisect
import random
from array import array
from collections import deque

'''
introduce:
    list comprehension
    generator expression
    tuple
    slice
    list.sort&sorted
    bisect
    array
    deque
'''

# generator expression
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# tuple unstack
print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

a, b, *rest = range(5)
print(a, b, rest)

metro_ares = [
    ('tokyo', 'jp', 36.933, (35.689, 139.691)),
    ('sao paulo', 'br', 19.649, (-23.547, -46.635)),
]

for name, cc, pop, (latitude, longtitude) in metro_ares:
    print('{:15} | {:9.4f} | {:9.4f}'.format(name, latitude, longtitude))

# named tuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'jp', 36, (35.689, 139.691))
print(tokyo)
print(tokyo.coordinates)
print(City._fields)
print(tokyo._asdict())

# tuple as fixed list
# tuple can not add/eliminate element
# tuple can not reverse

# slice on object
file = open('chap2.txt')
text = file.read()
name = slice(0, 8)
num = slice(10, 12)
line_item = text.split('\n')[:]
for item in line_item:
    print(item[name], item[num])

# other slice operations
test = list(range(10))
test[1:6] = [100]
print(test)
print(test * 2)

# wrong way to initiate a list in list
board = [[0] * 3] * 3
print(board)

# right way
board = [[0] * 3 for i in range(3)]
print(board)

# increment on slice
# increment will create a new object if it operate on immutable object
t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))

# list.sort returns none,cause it is sorted locally(do not create a new object)
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
fruits.sort()
print(fruits)


# bisect(haystack,needle) divide haystack into pieces based on the needles
def grade(score, breakpoints=[60, 70, 80, 90], grade='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grade[i]


print([grade(score) for score in [33, 99, 77, 70, 89, 98, 100]])

# use bisect.insort to assure the sorted list is still sortable after insertion
size = 7
random.seed(144)
my_list = []
for _ in range(size):
    new_item = random.randrange(size * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

# array is more efficient than list if you just store numbers
floats = array('d', (random.random() for _ in range(10 ** 3)))
print(floats[1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 3)
fp.close()
print(floats2[1])

# use deque to safely add and delete elements on both ends of a list
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.appendleft(-100)
print(dq)
dq.extend([10, 20, 30])
print(dq)
dq.extendleft([-1, -2, -3])
print(dq)
