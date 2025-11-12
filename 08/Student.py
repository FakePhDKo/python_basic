from Person import NormalPerson

class Student(NormalPerson):
    def talk(self):
        super().talk()
        print("hello~")



stu = Student()
stu.talk()
stu.eat()
stu.sleep()

print(stu.eyes)