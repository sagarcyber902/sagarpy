n=int(input("Enter number of rows:"))
for i in range(n,0,-1):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(1,i+1):
            print("*",end=" ")
    print("\r")