while True:
    n=int(input("enter the number"))
    if n!=0:
      if (n%400==0 or n%4==0 & n&100==0):
        print('leap year')
      else:
        print("not a leap year")
    else:
      break
      
s
