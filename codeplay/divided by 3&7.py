while True:
    n=int(input("enter the number"))
    if n!=0:
      if (n%3==0 & n%7==0):
        print('divisible by 3 and 7')
      elif(n%3==0):
        print('divisible by only 3')
      elif(n%7==0):
        print('divisible by only 7')
      else:
        print("not divisible by 3 and 7")
    else:
      break
      
