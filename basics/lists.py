#not to be run
#python syntax notes

l=["apples","oranges","peaches"]	#mutable
len(l)								#returns number of elements in the list
l[-1]=["Guava"]						#can be mutated at specific index
l.append("Papaya")					#appends at the end of list, use it instead of l+=element
l.insert(index, "Cheeko")			#if index >=len(l), then it acts as an append
l.remove("apples")					#removes element
l.pop(index)						#removes by index and returns the removed element
l.sort(key=attribute)				#sorts list
l.sort(reverse=True)				#reverse sorts a list
sorted(l,key=attribute)				#returns sorted list(the original one remains unchanged)
l.reverse()							#reverses list
l.clear()							#empties list
l.copy()							#returns a duplicate copy of list
l.extend(other_list)			#joins two lists
l.index(element)					#returns index of element
"Papaya" in l 						#returns True if the element is in the list 
l[a:b]										#returns a list from index a to b-1. The original one is unchanged	#returns slice of list
 
list(string)						#returns list of characters
",".join(["Hey","I","am","Soubhik","Sen"]) #returns string
for x in l:							#iterable
	print(x)

#Its better not to iterate list via index, instead use 'in' or enumerate()
for i,x in enumerate(l):
	pass

for x in range(1,11):
	l.append(x*7)					#Gives a list of multiples of 7
									#When we have to create lists based on sequences we can use List Comprehensions

l=[x*7 for x in range(1,11)]		#returns a list of multiples of 7, its a List Comprehension

l=[x for x in range(0,101) if x%3==0]	#returns a list

l=[s.replace(".hpp",".h") for s in list1]

