print("Find the frequency of a character in a given String\n")
str = input("Enter the string: ")
char = input("Enter the character: ")
count = 0
for i in range(len(str)):
    if char == str[i]:
        count += 1
    else:
        continue
print()
print(count)
print(" \nThanks for using this program... \nMade by Devansh Tyagi")