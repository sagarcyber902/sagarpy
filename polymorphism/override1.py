class Animal:
    def Eat(self):
        print("Eating")
class Dog(Animal):
    def speak(self):
        print("Barking")
obj=Dog()
obj.speak()