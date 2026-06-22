class Student:
    schoool = "Government High School"

    def __init__(self, name):
        self.name = name
    def print_info(self):
        print(f"your school name is {Student.schoool}")

        print (f"your name is {self.name}")

s1 = Student("Ali")

s2 = Student("Rizwan")

s1.print_info()
s2.print_info