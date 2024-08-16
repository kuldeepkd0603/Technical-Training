# . *Check if a Number is an Armstrong Number*
n=int(input("enter number"))
n=str(n)
sum=0
cube_sum=0
for i in n:
    i=int(i)
    cube_sum=cube_sum+i**3
n=int(n)
if n==cube_sum:
    print("number is Armstrong")
else:
    print("number is not armstrong")
