a = [-1]*10
size = 10
cnt = 0
ans = 1
option = int(
    input("In case of collision, which method would you like to choose?\n1. linear probing.\n2.quadratic probing.\n"))
if (option == 1):
    while (ans == 1):
        key = int(input("Enter the Phone number to be inserted to Phone Book: "))
        loc = key % size
        flag = 0
        # linear probing
        while (flag == 0 and cnt < size):
            if (a[loc] == -1):
                a[loc] = key
                flag = 1
                cnt += 1
                break
            else:
                loc = (loc + 1) % size
        ans = int(input("\nDo u want to insert another Phone Number? [1/0]:"))
    for i in a:
        print(i)

    # linear search
    search = int(input("Do u want to search for any Phone number?[1/0]: "))
    while (search == 1):
        key = int(input("Enter the phone number to be searched for: "))
        loc = key % size
        flag = 0
        cnt1 = 0
        # linear probing
        while (flag == 0 and cnt1 < size):
            if (a[loc] == key):
                print("Phone number found at position " + str(loc))
                flag = 1
                cnt1 += 1
                break
            else:
                loc = (loc + 1) % size
        search = int(input("\nDo u want to search another Phone  Number?[1/0]:"))

else:
    # cnt=0
    # ans=1
    while (ans == 1):
        key = int(input("Enter the Phone number to be inserted: "))
        loc = key % size
        flag = 0
        step = 0

        # quadratic probing
        while (flag == 0 and cnt < size):
            loc_n = (loc + step ** 2) % size
            if (a[loc] == -1):
                a[loc] = key
                cnt += 1
                flag = 1
                break
            else:
                loc = loc_n
                step += 1
        ans = int(input("Do u want to insert another number?[1/0]: "))
    for i in a:
        print(i)

        # search using quadratic probing
    search = int(input("Do u want to search for any element?[1/0]: "))
    step = 0
    while (search == 1):
        key = int(input("Enter the Phone Number to be searched for: "))
        loc = key % size
        flag = 0
        step = 0
        cnt = 0
        # quadratic probing
        while (flag == 0 and cnt < size):
            loc_n = (loc + step ** 2) % size
            if (a[loc] == key):
                print("Phone number found at position " + str(loc))
                cnt += 1
                flag = 1
                break
            else:
                loc = loc_n
                step += 1
        search = int(input("Do u want to search another Phone Number?[1/0]: "))
