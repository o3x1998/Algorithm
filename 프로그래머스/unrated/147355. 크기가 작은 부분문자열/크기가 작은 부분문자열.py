def solution(t, p):
    answer = 0
    
    l = len(p)
    
    for i in range(0, len(t)-l+1):
        tmp = t[i:(i+l)]
        
        if int(tmp) <= int(p):
            answer += 1
            
    
    return answer