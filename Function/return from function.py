def is_even(list1):
    even_num=[]
    for n in list1:
        if n%2==0:
            even_num.append(n)
    #return list
    return even_num

#pass list to the function
even_num=is_even([2,3,42,51,62,70,5,9])
print("Even number are:",even_num)