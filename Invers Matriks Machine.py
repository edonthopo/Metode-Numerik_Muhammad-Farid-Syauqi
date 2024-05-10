def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def matrix_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * matrix_determinant(matrix_minor(matrix, 0, c))
    return determinant

def matrix_inverse(matrix):
    determinant = matrix_determinant(matrix)
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]
    
    cofactors = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            minor = matrix_minor(matrix, r, c)
            cofactor_row.append(((-1) ** (r + c)) * matrix_determinant(minor))
        cofactors.append(cofactor_row)
    cofactors = transpose_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors

# Example usage
A = [[4, 7, 1],
     [2, 7, 3],
     [5, 2, 7]]

A_inv = matrix_inverse(A)
print("Matrix A:")
for row in A:
    print(row)
print("\nInverse of matrix A:")
for row in A_inv:
    print(row)