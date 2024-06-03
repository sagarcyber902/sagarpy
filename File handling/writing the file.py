#writing the file

#open the file.txt to append.create a new file if no such file exist
fileptr=open("sagar.txt","w")

#appending the content to the file
fileptr.write("Python is the modern day language.It makes things so simple")
#closing the opened file
fileptr.close