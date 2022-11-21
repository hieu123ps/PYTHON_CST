#VD3-04
x = 3
def A(z):
    global x
    x = 2
    def B(y):
      x = y + 1
      y = x + 1
      return y
    a = B(x + z)
    return a 
y = A(x)
print(f'Gia tri bien x = {x}')
print(f'Gia tri cua bien y = {y}')
