from copy import deepcopy
import sys


def words():
    for line in sys.stdin:
        for word in line.split():
            yield word


def new_empty(n):
    return [x[:] for x in [[0.0] * n] * n]


def pivotize(mat_a, x):
    mat_a = deepcopy(mat_a)
    size = len(mat_a)
    row = max(range(x, size), key=lambda i: abs(mat_a[i][x]))
    if x != row:
        mat_a[x], mat_a[row] = mat_a[row], mat_a[x]
    return mat_a


def invert(mat_a):
    mat_a = deepcopy(mat_a)
    n = len(mat_a)
    for i in range(n):
        mat_a[i] += [int(i == j) for j in range(n)]
    for x in range(n):
        mat_a = pivotize(mat_a, x)
        for i in range(x + 1, n):
            coefficient = mat_a[i][x] / mat_a[x][x]
            for j in range(x, n * 2):
                mat_a[i][j] -= coefficient * mat_a[x][j]
                print(mat_a[i][j])
    for x in reversed(range(n)):
        for i in reversed(range(x)):
            coefficient = mat_a[i][x] / mat_a[x][x]
            for j in reversed(range(n * 2)):
                mat_a[i][j] -= coefficient * mat_a[x][j]
                print(mat_a[i][j], end=' ')
    print(mat_a)
    for i in range(n):
        denominator = mat_a[i][i]
        for j in range(n * 2):
            mat_a[i][j] /= denominator
    for i in range(n):
        mat_a[i] = mat_a[i][n:]
    return mat_a
