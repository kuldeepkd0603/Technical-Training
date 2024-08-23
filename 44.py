# Generate Magic Square
def magic_square(n):
    for i in range(n):
        for j in range(n):
            print(j,end=" ")
        print()
print(magic_square(3))