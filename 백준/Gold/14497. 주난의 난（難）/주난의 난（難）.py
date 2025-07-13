import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
arr = [input() for _ in range(N)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = 300
jump = [[INF] * (M) for _ in range(N)] # 점프 몇번에 쓰러뜨렸는지 기록 / 이미 쓰러뜨렸으면 무시하도록..min으로 확인?

dq = deque()
dq.append((0, x1-1, y1-1)) # (점프횟수, x좌표, y좌표)
jump[x1-1][y1-1] = 0

while dq:
    cnt, x, y = dq.popleft()
    
    if x == x2-1 and y == y2-1:
        break
    
    for a, b in dxy:
        na = x + a
        nb = y + b

        if 0 <= na < N and 0 <= nb < M:
            if jump[na][nb] != INF:
                continue
            if arr[na][nb] == '0':
                jump[na][nb] = cnt
                dq.appendleft((cnt, na, nb))
            else:
                jump[na][nb] = cnt + 1
                dq.append((cnt+1, na, nb))

print(jump[x2-1][y2-1])