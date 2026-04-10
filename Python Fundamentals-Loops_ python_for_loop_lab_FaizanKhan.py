#numbers =[1,3,5,7]
#target = 4
#for n in numbers:
   # if n == target:
  #      print("Found")
 #       break   
#else:    print("Not Found")


#fruits = ["apple", "banana", "cherry"]
#without enumerate 
#i =0    
#for fruit in fruits:
 #   print(f"Index: {i}, Fruit: {fruit}")
  #  i += 1

#with enumerate (given with index value  it is a function that returns both the index and the value of the item in the list)
#for i, fruit in enumerate(fruits):
 #   print(f"Index: {i}, Fruit: {fruit}")


#Basic Nested Loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for x in matrix:
    for y in x:
        print(y, end=' ')
    print()  

# WIth enumerate in nested loops
for i, row in enumerate(matrix):    
    for j, num  in enumerate(row):
        print(f"Element at ({i}, {j}): {num}")  

# With enumerate in nested loops in reverse order
for i, row in enumerate(reversed(matrix)):  
    for j, num  in enumerate(reversed(row)):
        print(f"Element at ({i}, {j}): {num}")


'''
Section 1 Warm Up
'''
#Q1 Count to 10 using for loop
for i in range(1, 11):
    print(i)

#Q2 Print Even Numbers using for loop and if statement
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#Q3 Use a for loop to calculate the sum of all numbers from 1 to 100.
total_sum = 0
for i in range(1, 101):
    total_sum += i
print(total_sum)

#Q4 Print numbers from 10 down to 1 using range().
for i in range(10, 0, -1):
    print(i)    


''''
Section 2 List Iteration
'''    
#Q5. Greet Everyone Given the list below, print a greeting for each person:
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
for name in names:
    print(f"Hello, {name}!")

#Q6. Without using the built-in max() function, find and print the largest number in this list:
numbers = [34,12,89,45,67,23,91,8]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num   
print(f"The largest number is: {largest}")

#Q7 Count Vowels Loop through the string below and count the number of vowels
sentence = "Python programming is fun and poweful"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count += 1    
print(f"Number of vowels: {vowel_count}")

#Q8. Multiplication Table Ask the user to enter a number, print its multiplication table.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Q9 Reverse a list Using a for loop (no reverse() or slicing), reverse the following list and print it:
original_list = [10, 20, 30, 40, 50]
reversed_list = []    
for i in range(len(original_list)-1, -1, -1):
     reversed_list.append(original_list[i])  
print(reversed_list)

'''
Section 3 Nested Loops 
'''
#Q10 Print a following traingle pattern.
for i in range(5):   
    for j in range(i+1):
        print("*", end=' ')
    print()

#Q11. Number Grid
#Print a 5×5 grid using nested loops where each cell contains the product of its row and column index
for i in range(5):
    for j in range(5):
        print(i * j, end=' ')
    print()
'''
Q12. FizzBuzz Classic
Loop from 1 to 50:
• Print Fizz if the number is divisible by 3
• Print Buzz if the number is divisible by 5
• Print FizzBuzz if divisible by both
• Otherwise, print the number
'''    
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

'''
Section 4 (2D List Questions)
'''
#Q13 2D List — Sum of All Elements
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum = 0
for row in matrix:
    for num in row:
        total_sum += num    
print(f"Total sum of all elements: {total_sum}")

#Q14. 2D List — Row-Wise Maximum
grid = [

[3, 17, 5, 9],
[22, 8, 14, 6],
[11, 4, 19, 2],
[7, 13, 1, 25]

]
for i, row in enumerate(grid):   
    max_value = row[0]  
    for num in row:
        if num > max_value:
            max_value = num
    print(f"Maximum in row {i}: {max_value}")



'''
■ SECTION 5 — Challenge Round
'''

#Q15. Prime Numbers

#Print all prime numbers between 1 and 50 using nested for loops

for num in range(2, 51):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        