# 3-a
print('3-a')
n1 = int(input('nhập số nguyên n: '))
tong1 = 0
for i in range(n1 + 1):
    if (i % 2 == 0):
        tong1 = tong1 - i
    else:
        tong1 = tong1 + i
print('tổng cần tìm là:',tong1)    
# 3-b
print('3-b')
n2 = int(input('nhập số nguyên '))
tong = 0
for i in range(1,n2+1):
    tong = tong + 1/i
print('tổng cần tìm là:',tong)
#3-c
print('3-c')
import math
a = float(input('nhập số thứ nhất: '))
b = float(input('nhập số thứ hai: '))
c = float(input('nhập số thứ ba: '))
if (a==0):
    if(b==0):
        if(c==0): print('vô số nghiệm')
        else: print('vô nghiệm')
    else:
        print('x =',-c/b)
else:
    delta = b*b - 4*a*c
    if(delta < 0): print('vô nghiệm')
    elif(delta == 0): print('có nghiệm kép bằng',-b/(2*a))
    else:
        print('nghiệm thứ nhất là',(-b + math.sqrt(delta))/(2*a))
        print('nghiệm thứ hai là: ',(-b - math.sqrt(delta))/(2*a))