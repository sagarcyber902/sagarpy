class Person:
    def __init__(self,name,sex,profession):
        #data members(instance variabless)
        self.name=name
        self.sex=sex
        self.profession=profession

    #Behavior(instance methods)
    def show(self):
        print("Name:",self.name,"\nSex:",self.sex,"\nProfession:",self.profession)

    #Behavior(instance methods)
    def work(self):
        print(self.name,"working as ",self.profession)

#create object of class
sagar=Person("Sagar","Male","Software Engineer")

#call methods
sagar.show()
sagar.work()
