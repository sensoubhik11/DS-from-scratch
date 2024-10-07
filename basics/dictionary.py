#not to be run
#python syntax notes

#duplicate keys not allowed
#keys must be hashable
file_counts={"jpg":10, "csv":5, "pdf":13}			#Dictionary {key:value}, mutable
													#String "" | List [] | Tuple () | Dictionary{}
file_counts["jpg"]									#returns value(reference, in fact mostly python uses as reference) corresponding to key
file_counts["jpg"]=11								#can modify
file_counts["html"]=22							#inserting a new pair
file_counts.items()									#returns list of tuples containing (key,value) class type is <dict_items>
file_counts.keys()									#returns list of keys <class 'dict_items'>
file_counts.values()								#returns list of values <class 'dict_items'>
file_counts.clear()									#removes all items from dictionary
file_counts.get()									  #returns value corresponding to key, if key not present, then returns default key(not its value)
file_counts.update(dict2)						#joins two dictionaries(updates the existing entries with dict2)
"csv" in file_counts								#returns True
del file_counts["jpg"]							#deleted key-value pair from dictionary

for extension in file_counts:						#iterates over keys
	print(extension)

for extension in file_counts.keys():    #iterates over keys
  
for extension in file_counts.values():  #iterates over values
  
for extension in file_counts:
	print("{} files with .{} extension".format(file_counts[extension], extension))		#iterates over keys, we can print values through keys

for extension,amt in file_counts.items():
	print("There are {} files with .{} extension".format(amt,extension))


#list of tuples to dict
d = dict([(1,'a'),(2,'b')])

#dictionary comprehension
d={key:value for key,value in file_counts.items() if <condition> }

coord={'x':1,'y':5,'z':10,'theta':2,'phi':7,'r':1};

polar_keys=['theta','phi','r']
polar_coord={key:value for key,value in coord.items() if key in polar_keys}
