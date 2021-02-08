from math import pow


def exponential(base, exponent):
    return pow(base, exponent)


def horner(poly, n, x):
    # Initialize result
    result = poly[0]

    # Evaluate value of polynomial using Horner's method
    for i in range(1, n):
        result = result * x + poly[i]

    return result


while True:
    option = input("""
        Choose between the two options:
        1. Exponential
        2. Polynomial
        Type 1 or 2: 
    """)

    if option == '1':
        base = int(input('Enter your base number: '))
        exponent = int(input('Enter your exponent number: '))
        expo = exponential(base, exponent)
        print('Value of the Exponential is {}'.format(expo))

    elif option == '2':
        print("""
        Type in your equation like this: for example 2x3 - 6x2 + 2x - 1 for x = 3
        Polynomial equation co-efficient = 2 -6 2 -1
        x = 3
        n = length of polyEqn
        """)
        n = int(input('input n: '))
        polyEqn = []
        for i in range(0, n):
            polyList = int(input('Input co-efficient: '))
            polyEqn.append(polyList)
        x = int(input('Input x: '))
        polynomial = horner(polyEqn, n, x)
        print('Value of the polynomial is {}'.format(polynomial))
    else:
        print('Input a valid option: ')
