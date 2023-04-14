def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x : x[1])
    missile = 0
    
    for s, e in targets:
        if missile > s:
            continue
        else:
            answer += 1
            missile = e
    
    return answer