#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

#THIS FOR CODE DOES WORK ITS A LIL IFFY BUT THATS COOL

for i in range(3):
    guess = input("Guess a number between 1 and 20 (inclusive):\n ")
    if not guess.isnumeric():
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess) # converts a string to an integer
    if guess == aRandomNumber:
        print("Congrats")
        break
    if guess > aRandomNumber:
        print("Guess lower!")
    else:
        print("Guess higher!")
    if  i >= 3:
        print("game over")
        break
    
# EVERYTHING BELOW WORKS TOO THIS IS THE WHILE ONE WITH A NEW VARIABLE

#tries = 0 
#while tries < 3:
    #guess = input("Guess a number between 1 and 20 (inclusive):\n ")
    #if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        #print("That's not a positive whole number, try again!")
    #else:
        #guess = int(guess) # converts a string to an integer
    #if guess > aRandomNumber:
        #print("Guess lower!")

    #else:
        #print("Guess higher!")


    #if guess == aRandomNumber:
        #print("Congrants")
        #break

    #if tries == 3:
        #print("ok thats enough")
        #break
    #tries += 1

