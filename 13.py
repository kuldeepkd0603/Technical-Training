# 13. *Sum of Digits of a Number*
n=int(input("enter number"))
sum=0
n=str(n)
for i in n:
    i=int(i)
    sum=sum+i
print(sum)