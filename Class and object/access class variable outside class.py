#class variable or static variable with class method
class Mobile:
    fp="Yes"                  #class variable

    def __init__(self):
        self.model="Realme X"                  #instance method

    def show_model(self):                      #instance method
        print("Model:",self.model)             #accessing instance method

    @classmethod
    def is_fp(cls):
        print("Finger print:",cls.fp)           #accessing class variable

realme=Mobile()
realme.show_model()
Mobile.is_fp()
Mobile.fp="No"                                 #accessing class variable outside class method
Mobile.is_fp()