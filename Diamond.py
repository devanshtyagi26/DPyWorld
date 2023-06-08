def Diamond():
    n = int(input("Enter the length: "))
    x = n
    y = 1
    if n%2==0:
        s=int(n/2)
        t = int(n/2)
    else:
        s = int(n/2)
        t = int(n/2)+1
    for i in range(s):
        print(" "*x, "*"*y)
        x -=1
        y +=2
    for i in range(t):
        print(" "*x, "*"*y)
        x +=1
        y -=2       
Diamond()