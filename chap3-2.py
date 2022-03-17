# Chapter3 Ex.2)
# Write a program that flips a coin 100 times 
# and then tells you the number of heads and tails.

import random

cthead = 0
cttail = 0

#for loop 1 to 100 times
for i in range(0, 100):
    coin = random.randint(0,1)
    if (coin == 1):
        cthead += 1
    if (coin == 0):
        cttail += 1

print("Heads: ",cthead)
print("Tails: ", cttail)

input("\n\nPress the enter key to exit.")
    