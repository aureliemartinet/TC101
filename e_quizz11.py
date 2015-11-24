import math

def is_accurate_enough(num1, num2, accuracy):
    # we use abs so we don't have to care about the order of the 2 numbers
    if (abs(num1 - num2) < accuracy):
        return True
    else:
        return False


def calculate_e(accuracy):
    # we initialize e_previous to a dummy value
    # so we can enter in the while 
    e_previous = -10
    e_current = 0
    i = 0
    while (is_accurate_enough(e_previous, e_current, accuracy) == False):
        fact = math.factorial(i)
        e_previous = e_current
        e_current = e_current + (1 / fact)
        i += 1
    return e_current

precision_number = float(input("Please give me the accuracy of the approximation of e to be calculated: "))

approximation_e = calculate_e(precision_number)
print("approximation of e : " + str(approximation_e))
