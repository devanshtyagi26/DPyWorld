print("Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’\n")
f = open(r"file.txt", "r")
line = f.readlines()

File1 = open(r"File1.txt", "w")
File2 = open(r"File2.txt", "w")
for i in range(len(line)):
    if (i+1) %  2 == 0:
        File1.writelines(line[i])
    else:
        File2.writelines(line[i])

f.close()
File1.close()
File2.close()

print(" \nThanks for using this program... \nMade by Devansh Tyagi")