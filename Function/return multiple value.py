def arithmatic(num1,num2):
    add=num1+num2
    sub=num1-num2
    multiply=num1*num2
    divison=num1/num2
    #return four values
    return add,sub,multiply,divison

#read four return values in four variables
a,b,c,d=arithmatic(10,2)
print("Addition:",a)
print("Substarction:",b)
print("Multiplication:",c)
print("Division:",d)