class Account:
    def __init__(self, name,  account_number):
        self.name = name
        self.balance = 0
        self.account_number = 3073301000000000 + account_number
        
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print('Invalid Amount')
            
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance > amount:
                self.balance = self.balance - amount
            else:
                print('Insufficient Balance')
        else:
            print('Invalid Amount')
        return self.balance
            
    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number
    
class Bank:
    def __init__(self):
        self.accounts = []
        
    def create_account(self, name, account_number):
        account = Account(name, account_number)
        self.accounts.append(account)
        return account
    
    def get_account(self, account_number):
        account_number = 3073301000000000 + account_number
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
            
    def perform_transaction(self, sender_account_number, receiver_account_number, amount):
        sender = self.get_account(sender_account_number)
        reciever = self.get_account(receiver_account_number)
        if amount > 0:
            if sender.get_balance() > amount:
                sender.withdraw(amount)
                reciever.deposit(amount)
                print("Transaction Successfull.\n")
                print(f"Sender Account : {sender.get_account_number()}\nSender Name : {sender.name}\nReciever Account : {reciever.get_account_number()}\nReciever Name : {reciever.name}\nAmount : {amount}")
            elif sender.get_balance() < amount:
                print("You don't have enough money.")
        else:
            print("Invalid Transaction")
            
    
bank = Bank()
account1 = bank.create_account('Abdullah Tahir', 1)
account2 = bank.create_account('Hamza Tahir', 2)
account3 = bank.create_account('Usama Tahir', 3)
account4 = bank.create_account('Umair Tahir', 4)
account10 = bank.create_account('Usman Tahir', 10)

print('Deposit Money in Accounts')
print(account1.deposit(500000))
print(account2.deposit(20000))
print(account3.deposit(500))
print(account4.deposit(900000))

print()
print('Balance of Account')
print(account1.get_balance())
print(account2.get_balance())
print(account3.get_balance())
print(account4.get_balance())
print(account10.get_balance())

print()
print('Withdraw Money From Accounts')
print(account3.withdraw(200))
print(account4.withdraw(100000))

print()
print('Online Transaction 1')
print(bank.perform_transaction(1, 3, 100000))

print()
print('Deposit Money in Accounts')
print(account1.get_balance())
print(account3.get_balance())

print()
print('Online Transaction 2')
print(bank.perform_transaction(10, 1, 5))

print()
print('Online Transaction 3')
print(bank.perform_transaction(1, 10, -1))
