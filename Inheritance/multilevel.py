class Animal:
    def speak(self):
        print("The dog is black")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
class Dogchild(Dog):
    def eat(self):
        print("The dog eat non-veg")
d=Dogchild()
d.speak()
d.eat()
d.bark()