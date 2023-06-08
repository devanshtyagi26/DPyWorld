f = open(r"Poem.txt", "r")
file = f.read()
alphabets = 0
blank_spaces = 0
lower = 0
upper = 0
vowel = 0
occur = {}
for i in file:
    if i!=" ":
        alphabets +=1
    else:
        blank_spaces +=1
f.seek(0)
for i in file:
    if i.islower():
        lower +=1
    elif i.isupper():
        upper +=1
f.seek(0)
file = f.readline().split()
for i in file:
    if i[0] in 'aeiouAEIOU':
        vowel +=1
f.seek(0)
file = f.readline().split()
for i in file:
    if i not in occur:
        occur[i]=1
    else:
        occur[i] +=1

print(alphabets)
print(blank_spaces)
print(lower)
print(upper)
print(vowel)
print(occur)