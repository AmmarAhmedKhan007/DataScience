# **Task 7:**
# Object Oriented Programming **(Oop)** in Python
**Object-oriented programming (OOP)** is a computer programming model that organizes software design around data, or objects, rather than functions and logic.  
An object can be defined as a data field that has unique attributes and behavior.
# Classes:
Classes are user-defined data types that act as the blueprint for individual objects, attributes and methods.
```python
class ClassName:
```
# Objects:
Object is one of instances of the class. which can perform the functionalities which are defined in the class.
```python
Obj = ClassName (arguments)
```
# Example:
```python
class Person:         
    name = "Ammar"      
    age = 20  
    def display (self):      
        print(self.age,self.name)         
per = Person()      
per.display() 
```  

# **Self and __init__ method:**
# Self :
**Self** represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

# Init :
__Init__ is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
# Example:
```python
class Car(object):

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")
```

# **Object-oriented programming** is based on the following **principles:**

# Encapsulation:
This principle states that all important information is contained inside an object and only select information is exposed.  
The implementation and state of each object are privately held inside a defined class. Other objects do not have access to this class or the authority to make changes. They are only able to call a list of public functions or methods. 
```python
class ABC:
   def __init__(self, name, project)
      self.name = name
      self.__project = project

a = edpresso('Ammar', 3)
print("Name:",a.name)
print("Project:",a._ABC__project)
```
# Abstraction:
Objects only reveal internal mechanisms that are relevant for the use of other objects, hiding any unnecessary implementation code. The derived class can have its functionality extended. This concept can help developers more easily make additional changes or additions over time.
```python
from abc import ABC  
  
class Polygon(ABC):   
    def sides(self):   
      pass  

class Triangle(Polygon):   
    def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):      
    def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):   
    def sides(self):   
      print("Hexagon has 6 sides") 

class Square(Polygon):   
   def sides(self):   
      print("I have 4 sides")   
  
T = Triangle()   
T.sides()   
S = Square()   
S.sides()     
P = Pentagon()   
P.sides()    
K = Hexagon()   
K.sides()   
```
# Inheritance:
In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class. A child class can also provide its specific implementation to the functions of the parent class.
```python
class Library:  
    def write(self):  
        print("Write Books")    
class Person(Library):  
    def Read(self):  
        print("Read Books")  
P = Person()  
P.Read()  
P.Write()  
```
# Polymorphism: 
Objects are designed to share behaviors and they can take on more than one form. The program will determine which meaning or usage is necessary for each execution of that object from a parent class, reducing the need to duplicate code. A child class is then created, which extends the functionality of the parent class. Polymorphism allows different types of objects to pass through the same interface.
```python
class Pakistan():
     def capital(self):
       print("Islamabad")
 
     def language(self):
       print("Urdu, Punjabi and English")
 
class UnitedStates():
     def capital(self):
       print("Washington")
 
     def language(self):
       print("English")
 
Pak = Pakistan()
USA = UnitedStates()
for country in (Pak, USA):
country.capital()
country.language()
```