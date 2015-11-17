def whileloop_factorial(w):
    if (w == 0):
        return 1
    result = m
    i = w-1
    while (i>=1):
        result = result * i
        i -= 1
    return result


run = True
while (run):
    m = int(input("Please enter a non negative integer: "))
    factorial = whileloop_factorial(m)
    print(factorial)

    answer = input("Would you like to try again ? (y/n)")
    if (answer == "n"):
        print("Have a nice day!")
        run = False
