#  Convert a Decimal Number to Octal
def decimal_octal(n):
    binary_number=""
    while n>0:
        remainder=n%8
        binary_number=str(remainder)+binary_number
        n=n//8
    return binary_number
    
print(decimal_octal(83))