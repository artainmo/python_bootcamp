from time import *
import math

def ft_progress(lst):
    time_seconds = 0
    multiplier = 1/len(lst) * 25
    start_time = time()
    yield  0
    elapsed_time = time() - start_time
    tot_time = elapsed_time * len(lst)
    for i in range(1, len(lst)):
        equal = i * multiplier
        space = len(lst) * multiplier - equal
        time_seconds += elapsed_time
        ema = tot_time - time_seconds - 0.01
        percentage = math.ceil(i * multiplier * 4)
        if ema < 0.000000:
            ema = 0
        print("ETA: %.2fs [ %d%%][" % (ema, percentage), end = "")
        print("=" * int(equal) + ">" + " " * int(space), end = "")
        print("] %d/%d | elapsed time %.2fs" % (i + 1, len(lst), time_seconds), end = "\r")
        yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
