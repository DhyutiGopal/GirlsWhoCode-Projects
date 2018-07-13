#imports the ability to get a random number
from random import *

#Create the list of words you want to choose from.

aList = ["Happy", "Game", "Garden", "Gas" , "Gate" , "Girl", "Hammer",  "Hat", "Hieroglyph", "Highway", "Ice",  "Ice-cream" ,"Insect", "Kaleidoscope", "Kitchen", "Milkshake", "Money", "Monster", "Perfume", "Rainbow"]

#Generates a random integer
aRandomIndex = randint(0, len(aList)-1)

print(aList[aRandomIndex])
