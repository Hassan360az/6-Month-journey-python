class CreditCardPayment:
    def pay(self, amount):
        print(f"Charging Rs.{amount} to credit card.")

class EasypaisaPayment:
    def pay(self, amount):
        print(f"Sending Rs.{amount} via Easypaisa.")

class BankTransferPayment:
    def pay(self, amount):
        print(f"Transferring Rs.{amount} via bank.")

payment_methods = [CreditCardPayment(), EasypaisaPayment(), BankTransferPayment()]

for method in payment_methods:
    method.pay(1000)