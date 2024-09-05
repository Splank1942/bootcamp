class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdrawal(self):
        w_amount = input("How much would you like to withdraw? ")
        if int(w_amount) > self.balance:
            print("Unable to process transaction, Insufficient Funds!")
        else:    
            self.balance -= int(w_amount)
            print(f"the new balance is {self.balance}")
              
    def deposit(self): 
        d_amount = input("How much would you like to deposit? ")
        self.balance += int(d_amount)
        print(f"The new balanace is {self.balance}")

    def welcome(self):
        print("Welcome to the bank of Splank!")
        print(f"The current balance for {self.account_holder}'s account is {self.balance}")
    

        
mybankaccount = BankAccount("Aric Abbott", 5000)    
mybankaccount.welcome()
q = input("What would you like to do today? ")
if q == "deposit":
    mybankaccount.deposit()
else:
    mybankaccount.withdrawal()
