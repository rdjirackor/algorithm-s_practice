def checkIfPrime(num):
    factors=[]
    for i in range(2,num):
        if num%i==0:
            factors.append(i)
            
    if len(factors)==0:

        return True
    return False
        
        

def allprimes(num):
    list_of_all_primes=[]
    for i in range(2,num+1):
        if checkIfPrime(i)==True:
            list_of_all_primes.append(i)
    return list_of_all_primes

def filter(limit):
    list_of_primes=[]
    multiples=[]
    for i in range(1,limit+1):
        if checkIfPrime(i)==True:
            for j in range(1,limit+1):
                if j%i==0:
                    multiples.append(i)
#Confused on why i am doing this