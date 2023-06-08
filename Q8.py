def factorial(n):
    if n<=1 and n>=0:
        fact = 1
    elif n<0:
        fact = "Negative Number"
    else:
        fact = 1
        for i in range(1,n+1):
            fact *=i
    return fact

def sum(n):
    s = 0
    for i in range(1,n+1):
        s += ((i)*((2*i)+1))/factorial(i)
    print(s)
sum(5)
s=0
i=1
def Sum(n):
    global s,i
    s += ((i)*((2*i)+1))/factorial(i)
    i +=1
    n-=1
    if n ==0:
        pass
    else:
        Sum(n)
    return s
print(Sum(5))