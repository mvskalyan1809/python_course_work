while True:
    num=int(input('enter the number:'))
    isPrime=0
    for i in range(2,(num//2)+1):
        if num%i==0:
            isPrime+=1
    if isPrime==0:
        print('it is a prime number')
    else:
        print('it is not a prime number')
    
 
