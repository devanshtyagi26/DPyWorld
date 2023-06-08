def searchKey(inList, key):
    for i in inList:
        if i==key:
            print(inList.index(i))
    else:
        print("-1")

            

    
inList=[10,4,5,-7,23]
key = -7  
searchKey(inList, key)