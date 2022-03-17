'''
chapter3 Ex.4)
Write the pseudocode for a program where the player and 
the computer trade places in the number guessing game. 
That is, the player picks a random number between 1 and 100 
that the computer has to guess. 
Before you start, think about how you guess. If all goes well,
try coding the game.
'''
#In chapter 3, we studied "Guess My Number" which the player guesses the number that the computer picked.
#Now we create the game that the computer guesses the number the player picked.

#a random number from 1:100, store in a variable randNum
#generate a random number that is the computer guessed number guessNum
#ask player to guess the number
#player enters the guessed number guessNum
#message will be Enter the number between 1 to 100 and press Enter. Computer will not see this number. She will try to guess.
#computer has only one chance to guess.
#player enters a number.

#if computer guessed the number correctly,
#output message "Computer guessed the right random number randNum"
#if not,
#ouput message "Computer guessed number randNum but the number to guess was guessNum"

    
import random

guessNum = ""
randNum = 0 

guessNum = int(input("Enter the number between 1 and 100 and press Enter. Computer will not see this number. She will try to guess. "))

while guessNum != 0:
    
    randNum = random.randint(1,101)

    #guessNum = int(input("Guess the number: "))
    
    if randNum == guessNum :
            print("Computer guessed right! The right number is ", randNum)
            
    else:
            print("Computer guessed wrong. Computer Guessed: ",randNum, ". The right number was: ", guessNum, "\n")
            break
        
          
print("Thank you for playing. GoodBye")
