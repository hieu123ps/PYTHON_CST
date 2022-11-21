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

def Karatsuba(x, y, n):
    if n == 1:
        return int(x[0])*int(y[0])
    a = x[:(n//2)+1]
    b = x[(n//2)+2:]
    c = y[:(n//2)+1]
    d = y[(n//2)+2:]

    U = Karatsuba(a, b, n//2)
    V = Karatsuba(c, d, n//2)
    W = Karatsuba(int(a)+int(b), int(c)+int(d), n//2)
    return U*(10**n) + (W - U - V)*(10**(n//2))+V

def main():
    print(Karatsuba('123', '456', 3))

if __name__ == '__main__':
    main()
