#BT3-02
def nhap_du_lieu():
    a = int(input("Cho so a: "))
    b = int(input("Cho so b: "))
    return a, b
    
#trả về ước số chung lớn nhất của a và b    
def USCLN(a, b):
    if (a % b == 0):
        return b
    else:
        return USCLN(b, a % b)

def main():
    a, b = nhap_du_lieu()
    print(f'USCLN của ({a}, {b}) là: {USCLN(a, b)}')

if __name__ == "__main__":
    main()
    
