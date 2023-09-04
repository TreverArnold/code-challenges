def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    
    answer = [sequence[0]]
    
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            answer.append(sequence[i])
            
            
    return answer