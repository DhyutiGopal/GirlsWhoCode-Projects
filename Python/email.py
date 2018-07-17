user = input("Enter email. ")
isNameValid = user[0:user.index("@")]
print(isNameValid)
# symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','+','=','{','[','}','}','|',',',':',';','<','?',
# '>','?','/']
for i in range(len(user)):
    print(i)
    if (((user[len(user)-1] == "m") and (user[len(user)-2] == "o") and (user[len(user)-3] == "c") and (user[len(user)-4] == ".")) or
    ((user[len(user)-1] == "u") and (user[len(user)-2] == "d") and (user[len(user)-3] == "e") and (user[len(user)-4] == ".")) or
      ((user[len(user)-1] == "n") and (user[len(user)-2] == "i") and (user[len(user)-3] == ".")) ):
        if (len(user[user.index("@"): (len(user)-4)]) > 3):
            if (isNameValid.isalnum() == False):
                print("Invalid")
                break
    # elif((user[len(user)-1] == "u") and (user[len(user)-2] == "d") and (user[len(user)-3] == "e") and (user[len(user)-4] == ".")):
    #     if (len(user[user.index("@"): (len(user)-4)]) > 3):
    #         if (isNameValid.isalnum() == False):
    #             print("Invalid")
    #             break
    # elif((user[len(user)-1] == "n") and (user[len(user)-2] == "i") and (user[len(user)-3] == ".")):
    #     if (len(user[user.index("@"): (len(user)-3)]) > 3):
    #         if (isNameValid.isalnum() == False):
    #             print("Invalid")
    #             break
