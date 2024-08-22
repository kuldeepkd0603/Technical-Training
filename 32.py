# nCheck if a Number is a Strong Number
num=int(input("enter number to check number is strong number ot not: "))

def factorial(n):
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    return sum

    
def is_strong_num(num):
    num=str(num)
    
    fac_sum=0
    for j in num:
        fac_sum=fac_sum+factorial(int(j))
    num2=int(num)
    return fac_sum==num2

if is_strong_num(num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")
    
        