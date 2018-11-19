from matrices import SquareMatrix, Vector

# przerobic to (metode potegowa) na odwrotna metode potegowa
# dodac menu uzytkownika

matrixvalues = [[4.0, 1.0, 0.0], [0.0, 2.0, 1.0], [0.0, 0.0, -1.0]]
vectorvalues = [1.0, 1.0, 1.0]

matrix = SquareMatrix(matrixvalues)
vector = Vector(vectorvalues)
vector = vector.normalize()

iterations = 100
print(matrix.matrix)
print(vector.values)

for i in range(0, iterations):
    print("Iteration: " + str(i))
    vector = matrix.multiply(vector)
    print("After multiplying:")
    print(vector.values)
    eigenvalue = vector.maxval()
    vector = vector.normalize()
    print("After normalization:")
    print("Eigenvector: " + str(vector.values) + " - Eigenvalue: " + str(eigenvalue))

