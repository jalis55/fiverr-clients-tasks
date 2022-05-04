from unicodedata import name


class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def display(self):
        print(f"{self.name} is {self.age} years old")

class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section=section
    
    def display_student(self):
        print(f"{self.name} is {self.age} years old and in section {self.section}")

student=Student('Habib',13,2)
student.display_student()
