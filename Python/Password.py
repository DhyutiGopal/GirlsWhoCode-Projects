#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("newDictionary.txt","r")


print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
#string = test_password.strip()

#Write logic to see if the password is in the dictionary file below here:
for line in f:
    print(line)
    if line.strip() == test_password:
        print("This password is weak. Please enter another password.")
        test_password = input("Type in another trial passoword. ")
print("This password is strong.")
f.close()
