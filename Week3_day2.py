'''
Single Inheritance:
1. In single inheritance, a class can inherit from only one parent class.

2. Single level Inheritance arrow is from child class to parent class. 

3. When both exist on the same level parent or child
then it is called single inheritance.
'''

'''
Multilevel Inheritance:
1. In multilevel inheritance, a class can inherit from
another class which in turn inherits from another

2. Multilevel inheritance arrow is from child class to parent class 
and then from parent class to grandparent class.

3. When parent and child are on the level wise like nodes then it is called multilevel inheritance.
'''

'''
Multiple Inheritance & MRO
MRO(Method Resolution Order) is the order in which Python 
looks for a method in a hierarchy of classes.
MRO Rules:
1. The method is searched in the current class first.
2. If not found, it is searched in the parent classes from left to right.
3. If there are multiple parent classes, the method is searched
   in the order they are defined in the class declaration.
4. If the method is not found in any class, an AttributeError is raised.
'''

'''
Relationships between classes:
1. Association: It is a relationship between two classes where one class uses the other class.
It is a weak relationship. If one class is destroyed, the other class can still exist.
2. Aggregation: It is a relationship between two classes where one class contains the other class
It is partial dependency. If the parent class is destroyed, the child class can still exist.

3. Composition: It is a relationship between two classes where one class is a part of the other class.
It is completely dependent on the other class. If the parent class is destroyed,
 the child class will also be destroyed.
'''

'''
Revised OOP Concepts:
PSL cricket entities:
1. Franchise
2. Player
3. Management   
4. Venues
5. Matches
6. Tournaments

'''


# Task 1 Making  a PSL project using OOP concepts and realtionship between classes.
# PSL Class
class PSL:
    def __init__(self, name):
        self.name = name
        self.franchises = []
        self.management = []
        self.venues = []
    def add_franchise(self, franchise):
        self.franchises.append(franchise)
    def add_management(self, management):
        self.management.append(management)
    def add_venue(self, venue):
        self.venues.append(venue)
# Franchise Class
class Franchise:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
# Player Class
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Management Class
class Management:
    def __init__(self, name):
        self.name = name
        self.franchises = []

    def add_franchise(self, franchise):
        self.franchises.append(franchise)
# Venue Class
class Venue:
    def __init__(self, name, location):
        self.name = name
        self.location = location

# Create PSL Object
psl = PSL("Pakistan Super League")
# Create Franchises
franchise1 = Franchise("Karachi Kings")
franchise2 = Franchise("Lahore Qalandars")
franchise3 = Franchise("Islamabad United")

# Add franchises to PSL
psl.add_franchise(franchise1)
psl.add_franchise(franchise2)
psl.add_franchise(franchise3)
# Create Players
player1 = Player("Babar Azam", 28)
player2 = Player("Shaheen Afridi", 25)
player3 = Player("Shadab Khan", 27)
# Add players to franchises
franchise1.add_player(player1)
franchise2.add_player(player2)
franchise3.add_player(player3)
# Create Management
management = Management("PSL Management")
management.add_franchise(franchise1)
management.add_franchise(franchise2)
management.add_franchise(franchise3)

# Add management to PSL
psl.add_management(management)

# Create Venues
venue1 = Venue("National Stadium", "Karachi")
venue2 = Venue("Gaddafi Stadium", "Lahore")
venue3 = Venue("Rawalpindi Cricket Stadium", "Rawalpindi")

# Add venues to PSL
psl.add_venue(venue1)
psl.add_venue(venue2)
psl.add_venue(venue3)

# Display 
print("PSL Name:", psl.name)

print("\nFranchises:")
for franchise in psl.franchises:
    print("-", franchise.name)
    for player in franchise.players:
        print("  Player:", player.name, "| Age:", player.age)

print("\nManagement:")
for m in psl.management:
    print("-", m.name)

print("\nVenues:")
for v in psl.venues:
    print("-", v.name, "(", v.location, ")")