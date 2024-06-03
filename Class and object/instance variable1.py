#instance variable
class Mobile:
    def __init__(self):
        self.model="Realme X";       #instance variable

    def show_model(self):            #instance method
        print(self.model)            #accessing instance variable

realme=Mobile()
redmi=Mobile()
geek=Mobile()

print("Realme:",realme.model)
print("Redmi:",redmi.model)
redmi.model="redmi 7s"              #modifying instance variable
print("Realme:",realme.model)
print("Redmi:",redmi.model)

