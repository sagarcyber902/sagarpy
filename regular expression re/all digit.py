import re

str="this is  59 dollar "
#find all digits in string
x=re.findall("%D",str)
print(x)