print("Check the type of Input\n")

while True:
    n = input("Enter the Input text: ")
    if n.isalpha():
      print("The input is a Letter.")
    elif n.isdigit():
      print("The input is a Number.")
    elif n.isalnum():
      print("The input is Alpha-Numeric.")
    else:
      print("The input is a Special Character.")
      
    cond = input("Do you want to continue? (Y/N)  ")
    print()
    if cond not in "Yy":
      print(" \nThanks for using this program... \nMade by Devansh Tyagi")
      break
