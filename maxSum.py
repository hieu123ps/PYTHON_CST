#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     18/10/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a = [-15, 7, 9, -8, -5, 9, -3, 4]
    maxSum = a[0]
    for i in range(0, len(a), 1):
        sum = 0
        for j in range(i, len(a), 1):
            sum += a[j]
            if sum > maxSum:
                maxSum = sum
    print(maxSum)
if __name__ == '__main__':
    main()
