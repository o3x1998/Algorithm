import sys
from collections import deque

input = sys.stdin.readline

def DFS(node):
    v1[node] = 1
    r1.append(node)
    
    for n in graph[node]:
        if v1[n] == 0:
            DFS(n)
            
def BFS(node):
    dq = []
    dq = deque(dq)
    v2[node] = 1
    dq.append(node)
    
    while dq:
        node = dq.popleft()
        r2.append(node)
        
        for n in graph[node]:
            if v2[n] == 0:
                v2[n] = 1
                dq.append(n)
                
                
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    x.sort()

v1 = [0] * (N+1)
r1 = []
DFS(V)
print(' '.join(map(str, r1)))

v2 = [0] * (N+1)
r2 = []
BFS(V)
print(' '.join(map(str, r2)))