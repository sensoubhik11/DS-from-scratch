#not to be run
#python syntax notes

#sets are unordered containers. Sets are not sequence.
#like mathematical sets, they do not allow duplicate elements
#can contain various data types

#represent by curly brackets {}
st=set()    #empty set
d={}        #empty dictionary
#both set and dict use curly brackets but their empty syntax are different
#list to set
st=set(l)

#string to set
st=set(string)   #returns set of char in string (to want s as a complete element, turn it into a list first)

st=s | t #union (s and t are sets)
st=s & t #intersection
st=s - t # s & t'
st=s ^ t #symmetric difference
st=s <= t #subset
st=s < t   #proper subset

#Sets contain unique elements, i.e., the elements are hashable.
#only hashable elements can be placed in sets
#something which can be mapped to a unique integer is called a hashable element. Hashable elements are immutable.
#Thus lists not allowed in sets, though tuples are allowed if the elements in tuple are hashable

#But sets themselves are mutable, hence we can't have sets inside sets

#forzensets are immutable sets and hence can contain frozensets inside it.

#set comprehension
st={x+2 for x in range(0,10) if <condition>}

"""
docstrings can be viewed at runtime via help().
"""
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Removing an element
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}