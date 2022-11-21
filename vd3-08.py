#VD3-08
#ví dụ này tính công thức:
# 1 + 1/2 + 1/2*4 + 1/2*4*6 + ... + 1/2*4*6*...* 2n

def ABC(n):
    if (n == 0):
        return 1 
    else:
        return ABC(n - 1) * 2 * n
def XYZ(n):
    if (n == 0):
        return 1 
    else:
        return XYZ(n - 1) + 1 / ABC(n)

def main():
    n = int(input('Nhập số nguyên dương n = '))
    m = float(XYZ(n))
    print('{:.3f}'.format(m))
if __name__ == "__main__":
    main()
