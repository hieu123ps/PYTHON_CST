#VD3-07
def nhapdulieu():
    n = int(input('Cho so nguyen duong n: '))
    return n
def ABC(n):
    if (n != 0):
        ABC(n//2)
        print(n % 2, end = '')
def main():
    m = nhapdulieu()
    ABC(m)
if __name__ == '__main__':
    main()
