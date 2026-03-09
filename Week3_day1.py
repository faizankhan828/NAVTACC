'''
Objects creation in oop in python
'''
#Class is a combination of attributes and functions. It is a blueprint for creating objects.
#When class instance we make real world then it make object.
#In python we have two types of memory management:
#1. Stack Memory: It is used for storing references to objects and function calls. 
# It is managed automatically by the Python interpreter and is limited in size.
#2. Heap Memory: It is used for storing actual objects and data. 
# It is also managed automatically by the Python interpreter and can grow as needed.

'''
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")   

human1 = Human("Faizan", 30)
human2 = Human("Khan", 25)
print(human1.hello())  # Output: Alice (.is used to access the attributes of the object)
print(human2.hello())   # Output: 25
'''

#self is holding the itslef id or reference  of the object instance.

'''
OOP
'''
'''
1. Encapsulation: It is the process of hiding the internal
# details of an object and only exposing a public interface.
'''
'''
2. Inheritance: It is the process of creating a new class
that is a modified version of an existing class.
'''

'''
3. Polymorphism: It is the ability of an object to take on
many forms. It allows objects of different classes to be 
treated as objects of a common superclass.
'''

'''
4. Abstraction: It is the process of hiding the internal
 details of an object and only exposing a public interface.
'''

'''
5. Realtionship 
1. Association: It is a relationship between two classes where one class uses the other class.
2. Aggregation: It is a relationship between two classes where one class contains the other class
3. Composition: It is a relationship between two classes where one class is a part of the other class.

'''


'''
class Car: # Class Definition (Blueprint)
 def __init__(self, brand, speed): # Constructor
  self.brand = brand # Attribute
  self.speed = speed
 def drive(self): # Method
  print(f"{self.brand} is going {self.speed} km/h")

# Creating Objects (Instances)
car1 = Car("Toyota", 120) # Object 1
car2 = Car("BMW", 200) # Object 2
car1.drive() # → Toyota is going 120 km/h
car2.drive() # → BMW is going 200 km/h
print(car1.brand) # → Toyota
'''


# Scanario 1
#Design a BankAccount class for a simple banking system
'''
1. Create a BankAccount class with owner, account_no, and balance attributes.
2. Write a deposit(amount) method that adds to balance.
3. Write a withdraw(amount) method that deducts from balance (no overdraft allowed).
4. Write a show_balance() method to display current balance.
5. Create two account objects and perform sample transactions.
'''

class BankAccount:
    def __init__(self, owner, account_no, balance):
        self.owner = owner
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        self.balance +=amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def show_balance(self):
        print(f"Current balance: {self.balance}")            

acc = BankAccount("Faizan", "123456789", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_balance()



#Scanario 2
#Model a Library book catalog with a Book class

'''
6. Create a Book class with title, author, isbn, and is_available (default True) attributes.
7. Write borrow() — marks book unavailable; print message if already borrowed.
8. Write return_book() — marks book available again.
9. Override __str__ to return a readable book summary.
10. Create 3 book objects and simulate borrowing and returning.
'''
class Book:
    def __init__(self, title, author, isbn):
        self.title =title
        self.author= author
        self.isbn = isbn
        self.is_available = True
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")
    def return_book(self):
        self.is_available = True
        print(f"You have returned '{self.title}' by {self.author}.")
    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {'Available' if self.is_available else 'Unavailable'}"
book1 = Book("The Great Gatsby", "F. Scott", "978-0743273565")
book2 = Book("To Kill a Mockingbird", "Harper ", "978-0061120084")
book3 = Book("1984", "George ", "978-0451524935")
print(book2)
book2.borrow()  
book2.borrow()           


#Scanario 3
#Build a Player class for a simple RPG game
'''
11. Create a Player class with name, level=1, health=100, xp=0.
12. Write gain_xp(points) — adds XP; if XP >= 100, call level_up().
13. Write level_up() — increments level, resets XP, restores health, prints message.
'''

class Player:
    def __init__(self,name):
        self.name =name
        self.level =1
        self.health =100
        self.xp =0
    def gain_xp(self, points):
        self.xp +=points
        if self.xp >=100:
            self.level_up()
    def level_up(self):
        self.level +=1
        self.xp =0
        self.health =100
        print(f"{self.name} leveled up to level {self.level}!")
player1 = Player("Faizan")   
player1.gain_xp(50)  
player1.gain_xp(60) 


