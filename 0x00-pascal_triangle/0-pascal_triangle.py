#!/usr/bin/python3
""" Generate pascal's triangle """

def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(len(triangle[i - 1]) - 1):
            curr = triangle[i - 1]
            row.append(curr[j] + curr[j + 1])

        row.append(1)
        triangle.append(row)

    return triangle
