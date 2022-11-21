def tron_2_ds(listA,listB):
    newlist = []
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
    return newlist

def sx_tron(s):
    if len(s) <= 1:
        return s
    else:
        mid = len(s) // 2
        LeftHalf = sx_tron(s[:mid])
        RightHalf = sx_tron(s[mid:])
    newlist = tron_2_ds(LeftHalf,RightHalf)
    return newlist


def main():
    x = [3, 5, 4, 9, 15, 1, 2, 4, 7, 8, 14, 17, 21]
    print('Chuỗi ban đầu:')
    print(x)
    print('Sau khi sx:')
    b = sx_tron(x)
    print(b)


if __name__ == "__main__":
    main()