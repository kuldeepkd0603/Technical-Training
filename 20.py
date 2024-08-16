# 20. *Generate Fibonacci Series up to N Terms*
fibo=[0,1]
n=int(input("enter number ; "))

for i in range(1,n):
    fibo.append(fibo[i]+fibo[i-1])
print(fibo)