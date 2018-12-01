import math


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
        newmatrix = [list(x) for x in zip(*self.matrix)]
        return SquareMatrix(newmatrix)

    def leibniz(self):
        """Leibniz rule"""
        return self.matrix[0][0] * self.matrix[1][1] - (self.matrix[0][1] *
                                                        self.matrix[1][0])

    def sarrus(self):
        """Sarrus rule"""
        det = 0.0
        for i in range(0, len(self.matrix)):
            prod = self.matrix[0][i]
            k = i
            for j in range(1, len(self.matrix)):
                k += 1
                if k == len(self.matrix):
                    k = 0
                prod *= self.matrix[j][k]
            det += prod
        for i in reversed(range(0, len(self.matrix))):
            prod = self.matrix[0][i]
            k = i
            for j in range(1, len(self.matrix)):
                k -= 1
                if k == -1:
                    k = len(self.matrix) - 1
                prod *= self.matrix[j][k]
            det -= prod
        return det

    def determinant(self):
        if len(self.matrix) == 2:
            return self.leibniz()
        elif len(self.matrix) == 3:
            return self.sarrus()

    def complement(self):
        if len(self.matrix) == 3:
            rows = []
            row_a = []
            row_b = []
            row_c = []
            rows.append(row_a)
            rows.append(row_b)
            rows.append(row_c)

            counter = 0

            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    small_rows = []
                    for k in range(len(self.matrix)):
                        if k != i:
                            small_row = []
                            for ll in range(len(self.matrix)):
                                if ll != j:
                                    small_row.append(self.matrix[k][ll])
                            small_rows.append(small_row)
                    small_matrix = SquareMatrix(small_rows)
                    det = small_matrix.determinant()
                    if counter % 2 == 1:
                        rows[i].append(det * (-1.0))
                    else:
                        rows[i].append(det)
                    counter += 1

            return SquareMatrix(rows)
        elif len(self.matrix) == 2:
            rows = []
            row_a = []
            row_b = []
            rows.append(row_a)
            rows.append(row_b)
            rows[0].append(self.matrix[1][1])
            rows[0].append(self.matrix[0][1] * (-1.0))
            rows[1].append(self.matrix[1][0] * (-1.0))
            rows[1].append(self.matrix[0][0])
            return SquareMatrix(rows)

    def invert(self):
        det = self.determinant()
        compl = self.complement()
        compl = compl.transpose()
        for i in range(len(compl.matrix)):
            for j in range(len(compl.matrix)):
                compl.matrix[i][j] = compl.matrix[i][j] / det
        return compl


class Vector:
    def __init__(self, values):
        self.values = values

    def maxval(self):
        return max(self.values)

    def norm(self):
        value = 0.0
        for i in range(len(self.values)):
            value += self.values[i] ** 2
        value = math.sqrt(value)
        return value

    def normalize(self):
        newvalues = [0 for i in range(len(self.values))]
        maxval = self.maxval()
        for i in range(0, len(self.values)):
            newvalues[i] = self.values[i]/maxval
        return Vector(newvalues)

    def value_proportion(self, vector):
        sum = 0.0
        for i in range(len(self.values)):
            sum += self.values[i]/vector.values[i]
        return sum / len(self.values)
