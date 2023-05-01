import copy

class Vector:
    def __init__(self, values):
        self.values = values
        if len(self.values) > 1:
            self.shape = [len(self.values), 1]
        else:
            self.shape = [1, len(self.values[0])]
    def __repr__(self):
        return str(self.values)
    def __str__(self):
        return self.__repr__()
    def dot(self, v2):
        if v2.shape == self.shape:
            result = 0
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    result += self.values[x][y] * v2.values[x][y]
            return result
        else:
            raise Exception("Vectors have to be of the same shape")
            
    def T(self):
        tr = [[0 for x in range(self.shape[0])] for y in range(self.shape[1])]
        for a in range(self.shape[0]):
            for b in range(self.shape[1]):
                tr[b][a] = self.values[a][b]
        return Vector(tr)
    def __add__(self, v2):
        if isinstance(v2, Vector) and self.shape == v2.shape:
            sum_vec = copy.deepcopy(self.values)
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    sum_vec[x][y] = self.values[x][y] + v2.values[x][y]
            return Vector(sum_vec)
        else:
            raise Exception("Sum and substraction can only be done with vectors of the same shape")
    def __radd__(self, v2):
        return self.__add__(v2)
    def __mul__(self, mint):
        if isinstance(mint, (int, float)):   
            mul_vec = copy.deepcopy(self.values)
            for x in range(self.shape[0]):
                    for y in range(self.shape[1]):
                        mul_vec[x][y] = self.values[x][y] * mint
            return Vector(mul_vec)
        else:
            raise Exception("Can only multiply vector with scalar")
    def __rmul__(self, mint):
        return self.__mul__(mint)
    def __sub__(self, v2):
        return self.__add__(-1*v2)
    def __rsub__(self, v2):
        return self.__radd__(-1*v2)
    def __truediv__(self, dint):
        if isinstance(dint, (int, float)) and dint != 0:
            return self.__mul__(1/dint) 
        else:
            print("Can only divide by a non-null scalar")
            return
    def __rtruediv__(self, dint):
        raise Exception("Arithmetic error: division of scalar and vector not defined")

