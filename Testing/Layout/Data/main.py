from Data.factorial import factorial
from Data.fibonacci import fibonacci

print("Select and option\n1) factorial\n2) fibonacci\n")

option=1
while option!=0:
    option = int(input(": "))
    if option == 1:
        n = int(input("N: "))
        print(factorial(n))
    elif option == 2:
        n = int(input("N: "))
        print(fibonacci(n))
    else:
        print("Invalid")
