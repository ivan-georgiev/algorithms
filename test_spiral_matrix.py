import pytest

from spiral_matrix import spiral


def test_spiral():
    res = spiral(n=1)
    assert res == [[1]]

    res = spiral(n=3)
    assert res == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]

    res = spiral(n=4)
    assert res == [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]

    res = spiral(n=8)
    assert res == [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [28, 29, 30, 31, 32, 33, 34, 9],
        [27, 48, 49, 50, 51, 52, 35, 10],
        [26, 47, 60, 61, 62, 53, 36, 11],
        [25, 46, 59, 64, 63, 54, 37, 12],
        [24, 45, 58, 57, 56, 55, 38, 13],
        [23, 44, 43, 42, 41, 40, 39, 14],
        [22, 21, 20, 19, 18, 17, 16, 15],
    ]

def test_spiral_err():

    with pytest.raises(ValueError):
        spiral(n=-1)

    with pytest.raises(ValueError):
        spiral(n="2")

    with pytest.raises(ValueError):
        spiral(n=2.22)
