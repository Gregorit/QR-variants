from matrices import SquareMatrix, Vector

# matrixvalues = [[4.0, 1.0, 0.0], [0.0, 2.0, 1.0], [0.0, 0.0, -1.0]]
# vectorvalues = [1.0, 1.0, 1.0]

matrixvalues = [[0.0, 1.0], [1.0, 1.0]]
vectorvalues = [1.0, 1.0]

mat = SquareMatrix(matrixvalues)
matrix = mat.invert()
print("Original matrix: " + str(mat.matrix))
print("Inverted matrix: " + str(matrix.matrix))
vector = Vector(vectorvalues)
print("Initial vector: " + str(vector.values))
vector = vector.normalize()

iterations = 200

for i in range(0, iterations):
    print('----------------------')
    print("Iteration: " + str(i))
    vector = matrix.multiply(vector)
    print("After multiplying:")
    print(vector.values)
    vector = vector.normalize()
    print("After normalization:")
    print("Eigenvector: " + str(vector.values))

print('-----------------')
print('After ' + str(iterations) + ' iterations:')
print('For eigenvector: ' + str(vector.values))
result_vector = mat.multiply(vector)
prop = result_vector.value_proportion(vector)
print('Smallest eigenvalue: ' + str(prop))

