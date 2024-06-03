import re
str="simplilearn tutorial"
x=re.findall("[agh]",str)
print(x)
if(x):
    print("Match found")
else:
    print("No match")