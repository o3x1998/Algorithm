def solution(n, lost, reserve):
    answer = 0
    s = [1]*(n+1)
    for x in lost: s[x] -= 1
    for y in reserve: s[y] += 1

    for i in range(1, n+1):
        if s[i] == 0:
            if i-1 > 0 and s[i-1] == 2:
                s[i-1] -= 1
                s[i] += 1
                continue
            elif i+1 < n+1 and s[i+1] == 2:
                s[i+1] -= 1
                s[i] += 1
    
    for x in s[1:]:
        if x >= 1: answer += 1
    
    return answer