t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print("Tuple t1:",t1)
print()
print("Print half the values of the tuple in one line and the other half in the next line.")

print(t1[0:5])
print(t1[5:10])
print()

print("Print another tuple whose values are even numbers in the given tuple.")

t2 = ()
for i in range(len(t1)):
    if t1[i] % 2 == 0:
        t2 += (t1[i],)
    else:
        continue
print(t2)
print()

print("Concatenate a tuple t2=(11,13,15) with t1")

t2 = (11, 13, 15)
t1 += t2
print(t1)
print()

print("Return maximum and minimum value from this tuple")
print("Maximum:",max(t1), "\nMinimum:", min(t1))
print(" \nThanks for using this program... \nMade by Devansh Tyagi")