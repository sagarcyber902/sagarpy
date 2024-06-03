#The \s sequence returns a match when the string contains white space characters
import re
str="python simplilearn tutorial"
x=re.findall("\s",str)
print(x)
if(x):
    print("Match found")
else:
    print("No match")