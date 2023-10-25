def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    for interval in intervals:
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = (
                merged_intervals[-1][0],
                max(merged_intervals[-1][1], interval[1]),
            )

    total_length = 0
    for interval in merged_intervals:
        total_length += interval[1] - interval[0]

    return total_length
