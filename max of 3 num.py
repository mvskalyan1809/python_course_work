l=list(map(int,input('enter the list: ').split()))
maxa=l[0]
minb=l[0]
for i in range(1,len(l)):
    if l[i]>maxa:
        maxa=l[i]
    if l[i]<minb:
        minb=l[i]
print('Maximum: ',maxa)
print('Minimum: ',minb)
    
