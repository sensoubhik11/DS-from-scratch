#not to be run
#python syntax notes

# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a = 'aabbbbccddefoo'
# The counter store the elements as keys(ordered way) and their frequencies in value
# we can also have list
frequency_of_letters = Counter(a)
print(frequency_of_letters)
# Output:
# Counter({'b': 4, 'a': 2, 'c': 2, 'd': 2, 'o': 2, 'e': 1, 'f': 1})

print(frequency_of_letters.values())         # return list of values
print(frequency_of_letters.items())          # return list of tuple pairs
print(frequency_of_letters.keys())           # returns list of keys
print(list(frequency_of_letters.elements())) # returns list of elements

print(frequency_of_letters.most_common(2))

# lightweight object type similar to struct
from collections import namedtuple

Point = namedtuple('Point','x,y')

pt1 = Point(1,2)
print(pt1)
print('x = {} y = {}'.format(pt1.x,pt1.y))

# defaultdict returns default value when value of a non-existent key is called
# On the other hand normal dict will return key error
from collections import defaultdict

d = defaultdict(int)  # values are of type int, the default value of int is 0

d['a'] = 1
d['b'] = 2
print(d['c'])         # output 0 which is default value of int

# deque is a double ended queue(bot sides remove or add)
from collections import deque
# confusion
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)
