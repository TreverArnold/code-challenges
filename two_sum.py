def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        solve_num = target - num
        if solve_num in num_dict:
            return (num_dict[solve_num], i)
        num_dict[num] = i
