def factorial(n):          # recursion function call itself 
    if(n==0 or n==1):     # base condition to stop program
        return 1
    return n * factorial(n-1)  # it is directly use mathematical formula as function
a= factorial(9)
print(a)