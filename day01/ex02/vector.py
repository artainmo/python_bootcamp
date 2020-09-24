class Vector:
    def __init__(self, values):
        if isinstance(values, list) == False:
            print("Wrong values")
        self.values = values
        self.size = len(self.values)

    def __add__(self, num):
        i = 0
        while i < len(self.values):
            self.values[i] += num
            i += 1

    def __radd__(self, nums):
        i = 0
        while i < len(self.values):
            self.values[i] += nums[i]
            i += 1

    def __sub__(self, num):
        i = 0
        while i < len(self.values):
            self.values[i] -= num
            i += 1
    def __rsub__(self, nums):
        i = 0
        while i < len(self.values):
            self.values[i] += nums[i]
            i -= 1

    def __truediv__(self, num):
        i = 0
        while i < len(self.values):
            self.values[i] /= num
            i += 1

    def __rtruediv__(self, nums):
        i = 0
        while i < len(self.values):
            self.values[i] += nums[i]
            i -= 1
    def __mul__(self, num):
        i = 0
        while i < len(self.values):
            self.values[i] *= num
            i += 1

    def __rmul__(self, nums):
        i = 0
        while i < len(self.values):
            self.values[i] *= nums[i]
            i -= 1
    # __str__
    # __repr__
