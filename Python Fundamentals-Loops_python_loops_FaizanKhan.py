'''
Python Lab: While and For Loops
'''
'''
Section A While Loops
'''

#Task1 Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:  
    print(i)  
    i += 1  
#Task2 Print odd numbers from 1 to 20 using a while loop.
i = 1
while i <= 20:  
    print(i)  
    i += 2
#Task 3: Print the multiplication table of a number entered by the user using a while loop.
num = int(input("Enter a number: "))
i = 1         
while i <= 10:  
    print(f"{num} x {i} = {num * i}")  
    i += 1
#Task 4: Keep asking the user for numbers until they enter 0. Print the total sum.
flag = True
while flag:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        flag = False
    else:
        total_sum += num

#Task 5: Reverse a number using a while loop.
num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(f"Reversed number: {reversed_num}")


"""
Section B For Loops
""" 
#Task 6 Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):  
    print(i)
#Task 7 Print even numbers from 1 to 50 using a for loop.
for i in range(2, 51, 2):  
    print(i)
#Task 8 Print the sequence of numbers from  1 to 10
for i in range (1, 11):
    print(i)
#Task9 Print all charcters of a string using a for loop.
s ="Faizan!"
for char in s:
    print(char)
#Task10 Find the sum of numbers from 1 to 100 using a for loop.
total_sum = 0
for i in range (1, 101):
    total_sum += i
print(f"Total sum: {total_sum}")


'''
Section C Challenge Questions
'''
#Task 11: Print a star pattern using a for loop.
rows = 5
for i in range(1, rows + 1):   
    print("* " * i)

#Task 12: Count how many digits are in a number using a while loop.
num = int(input("Enter a number: "))
count = 0
while num > 0:  
    num //= 10
    count += 1
print(f"Number of digits: {count}")

#Task 13: Find factorial of a number using a for loop.

num = int(input("Enter a number: "))
factorial = 1   
for i in range(1, num + 1):  
    factorial *= i  
print(f"Factorial of {num} is {factorial}")

#Task 14: Create a number guessing loop using while loop.
import random
number_to_guess = random.randint(1, 100)
while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break

# Task 15 Print Fibonacci series up to 10 terms.
n_terms = 10
a, b = 0, 1
for _ in range(n_terms):
    print(a, end=' ')
    a, b = b, a + b

