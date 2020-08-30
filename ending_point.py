x,y=map(int,input().split())
s=input()
for i in s:
    if i=='U':
        y+=1
    elif i=='D':
        y-=1
    elif i=='L':
        x-=1
    elif i=='R':
        x+=1
print(x,y)            
