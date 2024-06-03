class PVG:
    def name(self):
        print("Pune Vidyarthi Griha")
class Staff(PVG):
    def Teacher(self):
        print("Dharne Sir")
class Person(Staff):
    def student(self):
        print("Sagar")
d=Person()
d.name()
d.Teacher()
d.student()