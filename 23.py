#23	Print a Pyramid Pattern of Stars
for i in  range(5):
    
    for j in range(i,5):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()