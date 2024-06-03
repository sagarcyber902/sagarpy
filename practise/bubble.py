#Bubble sort
def Bubble_Sort(marks):
    for i in range(len(marks)-1):
        for j in range(0,len(marks)-1):
            if marks[j]>marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]
    print("Marks of students after performing Bubble Sort on the list :")
    print(marks)
#main
marks=[]
n = int(input("Enter number of students: "))
print("Enter marks for",n,"students:")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)
print("The marks of",n,"students are : ")
print(marks)
Bubble_Sort(marks)

