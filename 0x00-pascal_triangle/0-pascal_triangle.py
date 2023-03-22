#!/usr/bin/python3
"""
create a pascal triangle function
"""


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return (fact)


def pascal_triangle(n):
    """
        args(n): number of pascal triangle to create
    """
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))

        triangle.append(row)
    return triangle
