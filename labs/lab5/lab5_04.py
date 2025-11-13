def matrix_sum(n, a, b):
    if n < 2:
        return "Error!"

    result = [[0] * n] * n
    for i in range(n):
        for j in range(n):
            result[i][j] = a[i][j] + b[i][j]
    return result

matrix_sum(3,
           [
               [2, 4, 3],
               [2, 4, 3],
               [2, 4, 3],
           ],
           [
               [2, 4, 3],
               [2, 4, 3],
               [2, 4, 3],
           ])