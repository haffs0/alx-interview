#!/usr/bin/python3
"""Define rotate_2d_matrix func"""


def rotate_2d_matrix(matrix):
    """Return: 2D matrix rotate by 90 degree"""
    N = len(matrix[0])
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(N):
        matrix[i].reverse()
