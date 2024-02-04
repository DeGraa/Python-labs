class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"The replenishment was successful. Your current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(
                f"The withdrawal was successful. Your current balance: {self.balance}"
            )
        else:
            print("Insufficient funds")


person = Account("Adilbek", 1500)
person.deposit(1500)
person.deposit(500)

person.withdraw(500)
person.withdraw(2000)
