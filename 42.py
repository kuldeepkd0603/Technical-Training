#  Print a Hollow Diamond Pattern of Stars
# Print a Hollow Diamond Pattern of Stars
for i in range(5):
    for j in range(i, 5):
        print(" ", end=' ')
    print("*", end=' ')
    for k in range(2 * i - 1):
        print(" ", end=' ')
    if i > 0:
        print("*", end=' ')
    print()

for i in range(3, -1, -1):
    for j in range(i, 5):
        print(" ", end=' ')
    print("*", end=' ')
    for k in range(2 * i - 1):
        print(" ", end=' ')
    if i > 0:
        print("*", end=' ')
    print()
