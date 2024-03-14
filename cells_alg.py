import copy


def print_matrix(A):
    for strA in A:
        print(strA)


def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def det(A):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0

    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant


def inverse(A):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(A[0])):
            result[i].append(int(0))
    for i in range(len(A)):
        for j in range(len(A[0])):
            tmp = minor(A, i, j)
            if i + j % 2 == 1:
                result[i][j] = -1 * det(tmp) / det(A)
            else:
                result[i][j] = 1 * det(tmp) / det(A)
            print(result[i][j])
    return result


def transpose(array):
    res = []
    n = len(array)
    m = len(array[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [array[i][j]]
            print(tmp)
        res = res + [tmp]
        print(res)
    return res


