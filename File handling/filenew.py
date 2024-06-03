#open the sagar.txt in the read mode
fileptr=open("sagar.txt","r")

print(fileptr)

if fileptr:
    print("file created successfully")

#using with statement with rules
with open("ddd.txt","r") as f:
    content=f.read()
    print(content)