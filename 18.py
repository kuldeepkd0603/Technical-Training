# 18. *Find the GCD of Two Numbers*
n1=int(input("enter nu,ber 1 : "))
n2=int(input("enter number 2 : "))

for i in range(1,10):
    if n1%i==0 and n2%i==0:
        print(i)