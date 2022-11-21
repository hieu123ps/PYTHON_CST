#VD3-05
def nhap_du_lieu():
    M = int(input("Cho biết số giới hạn: "))
    return M
def dem_chu_so(P):
    d = 0
    while (P != 0):
        d = d + 1; 
        P = P // 10
    return d
def ABCXYZ(P):
    S = 0; Temp = P    
    scs = dem_chu_so(P) 
    while (P != 0):
        cs = P % 10     
        S = S + pow(cs, scs)   
        P = P // 10   
    if (Temp == S):   
        return True
    else:
        return False
def main():
    M = nhap_du_lieu()
    print("Các số tìm được là: ")
    for P in range (1, M+1):
        if (ABCXYZ(P) == True):
            print(P)
if __name__ == "__main__":
    main()
