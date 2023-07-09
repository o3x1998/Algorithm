from collections import Counter

def solution(participant, completion):
    p = Counter(participant)

    for c in completion:
        p[c] -= 1
        if p[c] == 0:
            del p[c]     
    
    return list(p.keys())[0]
