# Print All Palindrome Numbers Between 1001 and 9999
def Palindrome():
    Pali_list=[]
    for i in range(1000,10000):
        i=str(i)
        if i == i[::-1]:
            Pali_list.append(i)
        else:
            pass
    return Pali_list
print(Palindrome())