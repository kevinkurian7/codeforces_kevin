n=int(input())
a=list(map(int,input().split()))
sum_a=sum(a)
e,o=0,0
for i in a:
    if i%2==0:
        e+=1
    else:
        o+=1    
if(sum_a%2==0):
    print(e)
else:
    print(o)            