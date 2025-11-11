class Person:
    eyes = 2
    norse = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"eyes: {self.eyes}")

p1 = Person('John', 25)
p1.myfun()