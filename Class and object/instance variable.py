#instance variable with instance method
class Mobile:
    def __init__(self):
        self.model="Realme X";       #instance variable

    def show_model(self):            #instance method
        print(self.model)            #accessing instance variable

realme=Mobile()
realme.show_model()