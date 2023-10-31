import sys


def look_and_say(input_string: str) -> str:
    """
    Function to transfrom input_string string to look-and-say sequence
    https://en.wikipedia.org/wiki/Look-and-say_sequence
    """

    # validation
    if int(input_string) < 0:
        raise ValueError("Negative number")

    # result variable init
    res = ""
    # counter init
    n = 0
    # first symbol init
    prev = input_string[0]

    for i in input_string:
        # increase counter if char is like previous
        if i == prev:
            n += 1
        else:
            # new group, record prev to result
            res = f"{res}{n}{prev}"
            # update prev and counter
            n = 1
            prev = i
    # add last group
    res = f"{res}{n}{prev}"

    return res


if __name__ == "__main__":
    # get script argument
    inp = sys.argv[1]

    # print first 10 sequences
    for _ in range(10):
        print(inp)
        inp = look_and_say(inp)
