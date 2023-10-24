def pop_blocks(lst):
    i = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            j = i + 1
            while j < len(lst) and lst[i] == lst[j]:
                j += 1
            del lst[i:j]
            pop_blocks(lst)
        i += 1
    return lst
