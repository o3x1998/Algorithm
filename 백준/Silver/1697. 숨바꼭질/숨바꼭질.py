import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dq = deque([(N, 0)])
visited = [False] * 100001
visited[N] = True

while dq:
    a, b = dq.popleft()
    
    if a == K:
        print(b)
        break
    
    for na in (a-1, a+1, 2*a):
        
        if na < 0 or na > 100000:
            continue
        
        if visited[na] == False:
            dq.append((na, b+1))
            visited[na] = True
