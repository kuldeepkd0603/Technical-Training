# Sum of All Odd Numbers between 1 and N
n=int(input("enter number : "))
sum=0
for i in range(n):
    if i%3==0:
        sum=sum+i
    else:
        pass
print(sum)