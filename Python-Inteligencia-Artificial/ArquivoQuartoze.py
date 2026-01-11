class Account:

    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print(f" Value Error. Cannot be negative ")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit Success R$ {amount}")

personalAccount = Account("Maria", 5000.0)

print(personalAccount.holder)
print(personalAccount.balance)

personalAccount.balance = 2500.0

#Type Inference is indeed a powerful
personalAccount.balance = -100.0

print(f"Holder: {personalAccount.holder} Amount: {personalAccount.balance}")
