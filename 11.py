# Find the Largest Digit in a Number
n=int(input("enter number: "))
if n>=0 and n>=10:
    print(n)
else:
    for i in len(n):
        n=n//10
        
        