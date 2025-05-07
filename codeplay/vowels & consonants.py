while True:
    n=input("enter the letters:")
    if (n!=0):
        vowel="a,e,i,o,u,A,E,I,O,U"
        if (n in vowel):
            print('vowel')
        else:
            print('not a vowel')
    else:
        break
   
