import Parents

class Child(Parents.Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.fname = fname
        self.lname = lname
        self.age = 25

    def printname(self):
        print(f"{self.lname} {self.fname} {self.age}")

    def say(self):
        print('i want to go home!!')



chd = Child("michael", "Kane")
chd.printname()
chd.say()


