#reading the file

#open the file in read mode
fileptr=open("sagar.txt","r")

#stores the data of the file in variable name content
content=fileptr.read()

#print the type of the data
print(type(content))

#print the content of file
print(content)

#closing the file
fileptr.close()