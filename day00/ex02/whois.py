from sys import *

def odd_even():
    if int(argv[1]) == 0:
        print("I'm Zero")
    elif int(argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if len(argv) == 2:
    if argv[1].isdigit() == True:
        odd_even()
    else:
        print("ERROR")
elif len(argv) == 1:
    pass
else:
    print("ERROR")
