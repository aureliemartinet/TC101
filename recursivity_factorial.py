# Recursivity method

def recursivity_factorial(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    return  n * recursivity_factorial(n-1)

run = True
while (run):
    m = int(input("Please enter a non negative integer: "))
    factorial = recursivity_factorial(m)
    print(factorial)

    answer = input("Would you like to try again ? (y/n)")
    if (answer == "n"):
        print("Have a nice day!")
        run = False
