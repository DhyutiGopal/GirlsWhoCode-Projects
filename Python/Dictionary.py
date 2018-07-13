ages = {'Meg': 24, 'Caroline': 19, 'Matt': 29}

ages['Caroline'] = 20
## Changes the value of a key

ages['Carly'] = 16
##Adds key to dictionary

ages['Carrington'] = 15
ages['Mena'] = 15

##Cannot have same key different values, but can have same value different keys

print(ages)
## Prints {'Meg': 24, 'Caroline': 19, 'Matt': 29}
print(" ")
for name in ages:
    print(name)
##Prints all of the names in different lines
print(" ")
print(ages['Matt'])
##Prints the value of the key, Matt
print(" ")
for number in ages:
    print(ages[number])
##Just prints the values of the dictionary
print(" ")
for number in ages:
    print(1 + ages[number])
##Adds one to the values of the dictionary, but does not change the values of the dictionary

print(" ")
for number in ages:
    currentAge = ages[number]
    ages[number] = currentAge + 1
    print(ages[number])
##Changes the values in the dictionary and prints them 
