class Mobile:
    def __init__(self):
        self.model="Realme X"

    def show_model(self,p):
        self.price=p
        print(("Model:",self.model,"Price:",self.price))

realme=Mobile()
realme.show_model(25000)