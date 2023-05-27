"""def iterFact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def recurFact(n):
    if n<=1:
        return 1
    else:
        return n*recurFact(n-1)"""
def printOutSomeNums(n):
    if n==0:
        pass
    else:
        print(n)
        printOutSomeNums(n-1)
    return 0
print(printOutSomeNums(10))

