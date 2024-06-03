n= 5
print("* ", end="")
for i in range(1, n - 1):
    print("  ", end="")
for i in range(1, n + 1):
    print("* ", end="")
print("\r")
for i in range(1, n - 1):
    print("* ", end="")
    for j in range(1, n - 1):
        print("  ", end="")
    print("*")
for i in range(1, n + n):
    print("* ", end="")
print("\r")
for i in range(1, n - 1):
    for j in range(1, n):
        print("  ", end="")
    print("* ", end="")
    for j in range(1, n - 1):
        print("  ", end="")
    print("* ")
for i in range(1, n + 1):
    print("* ", end="")
for i in range(1, n - 1):
    print("  ", end="")
print("* ")