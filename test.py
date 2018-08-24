# This is a comment
# Why Hello, World?
# Its the first thing the OG's typed too

#This types out the words inside the quotes
#print("Hello, World")

#answer = input("Two bros.. where/what are they doing? \n")
#print(answer + " 5 feet apart bc theyre not gay")
#print("hello darkness my old friends")
#print:(answer, "is your favorite genre")

#while True:
#print("hi")

#for i in range(5):
    #print(i + 3)

#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer
