from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
numberOfGuesses = 1
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer

for i in range (2):
	if (int(guess) < aRandomNumber):
  		print ("Guess higher")
  		guess = input("Guess a number between 1 and 20 (inclusive): ")
	elif (int(guess) > aRandomNumber):
  		print ("Guess lower")
  		guess = input("Guess a number between 1 and 20 (inclusive): ")
	elif (int(guess) == aRandomNumber):
  		print("You are correct!")
  		break
print("The correct answer is:")
print (aRandomNumber)
