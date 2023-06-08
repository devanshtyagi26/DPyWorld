def fibonacci(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
n=0
def seq(t):
    global n
    print(fibonacci(n), end=" ")
    n+=1
    if n<=t:
        seq(t)

seq(77)