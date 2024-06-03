class calculation1:
    def addition(self,a,b):
        return a+b
class calculation2:
    def product(self,a,b):
        return a*b
class derived(calculation2):
    def divide(self,a,b):
        return a/b
d=derived()
print(isinstance(d,calculation1))
