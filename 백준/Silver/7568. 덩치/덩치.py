import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = []

for i in range(N):
    cnt = 0
    for j in range(N):
        if j == i: continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: 
            cnt += 1
    answer.append(cnt+1)

print(*answer)