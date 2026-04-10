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


#SCENARIO 01 · BEGINNER
#💊 Create a secure Patient record system using encapsulation

'''
Scenario:
A hospital stores sensitive patient data — medical ID, age, and diagnosis. Only doctors (inside the
class) should update the diagnosis. Age should never be negative. The patient's name is public, but
ID and diagnosis are private.
Tasks:
16. Create a Patient class. Make __medical_id and __diagnosis private.
17. Use @property for age with a setter that rejects negative values.
18. Write update_diagnosis(new_diag) — only updates if new_diag is a non-empty string.
19. Write get_report() — returns a formatted string showing patient info.
'''
class Patient:
    def __init__(self, name, medical_id, age):
        self.name = name
        self.__medical_id = medical_id
        self.__diagnosis = None
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative.")
        else:
            self._age = value
    def update_diagnosis(self, new_diag):
        if isinstance(new_diag, str) and new_diag.strip():
            self.__diagnosis = new_diag
            print("Diagnosis updated.")
        else:
            print("Invalid diagnosis. Must be a non-empty string.")
    def get_report(self):
        return f"Patient: {self.name}, Age: {self.age}, Diagnosis: {self.__diagnosis or 'N/A'}"
    
#SCENARIO 02 · INTERMEDIATE
#🔐 Build a secure ATM PIN validation system    

'''
Scenario:
An ATM stores a user's PIN privately. The user gets 3 attempts to enter the correct PIN. After 3 failed
attempts, the card is locked. The PIN itself must never be directly accessible — only verification is
allowed.
Tasks:
20. Create an ATM class with private __pin and __attempts (max 3).
21. Write verify_pin(entered) — returns True/False, tracks failed attempts.
22. After 3 failures, set a private __locked flag; block all further attempts.
23. Write is_locked() as a property to expose lock status safely.
24. Ensure __pin is never directly accessible from outside the class.
'''

class ATM:
    def __init__(self, pin):
        self.__pin = pin
        self.__attempts = 0
        self.__locked = False
    def verify_pin(self, entered):
        if self.__locked:
            print("Card is locked. No further attempts allowed.")
            return False
        if entered == self.__pin:
            print("PIN verified successfully.")
            self.__attempts = 0  # reset attempts after successful verification
            return True
        else:
            self.__attempts += 1
            print(f"Incorrect PIN. Attempt {self.__attempts}/3.")
            if self.__attempts >= 3:
                self.__locked = True
                print("Card has been locked due to too many failed attempts.")
            return False
    @property
    def is_locked(self):
        return self.__locked

