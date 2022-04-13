class BankAccount:
    def __init__(self):
        #pass
        self.bank_close = False
        self.bank_open = False
        
    def get_balance(self):
        #pass
        if self.bank_open == True:
            return self.bank
        elif self.bank_close == True: 
            raise ValueError("please open your account")

    def open(self):
        #pass
        if self.bank_open == True:
            raise ValueError("your account is already active")
        else:
            self.bank = 0
            self.bank_open = True

    def deposit(self, amount):
        #pass
        if self.bank_close == True or amount <= 0:
            raise ValueError("your account is already closed and/or you can't deposit negative value")
        else:
            self.bank += amount
            return self.bank

    def withdraw(self, amount):
        #pass
        if amount > self.bank or self.bank_close == True or amount <= 0:
            raise ValueError("You don't have enough money and/or your account is already closed and/or you can withdraw negative")
        else:
            self.bank -= amount
            return self.bank

    def close(self):
        #pass
        if self.bank_open == False:
            raise ValueError("there is no account under your name")
        else:
            self.bank_close = True
            self.bank_open = False
        
