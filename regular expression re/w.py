#sequence returns a match at every word character
import re
str="python simplilearn tutorial"
x=re.findall("\w",str)
print(x)
if(x):
    print("Match found")
else:
    print("No match")