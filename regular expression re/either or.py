#check either or condition
import re
str="python simpilearn tutorial"
x=re.findall("python|tutorial",str)
if(x):
    print("Match found")
else:
    print("No match")