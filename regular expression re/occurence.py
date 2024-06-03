#returns the zero or more occurrences of a character in a string
import re
str="This is python simplilearn tutorial"
x=re.findall("This*",str)
if(x):
    print("Match found")
else:
    print("No match")