class Crout:
    def __init__(self, A, b):
        self.A = A
        self.b = b
    
    def hitung(self):
        n = len(self.A)
        L = [[0.0] * n for _ in range(n)]
        U = [[0.0] * n for _ in range(n)]

        for i in range(n):
            L[i][i] = 1

            for j in range(i, n):
                L[j][i] = self.A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))
            
            for j in range(i, n):
                U[i][j] = (self.A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))) / L[i][i]

        # Forward substitution for Ly = b
        y = [0] * n
        for i in range(n):
            y[i] = (self.b[i] - sum(L[i][k] * y[k] for k in range(i))) / L[i][i]

        # Backward substitution for Ux = y
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(U[i][k] * x[k] for k in range(i + 1, n))) / U[i][i]

        return x

# Example usage:
A = [[2, -1, 0], [-1, 2, -2], [0, -1, 1]]
b = [1, 1, 0]

crout_solver = Crout(A, b)
solution = crout_solver.hitung()
print("Solution:", solution)
