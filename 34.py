#  Check if a Number is a Perfect Number
#What are Perfect Numbers?
#In number theory, a perfect number is a positive integer that is equal to 
# the sum of its positive divisors, excluding the number itself. Few of the 
# starting Perfect Numbers are 6, 28, 496, 8128, and so on.


def perfect_number(num):
    if num<=0:
        return "number is not perfect number"
    else:
        diviser=[]
        for i in range(1,num):
            if num%i==0:
                diviser.append(i)
        sum=0
        for j in range(len(diviser)):
            sum=sum+diviser[j]
        if num==sum:
            return f"{num} is perfect  number"
        else:
            return f"{num} is not perfect number"
            
        
        
print(perfect_number(28))