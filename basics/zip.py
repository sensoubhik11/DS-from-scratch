# The zip function transforms
# multiple iterables into a single iterable of tuples of corresponding function

list1 = ['a', 'b', 'c']
list2 = [2, 4, 6, 8, 9]

list3 = [pair for pair in zip(list1, list2)]
print(list3)

#unzipping
letters, numbers = zip(*list3)
print(letters)
print(numbers)

# The asterisk (*) performs argument unpacking, which uses the elements of pairs as
# individual arguments to zip. It ends up the same as if you’d called:
letters, numbers = zip(('a', 2), ('b', 4), ('c', 6))
print(letters)
print(numbers)
