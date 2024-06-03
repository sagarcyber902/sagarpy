class Mobile:
    #constructor
    def __init__(self,m):
        self.model=m

    def show_model(self,p):
        price=p
        print("Model:",self.model,"Price:",price)

realme=Mobile("Realme X")
realme.show_model(25000)
print(id(realme))

redmi=Mobile("Redmi 7s")
redmi.show_model(12000)
print(id(realme))

geek=Mobile("Python")
geek.show_model(49)
print(id(geek))