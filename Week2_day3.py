'''
List Comprehension
'''
'''
dict = {"ALi":1, "Ahmed":2, "Sara":3}
for k,v in dict.items():
    print(f"Key: {k}, Value: {v}")
Part A – Topic Understanding & Direct Usage
'''

#Q1 Write a list comprehension that creates a list of numbers from 1 to 10.
from unittest import result


numbers = [i for i in range(1, 11)]
print(numbers)

#Q2 Create a list of squares for numbers from 1 to 8 using list comprehension.
squares = [i**2 for i in range(1, 9)]
print(squares)



#Q3. Generate a list of even numbers from 1 to 20 using list comprehension.    
numbers = [i for i in range(1, 21) if i % 2 == 0]
print(numbers)

#Q4. Convert ['python','java','ai','data'] into uppercase using list comprehension.
s = ['python','java','ai','data']
uppercase = [lang.upper() for lang in s]
print(uppercase)

'''
Defining and Calling FUnctions
'''
#def(keyword) variable name ()://  Define a function

#There are 2 types of functions:
#Anonymous Functions without name(Lambda Functions) and Named Functions
#void type functions 

def add (a, b):
    return a + b #This function is called callee

x = 2
y = 5
x = add(x, y) #This function is called caller


'''
Parameters and Arguments
'''
#Positive argumemts = passed order
#Keyword arguments = passed with name
#Default arguments = have a fallback value
#args = accepts any number of positional arguments and stores them in a tuple
#kwargs = accepts any number of keyword arguments and stores them in a dictionary


x =2
y =7 
x =add(x,y)

def add (a, b =6): #default argument if no value occurs then take 6 
    return a+b #Return 9 beacuse on b y already gives 7 value so 2+7 = 9


def add (a, *args): #args is a tuple that can take any number of arguments
     result = a
     if len(args) > 0:
         for x in args:
             result += x
     return result   

'''
Variable Scope
'''
#Local Scope: Variables defined inside a function are local to that function and cannot be accessed outside of it.
x ='global'

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x) 
    inner()
    print(x)
outer()
print(x)    