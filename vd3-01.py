#VD3-01
#cho biết chương trình này hiển thị bao nhiêu chữ Y lên màn hình
def F(n):
    for i in range(1, n+1, 1):
        if i % 2 == 0:
            print('Y')
m = 5
for i in range(1, m+1, 1):
    F(i);
