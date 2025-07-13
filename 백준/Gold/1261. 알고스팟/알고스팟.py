import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
maze = [input() for _ in range(N)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * M for _ in range(N)]

dq = deque()
dq.append((0, 0, 0))

while dq:
    cnt, x, y = dq.popleft()
    
    if x == N-1 and y == M-1:
        print(cnt)
        break
    
    for a, b in dxy:
        nx = x + a
        ny = y + b
        
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            if maze[nx][ny] == '0':
                visited[nx][ny]= True
                dq.appendleft((cnt, nx, ny))
            else:
                visited[nx][ny]= True
                dq.append((cnt+1, nx, ny))