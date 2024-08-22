# 24	Print a Diamond Pattern of Stars	Intermediat
for i in  range(5):
    
    for j in range(i,5):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')    
    print()
for i in  range(5,-1,-1):
    
    for j in range(i,5):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()