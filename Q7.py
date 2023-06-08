n = "My name is Jessa"
list = n.split()
for i in range(len(list)):
        list[i] = list[i][::-1]
n = " ".join(list)
print(n)