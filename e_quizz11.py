import math

def is_less_accuracy (num1,num2,precision):
    # we use precision + 1 because it's rounded !
    if ( float((round(num1, precision+1) - round(num2, precision+1)) < precision)):
        return True
    else:
        return False


def calculate_e(accuracy):
    e_previous = -1
    e_current = 0
    i = 0
    while (is_less_accuracy(e_previous, e_current, accuracy) == False):
        fact = math.factorial(i)
        e_previous = e_current
        e_current = e_current + (1 / fact)
        i += 1
    return e_current

precision_number = float(input("Give me the accuracy of the number e please: "))

calculation_e = calculate_e(precision_number)
print(calculation_e)
