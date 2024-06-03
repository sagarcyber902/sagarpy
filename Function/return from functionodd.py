def is_odd(list1):
    odd_num=[]
    for n in list1:
        if n%2!=0:
            odd_num.append(n)
    #return list
    return odd_num

#pass list to the function
odd_num=is_odd([2,3,42,51,62,70,5,9])
print("Odd number are:",odd_num)