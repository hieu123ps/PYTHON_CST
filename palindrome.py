#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     26/10/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def palindrome(s):
    left = 0
    right = len(s) - 1
    flag = True
    list = ['[]', '{}', '()']
    while(left <= right):
        res = s[left] + s[right]
        if(res not in list):
            flag = False
            break
        left += 1
        right -= 1
    print(flag)

def main():
    s = '{(([|]))}'
    palindrome(s)

if __name__ == '__main__':
    main()
