print("Check for Upper or Lower Case\n")

while True:
    n = input("Enter the Input text: ")
    if n.isalpha():
      print("The input is a Letter.")
      if n.isupper():
          print("The letter is in Upper Case.")
      elif n.islower():
          print("The letter is in Lower Case.")
      else:
          print("The letter has Mixex Cases.")
          
    else:
      print("The input is not a Letter.")

    print()
    cond = input("Do you want to continue? (Y/N)  ")
    print()
    if cond not in "Yy":
      print(" \nThanks for using this program... \nMade by Devansh Tyagi")
      break