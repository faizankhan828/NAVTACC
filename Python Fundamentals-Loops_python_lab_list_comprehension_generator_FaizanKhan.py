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


#Q5. Create a generator expression from 1 to 5 and print values using a loop.

generator = (i for i in range(1, 6))
for num in generator:
    print(num)

#Q6 Create cubes from 1–5 using both list comprehension and generator.
cubes_list = [i**3 for i in range(1, 6)]
print(cubes_list)
cubes_generator = (i**3 for i in range(1, 6))
for cube in cubes_generator:
    print(cube)

 #Q7. Create a generator from 10–15 and convert it into a list.
generator = (i for i in range(10, 16))
list_from_generator = list(generator)
print(list_from_generator)


'''
Part B – Scenarios & Implementation

'''

#8. Filter marks greater than 60 from [45,78,90,34,67,88,50].
marks = [45,78,90,34,67,88,50]
filtered_marks = [mark for mark in marks if mark > 60]
print(filtered_marks)

#Q9. Remove negative numbers from [-5,3,-1,9,-7,6].
numbers = [-5,3,-1,9,-7,6]
positive_numbers = [n for n in numbers if n >= 0]
print(positive_numbers)

#Q10. Create a generator that produces word lengths from ['apple','banana','kiwi','grape'].
words = ['apple','banana','kiwi','grape']
word_lengths = (len(word) for word in words)
for length in word_lengths:
    print(length)

#Q11. Convert Celsius [0,10,20,30,40] into Fahrenheit using list comprehension.
celsius = [0,10,20,30,40]
fahrenheit = [((temp * 9/5) + 32) for temp in celsius]
print(fahrenheit)


#Q12  Create a generator from 1–1000 and print first 10 values.
generator = (i for i in range(1, 1001))
for _ in range(10):
    print(next(generator))

#Bonus: Create [(1,1),(2,4),(3,9),(4,16),(5,25)] using list comprehension.
squares = [(i, i**2) for i in range(1, 6)]
print(squares)
