#initialising starting number
num=1
#outer loop to handle number of rows
for i in range(0,5):

    # not re assigning num
    # num=1

    #inner loop to handle number of column
    #values changing acc. to outer loop
    for j in range(0,i+1):
        #printing number
        print(num,end=" ")

        #incrementing number at each column
        num=num+1
    #endling line after each row
    print("\r")