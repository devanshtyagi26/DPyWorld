print("Replace a character by another character in a string\n")
str = input("Enter the string: ")
char = input("Enter the character: ")
rep = input("Enter the character to replace with: ")
str1 = ""
for i in range(len(str)):
    if char != str[i]:
        str1 += str[i]
    else:
        str1 += rep
print()
print(str1)
print(" \nThanks for using this program... \nMade by Devansh Tyagi")