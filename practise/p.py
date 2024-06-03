def average(l1):
  sum=0
  count=0
  for i in range(len(l1)):
    if l1[i]!=-999:
      sum+=l1[i]
      count+=1
  avg=sum/count
  return avg
def highest(l1):
  for i in range(len(l1)):
    if l1[i]!=-999:
      Max=l1[0]
      break
  for i in range(1,len(l1)):
    if l1[i]>Max:
      Max=l1[i]
  return Max
def lowest(l1):
  for i in range(len(l1)):
    if l1[i]!=-999:
      Min=l1[0]
      break
  for i in range(1,len(l1)):
    if l1[i]<Min:
      Min=l1[i]
  return Min
#main
marksinFDS=[]
n=int(input("Enter the number of students:"))
print("Enter the marks of",n,"students:")
for i in range(0,n):
  ele=int(input())
  marksinFDS.append(ele)
print("List of marks:")
print(marksinFDS)
print("Average score:",average(marksinFDS))
print("Highest score:",highest(marksinFDS))
print("Lowest score:",lowest(marksinFDS))
