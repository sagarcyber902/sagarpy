def greet(botname, year):
    print("Hello dear this is me {0}!".format(botname))
    print("I was crerated in {0}!".format(year))


def remind_name():
    print("\n\ncan u plaase enter your name to remind me:")
    name = input("name: ")
    print("HEY {0}! welcome to TechBot".format(name))


def guess_age():
    print("\nlet me guess ur age")
    print("enter a remainder by dividing your age with 3,5,7\n")
    rem3 = int(input("remainder using 3: "))
    rem5 = int(input("remainder using 5: "))
    rem7 = int(input("remainder using 7: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your AGE is {0} : ".format(age))


def count():
    print("\nenter a no for even or odd:")
    num = int(input())
    if (num % 2 == 0):
        print("Even")
    else:
        print("Odd")


def test():
    print("Answer the following question correctly")
    print("Q1. Which Data structure is used by DFS ?")
    print('1. Queue')
    print('2. Stack')
    print('3. vector')
    print('4. dectionary')
    R_ans = 2
    ans = int(input("Enter right option no.: "))
    while ans != R_ans:
        print("Please, try again")
        ans = int(input("Enter right option no.: "))
    print("Congrats its a right ans")

    print("Q1. Which Data structure is used by BFS ?")
    print('1. Queue')
    print('2. Stack')
    print('3. vector')
    print('4. dectionary')
    R_ans = 1
    ans = int(input("Enter right option no.: "))
    while ans != R_ans:
        print("Please, try again")
        ans = int(input("Enter right option no.: "))
    print("Congrats its a right ans")


def end():
    print("-------------------------")
    print("-------------------------")
    print("-------------------------")
    print("Have A Good Day")
    print("-------------------------")
    print("-------------------------")
    print("-------------------------")
    print("have A good Day")


greet('techbot', '2024')
remind_name()
guess_age()
count()
test()
end()
