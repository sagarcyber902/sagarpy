import re

str="hello"

#find hello in str
x=re.findall("^hello",str)
if(x):
    print("Match found")
else:
    print("No match")