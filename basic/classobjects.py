class BankAccount:
    def __init__(self, account_owner, balance=0):
        self.account_owner = account_owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance-= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    
    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Final balance: {account.get_balance()}")