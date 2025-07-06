import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

left, right = 1, (house[-1] - house[0])
answer = 0

while left <= right:
    m = (left+right)//2
    cnt = 1
    last = house[0]
    
    for i in range(1, N):
        if house[i] - last >= m:
            cnt += 1
            last = house[i]
        if cnt >= C:
            break
    
    if cnt >= C:
        answer = m
        left = m + 1
    else:
        right = m - 1
            
print(answer)