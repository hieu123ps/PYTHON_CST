#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     20/08/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def showNumber():
    arr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "teen"]
    x = int(input("Enter number: "))
    print(arr[x - 1])

def main():
    showNumber()

if __name__ == '__main__':
    main()
