n, m = map(int, input().split())
arr = [0] * m
visited = [False] * n

def DFS(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(n):
        if not visited[i]:
            arr[cnt] = (i+1)
            visited[i] = True
            DFS(cnt+1)
            visited[i] = False
            
DFS(0)