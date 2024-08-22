#  Calculate the Power of a Number Using  loops

def power(num,exponent):
    result=1
    for i in range(exponent):
        result=result*num
    return result
    
print(power(5,2))