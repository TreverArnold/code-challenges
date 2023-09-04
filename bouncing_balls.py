def bouncing_balls(h, bounce, window):
    count = 0
    solution = 0
    if h <= 0 or bounce >= 1 or bounce <= 0 or window >= h:
        return -1
    
    while h > window:
        solution += 1
        h *= bounce
        
    return solution + solution -1