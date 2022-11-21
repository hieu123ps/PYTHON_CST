#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     13/10/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def findMax(theSeq, L, R):
    if (L == R):
        return theSeq[L]
    if (R - L == 1):
        if (theSeq[R] > theSeq[L]):
            return theSeq[R]
        return theSeq[L]
    aL = findMax(theSeq, L, len(theSeq)//2)
    aR = findMax(theSeq, (len(theSeq)//2) + 1, R)
    if (aL < aR):
        return aR
    return aL

def main():
    theSeq = [5, 6, 8, 10]
    print(findMax(theSeq, 0, 3))

if __name__ == '__main__':
    main()
