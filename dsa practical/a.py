a = [-1] * 10
size = 10
option = int(input("1.linear probing\n2.quadratic probing "))
ans = 1
if (option == 1):
    while (ans == 1):
        n = int(input("Enter phone number to be inserted in phonebook:"))
        loc = n % size
        flag = 0
        cnt = 0
        while (flag == 0 and cnt < size):
            if a[loc] == -1:
                a[loc] = n
                flag = 1
            elif cnt > size:
                cnt = 0
            else:
                loc = (loc + 1) % size
                cnt += 1
        ans = int(input("Do u want to add number[1/0]:"))
    for i in a:
        print(i)

    search = int(input("U want to search phone number:"))
    while (search == 1):
        key = int(input("Enter phone number to be searched in phonebook:"))
        loc = n % size
        flag = 0
        cnt = 0
        while (flag == 0 and cnt < size):
            if a[loc] == key:
                print("Phone number is found at " + str(loc))
                flag = 1
                cnt += 1
                break
            else:
                loc = (loc + 1) % size
        search = int(input("do U want to search another phone number[1/0]:"))

else:
    while (ans == 1):
        n = int(input("Enter phone number to be inserted in phonebook:"))
        loc = n % size
        flag = 0
        step = 0
        cnt = 0
        while (flag == 0 and cnt < size):
            loc1 = (loc + step ** 2) % size
            if a[loc] == -1:
                a[loc] = n
                flag = 1
                cnt += 1
            elif cnt > size:
                cnt = 0
            else:
                loc = loc1
                cnt += 1
                step += 1
        ans = int(input("Do u want to add number[1/0]:"))
    for i in a:
        print(i)

    search = int(input("U want to search phone number:"))
    while (search == 1):
        key = int(input("Enter phone number to be searched in phonebook:"))
        loc = n % size
        flag = 0
        cnt = 0
        while (flag == 0 and cnt < size):
            if a[loc] == key:
                print("Phone number is found at " + str(loc))
                flag = 1
                cnt += 1
                break
            else:
                loc = (loc + 1) % size
        search = int(input("do U want to search another phone number[1/0]:"))
