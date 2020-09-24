from sys import *
import string

if len(argv) != 3 or argv[1].isalnum() == True or argv[2].isalnum() == False:
    print("ERROR")
    exit()
for punctuation in string.punctuation:
    argv[1] = argv[1].replace(punctuation, "")
argv[1] = argv[1].split()
i = 0
while i < len(argv[1]):
    if len(argv[1][i]) <= int(argv[2]):
        argv[1].remove(argv[1][i])
        i -= 1
    i += 1
print(argv[1])
