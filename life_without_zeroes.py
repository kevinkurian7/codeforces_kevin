a=input()
b=input()
an=int(a.replace('0',''))
bn=int(b.replace('0',''))

v=str(int(a)+int(b)).replace('0','')

if an+bn==int(v):
    print('YES')
else:
    print('NO')    