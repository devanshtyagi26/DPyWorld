x = 10
'''When x = 10 is executed an integer object 10 is created in memory and its reference is assigned to variable x, this is because everything is object in Python.
'''
y = x
print(id(x))
print(id(y))  
if id(x) == id(y):
    print("\nx and y refer to the same object")
#Here, x and y refer to the same object

#Now, let’s change the value of x and see what happens.
x += 1

print()
print(id(x))
print(id(y))

if id(x) == id(y):
    print("x and y refer to the same object")
else:
    print("x and y do not refer to the same object")
#Here, x and y do not refer to the same object
#So now x refer to a new object x and the link between x and 10 disconnected but y still refer to 10.


def func():  
    # All these variables get memory allocated on stack  
    a = 20
    b = [] 
    c = "" 


# This memory for 10 integers is allocated on heap.  
a = [0]*10
print(a)