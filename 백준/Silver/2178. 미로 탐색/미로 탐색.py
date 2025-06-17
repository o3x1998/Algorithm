# 미로 탐색
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
dq.append((0, 0))

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1:
                dq.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
                
print(maze[N-1][M-1])