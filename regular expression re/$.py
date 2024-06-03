#find string at end
import re
str="python learn tutorial"
x=re.findall("tutorial$",str)
if(x):
    print("Match found")
else:
    print("No match")
