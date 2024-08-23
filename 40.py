# Find the Sum of the Series 1 + 1/2 + 1/3 + ... + 1/N
def sum_series(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+1/i
    return  sum
print(sum_series(10))