from collections import Counter

def solution(participant, completion):
    answer = ''
    p = Counter(participant)

    for c in completion:
        p[c] -= 1
        if p[c] == 0:
            del p[c]  
            
    for x in p: 
        answer = x         
    
    return answer