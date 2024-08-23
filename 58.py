#  Print All Prime Numbers Between N and M (User Input)
import math
def prime_number(n,m):
    prime_list = []
    for i in range(n, m):
        if i == 2 or i == 3:
            prime_list.append(i)
        else:
            
            is_prime = True
            if i % 2 == 0 or i % 3 == 0:
                is_prime = False
            else:
                for j in range(5, int(math.sqrt(i)) + 1, 6):
                    if i % j == 0 or i % (j + 2) == 0:
                        is_prime = False
                        break
            if is_prime:
                prime_list.append(i)
    return prime_list
n=int(input("enter starting point of prime number"))
m=int(input("enter ending point of prime number"))
print(prime_number(n,m))