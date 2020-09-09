n=int(input())
s=0
c=0
r=0
for i in range(1,n+1):
    s=s+i
    c=s+c
    if c<=n:
        r+=1
print(r)        