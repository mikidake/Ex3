# Chapter3 Ex.3)
# Modification of 'Guess My Number'

# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
# The player can try to guess up to three times

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("You have three chances to try!\n")

# set the initial values
the_number = random.randint(1, 100)
tries = 1
maxTries = 3

# guessing loop
while tries <= maxTries:
    guess = int(input("Take a guess: "))
    if guess == the_number:
        print("\nYou guessed it! The number was", the_number)
        if tries == 1:
            print("And it only took you", tries, "try!\n")
            break
        else:
            print("And it only took you", tries, "tries!\n")
            break
    elif guess > the_number:
        print("Guess Lower..")
    else:
        print("Guess Higher..")
    tries += 1
    if tries > maxTries:
        print("\nSorry you ran out of tries! The random number was ", the_number)
        
input("\n\nPress the enter key to exit.")