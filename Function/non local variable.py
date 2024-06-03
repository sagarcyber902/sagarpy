def outer_func():
    x=777
    def inner_func():
        #local variable now acts as global variable
        nonlocal x
        x=700
        print("Value of x inside inner function:",x)

    inner_func()
    print("Value of x inside outer function:",x)

outer_func()
