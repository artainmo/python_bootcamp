from random import sample
from numpy import *

def unique_list(str):
    new=""
    for char in str:
        if char not in new:
            new += char
    return new

def ft_optional(substr, option):
    if option == "shuffle":
        substr = sample(substr, len(substr))
        substr = "".join(substr)
        return substr
    elif option == "unique":
        substr = unique_list(substr)
        return substr
    elif option == "ordered":
        substr = sorted(substr)
        substr = "".join(substr)
        return substr
    elif option == None:
        return substr
    else:
        print("ERROR option not found")
        exit()

def generator(text, sep, option=None):
    i = 0
    start = 0
    if isinstance(text, str) == False:
        print("Error text")
        return None
    for i in range(0,len(text)):
        if text[i] == sep:
            substr = text[start:i]
            yield ft_optional(substr, option)
            start = i + 1
        if i == len(text) - 1:
            substr = text[start:i + 1]
            yield ft_optional(substr, option)
            start = i + 1

t = "xbxbavvfff"
for y in generator(t, "a", "unique"):
    print(y)
