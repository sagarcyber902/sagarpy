n=int(input("Enter number of rows:"))
for i in range(1,n):
    for k in range(1,n-i):
        print(" ",end=" ")
    for j in range(1,(2*i-1)+1):
            print("*",end=" ")
    print("\r")