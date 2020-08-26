

def max_timeslots(st_times: int, end_times: int) -> int:
    '''
    Function which receives list of timeslots and output the max number of non-overlapping

    st_times is list of integers (0-12) containing starting times of timeslots
    end_times is list of integers (0-12) containing ending times of timeslots
    Combination st_times[i] and end_times[i] define a timeslot
    Assumed: st_times[i] < end_times[i] and len(st_times) = len(end_times)

    '''

    # combine timeslot in single array
    timeslots = [(x,end_times[i]) for i, x in enumerate(st_times)]
    
    # sort by endtime, inc
    timeslots.sort(key=lambda ts: ts[1])

    # next timeslot is with endtime and starttime after those of the current
    cslot = timeslots[0]
    max = 1
    for ts in timeslots[1:]:
        if ts[1] > cslot[1] and ts[0] >= cslot[1]:
            cslot = ts
            max = max +1
    
    return max


if __name__ == '__main__':
    st_times = [1, 1, 2, 2, 5]
    end_times = [2, 3, 3, 3, 6]
    res = max_timeslots(st_times, end_times)
    print(res)
