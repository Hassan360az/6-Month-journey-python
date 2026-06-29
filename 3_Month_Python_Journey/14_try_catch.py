try:
    age = int (input("Enter your age Please : "))
except ValueError:
    print ("Please enter a integer number.")
else:
    print (f"{age}")
