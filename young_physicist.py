n=int(input())
lis=[]
sumx=0
sumy=0
sumz=0
for i in range(n):
    lis.append(list(map(int,input().split())))
    sumx=sumx+lis[i][0]
    sumy=sumy+lis[i][1]
    sumz=sumz+lis[i][2]
#for i in range(n):
    #print(sum(lis[i]))
    #sumx=sumx+sum(lis[i][0])
    #sumy=sumy+sum(lis[i][1])
    #sumz=sumz+sum(lis[i][2])
#print(sumx)
#print(sumy)
#print(sumz)    
if sumx==0 and sumy==0 and sumz==0:
    print('YES')
else:
    print('NO')      