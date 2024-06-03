#quick sort
def quicksort(l1,left,right):
    if left<right:
        partition_pos=partition(l1,left,right)
        quicksort(l1,left,partition_pos-1)
        quicksort(l1,partition_pos+1,right)
#partition
def partition(l1,left,right):
    i=left
    j=right-1
    pivot=l1[right]
    while i<j:
        while i<right and l1[i]<pivot:
            i+=1
        while j>left and l1[j]>=pivot:
            j-=1
        if i<j:
            l1[i],l1[j]=l1[j],l1[i]
    if l1[i]>pivot:
        l1[i],l1[right]=l1[right],l1[i]
    return i
#main
perc=[]
n=int(input("Enter the number of students:"))
print("Enter marks of",n,"students:")
for i in range(0,n):
    ele=int(input())
    perc.append(ele)
print("Unsorted percentage of students:")
print(perc)
quicksort(perc,0,len(perc)-1)
print("Sorted percentage  using quick sort:")
print(perc)
print("Top five score:")
top=(perc[-5:n])
print(top[::-1])