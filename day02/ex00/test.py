from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

def fahrenheit(T):
     return ((float(9)/5)*T + 32)

def celsius(T):
     return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = ft_map(fahrenheit, temperatures)
C = ft_map(celsius, F)
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)




fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

f = lambda a,b: a if (a > b) else b
print(ft_reduce(f, [47,11,42,102,13]))
