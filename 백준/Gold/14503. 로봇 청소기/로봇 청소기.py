import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 북:0, 동:1, 남:2, 서:3
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0

while True:
    # 현재 자리 청소
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    
    # 주변 자리 확인
    for _ in range(4):
        # 현재 방향 기준 반시계 방향으로 회전
        d = (d + 3) % 4
        nx, ny = r+dxy[d][0], c+dxy[d][1]
        
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            r, c = nx, ny
            break
    else:
        # 주번에 자리가 없음
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진
        nx = r + (dxy[d][0] * -1)
        ny = c + (dxy[d][1] * -1)
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 1:
            r, c = nx, ny
        else:
            break
    
print(cnt)