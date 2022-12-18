print("Remove the first occurrence of a character from a string\n")
str = input("Enter the string: ")
char = input("Enter the character you want to remove: ")
str1 = ""
n = 0
for i in range(len(str)):
    if char == str[i] and n==0: 
        n += 1
    else:
        str1 += str[i]
print()
print(str1)
print(" \nThanks for using this program... \nMade by Devansh Tyagi")