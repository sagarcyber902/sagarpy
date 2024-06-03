#checks if the string end with particular word
import re
str="python simplilearn tutorial"
x=re.findall("tutorial\Z",str)
print(x)
if(x):
    print("Match found")
else:
    print("No match")