#LIST CHALLANGE make a 

#imports the ability to get a random number (we will learn more about this later!)             #ASK HOW TO INCLUDE THE RANDOM NUMBER INTO THE LIST. YOU WANT TO PRINT OUT THE RANDOM NUMBER OF 
#  from random import *

#Create the list of words you want to choose from.

#Generates a random integer.
#  aRandomIndex = randint(0, len(the_menu)-1)

breakfast = ["eggs", "bacon", "waffles"]

lunch = ["pizza", "sandwich", "soup"]

dinner = ["steak", "lasagna"]

the_menu = [breakfast + lunch + dinner]
#print(aRandomIndex(the_menu))

#the_menu(aRandomIndex)

#adds multiple lists together
#the_menu.extend(breakfast, lunch, dinner)

#for num in (the_menu):
#print(aRandomIndex(the_menu))

#for i in range((len(the_menu)-1)):
    #print(the_menu[i])

ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
print(sum(ages)//len(ages))





