# Generate Fibonacci Series up to N Terms
fibo=[0,1]
n=int(input("enter n th term : "))

for i in range(2,n):
    next=fibo[i-1]+fibo[i-2]
    fibo.append(next)
print(fibo)