class Mobile:
    def __init__(self):
        self.model="Realme X"

    def get_model(self):
        return self.model

realme=Mobile()
m=realme.get_model()
print(m)