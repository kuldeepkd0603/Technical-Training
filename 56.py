#  Print All Prime Numbers Between 1 and 100
import math
def prime_number():
    prime_list = []
    for i in range(2, 101):
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

print(prime_number())
