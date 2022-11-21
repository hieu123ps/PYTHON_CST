#Ho va ten: Le Quang Hieu
#MSV: 705102009
#Lop: K70A

import math

def single(x):
    temp = x
    sum = 0
    while temp != 0:
        p = temp%10
        sum += pow(p, 5)
        temp = temp // 10
    if sum == x:
        return True
    return False

def check():
    for i in range(10000, pow(10,10), 1):
        if single(i) == True:
            print(i)

def main():
    check()

if __name__ == '__main__':
    main()
