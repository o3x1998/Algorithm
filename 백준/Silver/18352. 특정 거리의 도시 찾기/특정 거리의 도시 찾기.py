import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dq = deque([(X)])
distance[X] = 0

while dq:
    tmp = dq.popleft()
    
    for x in graph[tmp]:
        if distance[x] == -1:
            distance[x] = distance[tmp] + 1
            dq.append((x))
        
rslt = []
for idx, d in enumerate(distance):
    if d == K:
        rslt.append(idx)

if not rslt:
    print("-1")
else:
    print(*rslt, end="\n")
