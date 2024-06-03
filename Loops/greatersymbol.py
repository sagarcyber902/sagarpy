n=int(input("Enter number of rows:"))
for i in range(1,n):
    print()
    for j in range(1,i+1):
        print("*",end=" ")
for i in range(n,0,-1):
    print()
    for j in range(1,i+1):
        print("*",end=" ")
