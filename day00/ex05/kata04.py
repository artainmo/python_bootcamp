tuple = ( 0, 4, 132.42222, 10000, 12345.67)


def set_front_zero(num):
    number = num
    number = str(number)
    if len(str(number)) == 1:
        return "0" + number
    else:
        return number

day = "day_" + set_front_zero(tuple[0])
ex = "ex_" + set_front_zero(tuple[1])
one = tuple[2]
two = tuple[3]
three = tuple[4]

print(day + ", " + ex + " : %.2f, %.2e, %.2e" % (one, two , three))
