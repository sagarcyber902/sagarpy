#union
def union(lst1,lst2):
    lst3=lst1.copy()
    for i in lst2:
        if i not in lst3:
            lst3.append(i)
    return lst3
#intersection
def intersection(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3
#difference
def diff(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i not in lst2:
            lst3.append(i)
    return lst3
#symmetric differnce
def sym_diff(lst1,lst2):
    lst3=[]
    D1=diff(lst1,lst2)
    D2=diff(lst2,lst1)
    lst3=union(D1,D2)
    return lst3
#both cricket and badminton
def CB(lst1,lst2):
    lst3=intersection(lst1,lst2)
    print("\n\nList of students who play both cricket and badminton is : ", lst3)
    return len(lst3)
#either cricket or badminton but not both
def eCeB(lst1,lst2):
    lst3=sym_diff(lst1,lst2)
    print("\nList of students who play either cricket or badminton but not both is : ",lst3)
    return len(lst3)

#main
SEComp = []
n = int(input("\nEnter number of students in SE COMP: "))
print("Enter the names of",n,"students :")
for i in range(0, n):
    ele = input()
    SEComp.append(ele)
print("Original list of students in SEComp : ",(SEComp))

#cricket
Cricket = []
n = int(input("\n\nEnter number of students who play cricket : "))
print("Enter the names of",n,"students who play cricket:")
for i in range(0, n):
    ele = input()
    Cricket.append(ele)
print("Original list of students playing cricket is :",(Cricket))

#football
Football = []
n = int(input("\n\nEnter number of students who play football : "))
print("Enter the name of",n,"students who play football:")
for i in range(0, n):
    ele = input()
    Football.append(ele)
print("Original list of students playing football :",Football)

#badminton
Badminton = []
n = int(input("\n\nEnter number of students who play badminton : "))
print("Enter the name of",n,"students who play badminton (Please press ENTER after entering each students name) :")
for i in range(0, n):
    ele = input()
    Badminton.append(ele)  # adding the element
print("Original list of students playing badminton :",(Badminton))

print("1.Number of students who play both cricket and badminton : ",CB(Cricket, Badminton))
print("2.Number of students who play either cricket or badminton but not both : ",eCeB(Cricket, Badminton))

