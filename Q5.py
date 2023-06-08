n = "NAMDAN"
j = -1
print(n[1])
for i in range(int(len(n)/2)):
    if n[i]!=n[j]:
        print("Not a Palindrome")
        break
    j -=1
        
else:
    print("Palindrome")