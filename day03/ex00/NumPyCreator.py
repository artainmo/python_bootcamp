import numpy as np

class NumPyCreator:

    def from_list(self, lst, type=np.int): #takes in a list and returns its corresponding NumPy array.
        return np.array(lst, dtype=type)

    def from_tuple(self, tpl, type=np.int): #takes in a tuple and returns its corresponding NumPy array.
        return np.array(tpl, dtype=type)

    def from_iterable(self, itr, type=np.int): #takes in an iterable and returns an array which contains all of its elements.
        return np.array(itr, dtype=type)

    def from_shape(self, shape, value=0, type=np.int): #returns an array filled with the same value.
        return np.full(shape=shape, fill_value=value, dtype=type)

    def random(self, shape): #returns an array filled with random values and takes a tuple that defines the shape
        return np.random.rand(shape[0], shape[1])

    def identity(self, n): #returns an array representing the identity matrix of size n.
        return np.identity(n)


a = NumPyCreator()
print(a.from_list(["wwdwd", "dwdwdw", "ddwdd"], np.str))
print(a.from_tuple((1, 2, 3, 4), np.int))
print(a.from_iterable(["wwdwd", "dwdwdw", "ddwdd"], np.str))
print(a.from_shape((2, 3), type=np.int))
print(a.random((2, 5)))
print(a.identity(5))
