def solution(s):
    answer = 0
    idx, c1, c2 = 0, 0, 0
    
    for i in range(len(s)):
        if s[i] == s[idx]:
            c1 += 1
        else:
            c2 += 1
        
        if c1 == c2:
            answer += 1
            idx, c1, c2 = (i+1), 0, 0
    
    if c1 != c2:
        answer += 1
    
    return answer