#SCENARIO 03 · CHALLENGE
'''

🛒 Design an e-commerce Product inventory system
Scenario:
An online store needs a Product class where price and stock are protected from invalid values. Price
must be positive. Stock can't go below 0. A discount can be applied but must be between 0–50%.
Tasks:
25. Create Product with private __price, __stock, __discount.
26. Use @property + setters for price (must be > 0) and discount (0–50%).
27. Add effective_price property — returns price after discount.
28. Write purchase(qty) — reduces stock if qty available, else raises error.
29. Write restock(qty) to add inventory.    
'''
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock
        self.__discount = 0
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Price must be positive.")
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, value):
        if 0 <= value <= 50:
            self.__discount = value
        else:
            print("Discount must be between 0 and 50%.")
    @property
    def effective_price(self):
        return self.__price * (1 - self.__discount / 100)
    def purchase(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            print(f"Purchased {qty} of {self.name}. Stock left: {self.__stock}")
        else:
            print("Not enough stock available.")
    def restock(self, qty):
        self.__stock += qty
        print(f"Restocked {qty} of {self.name}. Total stock: {self.__stock}")


#SCENARIO 01 · SINGLE INHERITANCE
#🏫 Model a School staff system: Teacher extends Person

'''
Scenario:
A school has people with a name and age. Teachers are people who also have a subject and salary.
Teachers should introduce themselves and teach a class.
Tasks:
30. Create Person class with name and age. Add greet() method.
31. Create Teacher(Person) adding subject and salary. Use super().
32. Override greet() in Teacher to include subject info.
33. Add teach() method that prints a teaching message.
34. Verify with isinstance() and issubclass().
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    def greet(self):
        print(f"Hello, I am {self.name}, a {self.subject} teacher.")
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
teacher1 = Teacher("Ms. Smith", 40, "Math", 50000)
teacher1.greet()
teacher1.teach()
print(isinstance(teacher1, Teacher))  # True
print(isinstance(teacher1, Person))   # True
print(issubclass(Teacher, Person))    # True


#SCENARIO 02 · HIERARCHICAL INHERITANCE
#🐾 Build an Animal shelter system with multiple animal types

'''
Scenario:
An animal shelter manages Dogs, Cats, and Birds. All share common data (name, age) and behavior
(feed, speak). But each makes a unique sound and has a unique trick to show adopters.
Tasks:
35. Create base Animal class with shared attributes and feed() and speak() methods.
36. Create Dog(Animal), Cat(Animal), Bird(Animal) — each overriding speak().
37. Add a unique method to each: fetch(), purr(), sing().
38. Create a shelter list and loop through it calling speak() — observe polymorphism.
'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def feed(self):
        print(f"{self.name} has been fed.")
    def speak(self):
        pass  # To be overridden by subclasses
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")
    def fetch(self):
        print(f"{self.name} is fetching the ball.")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")
    def purr(self):
        print(f"{self.name} is purring.")
class Bird(Animal):
    def speak(self):
        print(f"{self.name} says: Tweet!")
    def sing(self):
        print(f"{self.name} is singing a song.")

#SCENARIO 03 · MULTILEVEL INHERITANCE
#🏦 Banking system: Account → BankAccount → SavingsAccount

'''
Scenario:
A bank has a base Account (id, holder). BankAccount extends with deposit/withdraw.
SavingsAccount extends further — it earns monthly interest and has a minimum balance
requirement.
Tasks:
39. Create Account(id, holder) with get_info().
40. Create BankAccount(Account) adding balance, deposit(), withdraw().
41. Create SavingsAccount(BankAccount) adding interest_rate and min_balance.
42. Add apply_interest() — adds interest % to balance.
43. Override withdraw() to enforce minimum balance rule
'''
class Account:
    def __init__(self, id, holder):
        self.id = id
        self.holder = holder
    def get_info(self):
        return f"Account ID: {self.id}, Holder: {self.holder}"
class BankAccount(Account):
    def __init__(self, id, holder, balance=0):
        super().__init__(id, holder)
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
class SavingsAccount(BankAccount):
    def __init__(self, id, holder, balance=0, interest_rate=0.01, min_balance=100):
        super().__init__(id, holder, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"Cannot withdraw {amount}. Minimum balance of {self.min_balance} must be maintained.")
        else:
            super().withdraw(amount)


#SCENARIO 04 · MULTIPLE INHERITANCE · CHALLENGE
#⚡ Build a Smartphone that is both a Phone and a Camera

'''
Scenario:
A smartphone is both a Phone (can call, text) and a Camera (can take photos, record). Model this
using multiple inheritance and explore how MRO resolves method conflicts.
Tasks:
44. Create Phone with call(number), text(msg), and power_on().
45. Create Camera with take_photo(), record(), and power_on().
46. Create Smartphone(Phone, Camera) inheriting from both.
47. Call Smartphone.power_on() — which parent's version runs? Print Smartphone.__mro__.
48. Override power_on() in Smartphone to call both parents' versions.
'''
class Phone:
    def power_on(self):
        print("Phone is powering on...")
    def call(self, number):
        print(f"Calling {number}...")
    def text(self, msg):
        print(f"Sending text: {msg}")
class Camera:
    def power_on(self):
        print("Camera is powering on...")
    def take_photo(self):
        print("Taking a photo...")
    def record(self):
        print("Recording video...")
class Smartphone(Phone, Camera):
    def power_on(self):
        super().power_on()  # Calls Phone's power_on due to MRO
        Camera.power_on(self)  # Explicitly call Camera's power_on

phone1 = Smartphone()
phone1.power_on()