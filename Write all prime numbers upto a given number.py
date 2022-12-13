print("All Prime Numbers upto a given number \n")

while True:
    n = int(input("Enter the number: "))
    if n<1:
        print("Enter a positive natural number")
    else:
        for i in range(2,n):
            for j in range(2,i):
                if i%j == 0:
                    break
                else:
                    print(i)
                    break
    cond = input("Do you want to continue? (Y/N)  ")
    print()
    if cond not in "Yy":
      print(" \nThanks for using this program... \nMade by Devansh Tyagi")
      break
