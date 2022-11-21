#VD3-02
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b;
    return a, b
n = 100
m = 70
print(f'Trước khi gọi hàm: n = {n},  m = {m}')
n, m = swap(n, m)
print(f'Sau khi gọi hàm: n = {n},  m = {m}')
