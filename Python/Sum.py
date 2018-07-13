def calc_total (sumList):
    print(sumList)
    sum = 0
    for i in sumList:
        sum=i+sum
    return sum

def main():
    sumList = []
    going = True
    while going == True:
        num = input("Enter the number. Press the 0 when you are finished.")
        num = int(num)
        if num == 0 :
            print(calc_total(sumList))
            going = False
        else:
            sumList.append(num)
            going = True


if __name__ == '__main__':
    main()
