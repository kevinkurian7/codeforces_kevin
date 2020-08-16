#https://codeforces.com/problemset/problem/231/A
n=int(input())
countr=0
for i in range(n):
    arr=list(map(int,input().strip().split()))
    c=0
    c=arr.count(1)
    if c>=2:
        countr=countr+1
print(countr)        