from sys import *

def is_float(num):
    for char in num:
        if char == ".":
            return True
    return False

def calc():
    argv[1] = int(argv[1])
    argv[2] = int(argv[2])
    sum = argv[1] + argv[2]
    print("Sum:".ljust(13) + str(sum))
    substraction = argv[1] - argv[2]
    print("Difference:".ljust(13) + str(substraction))
    multiplication = argv[1] * argv[2]
    print("Product:".ljust(13) + str(multiplication))
    if argv[2] != 0:
        div = argv[1] / argv[2]
        modulo = argv[1] % argv[2]
        print("Quotient:".ljust(13) + str(div))
        print("Remainder:".ljust(13) + str(modulo))
    else:
        print("Quotient:".ljust(13) + "ERROR (div by zero)")
        print("Remainder:".ljust(13) + "ERROR (modulo by zero)")

if len(argv) == 3:
    if argv[1].isdigit() == True and argv[2].isdigit() == True and is_float(argv[1]) == False and is_float(argv[2]) == False:
            calc()
    else:
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")

elif len(argv) < 3:
    print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")
elif len(argv) > 3:
    print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3")
