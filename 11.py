# Find the Largest Digit in a Number

n=int(input("enter number: "))
n=str(n)
s=0
for i in n:
  i=int(i)
  if i>s:
      s=i
print(s)