n,k=map(int,input().split())
s=input()
for i in range(n):
    if s.count(s[i])>k:
        flag=1
        break
    else:
        flag=0
if flag==0:
    print('YES')  
else:
    print('NO')              