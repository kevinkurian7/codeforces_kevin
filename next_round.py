#https://codeforces.com/problemset/problem/158/A
n,k=map(int,input().split())
a=list(map(int,input().split()))

c=0
j=a[k-1]  #whn did thi first u did not consider k-1
for i in a:
    if i>0 and i>=j:
        c=c+1
    else:
        c=c+0
        continue    
print(c)        