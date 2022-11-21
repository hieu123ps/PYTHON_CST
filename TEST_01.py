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

def sortDict(d):
    return sorted(d.values())
    print(d)

def f(n):
    r = n.split()
    temp = {}
    for i in r:
        if i in temp.keys():
            temp[i] += 1
        else:
            temp[i] = 1
    return temp

def enter():
    temp = {}
    i = 1
    while(True):
        key = input(f"Enter key[{i}]: ")
        if (key == "stop"):
            break
        val = int(input(f"Enter value[{i}]: "))
        if key in temp.keys():
            temp[key] += val
        else:
            temp.update({key:val})
        i += 1
    return temp

def main():
    r = f("Ha Noi mua nay dao nay mua nhieu")
    sortDict(r)

if __name__ == '__main__':
    main()
