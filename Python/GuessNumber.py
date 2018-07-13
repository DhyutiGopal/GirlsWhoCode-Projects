#imports the ability to get a random number (we will learn more about this later!)
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


i=0
while i<=3:
	i+=1
	if (int(guess) < aRandomNumber):
		print ("Guess higher")
		guess = input("Guess a number between 1 and 20 (inclusive): ")
	if (int(guess) > aRandomNumber):
		print ("Guess lower")
		guess = input("Guess a number between 1 and 20 (inclusive): ")
	if (int(guess) == aRandomNumber):
		print("You are correct!")
		break
	if (i==2):
		break
print("The correct answer is:")
print (aRandomNumber)
