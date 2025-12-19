# from Dog import *
#
# dog = Dog()
# print(f"dog.legs = {dog.legs}")
# print(f"dog.ears = {dog.ears}")
# print(f"dog.type = {dog.type}")
# print(f"dog.age = {dog.age}")
# print(f"dog.color = {dog.color}")

print("==========BATTLE GAME===============")

from Enemy import *
zombie = Enemy('Zombie', 10, 1)
big_zombie = Enemy('Big Zombie', 100, 10)
# zombie.type_of_enemy = "Zombie"
#print(f"{zombie.type_of_enemy} has {zombie.health_points} health points and can do attack of {zombie.attack_damage} ")
print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage} ")
print(f"big_zombie.attack_damage = {big_zombie.attack_damage}")


"""
What is Abstraction?
- Abstraction - This means to hide the implementation and only show necessary details to the user
Let's say we add new code to allow the enemy to talk:
class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1
    
    def talk(self):
        print('I am an enemy')
"""

zombie.talk()
zombie.walk_forward()
zombie.attack()

"""
Why use Abstraction?
- This allows users to not have to understand what the functionality is behind the scenes
- You can create simple and reusable code
- Allows for a better use of the DRY principle (Don't repeat yourself)
- Enables Python objects to become more scalable
"""

""" 
What are constructors?
#######################
- Constructors - are used to create and initialise an object of a class with or without starting values
e.g.
from Enemy import *
enemy = Enemy() # this is a constructor call

Constructor types
#######################
1. Default / Empty constructors
2. No argument constructors
3. Parameter constructors
"""

"""
What is encapsulation?
- Encapsulation - Bundling of data
Enemy currently has 3 (public) attributes - which can be changed. Which we don't want. If a Zombie enemy is created, 
no-one should be able to change it to an Orc enemy.

So we need to change these public attributes to private attributes.
"""

"""
Why use Encapsulation?
- Helps keep related fields and methods together
- Makes our code cleaner and easier to read
- Provides more flexibility to our code
- Provides more reusability of our code.
"""

"""
What is inheritance?
- Inheritance - Process of acquiring properties from one class to other classes
- Creates a hierarchy between classes

(parent class)
class Animal:
    weight: int
    color: str
    age: int
    animal_type: str
    
    def eat(self):
        print('Animal eating')
    
    def sleep(self):
        print('Animal sleeping')

(child class)
class Dog(Animal):
    ** inherits all Animal attributes **
    
    # along with these new attributes specific to Dogs
    can_shed: bool
    domestic_name: str
    
    ** inherits all Animal methods **
    
    def talk(self):
        print('Bark!')
    
    ## overrides Animal.eat() method
    
    def eat(self):
        print('Chews on bone!')
        
What is method overriding?
- As we can see from the example, both Doc() and Animal() have the eat() functionality
- Method overriding is when a child class has its own method already present in the parent class.
- When the child class does not have the same method, it will default to the parent method.

class Bird(Animal):
    birdType: str
    
    def talk(self):
        print('Chirp!')
    
    def fly(self):
        print('Bird begins to soar!')

"""

"""
self vs super

- self is used to refer to the current object that is created or is being instantiated, 
while super is used to refer to the parent class

- self is used when there is a need to differentiate between the instance 
variables & parameters with the same name, while super is used to call 
the parent class methods and/or constructors

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
class Student(Person):
    def __init__(self, name, age, degree):
        super().__init__(name=name, age=age)
        self.degree = degree 
        
- Student has an extra property: degree
- Student uses super to call the Person constructor which assigns the properties name and age
- Student uses self to reference the degree property which is different from the degree parameter/argument coming in
"""
print("-----------ZOMBIE CLASS----------------")
from Zombie import *
zombie = Zombie(10, 1)
print(zombie.get_type_of_enemy())
print(zombie.talk())
print(zombie.spread_disease())

from Ogre import *
ogre = Ogre(20, 3)

print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}.")
print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage}.")
zombie.talk()
ogre.talk()

"""
What is Polymorphism?

- Polymorphism means to have many forms
- Polymorphism means changing an object at run time

e.g
zoo: Animal = []

dog = Animal()
dog2 = Dog()
zoo.append(dog) # this will work as dog is an Animal
zoo.append(cat) # this will work as dog2 is a Dog which is an Animal
"""

print("-----------BATTLE------------------")
def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
battle(zombie)
battle(ogre)


print("-----------BATTLE FINAL------------------")
def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and  e2.health_points > 0:
        print("---------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage
    print("---------------")

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
battle(zombie, ogre)

"""
What is a composition?
- A way to create objects made up of other objects
- In composition, a class contains one or more objects of another class as instance variables
- Provide layered functionality to the object
- Known as a HAS-A relationship between objects (different from an interface which is a IS-A relationship)
e.g a vehicle must have an engine, but an engine does not need to have a vehicle

class Engine:
    def __init__(self, engineType):
        self.engineType = engineType
    
    def startEngine(self):
        print("Engine is running")
    
    def stopEngine(self):
        print("Engine is off")

class Vehicle:
    def __init__(self, type, forSale, engine):
        self.type = type
        self.forSale = forSale
        self.engine = engine
    
engine = Engine("V6")
vehicle = Vehicle("Car", True, engine)
vehicle.engine.startEngine()
"""

print("-----------HERO BATTLE------------------")
from Hero import *
from Weapon import *

def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print("-------------")
        enemy.special_attack()
        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print("-------------")

    if hero.health_points > 0:
        print(f"Hero wins!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins!")

zombie = Zombie(10, 1)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)