class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

ali = Employee()
print(ali.get_salary())  # Access salary using getter

ali.set_salary(60000)   # Update salary using setter
print(ali.get_salary())

