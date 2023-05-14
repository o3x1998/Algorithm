from collections import deque

def solution(x, y, n):
    dq = deque()
    dq.append([y, 0])
    
    if x == y: return 0

    while len(dq) > 0:
        r, c = dq.popleft()
       
        if r-n == x: return c+1
        elif r-n > x: dq.append([r-n, c+1])
            
        if r%2 == 0:
            if r/2 == x: return c+1
            elif r/2 > x: dq.append([r/2, c+1])
            
        if r%3 == 0:
            if r/3 == x: return c+1
            elif r/3 > x: dq.append([r/3, c+1])

    return -1