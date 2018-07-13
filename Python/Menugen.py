#imports the ability to get a random number
from random import *

#Create the list of words you want to choose from.
aList = ["Spaghetti", "Pizza", "Pasta", "Burger", "Sandwich", "Wrap", "Fried Rice"]
bList = ["Salad", "Soup", "Egg Rolls", "Bread", "Brushetta", "Chips", "Dumplings"]
cList = ["Cake", "Cookies", "Brownies", "Pie", "Milkshake", "Tirimisu", "Ice Cream"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
bRandomIndex = randint(0, len(bList)-1)
cRandomIndex = randint(0, len(cList)-1)

print("Your Meal is")
print(bList[bRandomIndex])
print("and")
print(aList[aRandomIndex])
print("and")
print(cList[cRandomIndex])
