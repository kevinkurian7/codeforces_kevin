n,m,a,b=map(int,input().split())
if m*a<=b:
    print(n*a)
else:
    #x=int((n/m)*b)
    #print(x)
    #print(min((n%m)*a,b ))
    print((int(n/m)) * b + min((n%m) * a, b))
