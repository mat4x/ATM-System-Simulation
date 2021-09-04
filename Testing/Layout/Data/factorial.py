def factorial(n):
    if n<=0: return 1
    return n*factorial(n-1)


print("In mathematics, the factorial of a non-negative integer n, \n\
denoted by n!, is the product of all positive integers less than or equal to n.\n\
For example, The value of 0! is 1, according to the convention for an empty product.")
    
try:
    n = int(input("Enter number N: "))
    print("Ans:", factorial(n))
except:
    print("Invalid Input")
    
