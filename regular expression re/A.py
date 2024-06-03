# checks if the string starts with a particular character
import re
str="python simplilearn tutorial"
x=re.findall("\Apython",str)
print(x)
if(x):
    print("Match found")
else:
    print("No match")