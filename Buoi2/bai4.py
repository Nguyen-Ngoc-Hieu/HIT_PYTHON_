n = int(input('nhập n: '))
s1 = 0
s2 = 1
i=0
if(n == 1): print('0')
else:
    print('0 1',end=' ')
for i in range(n-2):
    s = s1 + s2
    s1 = s2
    s2 = s
    print(s,end=' ')