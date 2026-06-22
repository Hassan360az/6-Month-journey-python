class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

p1 = Person('Bilal', 45)
s1 = Student('Ali', 20, 'CS-101')

p1.show_info()
# Name: Bilal, Age: 45

s1.show_info()
# Name: Ali, Age: 20, Student ID: CS-101