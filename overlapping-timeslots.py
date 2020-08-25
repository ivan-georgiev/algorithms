

def overlaps(st_times: int, end_times: int) -> int:
    '''
    Function which receives list of timeslots and output the max number of non-overlapping

    st_times is list of integers (0-12) containing starting times of timeslots
    end_times is list of integers (0-12) containing ending times of timeslots
    Combination st_times[i] and end_times[i] define a timeslot
    Assumed: st_times[i] < end_times[i] and len(st_times) = len(end_times)

    Time complexity is O^2
    '''
    size = len(st_times)

    # current max set found
    maxSet = set()

    for i in range(size):
        # current slot - i
        istime = st_times[i]
        iendtime = end_times[i]

        # list of non-overlaping timeslots
        compatible = {i, }

        # check all timeslots after current timeslot i
        # range(size) will introduce duplicate sets
        for j in range(i + 1, size):
            # next slot - j
            jstime = st_times[j]
            jendtime = end_times[j]

            # overlap conditions:
            # j start/end time is between i(start,end)
            # i is fully nested in j(start,end)
            if jendtime > istime and jendtime < iendtime or jstime > istime and jstime < iendtime or jstime <= istime and jendtime >= iendtime:
                print(f'{i} and {j} overlaps')
            else:
                print(f'{i} and {j} do not overlap')
                compatible.add(j)

        # if currents set is max, update max
        if len(maxSet) < len(compatible):
            maxSet = compatible

    print(f'Maximum size set of timeslots: {maxSet}')
    return len(maxSet)


if __name__ == '__main__':
    st_times = [1, 1, 2, 0]
    end_times = [2, 3, 3, 4]
    res = overlaps(st_times, end_times)
    print(f'Result: {res}')
