n=int(input())
f=''
for i in range(n+1):
    for j in range(n+1):
        if i*j==n:
            print(i,j)
            f='done'
        if f=='done':
            break
    if f=='done':
        break                
       