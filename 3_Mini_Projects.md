# **1_Quiz Game**
```python
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for?")
if answer.lower() == "Central Processing Unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?")
if answer.lower() == "Graphics Processing Unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
```

# **2_Number Guessing Game**
```python
import random

top_of_range = input("Enter number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please enter number larger than 0 next time.')
        quit()
else:
    print('Please enter number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
```

# **3_Rock_Paper_Scissor Game**
```python
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
```

# **4_Snake Water Gun Game**
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
