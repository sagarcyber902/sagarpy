n=int(input("Enter number of rows:"))
for i in range(1,n):
    for k in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
            print("*",end=" ")
    print("\r")
for i in range(n,0,-1):
    for k in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
            print("*",end=" ")
    print("\r")

