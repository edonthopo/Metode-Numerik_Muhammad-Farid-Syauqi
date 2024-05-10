class LUGauss:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def lu_decomposition(self):
        n = len(self.A)
        L = [[0.0] * n for _ in range(n)]
        U = [[0.0] * n for _ in range(n)]

        for i in range(n):
            L[i][i] = 1.0
            for j in range(i, n):
                total = sum(L[i][k] * U[k][j] for k in range(i))
                U[i][j] = self.A[i][j] - total

            for j in range(i + 1, n):
                total = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (self.A[j][i] - total) / U[i][i]

        return L, U

    def forward_substitution(self, L, b):
        n = len(L)
        y = [0.0] * n
        for i in range(n):
            y[i] = b[i]
            for j in range(i):
                y[i] -= L[i][j] * y[j]
        return y

    def backward_substitution(self, U, y):
        n = len(U)
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            x[i] = y[i]
            for j in range(i + 1, n):
                x[i] -= U[i][j] * x[j]
            x[i] /= U[i][i]
        return x

    def solve(self):
        L, U = self.lu_decomposition()
        y = self.forward_substitution(L, self.b)
        x = self.backward_substitution(U, y)
        return x

# Example usage:
A = [[1, 0, 0],
     [2, 1, 0],
     [-1, -3, 1]]

b = [5, 3, 1]

lu_solver = LUGauss(A, b)
solution = lu_solver.solve()
print("Solution:", solution)
