def check_Eligibility(n):
    if n<=1:
        print("Sorry")
        return False
    if n ==2:
        print("Proceed for printing")
        return True
    if n>2 and n<29:
        for i in range(3,n):
            if n%i==0:
                print("Sorry")
                return False
        print("Proceed for Printing")
        return True

def displayPattern(n):
    check_Eligibility(n)
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    s = " "
    d = "*"
    x = 1
    y = n
    if check_Eligibility(n) == True:
        for i in range(n):
            if i == 0:
                print(s*y, alpha[i])
            else:
                print(s*y, alpha[i], d*x, alpha[i])
                x += 2
            y -= 1

displayPattern(7)
            