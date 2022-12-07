print("UPWARD PYRAMID\n")

t= int(input("Enter the length of Upward Pyramid: "))
s = " "
d = "* "
n=t+1
m=1
for i in range(t):
  print(n*s,m*d)
  n -= 1
  m += 1
print(" \nThanks for using this program... \nMade by Devansh Tyagi")
