def func():
    l1  = list(input("Enter the list: ").split())
    l2=[]
    for i in l1:
        l2.append(int(i))
    l3 = []
    for i in l2:
        if i not in l3:
            l3.append(i)
    size = len(l3)
    print(l3, size)
func()