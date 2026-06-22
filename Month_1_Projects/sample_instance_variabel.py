# Parent Class (Abba Ji)
class Father:
    def scold(self):
        print("Ghar se nikal doongaa! Pese band!")

# Child Class (Beta) - Jo Father se inherit kar raha hai
class Son(Father):
    # Yahan hum scold method ko OVERRIDE kar rahe hain
    def scold(self):
        print("Bhai, scene sahi nahi hai !")

# Agar hum Abba ka object banayein:
insan1 = Father()
insan1.scold()  # Output: Ghar se nikal doongaa! Pese band!

# Agar hum Betay ka object banayein:
insan2 = Son()
insan2.scold()  # Output: Bhai, scene sahi nahi hai !