#not to be run
#python syntax notes

#A tuple is like an immutable list, ex - (1,2,3,4)
#Every position has a significance

#lists are generally for homogenous data while tuples are for heterogeanous data with semantic meaning
#tuples are immutable but if a list is an element of tuple, then it can be modified
#tuples are immutable but can contain mutable elements
c=(23)  # not a tuple but a number
c=(23,) # a tuple
c=()    #length 0 tuple


def returnTime(seconds):
	hours=seconds//3600
	minutes = (seconds-hours*60)//60
	seconds=seconds-hours*60-minutes*60
	return hours, minutes,seconds			#Such functions return a tuple

result=returnTime(56897)					#result is a tuple
x,y,z = result								#unpacking tuple

l=['Hey','I','love','you']
obj1=enumerate(l)							#will return enumerate(iterable) object containing bunch of tuples in the form (0,'Hey') (1,'I'), etc.
x,y,z=obj1                    #unpacking tuples which are in an enumerate object
print(x,y,z)                  #output (0, 'Hey') (1, 'I') (2, 'love')
obj2=enumerate(l,2)							#counter will start from 2 instead of 0   (2,'Hey') (3,'I'), etc.

print(list(obj1))							#output [(0, 'Hey'), (1, 'I'), (2, 'love'), (3, 'you')]
print(obj1)									#output <enumerate object at 0x7fd051712280>

for index, element in obj1:
	print("{}, {}".format(index,element))


def info(listOfTuples):
	new_list=[]
	for name,email in listOfTuples:
		new_list.append("{} <{}>".format(name,email))
	return new_list

peoples=[("soubhik","soubhik@gmail.com"),("salim","ss2121@jgec.ac.in"),("Megha","megha@cse.jgec.ac.in")]

print(info(peoples))