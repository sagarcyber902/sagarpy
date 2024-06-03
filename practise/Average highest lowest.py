#AVERAGE MARKS
def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    return(avg)
#MAXIMUM MARKS
def highest(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max)
#MINIMUM MARKS
def lowest(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)
#MAIN
marksinFDS=[]
numberofstudents=int(input("Enter the number of students:"))
for i in range(numberofstudents):
    marks=int(input("Enter the marks of students :"))
    marksinFDS.append(marks)
print("The Average marks of students:",average(marksinFDS))
print("The highest marks of students:",highest(marksinFDS))
print("The lowest marks of students:",lowest(marksinFDS))