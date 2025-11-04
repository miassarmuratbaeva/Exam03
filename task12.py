class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"Mening ismim {self.name}.Men {self.age} yoshdaman."
class Student(Person):
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    def introduce(self):
        return f"Men ismim {self.name}. Men {self.age}yoshdaman va {self.grade} sinfman"
person1 = Person("Sarvinoz", 20)
student1 = Student("Diyora", 16, 10)
print(person1.introduce())
print(student1.introduce())