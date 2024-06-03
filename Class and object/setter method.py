class Mobile:
    def __init__(self):
        self.model="Realme X"

    def set_model(self):
        self.model="Realme 9"

realme=Mobile()
#before setting
print(realme.model)
#after setting
realme.set_model()
print(realme.model)