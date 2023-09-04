def smallest_int(arr):
    current = arr[0]

    for num in arr:
        if num < current:
            current = num
    
    return current
