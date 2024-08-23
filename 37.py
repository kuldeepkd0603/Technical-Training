def decimal_binary(n):
    binary_number=""
    while n>0:
        remainder=n%2
        binary_number=str(remainder)+binary_number
        n=n//2
    return binary_number
    
print(decimal_binary(10))