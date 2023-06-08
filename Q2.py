str1 = "Ronald Brown"
str2 = "Richard Brown"
str3 = "Harry/* Potter% is ^a fictional !! character-&"

def append_Strings():
    str4 = str1 + str2

    print(str4)
    a = ""
    b = ""
    for i in str4:
        if i.islower():
            a += i
        else:
            b += i
    a = a+b
    print(a)
    n = 0
    for i in range(len(str4)):
        if "row" == str4[i:i+3]:
            n += 1
    print(n)




append_Strings()
c = ""
for i in str3:
    if i.isalnum() or i.isspace():
        c += i
print(c)

