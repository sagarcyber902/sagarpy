class calculation1:
    def addition(self,a,b):
        return a+b
class calculation2:
    def product(self,a,b):
        return a*b
class derived(calculation1,calculation2):
    def divide(self,a,b):
        return a/b
d=derived()
print(d.addition(10,20))
print(d.product(10,20))
print(d.divide(10,20))

