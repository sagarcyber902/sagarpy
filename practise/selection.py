#selection sort
def Selection_Sort(marks):
    for i in range(len(marks)):
        min_idx = i
        for j in range(i+1,len(marks)):
            if marks[min_idx]>marks[j]:
                min_idx=j
        marks[i],marks[min_idx]=marks[min_idx],marks[i]
    print("Marks of students after performing Selection Sort on the list : ")
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
Selection_Sort(marks)
