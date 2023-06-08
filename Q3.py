List1= [5,10,15,20,25,30,35]
List2= [10,20,30,40,50,60,70]
List1.append(40)
List2 += List1
l1 = []
def remove_duplicate():

    for i in List2:
        if i not in l1:
            l1.append(i)
remove_duplicate()      
print(List1)
print(List2)
print(l1)