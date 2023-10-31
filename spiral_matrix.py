import sys

def valid_position(matrix, row, column) -> bool:
    """
    Validates if item[row,column] is valid for write
    """
    if column == len(matrix) or row == len(matrix):
        return False
    if column  < 0 or row < 0:
        return False
    if matrix[row][column] != 0:
        return False

    return True


def spiral(n: int):
    """
    Creates NxN sized matrix which will be filled by spiral with values starting from 1
    on item[0,0].
    """

    # validation
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be intiger higher than 1")

    # init empty matrix
    res = [[0] * n for i in range(n)]

    # define directions: right, down, left, up - [row, column]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # initial index
    r = 0
    c = 0
    # initial current direction: right
    cd = 0

    for i in range(n * n):
        # assign i to cell
        res[r][c] = i + 1

        # check if next position is valid and change direction if not
        if not valid_position(res, r + move[cd][0], c + move[cd][1]):
            # change curent direction
            cd = (cd + 1) % 4
        # change indecies based on current direction
        r += move[cd][0]
        c += move[cd][1]

    return res


if __name__ == "__main__":
    # input validation
    input_n = int(sys.argv[1])
    if input_n < 1:
        raise ValueError("Input must be higher than 1")

    # gen spiral matrix and print it
    result = spiral(n=input_n)
    print(*result, sep="\n")
