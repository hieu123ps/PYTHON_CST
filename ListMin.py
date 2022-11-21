#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     15/08/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# -2 11 -4 13 -5 2 ==> max: 11 -4 13

def MaxList_02(arr):
    length = len(arr)
    maxSum = arr[0]
    for i in range(0, length, 1): # O(n)
        sum = 0
        for j in range(i, length, 1): # O(n)
            sum += arr[j]
            if(sum > maxSum):
                maxSum = sum
    print(maxSum)
    # ==> O(n^2)

def MaxList_01(arr):
    length = len(arr)
    maxSum = 0
    for i in range(0, length, 1): # O(n)
        for j in range(i, length, 1): # O(n)
            sum = 0
            for k in range(i, j+1, 1): # O(k)
                sum += arr[k];
            if(sum > maxSum):
                maxSum = sum
    print(maxSum)
    # ==> O(n^3)

def main():
    #arr = [-2, 11, -4, 13, -5, 2]
    arr = [1, 2, 5, 4, -1, 6, 2]
    MaxList_01(arr)
    MaxList_02(arr)

if __name__ == '__main__':
    main()
