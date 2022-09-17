# **Name:** Ammar Ahmed
# **Email:** <ammar07ahmed08@gmail.com>
___
___
# **Week 1:**
# Task 1: **What is Data Science**
# 1_Need for Data Science: 
The need of data science is almost in all fields in world. Data Science is mainly needed for:
- **Better decision making:**  Making right Decision whether A or B, Right or Left?
- **Predictive Analysis:**  What will happen next?
- **Pattern Discovery:**  Is there any hidden information in data?
# 2_What is Data Science: 
Data Science is basically a decision making with data. Data Science is about:
- Asking the right questions and exploring the data.
- Modeling the data using various algorithms.
- Finally communicating and visualizing the results.
# 3_ Data Science vs Business Intelligence:  
- Business intelligence use Structured data such as Data warehouse while Data Science use Unstructured data such as web logs, customers feedback etc.
- Business intelligence use Analytical method while Data Science use Scientific method.
- Statistics and Visualization skills are necessary for Business Intelligence while for Data Science Statistics, Visualization and Machine Learning skill is necessary.
- Business intelligence focus on Past and Present data while Data Science focus on Present data and Future Predictions.
# 4_The Prerequisites for learning Data Science: 
The three essential traits of Data Scientist are:\
**Curiosity:**  When you ask a question then you will better understand the problem.\
**Common Sense:**   To identify new ways to detect and solve the problem.\
**Communication Skills:**  A Data Scientist need to communicate their findings to business teams to act upon insights.
## Prerequisites for Data Science are: 
- Machine Learning
-	Mathematical Modelling
-	Statistics
-	Programming
-	Databases
## Tools and Skills for Data Science:
1.	**Data Analysis:**\
**Skills:** R, Python, Statistics\
**Tools:** SAS, Rstudio, Jupyter, Matlab, Excel
2.	**Data Warehousing:**\
**Skills:** ELT, SQL, Hadoop, Apachi Spark\
**Tools:** Informatica, AwS Redshift
3.	**Machine Learning:**\
**Skills:** Algebra, Statistics, ML Algorithms\
**Tools:** Spark Mlib, Azure Ml Studio
4.	**Data Visualization:**\
**Skills:** R, Python libraries\
**Tools:** Jupyter, tableau, Congos, RAW
# 5_What does Data Science Do: 
The data Scientist find the problem in **Real world** and then gather **Raw data** required to solve the problem and then **Process and Analyze** the data and get the **Meaningful data** and communicate with **Useful Insights.**
# 6_ Data Science lifecycle with example:
**Concept Study:** Understanding the problem, Asking the right question.\
**Data Prepration:** Also known as Data Munging, for any valuable insights to pop up.\
**Model Building:** Use various analytical tools and techniques build the right model.\
**Communicate Results:** Key findings are identified and conveyed the stakeholder.\
**Operationalize:** Final report, Code and technical documents are delivered to their team.
# 7_Demand of Data Scientists: 
The Data Science in anary of great demand. The demand for Data Scientists is currently huge and supply is very low.
## Industries with High demand of Data Scientists Are:
-	Gaming
-	Healthcare
-	Finance 
-	Marketing
-	Technology
___
___
# Task 2: **The Basics of probability for Data Science**
# **Probability:** 
**Probability** provides information about the likelihood that something will happen. **OR**\
Probability is the chances of occurrence.\
**Probability = No of ways an event occur / No of possible outcomes.**
## **Examples:** 
-	Tossing of Coin
-	Rolling a dise
-	Weather forecast
-	Sports and gaming strategies
-	Determining blood group
-	Analyzing political strategies
# **Mutually Exclusive Events:** 
In probability theory, two events are said to be mutually exclusive if they cannot occur at the same time or simultaneously.\
In other words, mutually exclusive events are called disjoint events.\
If two events are considered disjoint events, then the probability of both events occurring at the same time will be zero. 
## **Example:**
If **A** and **B** are the two events, then the probability of disjoint of event **A** and **B** is written by: \
**Mutually Exclusive Event = P (A and B) = 0**

