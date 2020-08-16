#https://codeforces.com/problemset/problem/71/A
T=int(input())
for i in range(T):
    s=input()   
    
    n=len(s)
    if n>10:
        n2=len(s[1:n-1])
        s=s[0]+str(n2)+s[n-1]
   
    
    print(s)  