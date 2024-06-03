#check if there are any digit in the given string
import re
str="python simplilearn tutorial"
x=re.findall("\d",str)
print(x)
if(x):
    print("Match found")
else:
    print("No match")