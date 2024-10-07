#not to be run
#python syntax notes

# itertools : product, permutations, combinations, accumulate, groupby and infinite iterators

# cartesian product of lists 
from itertools import product

a = [1,2]
b = [3,4]
cartesian_product = product(a,b)  # a×b

print(list(cartesian_product))    # list of ordered pairs of a×b

# permuations
from itertools import permutations

balls = ['a','b','c']       # (3! or 3P3)

perm = permutations(balls)

print(list(perm))

perm_2 = permutations(balls,2)  # (3×2 or 3P2)
print(list(perm_2))

# combinations
from itertools import combinations

balls = ['a', 'b','c']
comb = combinations(balls, 3)   # (3C3)
print(list(comb))
comb = combinations(balls, 2)   # (3C2)
print(list(comb))

# combinations with replacement
from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(balls, 2)   # (3C2 + 3)
print(list(comb_wr))

# accumulate (for prefix sums and multiplications)
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(list(acc))  # output is [1,3,6,10]

import operator
acc = accumulate(a, func = operator.mul)
print(list(acc))  # output is [1,2,6,24]
acc = accumulate(a, key = lambda x:x*2)
print(list(acc))