
colors = ["green" , "blue" , "purple" , "pink" , "red" , "orange" , "yellow", 30]
print(colors)
#Prints the list
print(colors[0])
#Prints the index of given list
print(len(colors))
#Prints the length of the list
print(4 in colors)
print("blue" in colors)
#Prints false/true if this is part of the list

for num in colors:
    print(num)
#Everytime this loop goes around, it prints the next value of the list

for i in range(len(colors)):
    print(colors[i])
#Everytime this loop goes around, it prints the next value of the list
#range(8) == [0,1,2,3,4,5,6,7]
#numbers[0] == 1

print("ee" in colors)
#Output: false

print("ee" in "green")
#Output: true

colors.append("White")
print (colors)
#Output: ['green', 'blue', 'purple', 'pink', 'red', 'orange', 'yellow', 30, 'White']

colors.extend(["Black", "Brown"])
print(colors)
#Output: ['green', 'blue', 'purple', 'pink', 'red', 'orange', 'yellow', 30, 'White', 'Black', 'Brown']

colors.insert(1, "Cyan")
print(colors)
#Inserts the string in the list, colors, at the stated index
#if stated index is negative, the index starts at the back of the list, but at -1
# i.e. numbers.insert(-1, 6) -> [1,2,3,4,6,5]
# if stated index is too large, the string/number is inserted at either of the ends depending if it is negative or positive

colors.sort()
print(colors)
#Sorts a list in ascending order or alphabetizes the list
#Does not sort lists that consist of both numbers and strings

colors[-1]
print(colors)
#Starts from the back of the list and counts backwards for index -> 'yellow'
# 0 doesn't work when using negative indexes

colors[1:4]
print(colors)
 #Prints list items from the first index to the last index not including the last index
