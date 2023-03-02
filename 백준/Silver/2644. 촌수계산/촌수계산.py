import sys
from collections import deque
input = sys.stdin.readline

def BFS(node):
  dq = []
  dq = deque(dq)
  visit[node] = 1
  dq.append(node)
  
  while dq:
    node = dq.popleft()

    for n in graph[node]:
      if visit[n] == 0:
        visit[n] = visit[node] + 1
        dq.append(n)

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [0] * (n+1)

BFS(p1)

rslt = visit[p2]

if rslt == 0:
  print("-1")
else:
  print(rslt - 1)