If A and B are said to be mutually exclusive events then the probability of an event A occurring or the probability of event B occurring that is **P (a ∪ b)** formula is given by **P(A) + P(B), i.e.,**
-	P (A Or B) = P(A) + P(B)
-	P (A ∪ B) = P(A) + P(B)
# **Not Mutually Exclusive Events:**
The two events occur at the same time, they are called not mutually exclusive events.
## **Example:**
If we draw a card from an ordinary deck of 52 playing cards, it can be both a king and a diamond. Therefore, kings and diamonds are not mutually exclusive.
## **Multiplicative Role:** 
In multiplicative role two types of events are occur:
## **1. Independent Event**
**Example:** Tossing a coin.  
**Formula:** P (A and B) =P (A) * P (B)
## **2.	Dependent Event**
**Example:** Taking a card from deck.\
**Formula:** P (A and B) =P (A) * P (B/A)
___
___
# Task 3: **Combinatorics**
# Combinatorics:
**Combinatorics** are use to calculate the "total number of possible outcomes".\
There are three principles of Combinatorics:
1.	Addition
2.	Multiplication
3.	Inclusion-Exclusion
## **Example:**
Suppose that there are only four different types of cookies (A, B, C, D). You have funds for only two boxes.\
Answer: AB, AC, AD, BC, BD, CD.
___
___
# Task 4: **Python Basics**
# 1_Hello World:
Python is a very simple language, and has a very straightforward syntax.

It encourages programmers to program without prepared code. The simplest directive in Python is the "print" directive - it simply prints out a line.
## Example:
```python
Print ("Hello World")
```
```python
print("This line will be printed")
```
# 2_Variables and Types:
Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.
```python
a='ammar'
b=3.2
c=302
d="true"     #for boolean use true or false
print (a)
print (b)
print (c)
print (d)
```
# 3_List:
Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.

Here is an example of how to build a list.
```python
a = [1 ,2 ,3 ,4]       
print (a)
```
WE can create a list with items of different types:
```python
c = ["ammar" , "true" , 45 ,0.07]
print (c)
```
List Slicing:
```python
friends = ["ammar" , "khan" ,"abdullah" ,"hassan"]
print (friends[0:3])
print (type(friends))
```
## Example Question:
PROGRAM THAT ACCEPT MARKS OF SIX STUDENTS AND DISPLAY THEM IN SORTED MANNER?
```python
F1 = int(input ("enter marks of student 1: "))
F2 = int(input ("enter marks of student 2: "))
F3 = int(input ("enter marks of student 3: "))
F4 = int(input ("enter marks of student 4: "))
F5 = int(input ("enter marks of student 5: "))
F6 = int(input ("enter marks of student 6: "))

MyMarksList = [F1, F2, F3, F4, F5, F6 ]
MyMarksList.sort()
print (MyMarksList)
```
# List Methods:

**Insert()**	Adds an element at the specified position.
```python
l4 = [ 1,3,4,7,77,34,2,0]
l4.insert(2 ,99)         #this will insert 99 in index 2
print (l4) 
```
**Pop()**	Removes the element at the specified position.
```python
l5 = [ 1,3,4,7,77,34,2,0]
l5.pop(2)                # will delete element at index 2
print (l5)
```

**Remove()**	Removes the first item with the specified value.
```python
l6 = [ 1,3,4,7,77,34,2,0]
l6.remove(77)           #will remove 77 from the list
print(l6)
```

**Reverse()**	Reverses the order of the list.
```python
l2 = [ 1,3,4,7,77,34,2,0]
l2.reverse()
print (l2)
```

**Sort()**	Sorts the list.
```python
l1 = [ 1,3,4,7,77,34,2,0]
l1.sort()
print (l1)
```
**Index()**	Returns the index of the first element with the specified value.
```python
l6 = [ 1,2,3,4,7,77,34,2,0]
l6.index(77)           
print(l6)
```

**Append()**	Adds an element at the end of the list.
```python
l3 = [ 1,3,4,7,77,34,2,0]
l3.append(100)            #add 100 at the end of list
print (l3)
```

