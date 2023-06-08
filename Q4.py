Dict1 = {'BMW' :5, 'Mercedes': 10, 'Volkswagen': 10, 'Jaguar': 4, 'Landrover':15}

Tuple1 = (11,22,33)
Tuple2 = (99,88,77)

def Model(n,m):
    if m in n:
        print(n[m])
    else:
        print("-1")

def Change(n,m):
    if m in n:
        if n[m]<5:
            n.remove(m)
        else:
            n[m] -= 2

Model(Dict1, "BMW")
Change(Dict1, "BMW")

def Div3and5():
    tup = tuple(input("Enter the tuple with 10 elements: ").split())
    s3 =0
    s5 =0
    s3n5 =0
    print(tup)
    if len(tup)!=10:
        print("There should be 10 elements")
    else:
        for i in tup:
            if int(i)%3==0:
                s3 += int(i)
        for i in tup:
            if int(i)%5==0:
                s5 += int(i)
        for i in tup:
            if int(i)%3==0 and int(i)%5==0:
                s3n5 += int(i)
    print(s3)
    print(s5)
    print(s3n5)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
for i in set1:
    if i in set2:
        print(i, end=" ")
set3 = []
for i in set1:
    if i not in set2:
        set3 += i
for j in set2:
    if j not in set1:
        set3 += j
set3 = set(set3)
print(set3)


