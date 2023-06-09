def solution(m, n, puddles):
    a = [[0]*(m) for _ in range(n)]
    
    for p in puddles:
        a[p[1]-1][p[0]-1] = 'W' # 물에 잠긴 지역 표시
        
    for i in range(n):
        if a[i][0] != 'W':
            a[i][0] = 1
        else: # 물에 잠겼으면 옆쪽으로 이동 X
            break
    
    for i in range(m):
        if a[0][i] != 'W':
            a[0][i] = 1
        else: # 물에 잠겼으면 아래쪽으로 이동 X
            break
    
    for i in range(1, n):
        for j in range(1, m):
            if a[i][j] == 'W': continue
            elif a[i-1][j] == 'W' and a[i][j-1] == 'W': continue
            elif a[i-1][j] == 'W': a[i][j] = a[i][j-1]
            elif a[i][j-1] == 'W': a[i][j] = a[i-1][j]
            else: a[i][j] = (a[i-1][j] + a[i][j-1])
                
    return a[n-1][m-1] % 1000000007