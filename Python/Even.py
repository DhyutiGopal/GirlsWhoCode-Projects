#def question(num1):
    #if num1.isnumeric():
    #    return True
    #else:
    #    return False

def is_even(num1):
    #question(num1)
    if (num1 % 2) == 0:
        return True
    else:
        return False
def main():
    while True:
        num1 = input("Enter a number and I'll tell you if its even or not. ")
        if num1.isnumeric():
            num1 = int(num1)
            is_even(num1)
            print(is_even(num1))
        else:
            print("False. Please enter a number.")



if __name__ == '__main__':
    main()
