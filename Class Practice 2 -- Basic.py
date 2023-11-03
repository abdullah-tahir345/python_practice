class BankAccount:
    # Constructor
    def __init__(self, name, account_number):
        # Public variable or attributes
        self.name = name
        self.account_number = account_number
        self.balance = 0
    
    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f'You amount {amount} is deposit into your account.')
            return self.balance
        else:
            return 'Invalid Transaction'
    
    # Withdraw Method
    def withdraw(self, amount):
        if amount > 0:
            if self.balance < amount:
                return "You don't have enough money."
            elif self.balance > amount:
                self.balance = self.balance - amount
                print('You amount {amount} is withdraw from your account.')
                return self.balance
        else:
            return 'Invalid Amount'
    
    # Check Balance Method
    def check_balance(self):
        return self.balance
    
    # Account Information Method
    def get_account_info(self):
        return f"Account holder name : {self.name}\nAccount Number : {self.account_number}\nCurrent Balance : {self.balance}"

# 1st Object    
acc1 = BankAccount('John Abraham', 3070301000000001)

# Deposit money and check account balance
print(acc1.deposit(100))
print(acc1.deposit(102))
print(acc1.check_balance())

# Withdraw money and check account balance
print(acc1.withdraw(-50))
print(acc1.check_balance())

# Get account information
print(acc1.get_account_info())

# 2nd Object

acc2 = BankAccount('Imran Hashmi', 3070301000000002)

# Deposit money and check account balance
print(acc2.deposit(120512))
print(acc2.check_balance())

# Withdraw money and check account balance
print(acc2.withdraw(512))
print(acc2.check_balance())

# Get account information
print(acc2.get_account_info())

# Both Account Information
print('\n',acc1.get_account_info(),'\n')
print(acc2.get_account_info())