def transpose_matriks(matriks):
    return [[matriks[j][i] for j in range(len(matriks))] for i in range(len(matriks[0]))]

def minor_matriks(matriks, i, j):
    return [row[:j] + row[j+1:] for row in (matriks[:i] + matriks[i+1:])]

def determinan_matriks(matriks):
    if len(matriks) == 2:
        return matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0]
    
    determinan = 0
    for c in range(len(matriks)):
        determinan += ((-1) ** c) * matriks[0][c] * determinan_matriks(minor_matriks(matriks, 0, c))
    return determinan

def matriks_balikan(matriks):
    determinan = determinan_matriks(matriks)
    if len(matriks) == 2:
        return [[matriks[1][1] / determinan, -1 * matriks[0][1] / determinan],
                [-1 * matriks[1][0] / determinan, matriks[0][0] / determinan]]
    
    cofactors = []
    for r in range(len(matriks)):
        cofactor_row = []
        for c in range(len(matriks)):
            minor = minor_matriks(matriks, r, c)
            cofactor_row.append(((-1) ** (r + c)) * determinan_matriks(minor))
        cofactors.append(cofactor_row)
    cofactors = transpose_matriks(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinan
    return cofactors

# Example usage
A = [[2, 1, 1],
     [2, 3, 3],
     [8, 0, 6]]

A_inv = matriks_balikan(A)
print("Matriks A:")
for row in A:
    print(row)
print("\nMatriks A balikannya adalah:")
for row in A_inv:
    print(row)