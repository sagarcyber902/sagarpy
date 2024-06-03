num=65
#outer loop to handle number of rows
#5 in this case
for i in range(0,5):

    # inner loop to handle number of column
    #values changing acc. to outer loop
    for j in range(0,i+1):
        #explicitily converting to char
        ch=chr(num)

        #printing char value
        print(ch,end="")

        #incrementing number
        num=num+1
    #editing line after each row
    print("\r")