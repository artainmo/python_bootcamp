class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, values):
        sum = 0
        for value in values:
            sum += value
        return sum / len(values)

    def median(self, values):
        if len(values) == 0:
            return None
        values.sort();
        for value in enumerate(values):
            if value[0] >= len(values)//2:
                return value[1]

    def quartile(self, values, percentile):
        if len(values) == 0:
            return None
        values.sort()
        part1 = values[:len(values)//2]
        part2 = values[len(values)//2:]
        if percentile == 25:
            return self.median(part1)
        else:
            return self.median(part2)

    def var(self, values):
        if len(values) == 0:
            return None
        ret = 0;
        mean = self.mean(values)
        for value in values:
            ret += ((value - mean)**2 / len(values))
        return ret

    def std(self, values):
        if len(values) == 0:
            return None
        return self.var(values)**0.5

if __name__ == "__main__":
    t = TinyStatistician()
    a = [1, 42, 300, 10, 59]

    print(t.mean(a))
    print(t.median(a))
    print(t.quartile(a, 25))
    print(t.quartile(a, 75))
    print(t.var(a))
    print(t.std(a))
        
