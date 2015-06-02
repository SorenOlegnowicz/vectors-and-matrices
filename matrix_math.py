import math
from functools import reduce


class ShapeException(Exception):
    pass
# if the length is not the same then raise exception


def dot(a, b):
    return sum([a * b for a, b in zip(a, b)])


def magnitude(a, b):
    return [math.sqrt(a * b) for a, b in zip(a, b)]


def shape(a_shape):
    if type(a_shape[0]) is int:
        return (len(a_shape), )
    else:
        return (len(a_shape), (len(a_shape[0][:])))


def vector_add(a, b):
    return [a + b for a, b in zip(a, b)]


def vector_sub(a, b):
    return [a - b for a, b in zip(a, b)]


def vector_sum():
    pass


def vector_multiply(a, b):
    return [c * b for c in a]


def vector_mean():
    pass


def matrix_row(matrix, row_index):
    return matrix[row_index]


def matrix_col(matrix, col_index):
    return [row_index[col_index] for row_index in matrix]


def matrix_scalar_multiply(matrix, scalar):
    return [[num * scalar for num in vector] for vector in matrix]


def matrix_vector_multiply(matrix, vector):
    for v in vector:
        return [[num * v for num in vector] for vector in matrix]


def matrix_matrix_multiply():
    pass
