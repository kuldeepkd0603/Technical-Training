# 25	Print a Hollow Square Pattern of Stars	Intermediate
for i in range(5):
    for j in range(5):
        if i==0 or i==4:
            print("*",end=" ")
        elif j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()