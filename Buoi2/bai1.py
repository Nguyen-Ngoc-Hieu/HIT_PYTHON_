# 1-a
print('1-a')
a = int(input('nhập số nguyên dương bất kỳ: '))
tong = 0
while(a != 0):
    tong = tong + (a % 10)
    a = a // 10
print('tổng các chữ số là: ',tong)
# 1-b
print('1-b')
n = int(input('nhập số nguyên dương n: '))
print('các ước của',n,'là')
for i in range(1,n+1):
    if(n % i == 0):
        print(i,"   ",end='')

# 1-c
print('\n1-c')
a = float(input('nhập số thứ nhất: '))
b = float(input('nhập số thứ hai: '))
c = float(input('nhập số thứ ba: '))
if (a <= b + c) and (b < a + c) and (c < a + b):
    if (a == b == c): print('tam giác đều')
    elif (a == b) or (a == c) or (b == c): print('tam giác cân')
    elif (a**2 == b**2 + c**2) or (b**2 == c**2 + a**2) or (c**2 == a**2 + b**2): print('tam giác vuông')
    elif (a**2 + b**2 > c**2) or (a**2 + c**2 > b**2) or (b**2 + c**2 > a**2): print('tam giác nhọn')
    else : print('tam giác tù')
else:
    print('không là tam giác')