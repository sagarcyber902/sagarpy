x=5
def function1():
    print("Value in 1st function",x)

def function2():
    #modify global variable using global keyword
    global x
    x=555
    print("Value in 2nd function:",x)

def function3():
    print("Value in 3rd function:",x)

function1()
function2()
function3()