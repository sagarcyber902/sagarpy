def printme(*names):
    print("type of passed argument is:",type(names))
    print("printing the passed arguments...")
    for name in names:
        print(name)
printme("Sagar","Sushant","Tejas","Kedar")