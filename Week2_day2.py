'''
FIle Handling in Python
'''

#r is used for read(deafult). File must exist
#w is used to write, creates file  or overwrites existing content
#a is ued for append overwrite all content and existing content will be removed
# x is used for exclusive creation, creates file but if file already exists it will throw an error

#Every data pick and store in memeory(RAM)

#content point ot the RAM where data is stored is called pointer


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#import os 
# Get current working directory
#print(os.getcwd())
#path = os.getcwd() #Absoulte Path

# Read entire file
#with open(path + '/Kings.txt', 'r') as f:
#	content = f.read()
#	print(content)
	
# Read line by line
#with open(path + '/Kings.txt', 'r') as f:
#	for line in f:
#		print(line.strip())
		
# Read all lines into a list
#with open(path + '/Kings.txt', 'r') as f:
#	lines = f.readlines()
#print(lines)

# Read Number of lines how many lines are there in the file
#with open(path + '/Kings.txt', 'r') as f:
#    lines = f.readlines()
#    print(f"Number of lines: {len(lines)}") 

# Write a File


# Overwrite the content of the file
#with open(path + '/output.txt', 'w') as f:   
    #f.write("Line 5.\n")
    #f.write("Line 4.\n")

# Append to the file
#with open(path + '/output.txt', 'a') as f:   
 #   f.write("Line 3.\n")
  #  f.write("Line 2.\n")
   # f.write("Line 1.\n")    


# Write multiple lines at once
#lines = ['apple\n', 'banana\n', 'cherry\n']
#with open(path + '/output.txt', 'w') as f:
 #   f.writelines(lines)


#There are two types of libraries in python:
#Standard Library: Built-in libraries that come with Python, such as os, sys, math, datetime, etc.
#we can import using keyword import os 

#Third-Party Libraries: Libraries created by the community that can be installed using package managers like pip, such as NumPy, Pandas, Requests, etc.
#from datetime import datetime #importing only datetime class from datetime module
#whenever you import you will import the function or class
#like this from math import sqrt, pi #importing only sqrt and pi from math module


'''
Working with file Paths
'''
#import os
# Get current working directory 
#print(os.getcwd())
#path = os.path.join(os.getcwd(), 'data.txt')

#Check if file exists
#if os.path.exists('data.txt'):
 #print('File found!')

#Using pathlib library (modern approach)
#from pathlib import Path
#p = Path('data.txt')
#text = p.read_text() # Read
#p.write_text('Hello Faizan!') # Write


'''
Exception Handling
'''
#try:
 # number = int(input("Enter a number: "))
 # result = 10 / number
 # print(result)
# print("Error: Cannot divide by zero.")


'''
Raising Exceptions  We raise exceptions when
we want to signal that an error has occurred in our code.
This can be done using the raise  
'''

def set_age(age):
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age >150:
        raise ValueError("Age cannot be greater than 150.")
    return age
try:
    age = set_age(-5)
except ValueError as e:
    print(f"Error: {e}")