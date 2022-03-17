# Chapter3 Ex.1)
# Write a program that simulates a fortune cookie. 
# The program should display one of five unique fortunes, 
# at random, each time it’s run.

import random

#declaration of the variables
cookie1 = "You have good fortune."
cookie2 = "The life is beautiful."
cookie3 = "Love is everything."
cookie4 = "Time is money."
cookie5 = "A faithful friend is a strong defense."


#define the list
listCookies = [cookie1, cookie2, cookie3, cookie4, cookie5]

#define a variable to hold the random number
myRandomGeneratedIndex = random.randint(0, 4)

#print the result:
print(listCookies[myRandomGeneratedIndex])

input("\n\nPress the enter key to exit.")