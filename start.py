from matrices import SquareMatrix, Vector

# matrixvalues = [[4.0, 1.0, 0.0], [0.0, 2.0, 1.0], [0.0, 0.0, -1.0]]
# vectorvalues = [1.0, 1.0, 1.0]

matrixvalues = [[0.0, 1.0], [1.0, 1.0]]
vectorvalues = [1.0, 1.0]

mat = SquareMatrix(matrixvalues)
matrix = mat.invert()
print(f'Original matrix: {mat.matrix}')
print(f'Inverted matrix: {matrix.matrix}')
vector = Vector(vectorvalues)
print(f'Initial vector: {vector.values}')
vector = vector.normalize()

iterations = 200
for i in range(0, iterations):
    print('----------------------')
    print(f'Iteration: {i}')
    vector = matrix.multiply(vector)
    print('After multiplying:')
    print(vector.values)
    vector = vector.normalize()
    print('After normalization:')
    print(f'Eigenvector: {vector.values}')

print('**********************')
print(f'After {iterations} iterations:')
print(f'For eigenvector: {vector.values}')
result_vector = mat.multiply(vector)
prop = result_vector.value_proportion(vector)
print(f'Smallest eigenvalue: {prop}')