**Clear()**	Removes all the elements from the list.
```python
l6 = [ 1,3,4,7,77,34,2,0]
l6.clear()           
print(l6)
```
**Copy()**	Returns a copy of the list.
```python
l6 = [ 1,2,3,4,7,77,34,2,0]
l6.copy()           
print(l6)
```
**Count()**	Returns the number of elements with the specified value.
```python
l6 = [ 1,2,3,4,7,77,34,2,0]
l6.count(2)           
print(l6)
```
---
---
# Task 5:
# 4_Strings:
Strings can be written in Single, Double and triple coats.
```python
print ('My name is Ammar')
```
```python
print ("Data Scientist")
```
```python
Data ='''The best way to learn data science is to do data science.
“Data are just summaries of thousands of stories.”
“Big data is at the foundation of all the megatrends that are happening today, from social to mobile to cloud to gaming.'''
```
## String Methods:
```python
print (len(Data))                  # len is used to find length of string
```
```python
print (story.endswith("gaming"))       # endswith is used to find last character
```
```python
print (story.count("a"))             # count is used count number of occourance of charaters
```
```python
print (story.capitalize())         # capitalize charcter
```
```python
print (story.find("data"))          # find charsctes
```
# 5_Input Function:
```python
a = input ("enter your name")
b = input ("enter your age")
print (a)
print (b)
```
# 6_Operators:
```python
print(5==5)
print(5!=5)
print(4<=9)
print(5>=2)
print(5>66)
print(4<44)
```
# Types:
## 1- Arithmetic Operators:
```python
print("the value of 3+5 is",a+b)
print("the value of 3-5 is",3-5)
print("the value of 3*5 is",3*5)
print("the value of 3/5 is",3/5)
```
## 2-Assignment Operators:
```python
a=25
a+=5
print (a)
```
## 3-Comparison Operators:
```python
a=(25>=4)
print (a)
```
```python
b=(25==22)
print (b)
```
## 4-Logical Operators:
```python
bool1 = True
bool2 = False
print("the value of bool1 and bool2 is", (bool1 and bool2))
print("the value of bool1 or bool2 is", (bool1 or bool2))
print("the value of  not bool2 is", ( not bool2))
```
# 7_Type Casting:
```python
a = "5555"
# a = int(a)
print (int(a))
```
Calculate square of number entred by user?
```python
a = input ("enter number")
a = int (a)
print (a*a)
```
Find average of 2 numbers given by user
```python
a = input ("enter first number:")
b = input ("enter second number:")
a = int(a)
b = int(b)
avg = (a+b)/2
print ("the avg of a and b is",avg)
```
# 8_Tuples:
```python
t = (2 ,5 ,3 ,10 ,20 ,6)   
print (t[1])      # print elements of tuple
print (t)

# WE cannot update the value of tuple
t[0] = 34
```
# Tuple Methods:
## 1_Count:
```python
t = (1, 2, 5, 6, 1, 5, 2, 1,)
print (t.count(1))    #will count number of times 1 occours in t
```
## 2_Index:
```python
t2 = (1, 2, 5, 6, 1, 5, 2, 1,)
print (t2.index(5))       # find the index of element in t2
```
# 9_Dictionary:
```python
myDict = {
    "Fast": "in a quick manner",
    "Ammar": "is khan",
    "Marks": [1 ,4 ,6 ,8]
}
print (myDict["Fast"])
print (myDict["Ammar"])
print (myDict["Marks"])
```
# Dictionary Methods:
```python
print (myDict.keys())        #print the keys of dictionary
print (myDict.values())     # print values of keys
print (myDict.items())       #kind of list --> print (keys , values)
```
## Update Dictionary:
```python
updatedict = {
    "you": "are awesome"
}
print (myDict.update(updatedict))
print (myDict)
```
## Get dictionary:
```python
print (myDict.get("Ammar"))
```
# 10_Sets:
Set is a collection of non repetitive elements.
```python
a = {1, 3, 5, 7 , 9} 
print (type(a))            
print (a)
```
## Empty Set:
```python
b = set()
print (type(b))
```
# Set Methods:
## 1_Add:
```python
a = {1, 3, 5, 7 , 9} 
a.add(10)
print (a)
```
## 2_Len:
```python
a = {1, 3, 5, 7 , 9} 
print (len(a))
```
## 3_Remove:
```python
a = {1, 3, 5, 7 , 9} 
print (a.remove(5))
```
## 4_Clear:
```python
a = {1, 3, 5, 7 , 9} 
print (a.clear())
```
## 5_UNION and INTERSECTION
```python
a = {1, 3, 5, 7 , 9} 
a.union({1,5})
a.intersection({1,5})
print (a)
```
# 11_IF - Else Statement:
```python
if(cond 1):                         # if cond 1 is true 
    print ("yes")
elif (cond 2):                      # if cond 2 is true 
    print ("no")
else:                               # otherwise
    print ("maybe")
```
## Example 1:
```python
a = int(input ("enter your age:"))
if (a>=18):
    print ("YES")
else:
    print ("NO")
```
## Project: Create Game using Python if else statement:
# Snake(S) Water (W) Gun(G) Game:
```python
import random

def gamewin (comp, you):
    if (comp == you):
        return None
    elif (comp == 'S'):
        if (you == 'W'):
            return False
        elif (you == 'G'):
            return True
    elif (comp == 'W'):
        if (you == 'S'):
            return True
        elif (you == 'G'):
            return False
    elif (comp == 'G'):
        if (you == 'W'):
            return True
        elif (you == 'S'):
            return False

print ("Comp turn: Snake(S) Water(W) or Gun(G)?")
randno = random.randint(1, 3)
if randno == 1:
    comp = 'S'
elif randno == 2:
    comp = 'G'
elif randno == 3:
    comp = 'W'

you = input ("Your turn: Snake(S) Water(W) or Gun(G)?")
a = gamewin (comp, you)

print (f"Comp choose: {comp}")
print (f"You choose: {you}") 

if a == None:
    print ("THE GAME IS TIE")
elif a:
    print ("YOU WIN")
else:
    print ("YOU LOSE")
```
# 12_Is and In Function:
## 1_ Is:
```python
a = "ammar"
if (a is "ammar"):
    print ("yes")
else:
    print ("no")
```
## 2_ In:
```python
a = [2, 3 ,6]
print (5 in a)
```
# 13_While Loop:
```python
i = 0
while i<10:
    print ("yes" + str(i))
    i = i + 1
print ("DONE")
```
## Question:
Progran to print a content of list using while loop
```python
fruits = ["apple", "banana", "mango", "melon"]
i = 0
while i<len(fruits):
    print (fruits[i])
    i = i + 1
```
# 14_For Loop:
```python
fruits = ["apple", "banana", "mango", "melon"]
i = 0
while i<len(fruits):
    print (fruits[i])
    i = i + 1
```
## Range Function:
```python
for i in range (10):              
    print (i) 
```
## For Loop with Else:
```python
for i in range ( 10 ):            
    print (i)
else:
    print ("BSS") 
```
# 15_Break, Continue, Pass Statement:
# 1_Break:
```python
for i in range (10):            
    print (i)
    if i == 8:
        break
```
# 2_Continue:
```python
for i in range (10):           
    if i == 5:                  #its skip 5 
        continue
    print (i)
```
# 3_Pass:
```python
i = 5
if i>0:
    pass
while i>10:
    pass
print ("yeh boy")
```
# 16_Function:
```python
def func1 ():
    print ("func1")
```
```python
def ammar():
    a="hello ammar","how are you"
    print (a)
ammar()
```
# Sum:
```python
marks = [55, 88, 90, 70, 80]
percentage = (sum(marks)/500)*100                   # SUM is a builtin function
print (percentage)
```
## Function with if,elif,else statement:
```python
def Ammar():
    name = input("Enter your Name")
    MARKS = int(input("ENTER YOUR MARKS: "))

    if (MARKS>90):
        print (name,"=  A+")

    elif (MARKS>80):
        print (name,"=  A")

    elif (MARKS>70):
        print (name,"=  B")

    elif (MARKS>60):
        print (name,"=  C")

    elif (MARKS>50):
        print (name,"=  D")

    else:
        print (name,"=  FAIL")
Ammar()
```
# 17_Read & Write files:
# 1_Read:
```python
f = open ('sample.txt', 'r')        # 'r' use for read data
data = f.read()
print (data)
f.close()
```
# 2_Write:
```python
f = open ('sample.txt', 'r')                        # 'w' use for write data
f.write("Please write this to the file")            # 'a' use for appending
f.close()
```
# 3_With Statement:
```python
with open ('sample.txt', 'r'):
f.read()
```
---
---
---
---