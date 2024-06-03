class Add:
    def result(self,a,b):
        print("Addition",a+b)

class Multi(Add):
    def result(self,a,b):
        print("Multiplication",a*b)

obj=Multi()
obj.result(10,20)