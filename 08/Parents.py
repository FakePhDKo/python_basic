class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"{self.lastname} {self.firstname}")

me = Person('Minsu', 'Ko')
me.printname()
