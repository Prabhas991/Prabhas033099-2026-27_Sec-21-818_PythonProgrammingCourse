class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    # Deposit method
    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    # Display account details
    def display(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance)


# Creating an object
account = BankAccount("Prabhas", 12345, 5000)

# Performing operations
account.display()
account.deposit(2000)
account.withdraw(1000)
account.display()