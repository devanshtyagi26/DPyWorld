
print("Program to check whether the number is Prime. \n")


while True:
    n = int(input("Enter the number: "))
    if n<1:
        print("Enter a positive natural number")
    else:
        if n>1:
            for i in range(2,n):
                if n%i == 0:
                    print("The number is not Prime.")
                    break
            else:
                print("The number is prime.")
        else:
            print("The number is not Prime.")
    cond = input("Do you want to continue? (Y/N)  ")
    print()
    if cond not in "Yy":
      print(" \nThanks for using this program... \nMade by Devansh Tyagi")
      break