def fibonacci(n):
    if n==0: return 0
    if n<0: return int(((-1)**(n+1))*fibonacci(abs(n)))
    v1=0
    v2=1
    for i in range(n-1):
        v1 = v2+v1
        v1,v2 = v2,v1
    return v2


print('In mathematics, the Fibonacci numbers, commonly denoted Fₙ, \n\
form a sequence, called the Fibonacci sequence, such that each \n\
number is the sum of the two preceding ones, starting from 0 and 1, for n≥1.')

try:
    n = int(input("Enter number N: "))
    print("Ans:", fibonacci(n))
except:
    print("Invalid Input")
