import math

while True:
    print("Program to find the Roots of a Quadratic Equation")
    print("Sample: a(x^2) + b(x) + c \n")

    a = float(input("Enter the coefficient value, a: "))
    b = float(input("Enter the coefficient value, b: "))
    c = float(input("Enter the constant value, c: "))
    print()
    print("Equation: ", a,"(x^2) + ",b,"(x) + ",c,"\n")
    d = b**2 - 4*a*c
    if d>0:
        r1 = (-b + math.sqrt(d))/ 2*a
        r2 = (-b - math.sqrt(d))/ 2*a
        print("The given equation has two real roots, ",r1, "and", r2)
    elif d==0:
        r = -b/2*a
        print("The given equation has two same real roots, ",r)
    else:
        print("The given equation has no real roots.")

    cond = input("Do you want to continue? (Y/N)  ")
    print()
    if cond not in "Yy":
      print(" \nThanks for using this program... \nMade by Devansh Tyagi")
      break
