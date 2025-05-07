#even numbers in string&count
n=input("enter the string:")
count=0
for i in n:
    num=int(n)
    if num%2==0:
        count+=1
print("count",count)
