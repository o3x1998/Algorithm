def solution(triangle):
    answer = 0
    s = [triangle[0]]
    for i in range(2, len(triangle)+1):
        s.append([0]*i)
    
    for i in range(0, len(triangle)-1):
        for j in range(0, len(triangle[i])):
            s[i+1][j] = max(s[i+1][j], s[i][j] + triangle[i+1][j])
            s[i+1][j+1] = max(s[i+1][j+1], s[i][j] + triangle[i+1][j+1])
    
    answer = max(s[len(triangle)-1])       

    return answer