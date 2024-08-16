# Find the Smallest Digit in a Number*
n=int(input("enter number: "))
s=n
n=str(n)

for i in n:
  i=int(i)
  if i<s:
      s=i
print(s)