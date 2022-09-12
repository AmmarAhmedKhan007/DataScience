# 1_Python Modules:
A module is a Python file containing Python statements and definitions.
## Example:
A file evenodd.py is a module, and we call it ‘evenodd’. We put similar code together in one module.
```python
def check():
         a=int(input('Enter a number'))
         if a%2==0: print("Even")
         else: print("Odd")
```
# Import Module in Python:
A module simply contains Python code.We can import it simply like a package.
```python
import math
from math import pi
math.pi
```
```python
import random
random.randint(1, 3)
```
# 2_Python Packages:
A package is like a directory holding subpackages and modules.\
A package must hold the file __init__.py. 
# Import Modules from Packages in Python:
A Python package may contain several modules. To import one of these into your program, you must use the dot operator(.)
```python
import Game.Sound.load
```
```python
import Game.Level.start
```
```python
import random.randint(1, 3)
```