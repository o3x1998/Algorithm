from collections import deque

def solution(maps):
    answer = []
    dq = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])      
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                sum = int(maps[i][j])
                maps[i][j] = 'X'
                dq.append((i, j))
                
                while len(dq) > 0:
                    a, b = dq.popleft()
                    
                    for k in range(4):
                        ua = a + dx[k]
                        ub = b + dy[k]

                        if ua >= 0 and ua < len(maps) and ub >= 0 and ub < len(maps[0]) and maps[ua][ub] != 'X':
                            sum += int(maps[ua][ub])
                            maps[ua][ub] = 'X'
                            dq.append((ua, ub))
                answer.append(sum)
    
    if len(answer) > 0: return sorted(answer)
    return [-1]