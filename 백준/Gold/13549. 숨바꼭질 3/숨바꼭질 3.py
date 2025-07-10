import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 100001
visited[N] = True
dq = deque([(N, 0)])

while dq:
    p, t = dq.popleft()
    
    if p == K:
        print(t)
        break
    
    if 0 <= p*2 <= 100000 and not visited[p*2]:
        visited[p*2] = True
        dq.appendleft((p*2, t))  
    if 0 <= p-1 <= 100000 and not visited[p-1]:
        visited[p-1] = True
        dq.append((p-1, t+1))
    if 0 <= p+1 <= 100000 and not visited[p+1]:
        visited[p+1] = True
        dq.append((p+1, t+1))