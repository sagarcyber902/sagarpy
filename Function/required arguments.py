#Required Arguments

#the argument name is the required argument to the function
def func(name):
    message="Hii "+name
    return message
name=input("Enter the name:")
print(func(name))