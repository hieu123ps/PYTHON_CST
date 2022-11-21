#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     05/11/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def open():
    with open('Fib.Inp') as fh:
        fdata = next(fh).split()
        arr = []
        arr.append(fdata)
        for line in fh:
            arr.append(line)
    fh.close()
    return arr

def main():
    print(open())

if __name__ == '__main__':
    main()
