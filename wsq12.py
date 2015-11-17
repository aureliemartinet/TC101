def gcd(a, b):
    while ( b != 0 ):
        t = a #temporary
        a = b
        b = t % b
    return a


number1 = int(input("Give me a positive integer please: "))
number2 = int(input("Give me a second positive integer please: "))

calcul_gcd = gcd(number1, number2)
print(calcul_gcd)
