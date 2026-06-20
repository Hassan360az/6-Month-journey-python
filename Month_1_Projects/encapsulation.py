class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


account1 = Bank_account("ali" , 50000)
# cant access in the main 
print (account1._balance)


