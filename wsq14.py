import math

def is_equal (num1, num2, precision):
    # we use precision + 1 because it's rounded !
    if (round(num1, precision+1) == round(num2, precision+1)):
        return True
    else:
        return False


def calculate_e(precision):
    e_previous = -1
    e_current = 0
    i = 0
    while (is_equal(e_previous, e_current, precision) == False):
        fact = math.factorial(i)
        e_previous = e_current
        e_current = e_current + (1 / fact)
        i += 1
    return e_current

precision_number = int(input("Give me the accuracy of the number e please: "))

calculation_e = calculate_e(precision_number)
print(calculation_e)
