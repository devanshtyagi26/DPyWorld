print("Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.\n")
f = open(r"file.txt", "r")
dict ={}
word = f.read()
for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
print(" \nThanks for using this program... \nMade by Devansh Tyagi")