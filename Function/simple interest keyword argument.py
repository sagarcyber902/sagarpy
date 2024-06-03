#keyword arguments

#function func is called with the name and message as the keyword arguments
def func(name,message):
    print("printing the message with",name,"and",message)
func(name="Sagar",message="Hii")

def simple_interest(p,t,r):
    return (p*t*r)/100
print("Simple Interest:",simple_interest(p=1900,t=10,r=10))