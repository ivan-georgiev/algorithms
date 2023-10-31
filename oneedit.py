def check_samesize(s1: str, s2: str) -> bool:
    """
    Method comparing distance between two strings same length
    """
    # differences count
    cnt = 0
    for i, s1_c in enumerate(s1):
        # compare same position chars
        if s1_c != s2[i]:
            cnt += 1
    # same size string should have exactly one diff
    return cnt == 1


def check(short: str, long: str) -> bool:
    """
    Method comparing distance between two strings with differeng length
    """
    # differences count
    cnt = 0

    for i, cur_s in enumerate(short):
        # get coresponding char from the longer string, shift with cnt for mid-string insert
        cur_l = long[i + cnt]

        if cur_s != cur_l:
            # if 2nd different char, or not same as next char from long string, then False
            if cnt == 1 or cur_s != long[i + 1]:
                return False
            # shift 1 for next iterations
            cnt += 1

    return True


def one_edit_distance(s1: str, s2: str) -> bool:
    """
    Method calling the proper check method based on strings length

    An edit is:
    - Inserting one character anywhere in the word (including at the beginning and end)
    - Removing one character
    - Replacing one character

    """
    # run check with shortest string as first param
    if len(s1) == len(s2) - 1:
        return check(s1, s2)
    if len(s1) == len(s2) + 1:
        return check(s2, s1)

    # same-length string use different check
    if len(s1) == len(s2):
        return check_samesize(s1, s2)

    # all other cases are False
    return False


if __name__ == "__main__":
    # test same size
    assert one_edit_distance("calc", "cast") is False
    assert one_edit_distance("cast", "cast") is False
    assert one_edit_distance("cost", "cast") is True

    # test different size
    assert one_edit_distance("cat", "cats") is True
    assert one_edit_distance("cat", "zcat") is True
    assert one_edit_distance("cat", "coat") is True
    assert one_edit_distance("cat", "cots") is False
    assert one_edit_distance("cat", "zcats") is False
