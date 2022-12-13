print("Remove all occurrences of a character from a string\n")
str = input("Enter the string: ")
char = input("Enter the character you want to remove: ")
str1 = ""
for i in range(len(str)):
    if char == str[i]: 
        continue
    else:
        str1 += str[i]
print()
print(str1)
