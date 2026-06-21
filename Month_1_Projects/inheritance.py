class Countries ():
    def __init__ (self , name ):
        self.name = name



class Pakistan (Countries):
    def __init__ (self , name , unique_code):
        super().__init__(name)
        self.code = unique_code



Asia = Countries("pakistan")

Lahore = Pakistan("Lahore" , 4534)

Karachi = Pakistan ("Karachi" , 2342)

print (f"your country name is : {Asia.name}")

print (f"your City name and code is: {Lahore.name}, {Lahore.code} " )

print (f"your city name and code is : {Karachi.name} , {Karachi.code}")