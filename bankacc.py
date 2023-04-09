class BankAccount:
    def __init__(self, int_rate, balance):
      self.int_rate=int_rate
      self.balance=balance
    
    def deposit(self,amount):
       self.balance+=amount
       return self
    
    def withdraw(self,amount):
       if amount>self.balance:
          print("ERRO : You dont have enough money to withdraw!")
          self.balance-=5
          return self
       else:
          self.balance-=amount
          return self
    def display_account_info(self):
       print("Balance : $" +str(self.balance))
       return self
    def yield_interst(self):
       if self.balance>0:
          self.balance*=(self.int_rate+1)
       return self
    
enri=BankAccount(0.01,825)
arber=BankAccount(0.01,790)

enri.deposit(60).deposit(90).deposit(110).withdraw(76).yield_interst().display_account_info()
arber.deposit(93).deposit(150).withdraw(40).withdraw(70).withdraw(35).withdraw(120).yield_interst().display_account_info()
       

       
      