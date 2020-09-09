s=input()
l_l,l_u=0,0
for i in s:
    if i.islower():
        l_l+=1
    elif(i.isupper()):
        l_u+=1
if l_l==l_u or l_l>l_u:
    print(s.lower())
elif l_u>l_l:
        print(s.upper())
