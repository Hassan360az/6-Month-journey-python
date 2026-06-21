class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    #getter
    def get_balance(self):
        return self.__balance

    #setter
    def set_balance(self, amount):
        if amount < 20000:
            self.__balance = amount
            print(amount)
        else:
            print("Enter amount less than 20000")

    


account1 = Bank_account("ali" , 50000)
print(account1.get_balance())

print (account1.set_balance(10000))


