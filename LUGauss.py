class LUGauss:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def lu_dekomposisi(self):
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

    def substitusi_maju(self, L, b):
        n = len(L)
        y = [0.0] * n
        for i in range(n):
            y[i] = b[i]
            for j in range(i):
                y[i] -= L[i][j] * y[j]
        return y

    def substitusi_mundur(self, U, y):
        n = len(U)
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            x[i] = y[i]
            for j in range(i + 1, n):
                x[i] -= U[i][j] * x[j]
            x[i] /= U[i][i]
        return x

    def caranya(self):
        L, U = self.lu_dekomposisi()
        y = self.substitusi_maju(L, self.b)
        x = self.substitusi_mundur(U, y)
        return x

# Example usage:
A = [[2, 6, 0],
     [4, 1, 3],
     [-2, 0, 2]]

b = [3, 3, 1]

penyelesaian = LUGauss(A, b)
jawab = penyelesaian.caranya()
print("Jadi Didapatkan ", jawab)
