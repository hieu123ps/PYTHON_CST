#VD3-06
from math import trunc, sqrt 
def nhap_du_lieu():
    N = int(input("Cho số N: "))
    M = int(input("Cho số M: "))
    return N, M
def ABC(P):
    if P < 2:     
        return False
    for i in range(2, trunc(sqrt(P) + 1)):
        if (P % i == 0):
            return False   
    return True  
def ABCXYZ(N, M):
    dem = 0
    for P in range(N, M+1):
        if (ABC(P) == True):
            print(P)
            dem = dem + 1
    return dem
def main():
    N, M = nhap_du_lieu()
    print(f'Số lượng số tìm được là: {ABCXYZ(N, M)}')
if __name__ == "__main__":
    main()
