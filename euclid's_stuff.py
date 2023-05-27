def gcd(num1,num2):
    num1=abs(num1)
    num2=abs(num2)
    if (num1)>=num2:
        rem=num1%num2
        if rem ==0:
            return num2
        else:
            num1 = num2 
            num2 = rem
            return gcd(num1, num2)
    else:
        return gcd(num2,num1)

print(gcd(500,30))
        