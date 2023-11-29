m1 = [
    [1,   2],
    [30, 40]
]

m2 = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
]
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    count = 0
    sum_total = 0
    
    while count < len(matrix):
        row = matrix[count]
        sum_total += row[count]
        count += 1
    
    count = len(matrix) - 1
    while count >= 0:
        row = matrix[len(matrix) - 1 - count]
        sum_total += row[count]
        count -= 1
    
    return sum_total