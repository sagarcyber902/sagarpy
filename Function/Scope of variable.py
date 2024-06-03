def calculate(*sagar):
    sum=0
    for i in sagar:
        sum=sum +1
    print("The sum is",sum)
sum=0
calculate(10,20,40)
print("Value of sum outside the function:",sum)