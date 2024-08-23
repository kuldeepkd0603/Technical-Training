#  Print All Palindrome Numbers Between 100 and 999
def Palindrome():
    Pali_list=[]
    for i in range(100,1000):
        i=str(i)
        if i == i[::-1]:
            Pali_list.append(i)
        else:
            pass
    return Pali_list
print(Palindrome())