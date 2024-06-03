class Mobile:
    def __init__(self):
        self.model="Realme X"

    def show_model(self):
        print("Model:",self.model)

#creating object of class
realme=Mobile()

#accessing variable from outside the class
print(realme.model)

#assign variable a new value
realme.model="Realme Pro 2"
print(realme.model)

#accessing method from outside class
realme.show_model()