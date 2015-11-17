#For loop method

def forloop_factorial(m):
    if (m == 0):
        return 1
    result = m
    for i in range(1,m):
        result = result * i
    return result

run = True
while (run):
    m = int(input("Please enter a non negative integer: "))
    factorial = forloop_factorial(m)
    print(factorial)

    answer = input("Would you like to try again ? (y/n)")
    if (answer == "n"):
        print("Have a nice day!")
        run = False
