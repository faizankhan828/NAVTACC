'''
Part A: Topic Understanding & Direct Usage
'''
#A1, Given s = "Machine Learning" , write expressions that:

from matplotlib.pyplot import flag


s= "Machine Learning"
#(a) Return the first character.
print( s[0] ) 
#(b) Return the last character.
print( s[-1] ) 
#(c) Return the substring "Machine".
print(s[0:7])
#(d) Return the string reveresed
print( s[::-1]) 
    
'''
Part 2
'''
#Given s = " Python for AI " , write one expression or method call for each:
s = " Python for AI "
#(a) Remove the leading and trailing whitespace.
print(s.strip())
#(b)Replace "AI" with "ML"
print(s.replace("AI","ML"))
#(c) Split into a list of words (by spaces).
print(s.split())
#(d)Check whether the string ends with "AI " (no strip).
print(s.endswith("AI "))


'''
Part A3
'''
#Given words = ["AI", "ML", "DL"] , write one expression that produces the single
s="AI, ML, DL" \
"".join(["AI", "ML", "DL"])

'''
Part A4
'''
#What does "hello".find("l") return? What does "hello".find("z") return? Write
#he two expressions and print their results.

print("hello".find("l"))
print("hello".find("z"))

'''
Part A5
'''
#Given name = "Alice" and score = 95 , write an f-string that prints exactly: Alice scored 95
name = "Alice"
score = 95

print(f"{name} scored {score} in the exam.")

'''
Lists
'''
'''
Part A6
'''
#Create a list.Write expressions that:
L = [10, 20, 30, 40, 50] 
#(a) Return the first element.
print(L[0]) 
#(b) Return the last element.
print(L[-1])
#(c)Return a new list containing the middle three elements (20, 30, 40).
print(L[1:4])
#(d) Return the list reversed using slicing (new list).
print(L[::-1])

'''
Part A7
'''     
L=[10, 20, 30, 40, 50]
#(a)Change the element at index 2 to 99 (in place). What is L after?
L[2] = 99
print(L)
#(b) Append 60 to L .
print(L.append(60))
print(L)
#(c)Remove the element 20 from L
print(L.remove(20))
#(d)Return the index of 40 in L .
print(L.index(40))


'''
A8. What is the difference between L.append([1, 2]) and L.extend([1, 2]) ? Write two
short examples: start with L = [0] , do each operation, then print L and its length.
'''
L = [0]
L.append([1, 2])    
print(L)
print(len(L))

L = [0]
L.extend([1, 2])    
print(L)
print(len(L))



##################################################################
'''
Part A: Topic Understanding & Direct Usage
'''
#A1. Create a tuple. Write expressions that:
t = (10, 20, 30, 40, 50)
#(a) Return the first element.
print(t[0])
#(b) Return the last element.
print(t[-1])
#(c) Return a new tuple containing the middle three elements (20, 30, 40).
print(t[1:4])
#(d) Return the tuple reversed using slicing (new tuple).
print(t[::-1])

'''
Part A2
'''
# write one expression that produces a new
#Then write one expression that produces a tuple with t repeated 2 times.
t =(1,2,3)
u =(4,5)
print(t *2)

'''
Sets
'''
'''
A7
'''
#Create 2 sets. Write an exprssion that:
a = {1, 2, 3}  
b = {3, 4, 5}
#(a) Returns the union of a and b.
print(a.union(b))
#(b) Returns the intersection of a and b.
print(a.intersection(b))
#(c) Elements in a but not in b .
print(a.difference(b))
#(d) Elements in exactly one of a and b (symmetric difference).
print(a.symmetric_difference(b))
'''
Part A8
'''
#Create a set. Write expressions that:
s = {10, 20, 30}
#(a)Add 40 to s in place. What is s after?
print(s.add(40))
print(s)
#(b)Remove 20 from s in place. What is s after?
print(s.remove(20))
print(s)
#(c)Try to remove 99 from s using the method that does not raise if the element is missing.
#Write the method name and show the call.

print(s.discard(99))
print(s)


'''
Part B Scanario and Implementation
'''
'''
Scenario: You have a single string: text = "Python is used for AI and ML" .
Task: Print each word on a separate line (each word on its own line).
Implementation: Use string methods to split and then loop (or print) so each word
appears on one line. Do not use any external libraries.
'''
s = "Python is used for AI and ML"
words = s.split()
for word in words:  
    print(word)

'''
Part A: If/Else as a Concept
'''

'''
A1. Truthiness
'''
"""
(a) Write an if statement that runs a block only when the value is "falsy". Use the value
0 and print something like "falsy" inside the block.
(b) Write an if statement that runs a block only when the value is "truthy". Use the value
1 and print something like "truthy" .
(c) For each of these, write one line that prints True or False : "Is empty string ''
truthy?" "Is non-empty string ' ' truthy?" "Is empty list [] truthy?" Use an if or a
simple expression like bool(...) and print the result.
"""
#(a)
if 0:  
    print("falsy")  
#(b)
if 1:  
    print("truthy")
#(c)
print("Is empty string '' truthy?", bool(''))
print("Is non-empty string ' ' truthy?", bool(' '))
print("Is empty list [] truthy?", bool([]))


'''
A2  Simple If Elif Else
'''
x = -5
if x <0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")

'''
A3 Chained Comparison
'''    
age = 25
if 18 <= age <60:
    print("In Range")
elif 18< age >60:
    print("Out of Range")

'''
A4 Logical Operators (and, or, not)  
'''
#a 
a = True
b = False  
if a and b:
    print("Both a and b are True")
else:
    print("At least one is True")

#b
n = 4
if n % 2 == 0:
    print("Even")
else:       
    print("Odd")

#c
import flag
if flag == False:
    print("Flag is False")
else:   
    print("Flag is True")

'''
A5 Nested Conditionals:
'''
x = 3
y =-2
if x > 0:
    if y > 0:
        print("Both x and y are positive")
    else:
        print("x is positive but y is not")
        if x <=0:
            print("x is not positive")

'''
Part A6 Ternary (conditional expression) 
'''
n = 7
parity = "even" if n % 2 == 0 else "odd"
print(parity)

score = 85
result = "pass" if score >= 60 else "fail"
print(result)

'''
Part A7 no else/multiple elif
'''
code = 2
if code == 1:
    print("Code is 1")
if code == 2:
    print("Code is 2")  
if code == 3:
    print("Code is 3") 

'''
A8 Guard 
'''
value = None
if value is None:
    print("Value is None")
value = 42 
print("Value is not None:", value)
