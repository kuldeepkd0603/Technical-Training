# Convert a Decimal Number to Hexadecimal
def decimal_hexadecimal(n):
    binary_number=""
    hex_digits="0123456789ABCDEF"
    while n>0:
        remainder=n%16
        binary_number= hex_digits[remainder]+binary_number
        n=n//16
    return binary_number
    
print(decimal_hexadecimal(254))