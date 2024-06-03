l=[]
n=int(input("Enter the number of elements in the list"))
for i in range(0,n):
    l.append(input("Enter the iteam:"))
    print("printing the list items")
    for i in l:
        print(i,end=" ")