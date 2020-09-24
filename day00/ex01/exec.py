from sys import *

def reversed_string(a_string):
    return a_string[::-1]
# It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.

argv.reverse()
i = 0
while i < len(argv):
    argv[i] = reversed_string(argv[i])
    argv[i] = argv[i].swapcase()
    i += 1
i = 0
ret = ""
while i < len(argv) - 1:
    ret += argv[i]
    i += 1
    if i < len(argv) - 1:
        ret += " "
print(ret)
