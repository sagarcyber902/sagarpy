x=int(input("Enter the marks:"))
if x>90 and x<=100:
    print("You scored A Grade")
elif x>80 and x<=90:
    print("You scored B Grade")
elif x>60 and x<=80:
    print("You scored C Grade")
elif x>40 and x<=60:
    print("You scored D Grade")
else:
    print("Sorry you have failed")