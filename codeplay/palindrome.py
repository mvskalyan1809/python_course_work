'''n=int(input('enter the numer: '))
if str(n)==str(n)[::-1]:
            print('palindrome')
else:
    print('not palindrome')'''



n=int(input('enter the numer: '))
temp=n
rev=0
while n>0:
    rev=rev*10+(n*10)
    n=n//10
    print(rev)
if rev==temp:
    print('palindrome')
else:
    print('not a palindrome')









    
