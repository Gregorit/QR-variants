class SquareMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def multiply(self, vector):
        newmatrix = [[0 for i in range(len(self.matrix))] for i in range(len(self.matrix))]
        values = [0 for i in range(len(self.matrix))]
        if len(self.matrix) == len(vector.values):
            for i in range(0, len(self.matrix)):
                for j in range(0, len(self.matrix)):
                    newmatrix[i][j] = self.matrix[i][j] * vector.values[j]
                    values[i] += newmatrix[i][j]
        return Vector(values)

    def transpose(self):
        newmatrix = []
        newmatrix = [list(x) for x in zip(*self.matrix)]
        return SquareMatrix(newmatrix)


class Vector:
    def __init__(self, values):
        self.values = values

    def maxval(self):
        return max(self.values)

    def normalize(self):
        newvalues = [0 for i in range(len(self.values))]
        maxval = self.maxval()
        for i in range(0, len(self.values)):
            newvalues[i] = self.values[i]/maxval
        return Vector(newvalues)





