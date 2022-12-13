print("DOWNWARD PYRAMID\n")

t= int(input("Enter the length of Downward Pyramid: "))
s = " "
d = "* "
m=0
for i in range(t):
  print(m*s,t*d)
  t -= 1
  m += 1
print(" \nThanks for using this program... \nMade by Devansh Tyagi")