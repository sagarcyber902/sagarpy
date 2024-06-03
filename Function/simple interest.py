def simple_interest(p,t,r):
    return (p*t*r)/100

p=float(input("Enter the principle amount:"))
r=float(input("Enter the rate:"))
t=float(input("Enter the time in year:"))

print("The simple interest is:",simple_interest(p,t,r))