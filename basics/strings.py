#not to be run
#python syntax notes

s="I am Soubhik Sen"	#immutable
print("Hey, "+ s)		#concatenation
print(s,end="")			#instead of default newline char, the output ends with a different char
str(456)				#returns a string of int/float
len(s)					#returns length of string
ord(s)					#returns ascii value of character
s.index("Sen")			#returns the index at the first occurence of "Sen"
'''Rule:
Immutable objects in python always return a new object or return the reference, the old/original object(not talking abt the variable) is not changed
Mutable objects after calling suitable functions change the original one and don't return object rather return None'''
s*n                     #returns s repeated n number of times
bin(n)                  #returns string of binary representation of int n
l=list(s)				#returns list of char(not words) contained in s 
x in s 					#returns True if substring x is present in s
s[a:b]					#returns a slice of string from index a to b-1
s[:b]					#same as s[0:b]
s[a:]					#same as s[a:len(s)]
s[-1]					#returns last char of s, same as s[len(s)-1]
s.upper()				#returns string in UPPERCASE
s.lower()				#returns string in LOWERCASE
s.strip()				#returns string with no extra delimiters at beginning and end of string
s.lstrip()
s.rstrip()
s.endswith("Sen")		#returns True if string ends with the substring parameter
s.count("a")			#returns number of characters matching with parameter in string
s.split()				#returns list of substrings seperated by delimiters in string
s.isalpha()				#returns True if string is composed of only letters
s.isnumeric()			#returns True if string is composed of only numbers
"987".isnumeric() #as said earlier, the variable names are nothing but labels used for convenience. We can use the objects directly
s.replace("oldOccurrence","newOccurence")	#returns new modified string. The old string remains same since strings are immutable

s1="Hey"
s2=s1					#the string is not copied to s2, instead s2 and s1 now refer to the same object
						#In python, variable names are not containers that hold values, they are simply stickers or labels which represent the object
						#Here the object is "Hey" of class str and s1, s2 simply refer to that same object

"".join(["Hey","I","am","Soubhik","Sen"])	#returns string joined together by delimiter, opposite of split()
",".join(["Hey","I","am","Soubhik","Sen"])

mp=100.9898
sp=200.89
name="Soubhik"
age=20
print("My name is {} and I am {} years old".format(name,age))	#acts printf("%d, %f",var1,var2), use the format method instead of string concatenation
print("My name is {} and I am {} years old".format(name,age),end="")  #same as above but with no newline
print("The Market Price is ${:>3.2f} and The selling price is ${:>7d}".format(mp,sp))
print("{:.2s}".format(name))					#output is 'So'
first="apples"
second="Oranges"
third="Papaya"
print("{0},{2},{1}".format(first,second,third))	#According to numbers inside curly brackets, the parameters will be printed
print(f'My name is {name} and I am {age} years old')	#f strings were like format

for x in s:				#iterable
	print(x)

for x in range(0,len(s),1):
	print(x)

for x in reversed(range(len(s))):	#[n-1, n-2, n-3,..., 2, 1]


#string to list
l=list(s)   #list of individual characters
l=s.split() #list of words based on delimiter

#list to string
s=" ".join(l) #string made of elements of list joined together with delimiter

#string to int
a=int(s)

#int to string
s=str(a)

