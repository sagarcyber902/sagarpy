#open the file.txt in read mode.causes an error if no such file exists

fileptr=open("sagar.txt","r")

#running a for loop
for i in fileptr:
    print(i)  #i contains each line of the line
