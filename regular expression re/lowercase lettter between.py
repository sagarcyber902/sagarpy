import re

str="The rain in spain"
#finds all lowercase letter between a-p
x=re.findall("[a-p]",str)
print(x)