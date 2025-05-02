'''n=int(input('enter the number: '))
isPrime=0
for i in range(2,(n//2)+1):
    if n%i==0:
        isPrime+=1
    if isPrime==0:
        print('it is a prime number')
    else:
        print('it is not a prime number')'''




'''n=int(input("enter the numbers: "))
sum=0
for k in range(2,n+1):
    for i in range(2,k):
        if(int(k%i)==0):
            break;
    else:
        sum+=k
print("Sum of all prime numbers upto",n,':',sum)'''






    
n=int(input("enter the numbers: "))
sum=0
for i in range(2,n+1):
    prime=0
    for j in range(2,(i//2+1)):
        if i%j==0:
            prime+=1
    if prime==0:
        sum+=i
        print(i)
print(sum)
     


