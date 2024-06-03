import re

str="hello"
#find hello in the str with start he followed by two letter and end with o
x=re.findall("he..o",str)
print(x)