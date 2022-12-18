f = open(r"file.txt", "r+")
print("Print the total number of characters, words and lines in the file\n")
char = f.read()
word = 1
for i in range(len(char)):
    if char[i] == " ":
        word += 1

f.seek(0)
line = f.readlines()
print(char)
print("\n\n\n")
print("Number of characters:", len(char))
print("Number of lines:", len(line))
print("Number of words:", word)
f.close()