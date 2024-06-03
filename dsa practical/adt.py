
def hash_function(keys):
    return keys%n
def display_list(list):
    for i in range(n):
        print(i,"->",list[i])

n=int(input("Enter the width database:"))
values=int(input("enter the values t be entered:"))
list=[[] for i in range(n)]
for i in range(n):
    keys=int(input("Enter the keys"))
    value=int(input("Enter the values:"))
    index=hash_function(keys)
    temp=[]
    temp.append(keys)
    temp.append(value)
    list[index].insert(index,temp)
display_list(list)

