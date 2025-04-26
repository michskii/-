class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.__account_holder=account_holder
        self.__balance=balance  #private attributes.

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposit of {amount} recieved!!")
        else:
            print("Inssufficient amount!")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"{amount} Ksh withdrawn from account!")
        else:
            print("insufficient balance!!")
    def get_balance(self):
        return self.__balance
    def get_account_holder(self):
        return self.__account_holder
    
    def __str__(self):
        return f"Account Holder: {self.__account_holder}\nBalance: {self.__balance}"
    
Account=BankAccount("John Doe",1000)
print(Account)
Account.deposit(500)
print(f"New Balance: {Account.get_balance()}")
Account.withdraw(200)
print(f"New Balance: {Account.get_balance()}")
Account.withdraw(2000)


