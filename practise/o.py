#union
def union(l1,l2):
    l3=l1.copy()
    for i in l2:
        if i not in l3:
            l3.append(i)
    return l3
#intersection
def intersection(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

#differenece
def diff(l1,l2):
    l3=[]
    for i in l1:
        if i not in l2:
            l3.append(i)
    return l3

#symdiff
def symdiff(l1,l2):
    l3=[]
    d1=diff(l1,l2)
    d2=diff(l2,l1)
    l3=union(d1,d2)
    return l3

#play both cricket and badminton
def CB(l1,l2):
   l3=intersection(l1,l2)
   return l3

#play either cricket or badminton but not both
def eCB(l1,l2):
    l3=symdiff(l1,l2)
    return l3

#neither cricket nor badminton
def nCnB(l1,l2,l3):
    l4=diff(l1,union(l2,l3))
    return l4

#play cricket and football but not badminton
def CFnB(l1,l2,l3):
    l4=diff(intersection(l1,l2),l3)
    return l4
#main
SEcomp=[]
n=int(input("Enter the number of students in SE computer:"))
print("\nEnter name of",n,"students:")
for i in range(0,n):
    ele=input()
    SEcomp.append(ele)
print("SEComp list:",SEcomp)

cricket=[]
n=int(input("Enter the number of students who play cricket:"))
print("\nEnter name of",n,"students:")
for i in range(0,n):
    ele=input()
    cricket.append(ele)
print("Cricket list:",cricket)

football=[]
n=int(input("Enter the number of students who play football:"))
print("\nEnter name of",n,"students:")
for i in range(0,n):
    ele=input()
    football.append(ele)
print("Football list:",football)

badminton=[]
n=int(input("Enter the number of students in SE computer:"))
print("\nEnter name of",n,"students:")
for i in range(0,n):
    ele=input()
    badminton.append(ele)
print("Badminton List:",badminton)

flag=1
while flag==1:
    print("\n\n---------MENU______________")
    print("1.play both cricket and badminton\n")
    print("2.either cricket or badminton but not both\n")
    print("3.neither cricket nor badminton\n")
    print("4.play cricket and football but not badminton\n")
    print("5.Exit\n")
    ch=int(input("Enter the choice"))
    if ch==1:
        ans=CB(cricket,badminton)
        print(ans)
        a=input("\nDo you want to continue(yes/no)")
        if a=="yes":
            flag=1
        else:
            print("Thanks")
    if ch==2:
        ans=eCB(cricket,badminton)
        print(ans)
        a=input("\nDo you want to continue(yes/no)")
        if a=="yes":
            flag=1
        else:
            print("Thanks")
    elif ch==3:
        ans = nCnB(SEcomp, cricket, badminton)
        print(ans)
        a = input("\nDo you want to continue(yes/no)")
        if a == "yes":
            flag = 1
        else:
            print("Thanks")
    elif ch==4:
        ans=CFnB(cricket,football,badminton)
        print(ans)
        a=input("\nDo you want to continue(yes/no)")
        if a=="yes":
            flag=1
        else:
            print("Thanks")
    elif ch==5:
        print("THanks")
    else:
        print("Invalid chooice")
