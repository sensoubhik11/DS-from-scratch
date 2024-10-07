#not to be run
#python syntax notes

def name(args):
  <body>
  
def fun(x, a=1.0, b=0.0):
  return a*x + b

#if we want mutable container to be empty as default value
#then assign them to None
def fun(x, l=None):   
  <body>
  
def minimum(*args):
  """Takes any number of arguments"""
  m=args[0];
  for x in args[1:]:
    if x < m:
      m=x
  return m
#Args and Kwargs(Kwargs are for variable names as keys and their values in a dict  
def blender(*args,**kwargs):
  print("Arg List :",args)
  print("Kwarg Dictionary :",kwargs)
  
#returning multiple values result in returning tuples

#to view and set recursion limit
import sys
sys.getrecursionlimit() #returns current limit
sys.setrecursionlimit(9856) #sets recursion limit to 9856

#lambdas are anonymous fucntions(since they don't have names)
#They are flexible expressions which can be used inside functions, literal list or dictionary

lambda x: x**2

lambda x,y : x**2 + y**2

(lambda x,y:x**2+y**2)(3,4)

#just because its anonymous doesn't mean we can't give it a name
fun = lamda x,y:x**2+y**2
fun(x,y)  # will return x**2 + y**2


nums_list = [12,43,23,98]
sorted(nums_list, key = lambda x:x%13)  # will sort list based on modulo 13


#generators have yield statements which stop the execution midway
def countdown():
  yield 3
  yield 2
  yield 1
  yield 'Blast Off!'
  
# A decorator is a function that takes a function as its only parameter and returns a function.