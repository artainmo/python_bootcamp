date = (3,30,2019,9,25)

def set_front_zero(num):
    number = num
    number = str(number)
    if len(str(number)) == 1:
        return "0" + number
    else:
        return number

day = set_front_zero(date[3])
month = set_front_zero(date[4])
year = date[2]
year = str(year)
min = set_front_zero(date[1])
hour = set_front_zero(date[0])

print(day + "/" + month + "/" + year + " " + hour + ":" + min)
