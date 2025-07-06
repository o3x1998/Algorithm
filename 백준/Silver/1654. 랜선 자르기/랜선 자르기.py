import sys
input = sys.stdin.readline

K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]
line.sort()

left, right = 1, line[-1]
answer = 0

while left <= right:
    m = (left+right)//2
    p = 0
    
    for l in line:
        p += (l//m)
        
        if p >= N:
            break
    
    if p >= N:
        answer = m
        left = m + 1
    else:
        right = m - 1
    
print(answer)