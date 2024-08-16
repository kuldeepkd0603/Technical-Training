# 15. *Check if a Number is Palindrome*
n=input("enter value : ")
n=str(n)
if n==n[::-1]:
    print("yes")
else:
    print("no")