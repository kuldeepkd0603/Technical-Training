# Sum of All Even Numbers between 1 and N
n=int(input("enter number :"))
sum=0
for i in range(n):
    if i%2==0:
        print(i)
        sum=sum+i
    else:
        pass
print(sum)
