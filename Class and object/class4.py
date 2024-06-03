class Mobile:
    def __init__(self):
        self.model="Realme X"

    def show_model(self):
        price=25000                #local variable
        print("Model:",self.model,"Price:",price)

realme=Mobile()

#accessing method from outside class
realme.show_model()