data={
    1:{"username":"Teja","Password":"Teja@123","balance":0,"transactions":[]},
      2:{"username":"kalyan","Password":"kalyan@123","balance":1000000000,"transactions":[]},
      3:{"username":"Ram","Password":"Ram@123","balance":23450,"transactions":[]},
      4:{"username":"Dinesh","Password":"Dinesh@123","balance":87650,"transactions":[]},
      5:{"username":"pavani","Password":"Pavani!123#","balance":756430,"transactions":[]},
      }

class ATM:
    loginStatus=False
    def __init__(self,name,pwd):
        
        for i in data.keys():
            if data[i]["username"]==name and data[i]["Password"]==pwd:
                self.name=name
                self.__pwd=pwd
                ATM.loginStatus=True
                self.id=i
                print("Login successful",self.name)
                break
        else:
            print("Invalid Username or Password")

    def checkbalance(self):
        if (ATM.loginStatus):
            print(f"Hello {self.name}\ncurrent balance: ${data[self.id]['balance']}")
        else:
            print("Login Time is expired, Login Again")

    def viewTransactions(self):
        if ATM.loginStatus:
            if data[self.id]['transactions']:
                print("Hello {self.name}\n---------------Transaction History----------------")
                for i in data[self.id]['transactions']:
                    print(i)
                print("____________END_____________")
            else:
                print("No Transactions")
        else:
           print("Login Time is expired, Login Again") 

    def withdraw(self,amount):
        if ATM.loginStatus:
            if amount<=data[self.id]['balance']:
                data[self.id]['balance']-=amount
                w=f"${amount} is withdraw succussful from the account"
                print(f"Hello {self.name}\n{w}")
                data[self.id]['transactions'].append(w)
            else:
                print(f'Hello {self.name}\nInsuffient balance')
        else:
            print("Login Time is expired, Login Again")

    def depoist(self,amount):
        if ATM.loginStatus:
            data[self.id]['balance']+=amount
            d=f"${amount} is depoist succussful to your account"
            print(f"Hello {self.name}\n{d}")
            data[self.id]['transactions'].append(d)
        else:
            print("Login Time is expired, Login Again")
    
    
                
            
user1=ATM("Teja","Teja@123")
user2=ATM("pavani","Pavani!123#")

user1.checkbalance()
user1.depoist(10000000000)
user1.withdraw(100)
user1.withdraw(178900)
user1.withdraw(1678900)
user1.depoist(546789)
user1.viewTransactions()
user1.checkbalance()



user2.withdraw(1000)
user2.checkbalance()
user2.viewTransactions()

        
        


