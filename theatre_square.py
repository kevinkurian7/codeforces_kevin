#https://codeforces.com/problemset/problem/1/A
from math import ceil 
n,m,a=input().split()  
n,m,a=int(n),int(m),int(a)  
c=ceil(n/a)*ceil(m/a)  
print(c) 

#think of it as a matrix and we have to cover the length and breadth only
#if length is 7 and the tile size 4  we d0
#7/4 to get no of tile needed it will return 1.75 something
#in this case we can cover a larger area so 7/4 +1 which is 4 doing the same with breadth
#if breadth is 6 6/ 4 it is also giving remainder greater tha n 0 so add 1
#and the answer when 7 6 4 is 4