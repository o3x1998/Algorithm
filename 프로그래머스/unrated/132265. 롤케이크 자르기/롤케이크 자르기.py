from collections import Counter

def solution(topping):
    answer = 0
    r1 = Counter(topping)
    r2 = set()
    
    for t in topping:
        r1[t] -= 1
        if r1[t] == 0: del r1[t]
        r2.add(t)
        if len(r1) == len(r2): answer += 1
        
    return answer