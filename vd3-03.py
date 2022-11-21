#VD3-03
def F(x):
    x = x + 1
    return x
def G(y):
    y = y - 1
    return F(y)
def main():
    print(f'Kết quả: {F(4) + G(8)}')
if __name__ == "__main__":
    main()
